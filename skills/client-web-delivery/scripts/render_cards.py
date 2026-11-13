"""Render hype-set cards to PNG and check them (references/hype-set.md).

    python render_cards.py <out dir> <card.html> [more.html ...] [--size 1080x1350]

Each card becomes <out dir>/<name>.png at twice the size (a 1080x1350 card is a
2160x2700 PNG), so it stays sharp on a phone. --size 1080x1920 makes the story
version of the same HTML.

It fails when a card is taller or wider than its frame, an image didn't load,
or a {{placeholder}} is still on the card. Open every PNG afterwards anyway:
the script can't see a one-word last line or type over a busy photo.

Uses the installed Google Chrome. Needs: pip install playwright
"""
import argparse
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

CHECK = """() => {
  const el = document.documentElement;
  const card = document.querySelector('.card') || document.body;
  const frame = card.getBoundingClientRect();
  // Anything with words that ends below or beside the frame was cut off.
  const cut = [...card.querySelectorAll('h1, h2, h3, p, strong, span, footer, header')].filter(e => {
    const r = e.getBoundingClientRect();
    return r.width && (r.bottom > frame.bottom + 1 || r.right > frame.right + 1 || r.left < frame.left - 1 || r.top < frame.top - 1);
  }).map(e => (e.innerText || '').trim().slice(0, 40));
  return {
    scrolls: el.scrollWidth > el.clientWidth + 1 || el.scrollHeight > el.clientHeight + 1,
    cut,
    broken: [...document.images].filter(i => !i.complete || !i.naturalWidth).map(i => i.getAttribute('src')),
    placeholder: /\\{\\{|\\}\\}/.test(document.body.innerText),
  };
}"""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("out")
    ap.add_argument("cards", nargs="+")
    ap.add_argument("--size", default="1080x1350", help="card size in CSS px: 1080x1350 (post) or 1080x1920 (story)")
    a = ap.parse_args()
    try:
        width, height = (int(v) for v in a.size.lower().split("x"))
    except ValueError:
        sys.exit("--size looks like 1080x1350")
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    ok = True
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome")
        page = browser.new_context(viewport={"width": width, "height": height}, device_scale_factor=2).new_page()
        for html in map(Path, a.cards):
            page.goto(html.resolve().as_uri(), wait_until="load")
            page.evaluate("document.fonts.ready")
            page.wait_for_timeout(300)
            found = page.evaluate(CHECK)
            problems = []
            if found["scrolls"]:
                problems.append("larger than its frame")
            if found["cut"]:
                problems.append("cut off: " + "; ".join(found["cut"]))
            if found["broken"]:
                problems.append("image not loaded: " + ", ".join(str(s) for s in found["broken"]))
            if found["placeholder"]:
                problems.append("a {{placeholder}} is still on the card")
            png = out / (html.stem + ".png")
            page.screenshot(path=str(png))
            print(f"{html.name} -> {png.name} ({width * 2}x{height * 2})", "OK" if not problems else "FAIL: " + " | ".join(problems))
            ok &= not problems
        browser.close()
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
