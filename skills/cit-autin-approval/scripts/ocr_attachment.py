#!/usr/bin/env python3
"""Thin wrapper around tesseract OCR. Takes an image path, prints plain text to stdout.

Usage: python3 ocr_attachment.py <image_path> [--psm N]
Default page-segmentation mode is 6 (assume a uniform block of text). Pass
--psm 3 for fully automatic page segmentation when --psm 6 yields garbage.
"""
import sys
from PIL import Image, ImageOps
import pytesseract


def main():
    args = [a for a in sys.argv[1:]]
    psm = "6"
    path = None
    i = 0
    while i < len(args):
        if args[i] == "--psm":
            psm = args[i + 1]
            i += 2
            continue
        path = args[i]
        i += 1

    if not path:
        sys.stderr.write("usage: ocr_attachment.py <image_path> [--psm N]\n")
        sys.exit(2)

    try:
        img = Image.open(path)
    except Exception as e:
        sys.stderr.write(f"cannot open image: {e}\n")
        sys.exit(1)

    # Normalize: convert to grayscale and auto-contrast to help tesseract.
    img = img.convert("L")
    img = ImageOps.autocontrast(img)

    config = f"--psm {psm}"
    text = pytesseract.image_to_string(img, config=config)
    sys.stdout.write(text)


if __name__ == "__main__":
    main()
