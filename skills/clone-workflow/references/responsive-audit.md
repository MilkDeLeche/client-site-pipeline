# Responsive and cross-browser audit (end of Phase B)

Phase B changes content inside a layout that was verified at a few widths. Longer names, other photos, added sections, a second language and our own components land at widths and in browsers the template was never checked in. This pass finds what broke, before the Delivery Gate and before anything is shown. It runs on the production build (`npm run build`, then the preview server), never on the dev server.

The pass is evidence, not a look on one phone: every page, six widths, two browser engines, with each finding confirmed by a screenshot and fixed at its cause.

## When

- At the end of Phase B, after the finishing touches and before antislop's Delivery Gate.
- Again after Phase C (forms, popups and banners change the page), and again whenever the builder reports something on a phone.
- After any fix, re-run the whole matrix. A fix at one width often moves a problem to another.

## The matrix

| What | Values |
|---|---|
| Engines | Chromium (Chrome, Edge, Android) and **WebKit (Safari's engine, every iPhone browser)**. Firefox only if the client asks |
| Widths | 320, 360, 390 (phones: touch, 2x, a phone user agent), 768, 1024, 1440 |
| Pages | every built page in the main language at every width; the second language at the phone widths (longer words break phones first) |

Safari is where most layout faults show up. WebKit counts overflow that Chromium hides (a `nowrap` label in a narrow card, an over-wide grid), so a page that is fine in Chrome can slide sideways on an iPhone.

## The tool

`scripts/responsive_audit.py` (the pipeline setup installs Playwright's Chromium and WebKit; it reports `Responsive audit browsers`):

```bash
python scripts/responsive_audit.py --base http://127.0.0.1:4321 \
  --pages "/,/projects,/contact,/privacy,/missing-page" --phone-pages "/es,/es/projects,/es/contact" --out audit.json
python scripts/responsive_audit.py shot   --base <url> --page /x --width 390 --engine webkit --y 1200,2400
python scripts/responsive_audit.py bisect --base <url> --page /x --width 360 --engine webkit
```

In Git Bash, set `MSYS_NO_PATHCONV=1` or Bash rewrites `/x` into a Windows path.

Each load waits for loading screens, then **scrolls the whole page the way a person does** (wheel steps). Smooth-scroll libraries (Lenis, Locomotive, ScrollSmoother) ignore or undo `window.scrollTo`, so a script that jumps never fires in-view triggers and reports sections as blank that aren't, or misses ones that are. Then it checks:

- **OVERFLOW:** the page is wider than the screen. It then hides branches of the DOM one at a time until the width fits and prints the path to the culprit, its widest children and any pseudo-element with content.
- **BLANK:** a band taller than max(260 px, 45% of the screen) with nothing painted. It counts effective opacity (a component left at the server's opacity `.001` paints nothing, even though its children say `1`) and ignores boxes painted the page's own background color. Each candidate is screenshotted and kept only if the pixels are flat.
- **EMOJI:** any character a phone may draw as a color emoji: arrows like ↗ → ↘, stars, checks, play and pause signs, hearts, phones, envelopes, anything from the emoji planes. It scans the page text, every CSS `::before`/`::after` content, and titles, labels and placeholders. iOS turns these into emoji even when the desktop shows a plain glyph. One finding is one fix; there is no "acceptable" emoji on a client site.
- **ERROR:** uncaught errors and console errors from the site's own origin. Third-party errors (embedded players, widgets) are listed apart, and errors with no source location are listed for one read.

## Diagnose before fixing

1. **Look at it.** Open the screenshot for every finding. A detector can be wrong; the picture decides.
2. **Name the element.** `bisect` for overflow. For a blank band, list the elements in that range with their effective opacity, `display`, `visibility` and size.
3. **Ask: ours or the port?** Run the same check on the Phase A copy. If Phase A has it too, it came from the clone (a runtime-only behavior the port never ran). If not, a Phase B change caused it.
4. **Find the rule that does it**, with its media query. Fix that, not the symptom.

## Causes seen so far (and their fixes)

These are examples of the kinds of faults to look for, not a checklist that replaces the run.

| Symptom | Cause | Fix |
|---|---|---|
| Hundreds of px of blank page under a section, phones only | A fixed height tuned for the desktop pin track (sticky cards) applied at every width; the template uses `min-content` below the desktop breakpoint | Scope the override to the breakpoint where the section pins |
| A square or band of nothing where a gallery or slider should be | The template's server markup holds only one breakpoint's variant; the other is rendered by the template's runtime in the browser, which the port doesn't run. Or the component's script was never started for that breakpoint (opacity `.001`, slides `visibility: hidden`) | Show the variant that has the content at that breakpoint (and hide the empty one), or start the component's script for every variant, with its own controls (dots, swipe) |
| Page slides sideways on iPhone by a few px | A `nowrap` label or badge wider than a narrow card; Safari counts it toward page width | Let it wrap inside the card (`max-width: calc(100% - 16px)`, `white-space: normal` on phones) and clip the card |
| Same, in a grid section | A 12-column grid with a phone gap of 32 px: 11 gaps = 352 px, more than a 360 px screen | When every child spans the full row, keep the column gap at the grid's own value and change only the row gap |
| Same, in a footer or table | `1fr` columns grow to fit a long email or URL | `minmax(0, 1fr)` and `overflow-wrap: anywhere` on the cells |
| "Watch the walkthrough ↗" shows a color emoji arrow on iPhone | The ↗ character (U+2197) in copy and in a CSS `content` string; iOS draws it as an emoji | An inline SVG arrow after the text (`stroke="currentColor"`, about 0.7em, `aria-hidden`), or, inside a pseudo-element, the SVG as a `background-image` with padding for it. The words carry the meaning; the arrow is decoration |
| A Safari-only page error from a map | The map iframe has no fullscreen permission and its control checks for it | `allow="fullscreen" allowfullscreen` on the iframe |
| "No supported source" from an embedded video, Chromium only | Playwright's Chromium ships without H.264; real Chrome has it | None. Note it as a test-browser limit |

## Fix rules

- **Never a character that can turn into an emoji.** No arrow, star, check, play sign, heart or symbol character in copy, labels, buttons or CSS `content`, in any language. Icons are inline SVG (or the template's own icon font, if it has one). Variation selectors (U+FE0E) don't reliably stop it, so don't rely on them.
- Fix at the cause, scoped to the breakpoint that needs it, with a comment that says what broke and why the rule exists.
- Never `overflow-x: hidden` on `html` or `body` to hide a sideways scroll (see "Gotchas"): it hides the symptom, breaks sticky elements and the vertical scroll, and the real fault stays.
- Template CSS stays as it is. The fix goes in the rebrand stylesheet or the behaviors script.
- After the fixes: rebuild, re-run the full matrix, open the screenshots of every section that changed, and write the result in the project status (what was found, the cause, the fix, what's left and why).

## Done when

- Zero OVERFLOW, BLANK, EMOJI and own-origin ERROR findings across the matrix, or each remaining one explained in the status file (a third-party error, a test-browser limit).
- Screenshots opened for every fixed section, at a phone width in WebKit and at desktop in Chromium.
- The builder told plainly what was tested and how: engines, widths, page count. It was not a real iPhone unless one was used.
