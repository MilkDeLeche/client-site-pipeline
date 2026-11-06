# Building the clone and checking it

## General build rules

- **The template is the spec.** Build its structure, motion, stacking order, positions, timings, easing, input handling, fonts and breakpoints as written. Change only the subject, place, palette, copy and brand colors. When the prompt is silent on something, take the value from how its own assets and layout behave, and don't invent a new behavior.
- **Keep the template's relationships, not just its pieces.** Every client asset sits where its template counterpart sat: in front of or behind the same things, grounded on the same surface, in the same part of the frame, at the same scale relative to its neighbors. Check this against the template's description and its own assets.
- **Match the asset to its role.** A transparent layer stays transparent, a full plate stays full-bleed, a frame sequence stays continuous, and a sprite keeps its size relative to the scene. Size and trim in code.
- **Fit the art to the frames the template defines.** Don't change a frame's shape to suit a picture. Pick or make art that suits the frame, and keep any oversizing the template uses (parallax, zoom) to the smallest amount its motion needs.
- **Motion is code, and it runs both ways where the template says so.** Time- or scroll-driven, one animation loop, reduced motion respected (settle instantly or show a still), no layout jumps on the first frame.
- **Copy:** the client's published words first. Write to the reader as "you". Use one language per visit (browser language, with `?lang=` overriding), with the second language written natively. Make no claims or counts the facts file can't back.
- **Contrast in every state.** Text, nav and logo stay readable over every scene, section and image they pass over, using the client's brand colors. The logo is never inverted or tinted.
- **Disclose the art.** Every place that shows AI art carries a short credit ("Illustration of <project>, a home you designed") and alt text that starts "Illustration of …".
- **Accessibility:** hidden scenes or sections are `inert` and `aria-hidden`, every control is reachable by keyboard, and focus outlines are visible.
- **Showcase pages:** `noindex`, kept out of the sitemap and the nav. When the page links out to designs, there's a way back to where the visitor left.

## Verification (all of it, every time)

- [ ] Every part behaves the way the template describes: each transition or scroll effect forward and back, the first and last states, every input the template lists
- [ ] Each client asset sits where its template counterpart did (stacking, grounding, framing, scale), and none overlaps the text
- [ ] Desktop and phone, in each language, with no console or page errors
- [ ] Real clicks on every control, with `document.elementFromPoint` at its center returning that control
- [ ] Text, nav and logo readable in every state, and the logo in its real colors
- [ ] No template URLs, names or copy left (grep the build); `noindex` on showcase pages
- [ ] Assets logged in `image-prompts.md` and `media-inventory.md`; the final credit cost reported to the builder

## Worked example: the first job (one template, not a rule)

A five-scene cut-out site for a Nordic cabin brand, rebuilt as a residential building designer's design picker.

- **How it worked:**
  - The page never scrolled natively. Wheel, keys, swipe or nav played a transition, and each transition was a function of time that ran backwards going up.
  - Scenes were built from a sky plate, a transparent ground band and cut-out buildings and trees.
  - The last scene looped back to the first.
- **Assets made:**
  - Three covers, each one of the client's real houses redrawn in the template's grainy flat style.
  - From each cover, a sky plate, a house cut-out, a ground band and a tree cluster, made with a transparent-background model.
  - Two intro layers with no house.
  - About 1,780 credits, one generation each, after an early round of retakes the builder stopped.
- **What went wrong and the general lesson behind it:**
  - **The first covers were too detailed** (bricks drawn, storybook look). Describe the template's art style precisely and first.
  - **The same house in every scene looked weak.** Repeated subjects take different real projects.
  - **The houses sat behind their lawns,** because the layers were stacked differently from the template's buildings, which stand on their ground. Keep the template's relationships.
  - **Some text lost contrast** on light scenes. Check contrast in every state.
