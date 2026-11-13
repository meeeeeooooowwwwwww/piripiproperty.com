#!/usr/bin/env python3
"""Render a share-friendly 1200x630 JPEG from the existing crayon illustration."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "public" / "assets" / "piripi-property-coming-soon.webp"
OUTPUT = ROOT / "public" / "social-preview.jpg"
W, H = 1200, 630

def font(size: int, bold: bool = False):
    paths = (
        ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
         "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf"]
        if bold else
        ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
         "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf"]
    )
    for filename in paths:
        if Path(filename).exists():
            return ImageFont.truetype(filename, size)
    return ImageFont.load_default()

def main():
    with Image.open(SOURCE) as image:
        image = image.convert("RGB")
        if min(image.size) < 630:
            raise ValueError("Source illustration must be at least 630px")
        artwork = image.resize((630, 630), Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", (W, H), "#ffffff")
    canvas.paste(artwork, (570, 0))
    d = ImageDraw.Draw(canvas)
    blue = "#195d9c"
    d.text((48, 158), "Piripi", font=font(88, True), fill=blue)
    d.text((48, 263), "Property", font=font(86, True), fill=blue)
    d.line((49, 380, 492, 380), fill="#4caf4e", width=7)
    d.text((48, 408), "Website coming", font=font(35, True), fill="#d92d31")
    d.text((48, 453), "soon.", font=font(35, True), fill="#d92d31")
    d.text((49, 558), "piripiproperty.com", font=font(24), fill="#56616a")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(OUTPUT, "JPEG", quality=87, subsampling=0, optimize=True, progressive=True)
    print(f"Generated {OUTPUT}, {W}x{H}, {OUTPUT.stat().st_size} bytes")

if __name__ == "__main__":
    main()
