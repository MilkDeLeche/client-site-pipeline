"""Screenshots of the live pitch for the pitch kit (references/pitch-kit.md).

    python shots.py <site url> <out dir> [--state state.json]
        [--page /=desk] [--section ".section_our-work=work"] [--phone /contact=form]

--page     full desktop viewport (1440x900) of a path, named <name>.png
--section  one section of the home page by CSS selector; fixed and sticky
           elements (header, call bar) are hidden so they don't cover it
--phone    a path on a Pixel 7 (the iPhone devices fail with the Chrome channel)

--state is a Playwright storage-state file that sets the site's own
localStorage keys so the cookie banner and signup popup stay closed, e.g.
{"cookies":[],"origins":[{"origin":"<url>","localStorage":[
  {"name":"<consent key>","value":"declined"},{"name":"<popup key>","value":"1"}]}]}

Uses the installed Google Chrome. Needs: pip install playwright
"""
import argparse
import os

from playwright.sync_api import sync_playwright

HIDE_FIXED = """for (const e of document.querySelectorAll('body *')) {
  const p = getComputedStyle(e).position;
  if (p === 'fixed' || p === 'sticky') e.style.visibility = 'hidden';
}"""


def pair(value):
    target, _, name = value.rpartition("=")
    if not target or not name:
        raise argparse.ArgumentTypeError(f"expected TARGET=name, got {value!r}")
    return target, name


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("url")
    ap.add_argument("out")
    ap.add_argument("--state")
    ap.add_argument("--page", type=pair, action="append", default=[])
    ap.add_argument("--section", type=pair, action="append", default=[])
    ap.add_argument("--phone", type=pair, action="append", default=[])
    a = ap.parse_args()
    base = a.url.rstrip("/")
    os.makedirs(a.out, exist_ok=True)
    state = {"storage_state": a.state} if a.state else {}

    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome")
        desk = browser.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=1.5, **state)
        page = desk.new_page()
        for path, name in a.page:
            page.goto(base + path, wait_until="networkidle")
            page.wait_for_timeout(2500)
            page.screenshot(path=os.path.join(a.out, f"{name}.png"))
            print("page   ", path, "->", name)
        if a.section:
            page.goto(base + "/", wait_until="networkidle")
            for selector, name in a.section:
                el = page.locator(selector).first
                el.scroll_into_view_if_needed()
                page.wait_for_timeout(1500)
                page.mouse.wheel(0, 400)  # let scroll reveals finish
                page.wait_for_timeout(1200)
                page.evaluate(HIDE_FIXED)
                el.screenshot(path=os.path.join(a.out, f"{name}.png"))
                print("section", selector, "->", name)
                page.reload(wait_until="networkidle")
        if a.phone:
            mobile = browser.new_context(**p.devices["Pixel 7"], **state)
            m = mobile.new_page()
            for path, name in a.phone:
                m.goto(base + path, wait_until="networkidle")
                m.wait_for_timeout(2500)
                m.screenshot(path=os.path.join(a.out, f"{name}.png"))
                print("phone  ", path, "->", name)
        browser.close()


if __name__ == "__main__":
    main()
