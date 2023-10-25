"""
-*- coding: utf-8 -*-
========================
Random raster image creation with color information side by side
========================
Contributor: Chirag Rathod (Srce Cde)
========================
"""

from PIL import Image, ImageDraw, ImageFont
import svgwrite


def create_raster_e(filename: str = "raster_e.jpeg") -> None:
    img = Image.new("RGB", (100, 100), color="white")
    d = ImageDraw.Draw(img)
    # font path may differ in other operating system
    font = ImageFont.truetype(
        "/System/Library/Fonts/Supplemental/Arial Unicode.ttf", 100
    )
    d.text((0, -30), "@", fill="black", font=font)
    img.save(filename)


def create_vector_e(filename: str = "vector_e.svg") -> None:
    dwg = svgwrite.Drawing(filename, profile="tiny")
    dwg.add(dwg.text("@", insert=(0, 100), font_size="100px", font_family="Arial"))
    dwg.save()


if __name__ == "__main__":
    create_raster_e()
    create_vector_e()
