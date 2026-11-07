# Motion techniques: how to spot them and what they need

The techniques seen so far, as a starting point. Templates vary, and a new one may combine these or do something else entirely. Either way, study it first: what moves, what drives it, how the parts are built, and what assets that takes. Always list models live (`krea-generate`) and preflight the cost: the names below were current when this was written and change often.

## A. Layered cut-out scenes

**How to spot it in the prompt:**
- "sky plate", "foreground band", "cut-out sheet", sprite boxes `[x, y, w, h]`, `clip-path` hulls
- "the page never scrolls natively"
- transitions "as a pure function of time t", with going up running t backwards
- scenes counted 1–5, "loops back into scene 1"

**What it is:** full-screen scenes built from separate layers that move on their own (sky, ground band, buildings, trees, animals, people). Wheel, keys, swipe or a nav link plays a choreographed transition between scenes.

**Assets per scene** (made from the approved cover so every layer matches):

| Layer | Model (2026-11) | Notes |
|---|---|---|
| Sky plate | `gpt-image-2.5-sunburst`, opaque, 16:9 2K | The cover with the subject, lawn and trees removed; a flat horizon low in the frame |
| Ground band | `gpt-image-2.5-flare`, `background: transparent` | The bottom third only; transparent above an uneven top edge |
| Subject cut-out | flare, transparent | The client's real building or product, isolated, with its base on a straight line |
| Side elements | flare, transparent, 9:16 | Trees or palms, one cluster per file |
| Intro plate and band | sunburst plus flare, with the template plate as technique reference | No client subject: just the place |

Single cut-outs per file are easier than the template's sprite sheets: no box math, no clip hulls. Trim each to its alpha bounds in code.

**Cost on the first job:** 4 layers × 3 scenes + 2 intro layers = 14 images, about 127 credits each at 2K, so about 1,780 credits. The covers they came from were 3 more.

## B. Scroll-scrubbed frame sequence

**How to spot it in the prompt:**
- "image sequence", "frames", "canvas", `frame_0001.jpg … frame_0240.jpg`
- "scrub", "the video plays as you scroll", "sticky section N×100vh tall"
- an Apple-style product spin or a camera fly-through

**What it is:** a video cut into still frames, drawn to a `<canvas>` from scroll progress inside a tall sticky section. Scrolling down plays it forward; scrolling up plays it back.

**Assets:**
- **One video clip, image-to-video, started from a client image** (their rendering or the approved cover as the start frame, and an end frame if the model supports it). Pick the cheapest model that meets the length: Kling 4.0 Flash (`kling/kling-4-flash`, up to 20 s at 720p) is the default ask. Hailuo 2.3 Fast, Seedance 1.0 Pro Fast and Veo 3.1 Lite are the other low-cost options. Ask for one slow, continuous camera move with no cuts; the frames must flow. 5–8 seconds is plenty.
- **Frames:** cut in code with ffmpeg, which costs no credits:
  ```bash
  ffmpeg -i hero.mp4 -vf "fps=24,scale=1600:-2" -q:v 80 frames/f_%04d.webp
  ffmpeg -i hero.mp4 -vf "fps=12,scale=900:-2"  -q:v 75 frames-m/f_%04d.webp   # phone set
  ```
  6 s at 24 fps is 144 frames. Keep the desktop set under about 12 MB.
- **Build:**
  - preload the first 10 frames before showing the canvas, then the rest in the background
  - draw on `requestAnimationFrame` from `scrollProgress × (frameCount − 1)`, with cover-fit math for the canvas size
  - on phones, use the smaller set
  - with reduced motion, show the single middle frame

## C. Video hero or background loop

**How to spot it in the prompt:** `<video autoplay muted loop playsinline>`, an mp4 or webm URL, "background video".

**Assets:** one clip from the cheapest suitable model, started from a client image. Add a poster frame from the first frame (ffmpeg, free). Keep it under 8 MB and compress it with ffmpeg (`-crf 28`).

## D. Still plates with effects

**How to spot it in the prompt:** parallax speeds, masks, clip-path reveals, "grain overlay", gradients. No video and no separate layers.

**Assets:** usually the client's real photos or renderings, so no generation at all. Grain, masks and gradients are CSS or canvas. Check every image's frame shape against the photo's shape, so a wide rendering isn't zoomed into a square frame.

## E. Shader or 3D

**How to spot it in the prompt:** three.js or WebGL, GLSL, "model.glb", "particles", "displacement".

**Assets:** a `.glb` is real 3D work. Ask whether the client has a model (a designer's 3D files often exist) before generating one (Krea `generate_3d`, preflight it). Displacement and particle shaders run on a flat client image, which costs nothing.

## Something new

When a template matches none of these, work it out from the prompt and its assets:

- What does each asset look like?
- Is it transparent?
- Is it a still, a clip or a sequence?
- What moves it, and in what order?

Then plan the same kind of assets for the client, and say in the asset plan what you worked out, so the builder can confirm it before anything is generated. Add the technique to this file afterwards.

## F. Logo loading animation (generated, reversed)

A short loader that builds the client's logo on the loading screen, one per design in that design's look. Study the brand and the logo's construction, then ask the builder: coded (SVG + CSS: outline draw-on, isometric assembly, blueprint construction; no credits) or video (an image-to-video clip that takes the real logo apart, reversed so it ends on the exact file; one generation each). The full workflow is in `logo-loader.md`.

## Mixed templates

List the techniques per scene and plan assets per scene. The plan's total is what the builder approves.

## Writing the image prompts (any technique)

Write them in this order, and get each part right the first time:

1. **Deliverable:** what it is, and its role in the page.
2. **Style from the reference (this matters most).** Spell it out: "flat, reduced, about a dozen large color shapes, smooth gradients, heavy visible grain and stipple noise, walls as single flat tones with no bricks or shingles drawn". On the first job, a softer style line came back as a detailed storybook painting and needed a retake.
3. **Subject from the client image:** list the features that make it recognizable (tower, awning, roof lines, garage side).
4. **Place:** the client's region, said concretely.
5. **Palette and mood:** per scene, in the client's brand colors where they fit.
6. **Composition:** where the subject sits, and the calm space left for the headline.
7. **Clean surfaces:** no lettering, logos, people or cars, unless text is wanted and spelled out exactly.

**Technique-only style reference:** "take only the technique of image 2; its mountains, water, cabin and birds stay out of this picture".
