# Logo loading animation

A short loader that builds the client's logo on the loading screen, before the home page shows. A pitch with several design options gets one per design, each in that design's look. About 2–2.5 seconds of motion; the screen leaves once the mark is complete and the page has loaded, whichever is later.

**Credits: one generation per generated loader.** Write the strongest prompt you can, preflight the cost, submit once, and use what comes back. No retakes, variants or "let's see if it's perfect" rounds. Fix small faults in code. A second generation happens only when the builder asks for it, after you've told them what it costs. Coded loaders cost no credits.

## 0. Study the brand, then ask: coded or video?

Before proposing anything, study:

- **The logo's construction.** Is it geometric (straight lines, hexagons, grids, an isometric cube), a monoline drawing, a wordmark, a script or signature, an emblem with fine detail, or a photo-like mark?
- **The colors**, exactly, from the largest logo file, and which of them is the background on each design.
- **The trade and how its own world shows things.** Architecture and building show linework, construction lines, isometric views and title blocks. Food shows hand-drawn strokes. Tech shows grids and pixels.
- **Each design's look**: its background, line weight, type and how its own motion feels (fade, slide, curtain, spring).

Then **ask the builder which they want, coded or video**, with a short recommendation and the reason:

| | Coded (SVG + CSS) | Video (image-to-video, reversed) |
|---|---|---|
| Fits | Geometric, monoline or wordmark logos; anything built from clean lines | Detailed or organic marks; materials (metal, glass, ink, 3D) that code can't fake well |
| Looks | Exact and crisp at any size, brand colors exact the whole time | Rich, cinematic; the model invents the in-between frames |
| Cost | No credits; about 2 KB; runs from the first paint | About 200 credits per clip at the cheap tier, one generation; 100–300 KB |
| Risk | Takes careful timing work | The model's idea can miss ("made no sense"); the background drifts a little |

On the first job (a building designer whose mark is a geometric hexagon cube), the builder rejected two generated clips (ink bleeding into paper, glossy spheres) as making no sense for the brand. They kept a generated "blueprint lines" clip, and then preferred coded loaders for all three designs: the outline drawn on, an isometric face assembly, and a blueprint construction. For a geometric logo in a design or building trade, recommend coded.

## 1. Pick the idea per design

One idea per design, from the logo's construction and the trade, each different from the others. From the first job:

| Design look | Coded idea | How it moves |
|---|---|---|
| Dark navy, editorial (the builder's favorite) | **Blueprint construction** | Faint drafting guides sweep across the screen along the mark's own axes; gold points tick in at its corners; a white hairline draws the mark; the gold and white fill in (the letters wipe up); editorial corner labels (name, trade, city) and a 00→100 count with a hairline progress bar; the screen lifts away like a curtain |
| Cream, drafting sheet | **Outline draw-on** | A navy hairline draws the outer shape, the inner shape and the letters in turn while a small 00→100 count runs; then the real colors fill in |
| White, warm, rounded | **Isometric assembly** | A gold hairline outline draws; the mark's three cube faces slide in along their own axes and lock together; a soft shadow grows; the name fades in under it |

Other ideas: a stroke reveal along a signature's path (script logos), letters stacking in on a baseline grid (wordmarks), a mask wipe behind a ruler or title block (print), panels slicing into place (grid brands).

## 2. Coded: build it

1. **Trace the logo into vector paths** from the largest file, unless the client has an SVG. For flat-color logos, separate each color by threshold, then `cv2.findContours` and `cv2.approxPolyDP` (epsilon about 2.5 px at 1000 px tall) give clean polygons. Render the SVG next to the original and compare before using it.
2. **Layers per mark:** the fill paths in the real colors (`fill-rule="evenodd"` for rings), plus outline copies with `pathLength="1"`, `stroke-dasharray:1` and `stroke-dashoffset:1` that animate to 0 (the draw-on).
3. **Animate in CSS only**, with `@keyframes` and delays, so it starts at first paint before any script runs. Fills come in with an opacity fade or a `clip-path: inset()` wipe. A count can be pure CSS: `@property --n { syntax: "<integer>" }` animated to 100, shown with `counter-reset: n var(--n)` and `content: counter(n, decimal-leading-zero)`.
4. **Pieces that move apart** (cube faces, panels): clip a copy of the whole mark per piece with `<clipPath>`, translate each group along its own axis, then show the whole unclipped mark on top as they land, which hides hairline seams.
5. **Leave** once the mark is complete **and** the page's `load` has fired; hold about 0.4 s, then fade, or lift as a curtain (`translateY(-100%)`, `cubic-bezier(.76,0,.24,1)`, 0.9 s) where the design's own motion is bold. Cap the screen at 6 s. Reduced motion skips it.
6. **Text on the screen** (name, trade, city) comes from the facts file and follows the page language; numbers need no translation.
7. If the template already has a preloader, put the mark inside it and start the template's own exit when the mark is done.

## 3. Video: build it

1. **The start frame is the real logo**, square, centered at about a third of the width, on the loading screen's background color, built from the largest logo file (a small PNG scaled up gives jagged edges that the model copies). Brand colors and shapes are never redrawn, inverted or "improved".
2. **Prompt the logo coming apart, then reverse the clip.** Image-to-video models start from an image but can't promise to end on one, so prompt the mark coming apart in the chosen style, then reverse it (`ffmpeg -vf reverse`). The reversed clip builds the mark and ends on the real logo file.

   > Premium motion-graphics logo animation, [flat 2D vector / soft 3D], locked-off camera, no camera movement. [Background] stays flat and clean the whole time. The [logo's colors and shapes, described] [come apart how], then [fade / drift out], leaving only empty [background]. [Mood]. No text, no extra objects[, plus whatever the model tends to add].

   Image-to-video, the shortest length (3 s on Kling), 1:1, the cheapest tier of the model the builder names (on the first job, "Kling's newest, cheap option" was Kling 4.0 Flash, about 209 credits per clip). List models live: names and prices change.
3. **Encode:**

   ```bash
   ffmpeg -i raw.mp4 -vf "reverse,setpts=PTS/1.2,scale=640:640:flags=lanczos,format=yuv420p" -an \
     -c:v libx264 -preset slow -crf 24 -movflags +faststart public/assets/client/loader/d1.mp4
   ffmpeg -i raw.mp4 -vf "select=eq(n\,0),scale=640:640" -frames:v 1 -q:v 3 public/assets/client/loader/d1-end.jpg
   ```

   The raw first frame is the poster, so a phone that blocks autoplay still shows the logo. Sample the clip's corner color for the screen's background, and feather the video's edge with a radial `mask-image`.
4. **On the page:** `<video muted playsinline autoplay preload="auto" poster=…>`, about 320 px wide (62vw on phones); on `ended` hold about 0.5 s, then leave; if `play()` is refused, show the poster for about 1.2 s and go on; cap at 5 s.

## 4. Check

- Capture each loader frame by frame in a real browser (a screenshot about every 300 ms), on desktop and a phone, in both site languages.
- The last state is the logo, colors exact. Guides and labels fit the screen at phone width. The screen is gone by about 3 s on a fast load, with no console errors.
- Report each loader in a sentence. Say plainly if one came out weaker. Don't regenerate a video on your own.
