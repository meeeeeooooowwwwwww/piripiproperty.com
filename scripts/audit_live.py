#!/usr/bin/env python3
"""Live Cloudflare Pages smoke audit: all sitemap URLs, SEO and HTTP headers.

Does not submit enquiries or touch protected client data.
"""
from __future__ import annotations

import html.parser
import json
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse

ORIGIN = "https://piripiproperty.com"
PUBLIC = Path(__file__).resolve().parents[1] / "public"
UA = "PiripiReleaseAudit/1.0"
ERRORS: list[str] = []


class Head(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.canonical: list[str] = []
        self.description: list[str] = []
        self.robots: list[str] = []
        self.h1_count = 0
        self.title_count = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "link" and a.get("rel") == "canonical":
            self.canonical.append(a.get("href", ""))
        if tag == "meta" and a.get("name") == "description":
            self.description.append(a.get("content", ""))
        if tag == "meta" and a.get("name") == "robots":
            self.robots.append(a.get("content", ""))
        if tag == "h1":
            self.h1_count += 1
        if tag == "title":
            self.title_count += 1


def fetch(url: str, max_bytes=900000):
    request = urllib.request.Request(
        url, headers={"User-Agent": UA, "Accept": "text/html,application/xml,*/*"})
    last_error = None
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=18) as response:
                return response.status, response.headers, response.read(max_bytes)
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as err:
            last_error = err
            if attempt < 3:
                time.sleep(2)
    raise RuntimeError(f"HTTP read failed {url}: {last_error}")


def main():
    expected_xml = (PUBLIC / "sitemap.xml").read_text(encoding="utf-8")
    expected_root = ET.fromstring(expected_xml)
    urls = [el.text for el in expected_root.iter() if el.tag.endswith("loc")]
    if len(urls) < 16 or len(set(urls)) != len(urls):
        raise SystemExit("Unexpected generated sitemap route count or duplicates")
    try:
        status, headers, data = fetch(ORIGIN + "/sitemap.xml")
        if status != 200:
            ERRORS.append(f"sitemap status {status}")
        live_urls = [el.text for el in ET.fromstring(data).iter() if el.tag.endswith("loc")]
        if set(live_urls) != set(urls):
            ERRORS.append("Live sitemap URL set differs from generated release")
        print("LIVE_SITEMAP_ROUTES", len(live_urls))
    except Exception as exc:
        ERRORS.append("Cannot read sitemap: " + str(exc))
    for url in urls:
        try:
            parsed = urlparse(url)
            if parsed.scheme != "https" or parsed.netloc != "piripiproperty.com":
                ERRORS.append("Non-canonical sitemap URL: " + url)
                continue
            status, headers, data = fetch(url)
            source = data.decode("utf-8", errors="replace")
            head = Head()
            head.feed(source)
            if status != 200:
                ERRORS.append(f"{url}: HTTP {status}")
            if head.canonical != [url]:
                ERRORS.append(f"{url}: canonical mismatch {head.canonical}")
            if head.h1_count != 1 or head.title_count != 1:
                ERRORS.append(f"{url}: expected exactly one H1 and title")
            if len(head.description) != 1 or not head.description[0]:
                ERRORS.append(f"{url}: meta description missing")
            if "noindex" in " ".join(head.robots).lower() or "noindex" in headers.get("X-Robots-Tag", "").lower():
                ERRORS.append(f"{url}: production blocked from indexing")
            if "text/html" not in headers.get("Content-Type", ""):
                ERRORS.append(f"{url}: unexpected content type {headers.get('Content-Type')}")
            if headers.get("X-Content-Type-Options", "").lower() != "nosniff":
                ERRORS.append(f"{url}: static security header nosniff missing")
            if not headers.get("Content-Security-Policy"):
                ERRORS.append(f"{url}: static CSP header absent")
            print("LIVE_SEO_PASS", parsed.path, status, len(data))
        except Exception as exc:
            ERRORS.append(f"{url}: {type(exc).__name__} {exc}")
    for route, marker in (
        ("/assets/corrie-piripi-professional.webp", b"WEBP"),
        ("/assets/site.css?v=20261117-editorial-about-v2", b"home-proof__identity"),
        ("/robots.txt", b"Sitemap: https://piripiproperty.com/sitemap.xml"),
    ):
        try:
            status, headers, data = fetch(ORIGIN + route)
            if status != 200 or marker not in data:
                ERRORS.append(f"{route}: release asset mismatch")
            print("LIVE_ASSET_PASS", route, status)
        except Exception as exc:
            ERRORS.append(f"{route}: {exc}")
    # pages.dev can duplicate indexable content; never let its successful 200 be indexed.
    try:
        preview_status, preview_headers, preview_body = fetch("https://piripiproperty.pages.dev/")
        robots = preview_headers.get("X-Robots-Tag", "").lower()
        if preview_status == 200 and "noindex" not in robots:
            ERRORS.append("pages.dev duplicate is indexable: X-Robots-Tag noindex missing")
        else:
            print("LIVE_PAGES_DEV_NOINDEX=" + ("PASS" if "noindex" in robots else "UNVERIFIED"))
    except Exception as exc:
        print("LIVE_PAGES_DEV_NOINDEX=UNVERIFIED", type(exc).__name__)
    # Note: intentionally do NOT mark a missing Brevo key as a site deploy failure.
    try:
        status, headers, data = fetch(ORIGIN + "/api/enquiry")
        result = json.loads(data)
        if status != 200 or not result.get("ok"):
            ERRORS.append("Enquiry API GET readiness endpoint not healthy")
        else:
            print("LIVE_ENQUIRY_ENDPOINT=PASS")
            print("LIVE_BREVO_DIRECT_MAIL=" + ("READY_UNDELIVERED_TEST" if result.get("ready") else "NOT_CONFIGURED"))
    except Exception as exc:
        ERRORS.append("Enquiry API readiness probe: " + str(exc))
    if ERRORS:
        for err in ERRORS:
            print("LIVE_AUDIT_FAIL", err)
        raise SystemExit(f"Live audit failed: {len(ERRORS)} issue(s)")
    print("LIVE_AUDIT_PASS routes=" + str(len(urls)))


if __name__ == "__main__":
    main()
