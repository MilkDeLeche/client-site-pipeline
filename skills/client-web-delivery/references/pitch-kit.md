# Pitch kit: what the owner is handed to say yes

A near-final pitch site wins the job only if someone can walk it into the owner's office. The pitch kit is the small set of print-ready pieces the builder (or whoever does the selling) takes to that meeting. It is built once the pitch site is live and passes the live showcase standard, and it is sent to the client or printed only when the builder says it is ready.

First used on a home-builder pitch: a one-page plan poster with a QR to the live pitch, plus a contract-questions sheet the seller kept on hand. The builder called it "easy to present to the client".

## Where it lives: `deliverables/`, gitignored

Every client project has a `deliverables/` folder at its root, listed in `.gitignore`. It holds everything that goes to the client by hand instead of through the site: the pitch kit, the setup-list, the handoff. Client prices, contract terms and the owner's private details never reach the repo, which may be public or shared.

```
deliverables/
  setup-list.md                    the asks (step 1)
  pitch/
    <client>-plan-poster.png       2550x3300, letter at 300 dpi
    <client>-plan-poster.pdf       one letter page
    <client>-qr.png                the QR alone, for cards and stickers
    <client>-contract-questions.pdf
    src/                           poster.html and its images, to rebuild it
  client-handoff.md                after step 5
  client-handoff-visual-prompt.md
```

- New project: add `deliverables/` to `.gitignore` when the folder is created.
- Existing project where `deliverables/` is already tracked: add it to `.gitignore`, then `git rm -r --cached deliverables` so the files stay on disk and leave the repo. Say so in the commit message.
- Because it is ignored, git doesn't back it up. Tell the builder where the folder is. Nothing in it is rebuilt by a clean clone.

## Before any of it: the pitch is live

- The pitch site is deployed at its showcase URL (`*.workers.dev`, `noindex`) with the latest copy. If the project's repo is connected to Cloudflare, pushing to `main` deploys it. Confirm the live URL shows the change before you make a QR for it.
- Check the live pages once: home in both languages, privacy in both languages, and a missing page returning the custom 404. Grep the HTML for leftover template names, `lorem`, `coming soon`, `prototype`, `demo` (read the context, because form hints and other-language words are false hits).

## 1. The plan poster (one page)

Template: `assets/pitch-poster-template.html`. One letter-size page that says what the owner gets, what it costs, and lets them see it right away.

Top to bottom:

1. **Header:** the client's logo (left) and a plan label (right), for example `MONTHLY WEBSITE PLAN`.
2. **Headline:** the fact that sells a pitch: the site is already built. "Your new website is already built." Then one line on what's on it, in the owner's terms (their work, their photos, both languages, an easy way for buyers to reach them). It has to fit on two lines.
3. **Visual band:** a real photo of the client's own work, with a desktop screenshot and a phone screenshot of the live pitch in front of it, plus one proof chip with a real count from the data file ("All 15 homes, each with its own page"). Upscale a small photo (Krea Topaz standard enhance needs `upscaling_activated: true`, scale 2) and don't generate one. A made-up photo of "their" work on a sales piece is a fabricated claim.
4. **The plan card:** the price as the biggest thing on the page, "Everything below is included", then each included item as a bold name plus one plain line on what it does for the owner. Add-ons the owner can choose go in a dashed box with an "Included if you want it" pill, so the base offer stays honest (AI chat stays opt-in per client: list it only when the builder offers it to this client).
5. **QR card:** "Scan to see it" plus one line of instruction. It points to the live pitch.
6. **What changes:** three rows comparing their current site with the new one. Check every "today" claim on their live site the day you make the poster ("only a search box", "a phone number you can't tap", "English only"). Never compare against something you didn't see.
7. **Footer:** `Prepared for <Client> · <area>`. Leave out the seller's name and contact details unless the builder asks for them.

Rules:
- Every item on the plan card is something the builder will really deliver at that price. "Set up to be found on Google, Maps and tools like ChatGPT" is a setup promise; "rank #1" or "more sales" is a result nobody can promise. Leave out results.
- A feature that depends on a client account or setup (auto-replies, alerts by email, review requests) is described as what it does once set up, and its setup goes on the setup-list.
- Don't claim a capability the chosen vendor hasn't confirmed (for example, an AI chat answering in the second language).
- Use the site's own fonts, brand color and logo, so the poster reads as the same brand as the site.
- The poster goes through the same copy filter as the site (`copywriting` + `antislop-copywriting`): plain words, no hype, no em-dash pile-ups.

### Screenshots of the live pitch

Hide the cookie banner and signup popup with a storage-state file that sets the site's own localStorage keys (for example `{"origins":[{"origin":"<url>","localStorage":[{"name":"<consent key>","value":"declined"},{"name":"<popup key>","value":"1"}]}]}`), then:

```bash
npx -y playwright@1.49.1 screenshot --channel chrome --load-storage state.json \
  --viewport-size "1440,900" --wait-for-timeout 2500 <url> desk.png
npx -y playwright@1.49.1 screenshot --channel chrome --load-storage state.json \
  --device "Pixel 7" --wait-for-timeout 2500 <url> phone.png
```

The iPhone devices fail with `--channel chrome` ("Unsupported webkit channel"); Pixel 7 works.

### Rendering

Render with headless Chrome. The page is 1275x1650 CSS px, and scale 2 gives 2550x3300 (letter at 300 dpi):

```bash
chrome --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=2 \
  --window-size=1275,1650 --screenshot=poster.png "file:///<abs path>/poster.html"
chrome --headless=new --disable-gpu --no-pdf-header-footer \
  --print-to-pdf=poster.pdf "file:///<abs path>/poster.html"
```

The template's print rule (`@media print { html, body { width: 816px; height: 1056px } .poster { zoom: .64 } }`) keeps the PDF to one letter page. Check that the PDF has exactly one page, and look at the PNG before calling it done: text covered by a mockup, an orphaned word, or a card running past the page are the usual faults.

## 2. The QR code

Script: `scripts/make_qr.py` (needs `pip install qrcode pillow opencv-python-headless numpy`).

```bash
python make_qr.py <live pitch url> <logo.png> <out.png> [hex color]
```

- Error correction H, the logo at most 24% of the width on a white pad, the client's brand color (dark enough to scan) on white.
- The script decodes the result at full size and at 600, 300 and 200 px and prints OK or FAIL for each. Every size must be OK.
- After rendering the poster, decode the QR from the rendered PNG too (crop the QR card and run `cv2.QRCodeDetector`). Then scan the printed page with a phone before it goes out.
- The QR points at the pitch URL. When the client buys and the real domain is live, remake it for the real domain.

## 3. The contract-questions sheet

Template: `assets/contract-questions-template.md`. Plain questions an owner asks before signing, each with a one- or two-sentence answer the seller can read off the page: money and contract, changes and edits, canceling, ownership, what's not included, getting started.

- **The terms are the builder's to set.** The agent drafts sensible defaults where the builder hasn't said (month to month, notice period, how many edits a month, turnaround, go-live time), and lists every one it chose in its reply as a suggestion to confirm before the sheet is used. A sheet in front of an owner is a promise.
- **Ownership answers stay honest.** The client owns their domain, photos, wording, leads and email list. If the design is from a paid template, a buyout that hands over the files needs a template license that allows it. Until that's confirmed, the buyout answer says "we'll quote it" and nothing more.
- **"What's not included"** is said up front: domain renewal, ad spend, photography, guaranteed rankings or sales.
- End with the line for anything not on the sheet: "Good question. Let me confirm and get back to you today."
- Format: write it as a Claude Docs doc when that connector is attached (the seller can edit it, and its PDF export is clean), otherwise as Markdown rendered to PDF with headless Chrome. Save the PDF to `deliverables/pitch/`.

## Done when

- [ ] `deliverables/` exists and is in `.gitignore` (and untracked if it was tracked)
- [ ] The live pitch shows the latest copy, and the pages above load
- [ ] Poster PNG (2550x3300) and a one-page PDF, every claim checked against the data file and the current site
- [ ] The QR decodes at every size and on the rendered poster, and points at the live pitch
- [ ] Contract-questions PDF, with the defaults the agent chose listed for the builder to confirm
- [ ] The builder is told where the folder is, and that nothing goes to the client until they say it's ready
