"""Render pitch-kit pages to print files and check them (references/pitch-kit.md).

    python render_pages.py <out.pdf> <page1.html> [page2.html] [--qr <url>] [--vector]

For each page: a 2550x3300 PNG next to the HTML (letter at 300 dpi). The
merged <out.pdf> is built from those PNGs, one letter page each, so the PDF
looks exactly like the PNG on every viewer. Chrome's own print-to-PDF draws
soft shadows, blurs and rounded cards as many small image tiles, and phone
PDF viewers (iOS Files/Preview, several Android viewers) show them as
"buggy squares" and broken shadows. --vector merges Chrome's print instead
(selectable text, smaller file) for when the page has no shadows or blurs.

Chrome still prints each page once, as the overflow check: it fails if a page
prints to more than one sheet. With --qr, it fails if any page's QR code
doesn't decode to that URL (a trailing slash doesn't count as a difference).
Pages beyond two are refused: one page is good, two is the most an owner reads.

Uses the installed Google Chrome. Needs: pip install pypdf opencv-python-headless pillow
"""
import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

import cv2
import pypdf
from PIL import Image

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


def same_url(a, b):
    return (a or "").rstrip("/") == (b or "").rstrip("/")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("out")
    ap.add_argument("pages", nargs="+")
    ap.add_argument("--qr", help="URL every page's QR code must decode to")
    ap.add_argument("--vector", action="store_true", help="merge Chrome's vector print instead of the PNGs")
    a = ap.parse_args()
    if len(a.pages) > 2:
        sys.exit("Two pages at most.")
    exe = find_chrome()
    pngs, pdfs = [], []
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
            good = same_url(data, a.qr)
            ok &= good
            line += ", QR " + ("OK" if good else f"FAIL ({data or 'not found'})")
        print(line)
        pngs.append(png)
        pdfs.append(pdf)
    if a.vector:
        writer = pypdf.PdfWriter()
        for pdf in pdfs:
            writer.append(str(pdf))
        writer.write(a.out)
        kind = "vector (Chrome print)"
    else:
        # 2550x3300 at 300 dpi = exactly 8.5x11 in. High JPEG quality keeps the QR and small type crisp.
        imgs = [Image.open(p).convert("RGB") for p in pngs]
        imgs[0].save(a.out, "PDF", resolution=300, quality=92, save_all=True, append_images=imgs[1:])
        kind = "from the PNGs (looks the same on every viewer)"
    print("merged", len(a.pages), "page(s) ->", a.out, kind)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
