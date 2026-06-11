#!/usr/bin/env python3
"""OCR an attachment image via tesseract. Outputs plain text to stdout.

Usage:
    python3 scripts/ocr_attachment.py <image_path> [--psm 6]

Exit 0 on success, 1 on error. Stderr carries error messages only.
"""
import subprocess
import sys
from pathlib import Path

PSM = "6"   # default: uniform block of text — best for email/portal screenshots


def main() -> int:
    args = sys.argv[1:]
    psm = PSM
    path = None
    skip_next = False
    for i, a in enumerate(args):
        if skip_next:
            skip_next = False
            continue
        if a == "--psm" and i + 1 < len(args):
            psm = args[i + 1]
            skip_next = True
        elif not path:
            path = a
        else:
            print(f"Unexpected argument: {a}", file=sys.stderr)
            return 1

    if not path:
        print("Usage: ocr_attachment.py <image_path> [--psm N]", file=sys.stderr)
        return 1

    img = Path(path)
    if not img.exists():
        print(f"File not found: {path}", file=sys.stderr)
        return 1

    result = subprocess.run(
        ["tesseract", str(img), "stdout", "--psm", psm, "-l", "eng"],
        capture_output=True, text=True, timeout=30,
    )

    if result.returncode != 0:
        print(f"tesseract exited {result.returncode}: {result.stderr[:200]}",
              file=sys.stderr)
        return 1

    # Output the extracted text
    sys.stdout.write(result.stdout)
    return 0


if __name__ == "__main__":
    sys.exit(main())
