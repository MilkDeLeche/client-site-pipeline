---
name: motion-template
description: Turn a motion-site prompt template (a long "recreate this page exactly" prompt with hosted asset URLs, layers, timings and fonts, such as a scroll-scene or frame-sequence site) into a site for a different client, with the client's own work as the art. Studies how the template works, works out what assets it needs, maps each asset to the client, and hands the builder an asset plan with models and credit costs to approve before anything is generated. Then generates each asset once, clones the template as given with the client's art and copy, and checks it against the template. Use when the builder pastes a motion-site prompt or template, says "recreate this for <client>", "use this style for the design picker", "make the hero like this site", or wants the options shelf built as a motion site. Also makes the logo loading animation for each design (coded in SVG + CSS, or a generated clip reversed so it ends on the real logo; it studies the brand and asks the builder which), when the builder asks for a loader, a "Lottie-like" or motion-graphics logo, or a loading screen. Not a pipeline step: used inside Phase B (the options shelf, a hero) after the facts and copy exist.
---

# Motion template

No two motion templates are the same. Each prompt is written for one fictional brand and points at that brand's hosted assets. What's worth keeping is how it works: what moves, what drives it, how the parts hand off, how it looks. This skill clones the template as given, with the client's work as the art and the client's words as the copy.

Think like a cloner, not a designer:

- **Study** how the template works, until you could explain every moving part.
- **Work out** what kind of assets it needs to work that way.
- **Produce** the same kind of assets from the client's work.
- **Build** the same site.

The template is the spec. Where it gives a value (a layer order, a timing, a position, a font), use it. Change only what has to change for this client.

## Steps

1. **Study the template.** Read the whole prompt and write down, in your own words:
   - **What it is:** scenes or sections, and what the visitor sees in each.
   - **What drives the motion:** native scroll, wheel or keys hijacked, scroll position scrubbing something, time, hover.
   - **How the parts are built:** separate layers, a video, frames, a canvas, shaders, plain images with effects.
   - **The rules it states:** timings, easing, stacking order, positions, breakpoints, fonts, colors.
   - **Every asset:** URL, size, transparency, what it shows, its role.

   Download a few assets and look at them, to learn the art style. They're study and style reference only and never ship. `references/techniques.md` lists techniques seen so far as a starting point. A new template may use something that isn't on it. Then study it the same way.
2. **Work out the assets for this client.** For each template asset, decide what replaces it while keeping its role, shape, transparency and style:
   - a real client file, when one fits
   - an AI asset made from a client file, with their real work as the subject and the template's own asset as a technique-only style reference
   - code, which is free

   Carry the template's look over: the same art style, the same kind of asset, the same framing. Change the subject, the place and the palette to the client's. If the page repeats a subject (scenes, cards, slides), use a different real client project in each.
3. **Hand the builder the asset plan, then wait.** Fill in `assets/asset-plan-template.md`:
   - how the template works, in plain words
   - every asset to make, with its model, size and transparency, and a credit quote from `preflight`
   - the total
   - what's free

   Say what the technique needs ("this one scrubs a video, so it needs one short clip"). **Generate nothing until the builder says yes.**
4. **Generate once per asset.** Write the strongest prompt up front: describe the template's art style in detail first, then the client subject, place, palette, composition and clean surfaces. Submit each asset once and use what comes back. Don't run retake rounds or variants. Fix small faults in code (crop, trim, composite, cover a stray mark). A new generation happens only when the builder asks, after you've said what it costs. Where several assets must match (layers of one scene, frames of one clip), make them from one approved source so they share a look.
5. **Process and log.** Size and format each asset the way the template uses it. Log every AI asset in the project's `image-prompts.md` (prompt, model, references, use, alt) and in `media-inventory.md` (origin `AI-generated`, the only slots it may enter).
6. **Clone the template as given.** Build what the template specifies, in its order, with its values: structure, motion, stacking, timings, input, fonts, breakpoints. Swap in the client's assets, the client's copy and the client's brand colors. `references/build-and-check.md` has the general build rules.
7. **Check it against the template.** Every part should behave the way the template says, and the client's assets should sit where the template's did. That covers the same stacking, the same grounding and the same framing. Check desktop and phone, in each language, with no console errors and real clicks on every control. Then hand over with the final credit cost.

## Rules that don't bend

- **The client's work is the subject.** AI may redraw a real client project in the template's style for showcase art, labeled "Illustration of …". It never invents a project and calls it theirs, and it never fills a "this is our work" or proof slot (`clone-workflow` → `references/image-prompts.md`).
- **No other company's marks.** That means no real firms' logos, seals, signatures or names, on drawings, cards or anywhere else. Showing a partner's logo needs that partner's permission, so put the question on the setup-list.
- **Template assets never ship.** Not their URLs, their copy, their names, or their brand.
- **One generation per asset.** The builder decides on retakes.
- **Brand identity holds.** The client's logo keeps its real colors. Never use a blend, filter or effect that alters it, and keep accents on the client's palette.
- **Copy comes from the client first.** Use their published words. Only when they have nothing for a slot, write it with `copywriting` and `antislop-copywriting`. Make no claims or counts the facts file can't back.
- **Unlisted showcase pages** keep `noindex` and stay out of the sitemap and nav (`design-options-shelf.md`).

## Files

| File | Use |
|---|---|
| `references/techniques.md` | Techniques seen so far: how to recognize them, what assets they need, which models make them. A starting point, not a full list |
| `references/logo-loader.md` | The logo loading animation: study the brand, ask coded or video, ideas per design, tracing the logo to SVG, the reversed-clip trick, page code, checks |
| `references/build-and-check.md` | General build rules, the verification list, and a worked example from the first job |
| `assets/asset-plan-template.md` | The plan the builder approves before any credits are spent |
