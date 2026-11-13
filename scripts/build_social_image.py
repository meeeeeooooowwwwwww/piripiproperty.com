#!/usr/bin/env python3
"""Generate a 1200x630 social-sharing card from Corrie's approved team photograph.

Contain the entire photo and use a subdued blurred background to fill wide cards,
so neither the company logo at the top nor people at the bottom are cropped.
"""
from pathlib import Path
import os
import re
from PIL import Image, ImageEnhance, ImageFilter, ImageOps

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "public" / "assets" / "piripi-and-sons-real-estate.jpg"
OUTPUT = ROOT / "public" / "social-preview.jpg"
W, H = 1200, 630


def main():
    with Image.open(SOURCE) as original:
        image = ImageOps.exif_transpose(original).convert("RGB")
        if min(image.size) < 630:
            raise ValueError("Source photo must be at least 630px in each dimension")
        backdrop = ImageOps.fit(image, (W, H), method=Image.Resampling.LANCZOS)
        backdrop = backdrop.filter(ImageFilter.GaussianBlur(26))
        backdrop = ImageEnhance.Brightness(backdrop).enhance(0.35)
        photo = ImageOps.contain(image, (W, H), method=Image.Resampling.LANCZOS)
        backdrop.paste(photo, ((W - photo.width) // 2, (H - photo.height) // 2))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    backdrop.save(OUTPUT, "JPEG", quality=88, subsampling=0, optimize=True, progressive=True)
    # Each deployment advertises a unique preview image URL while the stable
    # /social-preview.jpg file stays available for existing links and embeds.
    version = os.environ.get("GITHUB_SHA", "local")[:12]
    if not re.fullmatch(r"[a-zA-Z0-9_-]{1,16}", version):
        raise ValueError("Unexpected release version")
    next_url = f"https://piripiproperty.com/social-preview.jpg?v={version}"
    for page in sorted((ROOT / "public").rglob("index.html")):
        old = page.read_text(encoding="utf-8")
        new = re.sub(r"https://piripiproperty\\.com/social-preview\\.jpg(?:\\?v=[^\\\"]*)?", next_url, old)
        if new == old and next_url not in old:
            raise ValueError(f"No social image metadata found in {page}")
        page.write_text(new, encoding="utf-8")
    print(f"Generated {OUTPUT}, {W}x{H}, {OUTPUT.stat().st_size} bytes; social version {version}")


if __name__ == "__main__":
    main()
