"""Render pitch-kit pages to print files and check them (references/pitch-kit.md).

    python render_pages.py <out.pdf> <page1.html> [page2.html] [--qr <url>]

For each page: a 2550x3300 PNG next to the HTML (letter at 300 dpi) and a
one-page letter PDF. Then all pages are merged into <out.pdf>. It fails if
a page prints to more than one sheet, or, with --qr, if any page's QR code
doesn't decode to that URL. Pages beyond two are refused: one page is good,
two is the most an owner reads.

Uses the installed Google Chrome. Needs: pip install pypdf opencv-python-headless
"""
import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

import cv2
import pypdf

CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
]


def find_chrome():
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome"):
        found = shutil.which(name)
        if found:
            return found
    for path in CANDIDATES:
        if os.path.exists(path):
            return path
    sys.exit("Google Chrome not found. Run the pipeline setup (client-site-pipeline/scripts/setup.mjs).")


def chrome(exe, *args):
    subprocess.run([exe, "--headless=new", "--disable-gpu", *args], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("out")
    ap.add_argument("pages", nargs="+")
    ap.add_argument("--qr", help="URL every page's QR code must decode to")
    a = ap.parse_args()
    if len(a.pages) > 2:
        sys.exit("Two pages at most.")
    exe = find_chrome()
    writer = pypdf.PdfWriter()
    ok = True
    for html in map(Path, a.pages):
        html = html.resolve()
        url = html.as_uri()
        png, pdf = html.with_suffix(".png"), html.with_suffix(".pdf")
        chrome(exe, "--hide-scrollbars", "--force-device-scale-factor=2", "--window-size=1275,1650",
               f"--screenshot={png}", url)
        chrome(exe, "--no-pdf-header-footer", f"--print-to-pdf={pdf}", url)
        sheets = len(pypdf.PdfReader(str(pdf)).pages)
        line = f"{html.name}: png {png.name}, pdf {sheets} page(s)"
        ok &= sheets == 1
        if a.qr:
            data, _, _ = cv2.QRCodeDetector().detectAndDecode(cv2.imread(str(png)))
            good = data == a.qr
            ok &= good
            line += ", QR " + ("OK" if good else f"FAIL ({data or 'not found'})")
        print(line)
        writer.append(str(pdf))
    writer.write(a.out)
    print("merged", len(a.pages), "page(s) ->", a.out)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
