# Logo loading animation

A short motion-graphics loader that builds the client's logo on the loading screen, before the home page shows. A pitch with several design options gets one per design, each in that design's look. Around 2.5 seconds of motion, about 3.5 seconds of screen time in all.

**Credits: one generation per loader.** Write the strongest prompt you can, preflight the cost, submit once and use what comes back. No retakes, variants or "let's see if it's perfect" rounds. Fix small faults in code (trim, crop, mask, background color). A second generation happens only when the builder asks for it, after you've told them what it costs.

## 1. Pick the look per design

Read each design's look from its template: background, palette, line weight, how its own motion feels. Pick one motion idea that belongs to that look and is different from the other designs. Examples from the first job (a building designer with three options):

| Design look | Loader idea | Background |
|---|---|---|
| Dark, editorial, architectural | The mark's strokes split into hairline drafting lines and construction lines, like an exploded blueprint | the dark brand color |
| Cream, print, drafting sheet | The mark bleeds into the paper as ink | the cream |
| White, warm, rounded, soft | The mark inflates into glossy 3D and bursts into small spheres | white |

Other ideas that fit other looks: the mark slicing into strips or panels (grid, Swiss), liquid metal (luxury), light sweeping across an embossed mark (premium print), paper folding (playful), pixels or scanlines (tech), brush strokes (food, craft).

Put each loader on the asset plan with its model and a `preflight` quote, and get the builder's OK before spending credits.

## 2. The start frame is the real logo

- A square image, the logo centered at about a third of the width, on the loading screen's background color.
- Build it from the largest logo file the client has. A small PNG scaled up gives jagged edges that the model copies. If the full-color version only exists small, rebuild it from a large one-color file: fill the enclosed shape in code.
- Brand colors and shapes are never redrawn, inverted or "improved".

## 3. Prompt the logo coming apart, then reverse the clip

Image-to-video models start from an image but can't promise to end on one. So prompt the mark **coming apart** in the chosen style, then reverse the clip (`ffmpeg -vf reverse`). The reversed clip builds the mark and ends on the real logo file, exact.

Prompt pattern:

> Premium motion-graphics logo animation, [flat 2D vector / soft 3D], locked-off camera, no camera movement. [Background] stays flat and clean the whole time. The [logo's colors and shapes, described] [come apart how], then [fade / drift out], leaving only empty [background]. [Mood: smooth eased motion, minimal, elegant]. No text, no extra objects[, no hands, no pen, no particles: name what the model tends to add].

Settings: image-to-video, the shortest length the model allows (3 s on Kling), 1:1, the cheapest tier of the model the builder names (on the first job, "Kling's newest, cheap option" was Kling 4.0 Flash, about 209 credits per clip). List models live: names and prices change.

## 4. Encode

```bash
ffmpeg -i raw.mp4 -vf "reverse,setpts=PTS/1.2,scale=640:640:flags=lanczos,format=yuv420p" -an \
  -c:v libx264 -preset slow -crf 24 -movflags +faststart public/assets/client/loader/d1.mp4
ffmpeg -i raw.mp4 -vf "select=eq(n\,0),scale=640:640" -frames:v 1 -q:v 3 public/assets/client/loader/d1-end.jpg
```

- Speed up about 1.2×. That gives about 2.5 s and roughly 100–300 KB.
- The raw clip's first frame is the reversed clip's last: use it as the poster, so a phone that blocks autoplay still shows the logo.
- Sample the clip's corner color for the loading screen's background. Models drift the background a little (a vignette, a floor), so feather the video's edge with a radial `mask-image`.

## 5. On the page

- Home pages only, as a full-screen layer above the page.
- `<video muted playsinline autoplay preload="auto" poster=…>`, about 320px wide (62vw on phones).
- On `ended`, hold about 0.5 s, then fade the screen in about 0.6 s and remove it.
- If `play()` is refused, show the poster for about 1.2 s and continue. Cap the whole screen at 5 s, so a slow connection never blocks the page.
- `prefers-reduced-motion`: skip the loading screen.
- If the template already has its own preloader, swap its logo for the video and start the template's exit sequence on `ended`.

## 6. Check

- Watch every loader through in a real browser (a contact sheet of the raw clip, then screenshots at about 0.7, 1.5, 2.3 and 3.5 s on the page).
- The last frame is the logo, colors untouched. The screen is gone by about 3.5 s, with no console errors.
- Report what each one shows in a sentence, and say plainly if one came out weaker (on the first job, the ink clip tinted its paper tan). Don't regenerate it on your own.
