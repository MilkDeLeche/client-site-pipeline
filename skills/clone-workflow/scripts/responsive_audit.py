"""Responsive + cross-browser audit for a built site (clone-workflow → references/responsive-audit.md).

    python responsive_audit.py --base http://127.0.0.1:4330 --pages "/,/projects,/contact" \
        [--phone-pages "/es,/es/projects"] [--engines chromium,webkit] [--out audit.json]

Opens every page in Playwright's Chromium (Chrome's engine) and WebKit (Safari's engine) at
320, 360, 390 (phones: touch, 2x, a phone user agent), 768, 1024 and 1440. `--phone-pages` (the
second language, usually) runs at the phone widths only. On each load it scrolls the whole page
once, so reveal animations and lazy components start, then checks:

  OVERFLOW  the page is wider than the screen (it slides sideways on a phone). The script then
            hides branches of the DOM until the width fits and prints the path to the culprit.
  BLANK     a band of the page taller than max(260px, 45% of the screen) with nothing painted in
            it. Each candidate is screenshotted and kept only if the pixels really are flat, so
            pinned sections and light backgrounds the DOM scan misses don't count.
  ERROR     an uncaught page error or console error from the site's own origin. Errors raised by
            third-party players and widgets are listed apart, since they aren't ours to fix.

Two helpers for the diagnosis:

    python responsive_audit.py shot --base URL --page /x --width 390 --engine webkit --y 1200,2400
    python responsive_audit.py bisect --base URL --page /x --width 360 --engine webkit

Needs: pip install playwright pillow && python -m playwright install chromium webkit
(the pipeline setup does both). Exits 1 when anything is found.
"""
import argparse
import asyncio
import io
import json
import sys
from urllib.parse import urlparse

from PIL import Image, ImageStat
from playwright.async_api import async_playwright

WIDTHS = [(320, 640, True), (360, 740, True), (390, 844, True), (768, 1024, True), (1024, 768, False), (1440, 900, False)]
PHONES = [w for w in WIDTHS if w[0] < 400]

async def go_to(page, y):
    """Scroll like a person. Smooth-scroll libraries (Lenis, Locomotive, GSAP ScrollSmoother) ignore or undo
    window.scrollTo, so in-view triggers never fire and sections look blank that aren't. Wheel first; fall
    back to scrollTo where the wheel does nothing (touch contexts)."""
    now = await page.evaluate("scrollY")
    if abs(now - y) < 4:
        return
    try:
        await page.mouse.move(10, 300)
        await page.mouse.wheel(0, y - now)
    except Exception:  # noqa: BLE001  (mobile WebKit has no wheel; touch scrolling isn't hijacked there)
        pass
    await settle_scroll(page)
    if abs(await page.evaluate("scrollY") - y) > 60:
        await page.evaluate(f"scrollTo(0, {y})")
        await settle_scroll(page)


async def settle_scroll(page):
    """Wait until a smooth scroll has stopped moving (or 2s)."""
    last = None
    for _ in range(20):
        await page.wait_for_timeout(100)
        now = await page.evaluate("scrollY")
        if now == last:
            return
        last = now


async def scroll_all(page):
    """Walk the whole page once, so reveal animations, lazy images and in-view components start."""
    y = 0
    while True:
        h, vh = await page.evaluate("[document.documentElement.scrollHeight, innerHeight]")
        if y > h:
            break
        await go_to(page, y)
        await page.wait_for_timeout(150)
        y += int(vh * 0.6)
    await page.wait_for_timeout(1500)  # let the last reveals finish

PROBE = """() => {
  const vw = document.documentElement.clientWidth, vh = innerHeight, H = document.documentElement.scrollHeight;
  const ys = [];
  // a box painted the page's own background color looks blank, so it doesn't count as content
  const clear = (c) => c === 'rgba(0, 0, 0, 0)' || c === 'transparent';
  const pageBg = [document.body, document.documentElement].map((x) => getComputedStyle(x).backgroundColor).find((c) => !clear(c)) || 'rgb(255, 255, 255)';
  // effective opacity: a component the server rendered at opacity .001 and the script never started
  // (a slideshow, a reveal) paints nothing, even though its children report opacity 1
  const op = new Map([[document.body, parseFloat(getComputedStyle(document.body).opacity)]]);
  const eff = (e) => { if (op.has(e)) return op.get(e); const v = parseFloat(getComputedStyle(e).opacity) * eff(e.parentElement); op.set(e, v); return v; };
  for (const e of document.body.querySelectorAll('*')) {
    const cs = getComputedStyle(e);
    if (cs.display === 'none' || cs.visibility === 'hidden' || cs.position === 'fixed' || eff(e) < 0.05) continue;
    const r = e.getBoundingClientRect(); if (r.width < 1 || r.height < 1) continue;
    const media = /^(IMG|VIDEO|IFRAME|SVG|CANVAS|PICTURE|INPUT|TEXTAREA|SELECT|BUTTON)$/i.test(e.tagName);
    const bg = cs.backgroundImage !== 'none' || (!clear(cs.backgroundColor) && cs.backgroundColor !== pageBg);
    let text = false; for (const n of e.childNodes) if (n.nodeType === 3 && n.textContent.trim()) { text = true; break; }
    if (media || bg || text) ys.push([r.top + scrollY, r.bottom + scrollY, bg && !media && !text]);
  }
  // a full-page background (body, a wrapper) would hide every gap: drop boxes taller than 3 screens that only paint a color
  const boxes = ys.filter(([a, b, onlyBg]) => !(onlyBg && b - a > vh * 3)).sort((p, q) => p[0] - q[0]);
  const gaps = []; let end = 0; const min = Math.max(260, vh * 0.45);
  for (const [a, b] of boxes) { if (end > 0 && a - end > min) gaps.push([Math.round(end), Math.round(a)]); end = Math.max(end, b); }
  // the empty bottom of a page shorter than the screen (a 404, a thank-you page) is not a layout gap
  if (H - end > min && end > 0 && H > vh * 1.05) gaps.push([Math.round(end), H]);
  return { sw: document.documentElement.scrollWidth, vw, vh, H, gaps };
}"""

BISECT = """() => {
  const vw = document.documentElement.clientWidth, sw = () => document.documentElement.scrollWidth;
  const label = (e) => { const c = getComputedStyle(e), r = e.getBoundingClientRect();
    return `${e.tagName.toLowerCase()}${e.id ? '#' + e.id : ''}${(e.getAttribute('class') || '').trim() ? '.' + e.getAttribute('class').trim().split(/\\s+/).slice(0, 3).join('.') : ''}`
      + ` [${Math.round(r.left)}..${Math.round(r.right)}, w${Math.round(r.width)}, ${c.position}${c.whiteSpace === 'nowrap' ? ', nowrap' : ''}${c.display.includes('grid') ? ', grid ' + c.gridTemplateColumns + ' gap ' + c.columnGap : ''}]`; };
  const path = []; let node = document.body;
  for (let d = 0; d < 40; d++) {
    let found = null;
    for (const c of node.children) { const old = c.style.display; c.style.display = 'none'; const v = sw(); c.style.display = old; if (v <= vw) { found = c; break; } }
    if (!found) break; path.push(label(found)); node = found;
  }
  // inside the last node, name the widest children and any pseudo-element with content
  const inner = [...node.querySelectorAll('*')].map((x) => [x, x.getBoundingClientRect()]).filter(([, r]) => r.right > vw + 1)
    .sort((a, b) => b[1].right - a[1].right).slice(0, 5).map(([x]) => label(x));
  const pseudo = [node, ...node.querySelectorAll('*')].flatMap((x) => ['::before', '::after'].map((p) => [x, p, getComputedStyle(x, p)]))
    .filter(([, , s]) => s.content !== 'none' && s.content !== 'normal' && s.content !== '""').slice(0, 5)
    .map(([x, p, s]) => `${label(x)}${p} content=${s.content.slice(0, 40)} white-space=${s.whiteSpace}`);
  return { sw: sw(), vw, path, inner, pseudo };
}"""


def ctx_opts(p, engine, w, h, phone):
    if not phone:
        return {"viewport": {"width": w, "height": h}}
    ua = p.devices["iPhone 14"]["user_agent"] if engine == "webkit" else p.devices["Pixel 7"]["user_agent"]
    return {"viewport": {"width": w, "height": h}, "device_scale_factor": 2, "is_mobile": engine != "firefox", "has_touch": True, "user_agent": ua}


async def load(p, browser, engine, url, w, h, phone, settle):
    ctx = await browser.new_context(**ctx_opts(p, engine, w, h, phone))
    page = await ctx.new_page()
    errs = []
    host = urlparse(url).netloc
    def where(loc):
        return "?" if not loc else ("own" if urlparse(loc).netloc == host else "3rd")
    page.on("pageerror", lambda e: errs.append((who_threw(e.stack or "", host), f"{e.name}: {e.message}")))
    # the 404 status of the page itself is expected when auditing the missing-page check
    page.on("console", lambda m: m.type == "error" and not (m.location.get("url", "").rstrip("/") == url.rstrip("/") and " 404 " in m.text)
            and errs.append((where(m.location.get("url", "")), m.text[:300])))
    await page.goto(url, wait_until="load", timeout=60000)
    await page.wait_for_timeout(settle)
    await scroll_all(page)
    return ctx, page, errs


def who_threw(stack, host):
    """own: a frame on the site's origin; 3rd: frames only on other origins; ?: no frames to tell."""
    hosts = {urlparse(t).netloc for t in stack.replace("(", " ").replace(")", " ").split() if t.startswith("http")}
    return "own" if host in hosts else ("3rd" if hosts else "?")


async def flat(page, a, b, vh):
    """Screenshot the band [a, b) and say whether it is really blank (one flat color)."""
    await go_to(page, max(0, a - int(vh * 0.2)))
    await page.wait_for_timeout(600)  # reveals triggered by arriving here
    sy = await page.evaluate("scrollY")
    shot = Image.open(io.BytesIO(await page.screenshot())).convert("L")
    s = shot.width / await page.evaluate("innerWidth")
    # the band in screen coordinates, 20px in from each edge, below a fixed header (top 15% of the screen)
    top = max(a - sy + 20, vh * 0.15)
    bottom = min(b - sy - 20, vh - 10)
    if bottom - top < 60:
        return False
    crop = shot.crop((0, int(top * s), shot.width, int(bottom * s)))
    return ImageStat.Stat(crop).stddev[0] < 2.5


async def audit(a):
    jobs = [(u, w) for u in a.pages for w in WIDTHS] + [(u, w) for u in a.phone_pages for w in PHONES]
    found, report = 0, []
    async with async_playwright() as p:
        for engine in a.engines:
            browser = await getattr(p, engine).launch()
            sem = asyncio.Semaphore(a.jobs)

            async def one(u, spec):
                w, h, phone = spec
                async with sem:
                    row = {"engine": engine, "page": u, "width": w}
                    try:
                        ctx, page, errs = await load(p, browser, engine, a.base.rstrip("/") + u, w, h, phone, a.settle)
                        r = await page.evaluate(PROBE)
                        if r["sw"] > r["vw"]:
                            row["overflow"] = {"page_width": r["sw"], "screen": r["vw"], **(await page.evaluate(BISECT))}
                        blanks = [g for g in r["gaps"] if await flat(page, g[0], g[1], r["vh"])]
                        if blanks:
                            row["blank"] = blanks
                        own = sorted({m for k, m in errs if k == "own"})
                        third = sorted({m[:120] for k, m in errs if k == "3rd"})
                        unknown = sorted({m[:160] for k, m in errs if k == "?"})
                        if unknown:
                            row["unattributed"] = unknown
                        if own:
                            row["errors"] = own
                        if third:
                            row["third_party"] = third
                        await ctx.close()
                    except Exception as e:  # noqa: BLE001
                        row["failed"] = str(e).splitlines()[0]
                    report.append(row)

            await asyncio.gather(*(one(u, s) for u, s in jobs))
            await browser.close()
    report.sort(key=lambda r: (r["engine"], r["page"], r["width"]))
    for r in report:
        bad = [k for k in ("failed", "overflow", "blank", "errors") if k in r]
        if not bad:
            continue
        found += 1
        print(f"{r['engine']:8} {r['page']:28} {r['width']:>5}  " + "  ".join(k.upper() for k in bad))
        if "overflow" in r:
            o = r["overflow"]
            print(f"           page {o['page_width']}px on a {o['screen']}px screen; culprit: {' > '.join(o['path'][-3:]) or '(not isolated)'}")
            for x in o["inner"][:3] + o["pseudo"][:2]:
                print(f"             {x}")
        for g in r.get("blank", []):
            print(f"           blank {g[0]}..{g[1]} ({g[1] - g[0]}px)")
        for m in r.get("errors", [])[:3]:
            print(f"           error {m[:160]}")
        if "failed" in r:
            print(f"           {r['failed']}")
    third = sorted({m for r in report for m in r.get("third_party", [])})
    if third:
        print(f"\nThird-party errors (not ours; check they don't break the page): {len(third)}")
        for m in third[:8]:
            print("  ", m)
    unknown = sorted({m for r in report for m in r.get("unattributed", [])})
    if unknown:
        print(f"\nErrors with no source location (often a browser warning or an embedded player; read each once): {len(unknown)}")
        for m in unknown[:8]:
            print("  ", m)
    print(f"\n{len(report)} loads, {found} with findings.")
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=1)
    return 1 if found else 0


async def helper(a):
    w = a.width
    spec = next((s for s in WIDTHS if s[0] == w), (w, 844 if w < 800 else 900, w < 800))
    async with async_playwright() as p:
        browser = await getattr(p, a.engine).launch()
        ctx, page, errs = await load(p, browser, a.engine, a.base.rstrip("/") + a.page, *spec, a.settle)
        if a.cmd == "bisect":
            print(json.dumps(await page.evaluate(BISECT), indent=1))
        else:
            for y in (a.y or "0").split(","):
                await go_to(page, int(y))
                await page.wait_for_timeout(900)
                out = f"{a.prefix}-{a.engine}-{w}-{y}.png"
                await page.screenshot(path=out)
                print(out)
        await ctx.close()
        await browser.close()
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", nargs="?", default="audit", choices=["audit", "shot", "bisect"])
    ap.add_argument("--base", required=True, help="the preview server, e.g. http://127.0.0.1:4330")
    ap.add_argument("--pages", default="/", help="comma-separated paths, audited at every width")
    ap.add_argument("--phone-pages", default="", help="comma-separated paths audited at phone widths only")
    ap.add_argument("--engines", default="chromium,webkit")
    ap.add_argument("--jobs", type=int, default=3, help="pages loaded at once per engine")
    ap.add_argument("--settle", type=int, default=2500, help="ms to wait after load (loading screens)")
    ap.add_argument("--out", help="write the full report as JSON")
    ap.add_argument("--page", default="/", help="shot/bisect: the path")
    ap.add_argument("--width", type=int, default=390, help="shot/bisect: the width")
    ap.add_argument("--engine", default="webkit", help="shot/bisect: the engine")
    ap.add_argument("--y", help="shot: comma-separated scroll positions")
    ap.add_argument("--prefix", default="shot", help="shot: output file prefix")
    a = ap.parse_args()
    a.pages = [x.strip() for x in a.pages.split(",") if x.strip()]
    a.phone_pages = [x.strip() for x in a.phone_pages.split(",") if x.strip()]
    a.engines = [x.strip() for x in a.engines.split(",") if x.strip()]
    sys.exit(asyncio.run(audit(a) if a.cmd == "audit" else helper(a)))


if __name__ == "__main__":
    main()
