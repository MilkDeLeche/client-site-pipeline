"""Make a logo QR code for a pitch kit and prove it scans.

    python make_qr.py <url> <logo.png> <out.png> [hex color]

Error correction H, the logo at most 24% of the width on a white pad,
dark modules in the brand color (default navy) on white. Decodes the
result at full size and at 600, 300 and 200 px and exits 1 if any fail.

Needs: pip install qrcode pillow opencv-python-headless numpy
"""
import sys

import cv2
import numpy as np
import qrcode
from PIL import Image


def hex_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def main():
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    url, logo_path, out = sys.argv[1:4]
    color = hex_rgb(sys.argv[4]) if len(sys.argv) > 4 else (30, 72, 114)

    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=24, border=2)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=color, back_color="white").convert("RGB")
    w = img.size[0]

    logo = Image.open(logo_path).convert("RGBA")
    lw = int(w * 0.24)
    lh = int(logo.size[1] * lw / logo.size[0])
    logo = logo.resize((lw, lh), Image.LANCZOS)
    pad = int(w * 0.02)
    box = Image.new("RGB", (lw + 2 * pad, lh + 2 * pad), "white")
    box.paste(logo, (pad, pad), logo)
    img.paste(box, ((w - box.size[0]) // 2, (w - box.size[1]) // 2))
    img.save(out)

    ok = True
    for size in (w, 600, 300, 200):
        arr = cv2.cvtColor(np.array(img.resize((size, size), Image.LANCZOS)), cv2.COLOR_RGB2BGR)
        data, _, _ = cv2.QRCodeDetector().detectAndDecode(arr)
        good = data == url
        ok &= good
        print(f"{size}px", "OK" if good else f"FAIL ({data!r})")
    print("version", qr.version, "size", w, "->", out)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
