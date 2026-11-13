# Brand kit: when the owner has no real logo or colors

Step 0b. It runs only when the homework finds no usable identity: no logo file, a logo that exists only as a blurry profile picture, or no consistent colors. A business with a real mark skips this, and its mark is used as it is.

Output: `brand-kit.md` at the project root, the files in `public/` and `assets/`, and a brand board in `deliverables/brand/` the owner can look at and post.

## 1. Find what already exists

Owners usually have more identity than files. Look at the sign on the building, the truck, the menu, the uniform, the business card, the oldest posts. Whatever customers already recognize wins.

- **A mark exists but the file is poor:** rebuild that same mark cleanly (trace it to SVG, upscale a photo of the sign). Never redesign a logo the owner already uses unless they ask.
- **Colors exist in the place:** the wall, the awning, the packaging. Sample them from the owner's own photos.

Record each find with where it was seen. A found identity is confirmed. Everything below this line is a proposal until the owner says yes.

## 2. If there is nothing: start with the name in type

A wordmark set well in the right typeface is a real logo and can't go wrong the way a generated symbol can.

- **The name** exactly as the owner writes it.
- **Type:** two families at most, chosen for the trade and the direction (`font-playbook`), with a license that allows the use. Write the reason in a line.
- **Color:** two or three core colors and one accent, taken from the place or the product where possible. Check every text pair for contrast (4.5:1 for body text) and write the pairs that pass.
- **Voice:** three words and two sample lines, from `creative-direction.md` and `language-bank.md`.
- **Photo treatment:** how their real photos are cropped and toned, shown on two of their own pictures.

## 3. A symbol, only with the builder's yes

Ask first. If yes, offer two routes and recommend one:

- **Drawn in code (SVG):** for letter-based and geometric marks. Exact, scalable, no credits. `motion-template` → `references/logo-loader.md` can animate it later.
- **Generated, then traced:** one Krea generation, quoted first, for a mark that needs an illustrative idea. Trace the result to SVG and clean it by hand in code. The generator's lettering is never used; the name is set in type.

Before showing any proposed mark: search the name with the trade and the area, and look at the nearest competitors' marks. A proposal that could be confused with a business nearby is dropped. This is a look-alike check, not legal clearance: say so, and leave trademark questions to the owner.

## 4. Write `brand-kit.md`

| Part | What it records |
|---|---|
| Name | As written, and how it is never written |
| Logo | Files (SVG, PNG on light, PNG on dark), minimum size, clear space, `found` or `proposed` |
| Colors | Name, hex, where each is used, the text pairs that pass contrast |
| Type | Families, weights, where each is used, the license |
| Voice | Three words, two lines that sound right, one that doesn't |
| Photos | The treatment, and which of their photos show it |
| Status | `found` / `proposed, not shown to the owner` / `approved by the owner` with date and channel |

The same values go into the site's tokens, so the site, the cards and the proposal can't drift apart.

## 5. The brand board

`client-web-delivery` → `assets/brand-board.html`, rendered with `scripts/render_cards.py` into `deliverables/brand/<client>-brand-board.png`. One image: the mark, the colors with their codes, the type, two of their own photos, one mockup, one line. It shows only real things and proposals labeled as proposals.

Check the current look of brand boards on **Pinterest and Reddit** first (r/logodesign, r/graphic_design, r/branding), date the note, and take the layout idea, never someone's board.

## 6. Ask the owner

A proposed identity goes on the owner sheet as a veto question with the board attached: "This is how we'd show your name. Anything you'd change?" Until they answer, mockups that show the proposed mark in the world (a sign, a billboard, a shirt) are labeled proposals and stay with the builder.

## Done when

- [ ] What already existed was looked for and recorded, and a real mark was kept
- [ ] Every proposed part is marked proposed, with its reason
- [ ] Contrast pairs are checked and listed
- [ ] A proposed symbol passed the look-alike check, and the owner knows it is not legal clearance
- [ ] `brand-kit.md` and the site's tokens agree
- [ ] The board is rendered and opened, and the veto question is on the owner sheet
