# Pitch kit: what the owner is handed to say yes

A near-final pitch site wins the job only if someone can walk it into the owner's office. The pitch kit is the small set of print-ready pieces the builder (or whoever does the selling) takes to that meeting. It is built once the pitch site is live and passes the live showcase standard, and it is sent to the client or printed only when the builder says it is ready.

First used on a home-builder pitch: a two-page plan poster with a QR to the live pitch (page 1 the plan, page 2 why it's worth it), plus a contract-questions sheet the seller kept on hand. The builder called it "easy to present to the client".

## Where it lives: `deliverables/`, gitignored

Every client project has a `deliverables/` folder at its root, listed in `.gitignore`. It holds everything that goes to the client by hand instead of through the site: the pitch kit, the setup-list, the handoff. Client prices, contract terms and the owner's private details never reach the repo, which may be public or shared.

```
deliverables/
  setup-list.md                    the asks (step 1)
  pitch/
    <client>-plan.pdf              both poster pages, letter
    <client>-plan-page1.png        2550x3300, letter at 300 dpi
    <client>-plan-page2.png
    <client>-qr.png                the QR alone, for cards and stickers
    <client>-contract-questions.pdf
    src/                           poster.html, page2.html and their images, to rebuild them
  client-handoff.md                after step 5
  client-handoff-visual-prompt.md
```

## Tools (installed by the pipeline setup)

`client-site-pipeline/scripts/setup.mjs` installs everything the kit needs: Google Chrome, and Python with `scripts/requirements.txt` (qrcode, pillow, numpy, opencv, playwright, pypdf). If the summary says `off` for the pitch kit, rerun the setup before you start. The kit's three scripts:

| Script | Does |
| --- | --- |
| `scripts/shots.py` | Screenshots of the live pitch: a desktop page, one section by CSS selector (fixed and sticky bars hidden), a phone page (Pixel 7) |
| `scripts/make_qr.py` | The logo QR, decoded at four sizes; exits 1 if any fail |
| `scripts/render_pages.py` | Each page to a 2550x3300 PNG and a one-page PDF, merged; checks one sheet per page and, with `--qr`, the QR on every page |

In Git Bash, set `MSYS_NO_PATHCONV=1` before passing site paths like `/=desk`, or Bash rewrites them into Windows paths.

- New project: add `deliverables/` to `.gitignore` when the folder is created.
- Existing project where `deliverables/` is already tracked: add it to `.gitignore`, then `git rm -r --cached deliverables` so the files stay on disk and leave the repo. Say so in the commit message.
- Because it is ignored, git doesn't back it up. Tell the builder where the folder is. Nothing in it is rebuilt by a clean clone.

## Before any of it: the pitch is live

- The pitch site is deployed at its showcase URL (`*.workers.dev`, `noindex`) with the latest copy. If the project's repo is connected to Cloudflare, pushing to `main` deploys it. Confirm the live URL shows the change before you make a QR for it.
- Check the live pages once: home in both languages, privacy in both languages, and a missing page returning the custom 404. Grep the HTML for leftover template names, `lorem`, `coming soon`, `prototype`, `demo` (read the context, because form hints and other-language words are false hits).

## 1. The plan poster (two pages)

Two letter pages, never more. Page 1 introduces the plan: what the owner gets and what it costs, and they can see the site right away. Page 2 sells it: why the monthly price is worth paying. One page is good and two are better. A third page is one the owner won't read.

### Page 1: the plan

Template: `assets/pitch-poster-template.html`.

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

### Page 2: why it's worth it

Template: `assets/pitch-poster-page2-template.html`. Page 1 lists what's included; page 2 sells it. It shows the owner a problem they haven't noticed yet, then shows the plan already handling it.

Top to bottom:

1. **Header:** same logo, with the label `WHAT YOU GET EVERY MONTH`.
2. **Headline: the problem.** Sites that get built once and then left alone fall behind the competitors who keep posting. "Most websites get built once, then forgotten." The line under it says the plan keeps their site working every month, so it keeps up with the businesses around them.
3. **Visual band:** two sections of the live pitch that aren't the hero shown on page 1. Pick the ones that prove the plan: the gallery or work section (new work keeps going up) on desktop, and the primary form with its call/text bar on a phone (requests come straight to them). Next to them is **one stat card**: a short hook ("Instagram isn't a search engine."), one number, a sentence on what it means, and the source with its year and sample size.
4. **Six to eight service cards.** Each card gives the service name a buyer understands and one or two lines on what it does for them. The standard set:
   - Found on Google and AI search (SEO + GEO). Social posts don't show up when someone asks Google or ChatGPT for a business nearby; a website set up with the right facts does.
   - Updates every month: new work, listings, photos, prices. The site keeps pace with competitors instead of going stale.
   - Email marketing to the signup list (the newsletter or alerts).
   - Google reviews: a ready link and QR card for every finished job.
   - Secure and private: encrypted pages, spam-protected forms, requests in a private database (when the site has one), never shared or sold.
   - A monthly growth report: visits, where people found them, how many asked.
   - Every request, right away: phone and inbox alerts with the person's name and number.
   - **Optional:** an AI chat card, only when the builder offers chat to this client. Not every client gets one.
5. **Value bar:** "One competitive monthly price." Then the bills it replaces ("No separate bills for hosting, search setup, email marketing and edits."), the price, and the QR again.
6. **Footer:** same as page 1, with `Page 2 of 2` (page 1 says `Page 1 of 2`).

Writing it:
- **Research first, the `copy-bank` way.** Look for what owners in this trade say about websites, social media and web designers (forums, Reddit, trade press) and log the useful words in the trade file. On the first kit, what came up was fear of a designer who disappears, sites left un-updated for years, and "Facebook is enough". The headline answers the second; the cards answer the rest.
- **The stat comes from a primary source you opened**, not a search snippet or a blog repeating it. Print the source, year and sample on the card. Check it again before each new kit, since these numbers move quickly. The first kit used BrightLocal's Local Consumer Review Survey 2026: 45% of US consumers used AI tools for local business recommendations, up from 6% in 2025 (1,002 US adults; [source](https://www.brightlocal.com/research/lcrs-ai-trust/), checked 2026-11-05).
- **"Competitive" stays general.** Don't compare against named competitors or prices you haven't checked. The value line names the separate bills the plan replaces.
- Every card is something the builder delivers at this price, written as what it does once set up (an alert needs the client's inbox, a report needs analytics on). The rules for page 1 apply here too: no results promised, no unconfirmed vendor capability.
- Copy through `copywriting` + `antislop-copywriting`. Look at the render for one-word last lines in the cards and rewrite them rather than shrinking the type.

### Screenshots of the live pitch

`scripts/shots.py` hides the cookie banner and signup popup with a storage-state file that sets the site's own localStorage keys (for example `{"cookies":[],"origins":[{"origin":"<url>","localStorage":[{"name":"<consent key>","value":"declined"},{"name":"<popup key>","value":"1"}]}]}`):

```bash
python scripts/shots.py <url> src --state state.json   --page "/=desk" --phone "/=phone"   --section ".section_our-work=work" --phone "/contact=form"
```

A section shot hides fixed and sticky bars so the header doesn't cover it, and scrolls first so reveal animations finish. Phone shots use Pixel 7, because the iPhone devices fail with the Chrome channel. Open every shot before using it: a half-revealed card or a popup that slipped through shows up here.

### Rendering

```bash
python scripts/render_pages.py ../<client>-plan.pdf poster.html page2.html --qr <live pitch url>
```

Each page is 1275x1650 CSS px. The script renders it at scale 2 to a 2550x3300 PNG (letter at 300 dpi) and prints it to a one-page PDF (the templates' print rule zooms to .64). It merges the pages and fails if a page runs to a second sheet or a QR doesn't decode. Then look at both PNGs: text covered by a mockup, a one-word last line, or a section squeezed because the page overflowed (keep `flex-shrink: 0` on fixed-height bands) are the usual faults. Copy the PNGs up to `deliverables/pitch/` with their final names.

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

- [ ] The pipeline setup reports Google Chrome and the pitch kit `ok`
- [ ] `deliverables/` exists and is in `.gitignore` (and untracked if it was tracked)
- [ ] The live pitch shows the latest copy, and the pages above load
- [ ] Both poster pages as PNGs (2550x3300) and one two-page PDF, every claim checked against the data file and the current site, the page 2 stat opened at its source and cited
- [ ] The QR decodes at every size and on the rendered poster, and points at the live pitch
- [ ] Contract-questions PDF, with the defaults the agent chose listed for the builder to confirm
- [ ] The builder is told where the folder is, and that nothing goes to the client until they say it's ready
