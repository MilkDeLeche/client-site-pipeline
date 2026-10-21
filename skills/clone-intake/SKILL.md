---
name: clone-intake
description: Intake checklist for template clones. Requires a live page URL plus JSX/HTML dumps saved as repo .txt files, captured while scrolled to the section being cloned. Use when cloning a site, redlining a section, starting a design mockup, or when the user pastes a DOM dump, reference.txt, or motion video.
---

# Clone intake

**Pipeline step 2** (`client-site-pipeline`, steps 0–5). Previous: `client-web-delivery`. Next: `clone-workflow`. Do not start cloning until this checklist passes.

Stop and check the kit before building. Missing pieces get guessed. Say which ones are missing, then proceed only if the user wants a guess.

This is the gate in front of `clone-workflow`. Read that skill after intake passes.

## Vet the template first (before collecting anything)

Read `creative-direction.md` (`brand-discovery`). Then check each candidate link, whether it was picked before or after discovery:

| Check | What to record |
|---|---|
| **Template or real company** | Templates: a marketplace page, `*.webflow.io` / `*.framer.website`, "Get template", demo copy. A real company's site (named team, real clients, a "website by" credit) is a reference brand: study it, never clone it. |
| **License** | Free, paid or unclear. Production needs it settled; it goes on the setup-list. |
| **Look** | A plain name plus the designer's term, and whether it matches the chosen direction. |
| **Size** | Screens tall, rough word count, number of sections. |
| **Work it needs** | How many projects or images it takes to look full, against what the client really has (`media-inventory.md`, PRD proof). A layout built for a deep portfolio looks empty with four pieces. |
| **Navigation** | Plain words in the menu? An icon-only menu fails buyers who aren't tech-savvy. |
| **Motion** | How much it moves, and whether toning it down would break it. |
| **Claim slots** | Can the hero and work slots carry the client's real media (video, if that's the work)? Which slots need claims the client can't make (partner logos, awards) and will come out in Phase B? |
| **Phone** | How the first screen and the menu read at phone width. |
| **Clone cost** | Webflow exports readable HTML and CSS that port close to verbatim. Framer generates hashed classes and its own animation runtime: doable, but a slower Phase A. |

Verdict per candidate: **fits**, **fits with noted removals**, or **poor fit**. If two candidates land on the same direction, say so. If the user keeps a poor fit, record the tradeoff and their approval in `creative-direction.md` §7 and clone it faithfully anyway; the mismatch is a Phase B conversation, never a Phase A fix.

## What to collect (you / the user)

**Required every clone**

1. **Live URL** of the template (the real page, not a screenshot of it).
2. **JSX or HTML dump in a `.txt` file in the repo** — never as the only copy in chat.
3. **Motion video** of a full scroll + the hovers that matter.

**Required for each section redline** (hero, services, projects, …)

4. **A dump taken while that section is on screen and settled** — not mid-wipe, not hovered unless the dump is *for* the hover.

**Optional**

- Screenshot — skip if the user says it was captured mid-render.
- TypeUI DESIGN.md / SKILL.md — tokens only. Not a substitute for 1–4.

## The scroll question (this is the part people mix up)

You do **not** need to scroll to the bottom for the footer *tags* to exist.

If the dump tool copied `<main>` or `<body>` from the top, later sections are usually already in the tree.

You **do** need to be looking at a section for its *numbers* to be right.

A dump is a photo of **right now**:

| You are here | What the dump records |
|---|---|
| Top of page | Hero sizes. Later cards may be `clip-path: inset(100%)`, opacity 0, fans at `scaleY(0)` |
| Scrolled until Projects looks finished | Real card width, gap, type, padding |
| Mouse on a button | Pixel-grid / hover styles |

So:

- One **full-page** file from the top = map of the whole tree. Fine.
- One **section** file, scrolled there, named after the section (`projects.txt`) = measurements for that redline. Required when fixing that part.

JSX vs HTML does not matter. Saving to a **file** does (chat truncates). Being **on that spot** matters for sizes, not for “is this HTML in the file.”

## Live URL (this is new — do not skip)

The dump cannot give:

- Original class names and `data-*` hooks (`data-tilt`, `data-scrub`, `data-scroll-animate`)
- Theme CSS (`perspective`, `--card-scale`, clip duration)
- Theme JS (lerp, stagger, cursor-follow)

Fetch the live page. Then fetch linked CSS/JS. Use the dump for numbers. Use the live source for behavior.

If the URL is missing, ask for it. Do not pretend the dump is the source.

**If the live page is a static site you can fetch, save the real HTML, CSS, and
JS to `reference/template/` before building anything.** This is not just
another intake artifact — once it exists, it *outranks* the DOM dump for
structure and outranks your own judgment entirely. `clone-workflow`'s first
build pass should port this close to verbatim (same class names, same CSS
rules), not reinterpret it into a new component/class system. Reinventing a
"faithful" version from scratch when the real source was sitting right there
is the most common way a clone quietly turns into a redesign — see the gate in
`clone-workflow`.

## Agent checklist (start of a clone or section redline)

```
- [ ] Template vetted against creative-direction.md (template, not a real company; license noted; verdict recorded)
- [ ] Live URL in the chat or PRD
- [ ] Dump is a repo .txt (reference.txt, referencenew.txt, projects.txt, …)
- [ ] For this section: dump was captured while that section was on screen
- [ ] Motion video on disk; ffmpeg contact sheet + zoom frames for THIS section
- [ ] Live HTML/CSS/JS fetched, saved to reference/template/, and grepped for data-* / class hooks
- [ ] Client stills exist (no 404 posters)
```

If a box is empty, say so in one line, then either wait or guess with that label.

## File names

```
assets/reference/voltlites-motion.mp4
referencenew.txt              full-page dump (map)
projects.txt                  scrolled to Projects
gear.txt                      scrolled to Gear
```

Do not re-paste a truncated chat dump. Read the file from disk.

## After intake

Follow `clone-workflow`: PRD → clone from dump + live source (verbatim, template's
own branding, no client content yet) → verify against screenshot/video → **only
then** rebrand, from `src/data/` only, touching content and not layout/CSS.
