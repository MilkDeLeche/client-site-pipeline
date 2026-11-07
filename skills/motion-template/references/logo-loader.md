# Logo loading animation

A loader is the first thing a visitor sees, and the best ones feel inevitable: the motion could only belong to this logo, this business and this design. Nothing here is a style to copy. Each loader comes from understanding three things, then designing motion that grows out of them.

**Credits:** coded loaders cost nothing. A generated video is one generation per loader: write the strongest prompt you can, preflight the cost, submit once, and use what comes back. No retakes or variants unless the builder asks, after you've said what it costs.

## 1. Understand before you design

### The logo: how was it made?

Every mark has a construction, and the strongest loader replays it. Look at the largest logo file the way a designer would and ask how it was drawn:

- **Geometry.** Is it built on a grid, a circle, isometric axes, a baseline, a golden ratio? What are its axes, its corners, its center? Which lines are structure and which are detail?
- **Stroke or fill.** A monoline mark wants to be drawn. A solid mark wants to be revealed, assembled or pressed into place. A mark with negative space hides a second shape in it: where does that shape appear?
- **Pieces.** Does it split into parts that mean something (faces of a cube, letters of a monogram, an icon and a wordmark, layers of an emblem)? Do they have a natural order?
- **Colors.** Which color is the frame, which is the field, which is the accent? The accent usually arrives last.
- **Type.** Is the wordmark geometric, serif, script, condensed? Script follows the pen. Geometric type follows its grid. A serif settles on its baseline.

Then write one line: *"This mark is ___, so it should come together by ___."* If you can't finish that sentence, you haven't understood the logo yet.

### The client: what do they do, and how does their world look?

- What does the business make, and how does its craft look while it's being made? Building trades sketch and measure (linework, construction lines, isometric views, title blocks, dimensions). Kitchens plate and pour. Salons cut and shape. Studios frame and focus. Law firms seal and sign.
- How do they want to come across (`creative-direction.md`): precise, warm, bold, luxurious, local, playful?
- What would they be proud to have their own clients see first?

The motion borrows from the craft, not from a generic "logo reveal" library.

### The design: how does this page already move?

- Its background, palette and line weights; the type in its header and labels.
- Its own motion vocabulary: soft fades or hard cuts, springs or long eases, slides, curtains, scroll reveals. The loader should feel like the first beat of the page's motion, not a separate intro.
- What comes right after: the hero. The loader's exit should hand off to it (lift away like a curtain, fade into the hero's first frame, shrink into the header logo).

## 2. Design the motion

Start with a one-sentence idea built from all three, for example: *"The mark is an isometric cube and the client draws buildings, so drafting guides run along the cube's own axes, its corners are marked, and the outline is drawn and filled like a finished elevation."* Then shape it:

- **Tell a short story: structure, then form, then color, then the brand.** Guides or bones first, outline next, fills last, the accent color at the very end. A mark that appears all at once has no story.
- **Use the logo's own geometry for everything.** Guides follow its axes, points land on its real corners, pieces travel along their own directions. Invented decoration reads as a template.
- **One idea per loader.** Several effects stacked together read as noise. If the designs differ, each gets its own idea from the same understanding.
- **Choreograph it.** Stagger the parts (about 60–150 ms apart), ease out of every move, hold the finished mark for a beat, then exit. About 2–2.5 s of motion in all.
- **Frame it like the design.** Small typographic labels in the design's own style (the name, the trade, the city, from the facts file, in the page language), a count or a hairline progress line tied to the real load. This frame is what turns a logo animation into part of the site.
- **Exit with the page's energy.** A bold editorial design can lift away like a curtain; a calm one fades; a playful one can scale or bounce.
- **Restraint:** thin lines, few colors, the brand's own palette, no glow or particles unless the brand truly is that.

Before building, pitch each idea to the builder in a sentence and **ask: coded or video?**, with your recommendation and why.

| | Coded (SVG + CSS) | Video (image-to-video, reversed) |
|---|---|---|
| Fits | Marks built from clean geometry or strokes: grids, polygons, monolines, wordmarks | Organic or detailed marks; materials code can't fake well (metal, glass, liquid, fabric) |
| Looks | Exact and crisp at any size, brand colors exact the whole time, can be choreographed to the frame | Cinematic, but the model invents the in-between frames and may miss the idea |
| Cost | No credits, a few KB, starts at first paint | Credits per clip, one generation, 100–300 KB, the background drifts |

**First job (example, not a template).** The client was a building-design firm with a geometric hexagon-cube mark. Two generated clips missed: ink spreading into paper and glossy spheres bursting apart. The builder said they "made no sense" for a firm that draws buildings. The coded loaders landed. The builder's favorite came from reading all three things together: an isometric mark, a trade that draws construction lines, and an editorial navy design with a bold curtain-like rhythm. That loader had guides on the cube's axes, gold points on its corners, a hairline draw, a fill, editorial corner labels with a count and a progress line, and a curtain lift into the hero. A different logo, trade or design should lead somewhere else entirely.

## 3. Build it: coded

1. **Get vector paths.** Use the client's SVG if they have one. Otherwise trace the largest file. For flat-color logos, separate each color by threshold, run `cv2.findContours` and `cv2.approxPolyDP` (epsilon about 2.5 px at 1000 px tall) for geometric marks, or potrace for curves. Render the SVG next to the original and compare before using it.
2. **Layers:** fill paths in the real colors (`fill-rule="evenodd"` for rings and counters), plus outline copies with `pathLength="1"`, `stroke-dasharray:1` and `stroke-dashoffset:1` that animate to 0 (the draw-on). Guides and markers are separate paths placed from the logo's real coordinates.
3. **Animate in CSS only**, with `@keyframes` and delays, so it runs at first paint before any script. Fills arrive with an opacity fade or a `clip-path: inset()` wipe. A count can be pure CSS: `@property --n { syntax: "<integer>" }` animated to 100, shown with `counter-reset: n var(--n)` and `content: counter(n, decimal-leading-zero)`.
4. **Pieces that travel:** clip a copy of the whole mark per piece with `<clipPath>`, move each along its own axis, then show the whole unclipped mark on top as they land (this hides hairline seams).
5. **Leaving:** once the mark is complete **and** `load` has fired, hold about 0.4 s, then exit (fade, or a curtain: `translateY(-100%)`, `cubic-bezier(.76,0,.24,1)`, 0.9 s). Cap the screen at 6 s. Reduced motion skips it. If the template has its own preloader, put the mark inside it and start the template's exit when the mark is done.

## 4. Build it: video

1. **Start frame:** the real logo, square, centered at about a third of the width, on the screen's background color, built from the largest file (a small PNG scaled up gives jagged edges that the model copies). Brand colors and shapes are never redrawn or "improved".
2. **Prompt the logo coming apart in the chosen idea, then reverse the clip** (`ffmpeg -vf reverse`). Image-to-video starts from an image but can't promise to end on one; reversed, the clip builds the mark and ends on the exact file. Lock the camera, name the background and keep it flat, describe the mark's real shapes and colors, and rule out what the model tends to add (text, hands, extra objects). Use the shortest length, 1:1, and the cheapest tier of the model the builder names. List models live: names and prices change.
3. **Encode:** `reverse,setpts=PTS/1.2,scale=640:640`, H.264, no audio, `+faststart`. Use the raw first frame as the poster, so a phone that blocks autoplay still shows the logo. Sample the clip's corner color for the screen's background, and feather the video's edge with a radial `mask-image`.
4. **On the page:** `muted playsinline autoplay`, about 320 px wide; on `ended`, hold, then exit; if `play()` is refused, show the poster briefly; cap at 5 s.

## 5. Check

- Capture each loader frame by frame in a real browser (a screenshot about every 300 ms), on desktop and a phone, in both site languages.
- Ask honestly: does the motion explain this logo? Would it make sense for a different client? If it would, it's generic: go back to step 1.
- The final state is the logo with exact colors. Labels and guides fit at phone width. The screen is gone soon after the page loads, with no console errors.
- Report each loader's idea in a sentence. Say plainly if one is weaker, and don't regenerate a video on your own.
