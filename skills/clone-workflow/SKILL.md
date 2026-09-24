---
name: clone-workflow
description: Clone a real website into a client-ready Astro mockup at near-100% visual fidelity, then rebrand it for a different business. Use when handed a template to clone, a computed-style DOM dump, a reference screenshot, or a screen recording of a site's scroll/hover motion — or when asked to build website concepts or mockups for a business based on an existing site. Covers reading motion out of a video with ffmpeg contact sheets, motion implementation rules, folder conventions, and content-integrity rules for the rebrand pass.
---

# Template Clone Workflow

**Pipeline step 3 of 5** (`client-site-pipeline`). Previous: `clone-intake`. Next: `launch-audit`. If the live URL, repo `.txt` dump, or motion video is missing, go back to `clone-intake` first.

Turn a real website into a client-ready mockup for a different business, in Astro,
at near-100% visual fidelity — then swap the content.

## The idea

The reason this works is that **no single input is enough on its own.** Each
input carries information the others are missing:

| Input | What it carries | What it CAN'T tell you |
|---|---|---|
| **Code** (computed-style DOM dump, `.txt` in the repo) | Exact structure, spacing, sizes, radii — at the scroll/hover freeze you copied | Fonts, motion, original JS/`data-*` hooks |
| **Live URL** | Source HTML, CSS, JS (`data-tilt`, scrub, real class names) | Exact computed px at a given scroll |
| **Screenshot** | Typeface, true colors | Precise measurements, anything animated |
| **Motion video** | Every animation, transition, scroll behavior | Precise measurements |

> **The key insight, in the client's words:** *"most of the styles that I want are
> rendered — they are not in the code."*
> A DOM dump is a snapshot of one frozen moment. Hover states, scroll reveals, nav
> transformations, marquees, parallax — none of it is in there. That's why the
> video exists, and why it is not optional.

If the user supplies only one or two of the three, say which one is missing and
what will be guessed without it, then proceed.

**Fourth input (new, required):** the **live URL**. The dump is a freeze of
computed sizes. It is not the site's source. Fetch the page and its CSS/JS for
`data-*` hooks, tilt/scrub math, and real class names. TypeUI DESIGN.md files
are tokens only — they do not replace the URL or the video.

**If the template turns out to be a live site you can fetch** (most are), the
fetched HTML + CSS is not "one more input among four" — it is the **primary
source**, ranked above the DOM dump and above your own judgment. See the gate
below before writing a single line of your own CSS.

---

## The non-negotiable gate: clone first, rebrand later — as two separate, verified phases

This is the rule the rest of this doc assumes. Violating it is the single most
common way a "clone" turns into a redesign that happens to be inspired by the
original.

**Phase A — Template clone. Zero client content.**

- If you fetched real source (`reference/template/*.html`, `*.css`, `*.js`),
  **port it into the framework close to verbatim.** Same class names, same
  CSS rules, same DOM nesting. Do not invent a new class system, a new type
  scale, or `clamp()`-based "equivalents" of the source's sizes — copy the
  source's actual values. Reinterpreting the template into your own component
  library is redesigning it, even when you're trying to be faithful.
- Keep the **template's own** colors, fonts, copy, and images for this phase —
  yes, even if a PRD or client data file already exists. Swapping brand color
  or font before the template is verified means you're now debugging your
  redesign against a moving target, not the template.
- Keep the template's **own motion stack** where practical (the real GSAP/
  Lenis/Splide/whatever scripts, or the copies saved during intake) rather
  than a simplified hand-rolled substitute — a simplified reveal is a design
  decision, and this phase has none of those yet.
- Place this at a clearly separate, clearly labeled location (e.g. `/` while
  nothing else is built yet, or `/design-1/` / `/template/` once other routes
  exist) — never mixed into the same files as a prior rebrand attempt. If a
  previous rebrand pass already exists, move it aside (e.g. `/wip/`) rather
  than deleting it or building the faithful clone on top of it.
- **Verify against the screenshot and the video, section by section, before
  calling Phase A done.** This is step 3 below — it is not optional and it is
  not the same as "it built without errors."

**Phase B — Rebrand. Starts only after Phase A is verified** (against the
reference media, and ideally with the user's explicit sign-off that the
template matches). Phase B changes **content only** — copy, images, links,
logo, and yes, brand colors and fonts once the client's identity calls for it.
It does **not** touch layout, spacing, or DOM structure inherited from Phase A
unless the user explicitly asks for a structural change.

### Red flags that mean you skipped the gate

Catch these in your own work before the user has to:

- You wrote new CSS class names instead of reusing the fetched stylesheet's.
- You built a `clamp()`-based fluid type scale instead of transcribing the
  source's actual sizes at each breakpoint.
- Brand colors, fonts, or client copy appear in the same commit/pass as the
  initial clone.
- A section from the reference is missing, simplified, or "improved" with no
  note explaining why (e.g. the content genuinely doesn't apply to the client
  — that's a Phase B decision, not something to pre-decide in Phase A).
- The motion feels like a generic fade-in-on-scroll rather than what the video
  actually shows.

If you notice any of these in progress, stop and say so — don't quietly
continue and hope it reads as "close enough."

### If you're reviewing another agent's clone and it failed this gate

Say exactly what's wrong, not just "try again":

> Stop. You redesigned. Reset to the fetched source in `reference/template/`
> (or the live URL if that doesn't exist), keep the template's own colors/
> fonts/copy, and don't touch client styling until template QA passes against
> the screenshot and video.

### Do not delegate Phase A

Never hand Phase A — the verbatim clone (markup, CSS, DOM nesting) and its
section-by-section screenshot QA — to a subagent. Checking a subagent's work
afterward is the backup plan, not the plan: reviewing a redesign still burns
the context the delegation was supposed to save, and then you rebuild it
anyway once it fails the gate. **The parent agent ports the fetched source
and diffs it, in this conversation.**

Subagents may still do mechanical work that carries no fidelity judgment:
downloading images, ffmpeg compression, scaffolding an empty Astro project,
fetching live HTML/CSS into `reference/template/`. "Faithfully reproduce this
layout" is not a valid subagent prompt — it is exactly the instruction a
subagent will quietly "improve" into a redesign.

Context pressure is not an exception. If the page is huge, clone it section
by section in this thread. Do not offload the layout to another model to
"save context" — that is how a redesign gets shipped as done.

### "Verified" is evidence, not a claim

You may not tell the user Phase A is done unless you — personally, in this
conversation — compared:

- Header/nav structure against `reference/template/` or the live URL, not
  against another agent's description of it.
- One screenshot crop per major section against the running clone.
- The red-flag list above: invented class system, `clamp()` type, client
  content mixed in, missing/simplified sections.

A green `astro build` does not count. "No fake testimonials" does not count.
Another agent's "I verified it" does not count. If you didn't open the source
and look, you didn't verify.

---

**Where you sit when you copy the dump matters for numbers, not for whether
the HTML exists.** A top-of-page copy of `<main>` often includes later
sections as tags, but cards still off-screen may dump as `clip-path: inset(100%)`
or `opacity: 0`. For a section redline, scroll until that section looks
settled, then save a `.txt` in the repo (chat truncates). See `clone-intake`.

---

## Intake (do this before step 1)

Follow the `clone-intake` skill. Do not start cloning until you have, or have
named as missing:

1. Live URL
2. JSX/HTML dump as a repo `.txt` (full page and/or per-section, scrolled there)
3. Motion video

---

## The steps

### 1. PRD first

Research the target business (their site, Instagram, delivery listings, review
sites, local directories) and write `PRD.md`: what they sell, their real
differentiators, hours, address, phone, ordering links, tone.

This is the content that gets plugged into every design later. Do it **first** so
the rebrand pass is a lookup, not an invention.

Put every business fact in **one data file** (see `src/data/`), never inline in
components. Phone, address, map link, ordering URLs — one source of truth.

### 2. Clone the template from the code

Build it in Astro at full fidelity, as **Phase A** above: template's own
markup, CSS, colors, fonts, copy, images. **Do not restructure, do not
"improve".** If you have fetched real HTML/CSS, port it close to verbatim —
transcribe the measured values exactly, don't re-derive them through a new
class or type system. This is what makes it look like the original, not a
sincere impression of it.

### 3. Verify against the screenshot, and fix

This step is not optional and it is where the real errors surface. On the project
this workflow came from, the screenshot revealed:

- The display font was a **Didone serif**, not the light sans the dump implied
  (dumps carry no `font-family` at all)
- Exact colors, sampled per-pixel rather than guessed
- A footer that was dark, not cream
- Sections that existed but weren't in the truncated paste

### 4. Apply the motion from the video

See "Reading a motion video" below. Do this **last** — animating a layout that's
still wrong is wasted work.

### 5. Rebrand

This is **Phase B** — do not start it until Phase A (step 3's verification) has
passed and, ideally, the user has said the template matches. Swap content only:
copy, images, links, logo, brand colors and fonts. **Never touch layout or DOM
structure** unless explicitly asked. If the client says "only replace images,
not the template," that means the `<style>` blocks stay byte-identical — prove
it by only editing frontmatter and markup.

---

## Reading a motion video

Requires ffmpeg (`winget install Gyan.FFmpeg`, once per machine, forever).

Reading frames one at a time is slow and burns context. **Tile them instead** —
survey wide, then zoom narrow.

```bash
# 1. SURVEY — whole video at 1fps as a 6x4 grid. One image, entire timeline.
ffmpeg -i motions.mp4 -vf "fps=1,scale=300:-1,tile=6x4" -frames:v 1 contact.png

# 2. ZOOM — one moment at 10fps, cropped to the region that matters.
ffmpeg -ss 18.2 -t 2.6 -i motions.mp4 \
  -vf "fps=10,crop=1884:420:0:0,scale=440:-1,tile=4x6" -frames:v 1 detail.png

# Probe first if you need duration / resolution:
ffprobe motions.mp4
```

`crop=W:H:X:Y` is worth learning — cropping to just the nav or just the hero
before tiling makes small motions readable at thumbnail scale.

### Writing the motion down before building it

For each animated element, record: trigger, properties, start → end, duration,
delay/stagger, easing, and **a confidence level**. Mark each as `high` (visible
directly in frames), `medium` (inferred), or `guess` (pattern-matching). Say what
you assumed on every guess. Three honest guesses beat nine confident fabrications.

### Motion implementation rules

1. **No new dependencies.** CSS + IntersectionObserver covers almost everything.
2. **One source of truth for timing** — a single `--motion-*` custom property
   block. The feel gets tuned there, not hunted across files.
3. **Animate `transform`, `opacity`, `filter`.** Never `top`/`left`/`width`/`height`.
4. **Fail visible.** The hidden start state must come from a class JS adds
   (e.g. `.motion-ready`), never baked into base CSS. If the script dies, content
   still reads instead of being stranded at `opacity: 0`.
5. **Respect `prefers-reduced-motion`** — land elements in their final state
   immediately, never stranded.
6. **Clean up** — disconnect observers, remove listeners on teardown.

### Motion hiding in the markup

Sometimes the code *does* encode the animation, and it's a gift. On one design every
headline word sat in its own `overflow: clip` wrapper containing an inner div —
that's a masked word-reveal, spelled out. The giveaway confirming it:

```css
@media (prefers-reduced-motion: no-preference) { .wrapper { padding-bottom: 3px } }
```

Padding added *only when motion is allowed* exists to stop descenders being shaved
mid-animation. If you see that pattern, you've found a mask reveal.

---

## Folder conventions

```
PRD.md                          business research, written first
src/data/<client>.ts            every business fact, one place
reference/template/             fetched real HTML/CSS/JS, when the template is a live site — primary source for Phase A
src/pages/index.astro           concept picker (links every design) — or the Phase A template clone, before rebrand begins
src/pages/design-N/index.astro  one page per concept
src/components/designN/         components, namespaced per concept
src/styles/designN.css          tokens + motion block, per concept
public/assets/designN/          that concept's art
assets/reference/               screenshots + videos (not served)
```

If a rebrand attempt already exists when you're asked to redo the template
clone properly, move it aside (e.g. `/wip/`) rather than deleting it or
overwriting it with the faithful clone — the user may still want to compare or
recover content from it.

Each design is fully self-contained, so concepts can't bleed into each other and
losing one never touches the others. Every design links back to the picker with a
button styled in **its own** design language.

Keep reference material out of `public/` — it ships to the CDN otherwise. One
project shipped a 179MB bundle that way; moving it out took it to 1.8MB.

---

## Gotchas paid for in real time

- **The 50k paste limit.** Big DOM dumps get truncated mid-file, usually inside a
  huge inline SVG. Don't re-paste — have the client save it to a `.txt` in the repo
  and read it from disk. Same for screenshots: a file path beats a chat attachment.
- **Media queries reveal truncated structure.** When a paste dies early, the
  `@media` block at the top still names IDs from sections you never received —
  carousel arrow positions, grid columns, footer layout. You can reconstruct a
  surprising amount from those rules alone.
- **`overflow-x: hidden` on `html`/`body` kills vertical scrolling.** Hidden on one
  axis forces the other to `auto`, making those elements scroll containers. Use
  `overflow-x: clip` — it contains horizontal bleed without creating one.
- **Percentage margins resolve against the containing block**, not the element. A
  negative-margin full-bleed trick computed against the wrong box silently becomes
  zero. Use absolute lengths or a CSS variable holding the resolved width.
- **Full-page screenshot tools break on scroll-driven sites.** Sections overlap,
  the bottom half comes back blank, and heroes get captured mid-transition — on one
  project that made a hero look like it had no text when it did. Trust the video
  over the screenshot for anything animated.
- **JSX whitespace leaks into rendered text.** `{value}\n{suffix}` renders as
  `730 +`, not `730+`. Use a single template literal.
- **Astro inlines small scripts and stylesheets** rather than emitting separate
  files. Don't conclude an asset "isn't shipping" because `dist/_astro/` looks
  empty — grep the HTML.
- **Fonts are never in a computed-style dump.** Always identify the typeface from
  the screenshot, zooming in on a heading if needed.

---

## Content integrity when rebranding

- Don't invent press credentials. If the reference has a Vogue/Forbes logo row and
  the client has none, swap it for something true — where they're actually
  reviewed, or their ordering partners.
- Don't fabricate named testimonials. Paraphrase praise that recurs in their real
  public reviews and attribute it to the platform, not to an invented person.
- Flag unverified facts rather than shipping them silently. Hours in particular
  tend to disagree across sources — mark them and confirm with the owner.
- Placeholder art should be dimension-exact so swapping in the real photo can't
  shift the layout.
