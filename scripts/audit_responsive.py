#!/usr/bin/env python3
"""Browser-level responsive and navigation QA of generated static Piripi pages.

Run: python scripts/audit_responsive.py
Needs playwright Python package and installed Chromium browser.
No external site credentials are used; test content is served locally.
"""
from __future__ import annotations

import asyncio
import functools
import json
import os
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from playwright.async_api import async_playwright

PUBLIC = Path(__file__).resolve().parents[1] / "public"
SCREENSHOTS = Path(__file__).resolve().parents[1] / "artifacts" / "responsive-qa"
CHECKS = [
    ("/", "homepage"),
    ("/about/", "about"),
    ("/about/corrie-piripi/", "corrie-profile"),
    ("/contact/", "contact"),
    ("/sell/", "sell"),
    ("/international/", "international"),
]
VIEWPORTS = [
    ("mobile", 375, 812),
    ("tablet", 768, 1024),
    ("desktop", 1440, 900),
]
ERRORS: list[str] = []


def handler(*args, **kwargs):
    class QuietHandler(SimpleHTTPRequestHandler):
        def log_message(self, format, *args):
            return
    return QuietHandler(*args, directory=str(PUBLIC), **kwargs)


async def run_browser(base_url: str) -> None:
    SCREENSHOTS.mkdir(parents=True, exist_ok=True)
    async with async_playwright() as p:
        launch = {"headless": True, "args": ["--no-sandbox"]}
        executable = os.environ.get("PIRIPI_CHROME_EXECUTABLE", "").strip()
        if executable:
            launch["executable_path"] = executable
        browser = await p.chromium.launch(**launch)
        for route, name in CHECKS:
            for viewport_name, width, height in VIEWPORTS:
                page = await browser.new_page(
                    viewport={"width": width, "height": height},
                    device_scale_factor=1,
                    reduced_motion="reduce",
                    locale="en-NZ",
                )
                runtime_errors: list[str] = []
                page.on("pageerror", lambda exc: runtime_errors.append(str(exc)))
                try:
                    response = await page.goto(base_url + route, wait_until="domcontentloaded", timeout=20000)
                    if not response or response.status != 200:
                        ERRORS.append(f"{route} {viewport_name}: HTML not HTTP 200")
                        continue
                    await page.locator("main#main-content").wait_for(timeout=5000)
                    await page.locator(".site-header__brand").wait_for(timeout=5000)
                    # DOM measurements: real computed CSS, not string-based assumptions.
                    data = await page.evaluate("""() => {
                      const img = document.querySelector('.home-proof__portrait img');
                      const hero = document.querySelector('.profile-hero__portrait img');
                      const nav = document.querySelector('#main-site-nav');
                      const toggle = document.querySelector('.site-header__toggle');
                      const source = document.querySelector('.seo-section .source-note');
                      const firstParagraph = document.querySelector('.seo-content > .seo-section > p:first-of-type');
                      const bounds = e => e ? e.getBoundingClientRect() : null;
                      return {
                        width: window.innerWidth,
                        scroll: Math.max(document.documentElement.scrollWidth, document.body.scrollWidth),
                        navVisible: nav ? getComputedStyle(nav).display !== 'none' : false,
                        toggleVisible: toggle ? getComputedStyle(toggle).display !== 'none' : false,
                        portrait: img ? { width: bounds(img).width, height: bounds(img).height } : null,
                        hero: hero ? { width: bounds(hero).width, height: bounds(hero).height } : null,
                        cssLoaded: !!Array.from(document.styleSheets).some(s => s.href && s.href.includes('/assets/site.css')),
                        noteFont: source ? getComputedStyle(source).fontSize : null,
                        paragraphFont: firstParagraph ? getComputedStyle(firstParagraph).fontSize : null,
                        initialFont: firstParagraph ? getComputedStyle(firstParagraph, '::first-letter').fontSize : null,
                      };
                    }""")
                    if data["scroll"] > data["width"] + 3:
                        ERRORS.append(f"{route} {viewport_name}: horizontal overflow {data['scroll']}>{data['width']}")
                    if not data["cssLoaded"]:
                        ERRORS.append(f"{route} {viewport_name}: stylesheet missing")
                    if runtime_errors:
                        ERRORS.append(f"{route} {viewport_name}: browser JS error {runtime_errors[0][:150]}")
                    if width <= 900:
                        if not data["toggleVisible"]:
                            ERRORS.append(f"{route} {viewport_name}: mobile navigation toggle not visible")
                        if data["navVisible"]:
                            ERRORS.append(f"{route} {viewport_name}: collapsed mobile nav unexpectedly visible")
                        await page.locator(".site-header__toggle").click()
                        if not await page.locator("#main-site-nav").is_visible():
                            ERRORS.append(f"{route} {viewport_name}: mobile menu failed to open")
                        await page.keyboard.press("Escape")
                        if await page.locator("#main-site-nav").is_visible():
                            ERRORS.append(f"{route} {viewport_name}: Escape failed to close mobile menu")
                    else:
                        if not data["navVisible"]:
                            ERRORS.append(f"{route} {viewport_name}: desktop links missing")
                    if route == "/" and data["portrait"]:
                        limit = 116 if width <= 650 else 180
                        if data["portrait"]["width"] > limit or data["portrait"]["height"] > 205:
                            ERRORS.append(f"Home {viewport_name}: oversized portrait {data['portrait']}")
                    if route == "/about/" and data["hero"]:
                        if data["hero"]["width"] > 230:
                            ERRORS.append(f"About {viewport_name}: portrait width {data['hero']['width']}")
                        if data["initialFont"] and data["paragraphFont"] and (
                                float(data["initialFont"].replace("px", "")) <=
                                float(data["paragraphFont"].replace("px", "")) * 1.5):
                            ERRORS.append(f"About {viewport_name}: manuscript initial styling not applied")
                    if name in ("homepage", "about", "corrie-profile", "contact"):
                        await page.screenshot(
                            path=str(SCREENSHOTS / f"{name}-{viewport_name}.png"),
                            full_page=(width <= 768),
                            animations="disabled",
                        )
                    print("RESPONSIVE_CHECK", route, viewport_name, json.dumps(data, sort_keys=True))
                except Exception as exc:
                    ERRORS.append(f"{route} {viewport_name}: {type(exc).__name__}: {exc}")
                finally:
                    await page.close()
        await browser.close()


def main() -> None:
    http = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=http.serve_forever, daemon=True)
    thread.start()
    try:
        asyncio.run(run_browser(f"http://127.0.0.1:{http.server_port}"))
    finally:
        http.shutdown()
        http.server_close()
    if ERRORS:
        for message in ERRORS:
            print("RESPONSIVE_FAIL", message)
        raise SystemExit(f"Browser responsive QA failed: {len(ERRORS)} issue(s)")
    print(f"RESPONSIVE_PASS pages={len(CHECKS)} viewports={len(VIEWPORTS)} screenshots={len(list(SCREENSHOTS.glob('*.png')))}")


if __name__ == "__main__":
    main()
