"""Make a launch reel from the real site and from coded animations (references/launch-reel.md).

    python reel.py record <url or file.html> <out.mp4> [--size 412x952] [--seconds 12] [--scroll]
    python reel.py join   <out.mp4> <a.mp4> <b.mp4> [...]

record  films a page in real Chrome. With --scroll it scrolls the live site the
        way a thumb would (hold, glide down, hold), which is the screen
        recording for a mockup. Without it, it films an animated HTML card for
        its length: the animation is written in code, so every word stays sharp.
        To show it in a phone, film assets/reel-phone-frame.html, which plays the
        recording inside a phone drawn in code (record without --scroll).
join    plays clips of the same size one after another.

Nothing here generates video: the site on the screen is the real site, moving.
Needs: Google Chrome, ffmpeg, pip install playwright
"""
import argparse
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

FPS = 30


def size_of(text):
    try:
        w, h = (int(v) for v in text.lower().split("x"))
        return w, h
    except ValueError:
        sys.exit("A size looks like 1080x1920")


def ffmpeg(*args):
    exe = shutil.which("ffmpeg")
    if not exe:
        sys.exit("ffmpeg not found. Run the pipeline setup (client-site-pipeline/scripts/setup.mjs).")
    done = subprocess.run([exe, "-y", "-loglevel", "error", *args])
    if done.returncode:
        sys.exit("ffmpeg failed")


def record(a):
    from playwright.sync_api import sync_playwright

    width, height = size_of(a.size)
    target = a.source if a.source.startswith(("http://", "https://")) else Path(a.source).resolve().as_uri()
    phone = width < 600
    with tempfile.TemporaryDirectory() as tmp, sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome")
        options = dict(viewport={"width": width, "height": height}, record_video_dir=tmp,
                       record_video_size={"width": width, "height": height})
        if phone:
            options.update(is_mobile=True, has_touch=True, user_agent=(
                "Mozilla/5.0 (Linux; Android 14; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Mobile Safari/537.36"))
        context = browser.new_context(**options)
        started = time.time()
        page = context.new_page()
        page.goto(target, wait_until="networkidle" if a.scroll else "load", timeout=60000)
        if a.scroll:
            page.wait_for_timeout(1500)  # let the first screen settle before filming it
        else:
            page.reload(wait_until="load")  # start the card's animation at the first frame we keep
        ready = time.time() - started
        if a.scroll:
            # Hold, glide, hold. Wheel events move smooth-scroll sites too, where scrollTo does not.
            distance = page.evaluate("Math.min(document.documentElement.scrollHeight - innerHeight, innerHeight * 5)")
            hold, steps = 1.0, int((a.seconds - 2.0) * FPS)
            page.mouse.move(width / 2, height / 2)
            page.wait_for_timeout(int(hold * 1000))
            ease = lambda t: t * t * (3 - 2 * t)
            for i in range(steps):
                page.mouse.wheel(0, distance * (ease((i + 1) / steps) - ease(i / steps)))
                page.wait_for_timeout(1000 / FPS)
            page.wait_for_timeout(int(hold * 1000))
        else:
            page.wait_for_timeout(int(a.seconds * 1000))
        video = page.video
        context.close()
        browser.close()
        ffmpeg("-ss", f"{ready:.2f}", "-i", video.path(), "-t", str(a.seconds), "-r", str(FPS),
               "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "16", "-movflags", "+faststart", a.out)
    print(f"recorded {a.out} ({width}x{height}, {a.seconds}s)")


def join(a):
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8") as listing:
        for clip in a.clips:
            listing.write(f"file '{Path(clip).resolve().as_posix()}'\n")
    # Re-encode instead of copying streams, so clips recorded in different ways still join cleanly.
    ffmpeg("-f", "concat", "-safe", "0", "-i", listing.name, "-r", str(FPS), "-c:v", "libx264", "-pix_fmt", "yuv420p",
           "-crf", "17", "-movflags", "+faststart", a.out)
    Path(listing.name).unlink(missing_ok=True)
    print(f"joined {len(a.clips)} clips -> {a.out}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("record")
    r.add_argument("source")
    r.add_argument("out")
    r.add_argument("--size", default="412x952")
    r.add_argument("--seconds", type=float, default=12)
    r.add_argument("--scroll", action="store_true")
    j = sub.add_parser("join")
    j.add_argument("out")
    j.add_argument("clips", nargs="+")
    a = ap.parse_args()
    {"record": record, "join": join}[a.cmd](a)


if __name__ == "__main__":
    main()
