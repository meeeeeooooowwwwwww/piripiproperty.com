#!/usr/bin/env python3
"""Fail deploys with broken indexable routes, canonicals, links or SEO metadata."""
from __future__ import annotations

import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"
ORIGIN = "https://piripiproperty.com"

class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = []
        self.h1 = []
        self._title = False
        self._h1 = False
        self._jsonld = False
        self.jsonld = []
        self.canonicals = []
        self.descriptions = []
        self.links = []
        self.images = []
        self.main_count = 0
        self.main_ids = []
        self.nav_toggles = []
        self.skip_links = []
        self.robots = []
        self.footnotes = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "main":
            self.main_count += 1
            self.main_ids.append(attrs.get("id", ""))
        if tag == "button" and attrs.get("aria-controls") == "main-site-nav":
            self.nav_toggles.append((attrs.get("aria-label"), attrs.get("aria-expanded")))
        if tag == "a" and "skip-link" in attrs.get("class", "").split():
            self.skip_links.append(attrs.get("href"))
        if tag == "title": self._title = True
        if tag == "h1": self._h1 = True; self.h1.append("")
        if tag == "script" and attrs.get("type") == "application/ld+json":
            self._jsonld = True; self.jsonld.append("")
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonicals.append(attrs.get("href", ""))
        if tag == "meta" and attrs.get("name") == "description":
            self.descriptions.append(attrs.get("content", ""))
        if tag == "meta" and attrs.get("name") == "robots":
            self.robots.append(attrs.get("content", ""))
        if tag == "a":
            self.links.append(attrs.get("href", ""))
        if tag == "img":
            self.images.append((attrs.get("src", ""), attrs.get("alt")))

        if tag == "p" and "source-note" in attrs.get("class", "").split():
            self.footnotes += 1

    def handle_endtag(self, tag):
        if tag == "title": self._title = False
        if tag == "h1": self._h1 = False
        if tag == "script": self._jsonld = False

    def handle_data(self, data):
        if self._title: self.title.append(data)
        if self._h1: self.h1[-1] += data
        if self._jsonld: self.jsonld[-1] += data

def actual_route(file: Path) -> str:
    relative = file.relative_to(PUBLIC)
    if relative.parts == ("index.html",): return "/"
    if relative.parts[-1] != "index.html": raise ValueError(str(file))
    return "/" + "/".join(relative.parts[:-1]) + "/"

def local_target(url: str) -> Path:
    clean = unquote(urlparse(url).path)
    if clean in ("", "/"): return PUBLIC / "index.html"
    if ".." in Path(clean).parts: raise AssertionError("Unsafe internal URL " + clean)
    clean = clean.lstrip("/")
    if clean.endswith("/"): return PUBLIC / clean / "index.html"
    if Path(clean).suffix: return PUBLIC / clean
    return PUBLIC / clean / "index.html"

def main():
    errors = []
    pages = sorted(PUBLIC.rglob("index.html"))
    sitemap_tree = ET.parse(PUBLIC / "sitemap.xml")
    sitemap_urls = [v.text for v in sitemap_tree.iter() if v.tag.endswith("loc") and v.text]
    sitemap_set = set(sitemap_urls)
    seen_canonicals, seen_titles = set(), set()
    if len(sitemap_set) != len(sitemap_urls):
        errors.append("Duplicate sitemap URLs")
    for file in pages:
        route = actual_route(file)
        body = file.read_text(encoding="utf-8")
        p = Page()
        p.feed(body)
        canonical = ORIGIN + route
        if p.canonicals != [canonical]: errors.append(f"{route}: bad canonical {p.canonicals}")
        if canonical not in sitemap_set: errors.append(f"{route}: missing from sitemap")
        if len(p.title) == 0 or not "".join(p.title).strip(): errors.append(f"{route}: title missing")
        elif "".join(p.title).lower() in seen_titles: errors.append(f"{route}: duplicate title")
        else: seen_titles.add("".join(p.title).lower())
        if len(p.h1) != 1 or not p.h1[0].strip(): errors.append(f"{route}: expected one nonempty H1, got {p.h1}")
        if p.main_count != 1 or p.main_ids != ["main-content"]:
            errors.append(f"{route}: expected one labelled main landmark")
        if p.skip_links != ["#main-content"]: errors.append(f"{route}: skip link missing")
        if p.nav_toggles != [("Open navigation", "false")]:
            errors.append(f"{route}: accessible navigation button missing")
        if "site-header__toggle-bars" not in body: errors.append(f"{route}: visual navigation icon missing")
        if ">Menu</button>" in body: errors.append(f"{route}: visible Menu label should not appear")
        if len(p.descriptions) != 1 or not p.descriptions[0].strip(): errors.append(f"{route}: description missing")
        if "noindex" in " ".join(p.robots).lower(): errors.append(f"{route}: accidentally noindex")
        if len(p.jsonld) != 1: errors.append(f"{route}: missing or repeated JSON-LD")
        else:
            try:
                graph = json.loads(p.jsonld[0]).get("@graph", [])
                if not any(e.get("@type") == "Brand" for e in graph):
                    errors.append(f"{route}: missing Brand schema")
                if not any(e.get("@type") == "Person" for e in graph):
                    errors.append(f"{route}: missing Person schema")
            except Exception as exc: errors.append(f"{route}: malformed JSON-LD: {exc}")
        if "licensed real estate agent" in body.lower():
            errors.append(f"{route}: unverified protected licence title")
        if canonical in seen_canonicals: errors.append(f"{route}: duplicate canonical")
        seen_canonicals.add(canonical)
        for img_src, alt in p.images:
            if alt is None: errors.append(f"{route}: image missing alt attribute: {img_src}")
            if img_src.startswith("/") and not local_target(img_src).is_file():
                errors.append(f"{route}: image not found: {img_src}")
        for link in p.links:
            if link.startswith(("#", "mailto:", "tel:")) or not link: continue
            if link.startswith("https://") or link.startswith("http://"):
                parsed = urlparse(link)
                if parsed.netloc not in ("piripiproperty.com", "www.piripiproperty.com"): continue
                local = parsed.path or "/"
            elif link.startswith("/"):
                local = link
            else:
                errors.append(f"{route}: relative link not root-absolute: {link}")
                continue
            target = local_target(local)
            if not target.is_file():
                errors.append(f"{route}: broken link {link} -> {target.relative_to(PUBLIC)}")
        if file.parts[-3:-1] and "guides" in file.parts and p.footnotes == 0:
            errors.append(f"{route}: guides missing official source-note")
    if not (PUBLIC / "assets" / "corrie-piripi-professional.webp").is_file():
        errors.append("Approved Corrie portrait missing from build output")
    for item in sitemap_set:
        if not item.startswith(ORIGIN + "/"): errors.append("Noncanonical sitemap URL " + item)
        elif not local_target(item).is_file(): errors.append("Sitemap points to missing file " + item)
    if errors:
        for e in errors: print("SEO_FAIL", e)
        raise SystemExit(f"SEO validation failed: {len(errors)} issue(s)")
    print(f"SEO_PASS pages={len(pages)} sitemap={len(sitemap_urls)} titles/canonicals/links/JSON-LD all valid")

if __name__ == "__main__":
    main()
