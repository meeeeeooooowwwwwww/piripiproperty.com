#!/usr/bin/env python3
"""Build source-controlled, SEO-readable Piripi content pages (stdlib only)."""
from __future__ import annotations

import html
import json
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "content" / "pages.json"
PUBLIC = ROOT / "public"
HOST = "https://piripiproperty.com"
PREVIEW = f"{HOST}/social-preview.jpg?v=brand-20261113"

def esc(value: object) -> str:
    return html.escape(str(value), quote=True)

def render_link(href: str, label: str, cls: str = "") -> str:
    external = href.startswith("http")
    if external and not href.startswith("https://"):
        raise ValueError(f"Non-HTTPS external link: {href}")
    if not external and not (href.startswith("/") and "//" not in href):
        raise ValueError(f"Invalid relative link: {href}")
    extras = ' target="_blank" rel="noopener noreferrer"' if external else ""
    class_attr = f' class="{esc(cls)}"' if cls else ""
    return f'<a href="{esc(href)}"{class_attr}{extras}>{esc(label)}</a>'

def nav(current: str) -> str:
    links = [
        ("/", "Home", ""),
        ("/sell/", "Sell", "sell"),
        ("/buy/", "Buy", "buy"),
        ("/areas/christchurch/", "Areas", "areas"),
        ("/about/", "About", "about"),
        ("/guides/", "Guides", "guides"),
        ("/contact/", "Contact", "contact"),
    ]
    content = []
    for route, title, section in links:
        active = (not section and current == "") or (section and (current == section or current.startswith(section + "/")))
        attr = ' aria-current="page"' if active else ""
        content.append(f'<a href="{route}"{attr}>{esc(title)}</a>')
    return (
        '<header class="site-header"><div class="site-header__inner">'
        '<a class="site-header__brand" href="/" aria-label="Piripi and Sons Real Estate home">'
        '<img src="/assets/brand/mark-gold.svg" alt="" width="30" height="30">'
        '<span>PIRIPI &amp; SONS<small>REAL ESTATE</small></span></a>'
        '<button class="site-header__toggle" type="button" aria-controls="main-site-nav" '
        'aria-expanded="false" aria-label="Open navigation">Menu</button>'
        '<nav class="site-header__nav" id="main-site-nav" aria-label="Main navigation">'
        + "".join(content) + "</nav></div></header>"
    )

def breadcrumbs(page: dict) -> list[tuple[str, str]]:
    path = page["path"]
    result = [("Home", "/")]
    if path.startswith("sell/"): result.append(("Sell", "/sell/"))
    elif path.startswith("guides/"): result.append(("Guides", "/guides/"))
    elif path.startswith("areas/"): result.append(("Areas", "/areas/christchurch/"))
    if result[-1][1] != "/" + path + "/":
        result.append((page["h1"], "/" + path + "/"))
    return result

def render(page: dict) -> str:
    path = page["path"]
    canonical = f"{HOST}/{path}/"
    crumbs = breadcrumbs(page)
    crumb_html = " / ".join(render_link(href, name) if i < len(crumbs) - 1 else esc(name)
                          for i, (name, href) in enumerate(crumbs))
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "WebSite", "@id": f"{HOST}/#website",
             "url": f"{HOST}/", "name": "Piripi & Sons Real Estate", "inLanguage": "en-NZ"},
            {"@type": "Brand", "@id": f"{HOST}/#brand",
             "name": "Piripi & Sons Real Estate", "url": f"{HOST}/",
             "logo": f"{HOST}/assets/brand/logo-horizontal-transparent.svg"},
            {"@type": "Person", "@id": f"{HOST}/#corrie-piripi",
             "name": "Corrie Piripi", "url": f"{HOST}/contact/"},
            {"@type": "WebPage", "@id": canonical + "#webpage",
             "url": canonical, "name": page["title"], "description": page["description"],
             "inLanguage": "en-NZ", "isPartOf": {"@id": f"{HOST}/#website"},
             "about": {"@id": f"{HOST}/#brand"},
             "dateModified": page["lastReviewed"]},
        ],
    }
    if len(crumbs) > 1:
        schema["@graph"].append({
            "@type": "BreadcrumbList",
            "@id": canonical + "#breadcrumbs",
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": name, "item": HOST + href}
                for i, (name, href) in enumerate(crumbs)
            ]
        })
    jsonld = json.dumps(schema, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    sections = []
    for i, section in enumerate(page["sections"], start=1):
        paragraphs = "".join(f"<p>{esc(p)}</p>" for p in section["paragraphs"])
        bullets = ""
        if section.get("bullets"):
            bullets = "<ul>" + "".join(f"<li>{esc(item)}</li>" for item in section["bullets"]) + "</ul>"
        refs = ""
        if section.get("refs"):
            refs = ('<p class="source-note"><em>* Official references: ' +
                " · ".join(render_link(ref["url"], ref["label"]) for ref in section["refs"]) +
                '.</em></p>')
        sections.append(f'<section class="seo-section" aria-labelledby="section-{i}">'
                        f'<h2 id="section-{i}">{esc(section["heading"])}</h2>'
                        f'{paragraphs}{bullets}{refs}</section>')
    related = ""
    if page.get("related"):
        related = ('<nav class="seo-related" aria-label="Related information">'
                   '<h2>Explore related information</h2><ul>' +
                   "".join("<li>" + render_link(x["href"], x["text"]) + "</li>"
                           for x in page["related"]) + "</ul></nav>")
    cta = page["cta"]
    lead = (f'<aside class="seo-cta" aria-labelledby="seo-cta-title">'
            f'<h2 id="seo-cta-title">{esc(cta["title"])}</h2>'
            f'<p>{esc(cta["text"])}</p>'
            f'{render_link(cta["url"], cta["label"], "seo-cta-link")}</aside>')
    full = f'''<!doctype html>
<html lang="en-NZ">
<head>
  <script async src="https://www.googletagmanager.com/gtm.js?id=GTM-555PWRPR"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
  </script>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <meta name="theme-color" content="#000000">
  <meta name="description" content="{esc(page["description"])}">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <link rel="canonical" href="{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="en_NZ">
  <meta property="og:site_name" content="Piripi &amp; Sons Real Estate">
  <meta property="og:url" content="{canonical}">
  <meta property="og:title" content="{esc(page["title"])}">
  <meta property="og:description" content="{esc(page["description"])}">
  <meta property="og:image" content="{PREVIEW}">
  <meta property="og:image:alt" content="Piripi &amp; Sons Real Estate logo and team photograph">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(page["title"])}">
  <meta name="twitter:description" content="{esc(page["description"])}">
  <meta name="twitter:image" content="{PREVIEW}">
  <title>{esc(page["title"])}</title>
  <script type="application/ld+json">{jsonld}</script>
  <link rel="icon" type="image/svg+xml" href="/favicon.svg?v=2">
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png?v=2">
  <link rel="shortcut icon" href="/favicon.ico?v=2">
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png?v=2">
  <link rel="manifest" href="/site.webmanifest">
  <link rel="stylesheet" href="/assets/site.css?v=20261117-seo">
  <script src="/assets/site-nav.js?v=20261117-seo" defer></script>
</head>
<body class="inner-page seo-page seo-{esc(page["category"])}">
  {nav(path)}
  <div class="seo-shell">
    <main id="main-content" class="seo-main">
      <div class="seo-breadcrumb" aria-label="Breadcrumbs">{crumb_html}</div>
      <header class="seo-intro">
        <span class="eyebrow">{esc(page["kicker"])}</span>
        <h1>{esc(page["h1"])}</h1>
        <p class="intro">{esc(page["intro"])}</p>
      </header>
      <div class="seo-columns">
        <article class="seo-content">{''.join(sections)}{related}</article>
        {lead}
      </div>
      <p class="seo-reviewed"><em>* General information reviewed {esc(page["lastReviewed"])}; check current official guidance. Specific legal, financial, tax or immigration advice should come from a qualified adviser.</em></p>
    </main>
  </div>
  <footer class="site-footer" aria-label="Site footer"><div class="site-footer__inner">
    <span>&copy; 2026 Piripi &amp; Sons Real Estate</span>
    <div class="site-footer__right">
      {render_link("/international/", "International", "site-footer__international")}
      {render_link("/privacy/", "Privacy", "site-footer__privacy")}
      {render_link("/sitemap/", "Sitemap", "site-footer__sitemap")}
      {render_link("https://americafirst.co.nz/", "Website by America First Limited")}
    </div>
  </div></footer>
</body>
</html>
'''
    return full

def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    if data.get("schemaVersion") != 1:
        raise SystemExit("Unexpected content schema version")
    seen_paths, seen_titles = set(), set()
    for page in data["pages"]:
        path = page["path"]
        if not re.fullmatch(r"[a-z0-9-]+(?:/[a-z0-9-]+)*", path):
            raise ValueError("Unsafe page path: " + path)
        if path in seen_paths or page["title"].lower() in seen_titles:
            raise ValueError("Duplicate page path or title: " + path)
        seen_paths.add(path)
        seen_titles.add(page["title"].lower())
        if not page["description"] or len(page["description"]) > 170 or not page["sections"]:
            raise ValueError("Incomplete content: " + path)
        if not page["related"] or not page["lastReviewed"]:
            raise ValueError("Missing links or editorial date: " + path)
        for section in page["sections"]:
            for ref in section.get("refs", []):
                if urlparse(ref["url"]).scheme != "https":
                    raise ValueError("Non-HTTPS reference on " + path)
        target = PUBLIC / path / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(render(page), encoding="utf-8")
        print("GENERATED", "/" + path + "/", target.stat().st_size, "bytes")
    xml_urls = ["/", "/contact/", "/international/", "/sitemap/"]
    xml_urls += ["/" + p["path"] + "/" for p in data["pages"]]
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path in xml_urls:
        lines.append(f'  <url><loc>{HOST}{path}</loc></url>')
    lines.append('</urlset>')
    (PUBLIC / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("GENERATED", len(xml_urls), "sitemap URLs")

if __name__ == "__main__":
    main()
