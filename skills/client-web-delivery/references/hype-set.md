# The hype set: what gets an owner excited before the meeting

The plan poster explains the offer (`pitch-kit.md`). The hype set makes the owner want it. It is a handful of images sized for a phone, each carrying one idea, that the builder texts ahead of a visit, posts, or prints. On an outbound pitch nobody asked for the site, so these do the job a first conversation would.

Build it after the pitch is live, from the market read (`brand-discovery` → `references/market-read.md`). It lives in `deliverables/hype/` and goes out only when the builder says so.

```
deliverables/hype/
  <client>-soon.png            the coming-soon card
  <client>-stat-1.png ...      one number each
  <client>-phone-1.png ...     the site on a phone, one feature each
  <client>-then-now.png        their page today next to the new one
  story/                       the same cards at 1080x1920
  hype-language.md             every line and number, with its source
  src/                         the HTML, screenshots and backgrounds, to rebuild them
```

Instagram mockups (the logo as the profile picture, the launch post, the site in the bio) are made first and live beside this folder in `deliverables/instagram/`: `mockups.md` has the method. The cards below can use them.

## One idea per image

A card with three numbers and a paragraph gets scrolled past. Each card has one thing the eye lands on: a number, a phone, or a line. If a second idea matters, it gets its own card.

## The pieces

1. **Coming-soon card.** "Your new website is on the way", in the client's own name, colors and logo, with a phone showing the real pitch. The builder texts it as the teaser. Once the owner says yes, the owner can post it for their customers. Templates: `assets/hype-soon-card.html` (a phone drawn in code on the brand color), or the post image from the Instagram mockups. `assets/hype-photo-card.html` puts the words on a real photo of their work.
2. **Stat cards, three to five.** One number per card: a hook, the number, one sentence on what it means for this business, and the source in small type. Local numbers first (their city or county), then the trade, then national. Template: `assets/hype-stat-card.html`.
3. **Phone cards, two or three.** The site on a phone with one feature per card: tap to call, the menu in Spanish, the request form. Template: `assets/hype-phone-card.html` (the phone drawn in code, the brand color behind it).
4. **Then-and-now card.** Their current page beside the new one, both captured the same day. Never compare against something that wasn't seen.
5. **Coming-soon page (opt-in).** A one-page site from the builder's coming-soon templates: the logo, one line, and a signup that really saves (`/api/subscribe`, the live showcase standard). It goes through `clone-intake` and Phases A and B like any template, and it never names a launch date the builder hasn't set. Ask the builder before building one.

## The copy

**Every line is researched, and current.** A card's line comes from one of three places, and `hype-language.md` says which:

1. A line the owner picked or the shortlist kept (`language-bank.md` sections 6 and 7). Use these first.
2. A buyer's or an owner's own words, opened and linked (`copy-bank` section 2).
3. A format that is working right now in this trade, found in a dated look at **Pinterest and Reddit** (and the trade's corner of Instagram or TikTok when the builder can show it): the opening question, the two-beat turn, the number-first line. Take the structure and write it with this business's words. Never lift a viral line, a slogan or a sound: most belong to someone, and a copied line is the first thing people recognize.

A plain statement of fact ("Your site is built.") is a caption, not a hook. Write at least ten candidates for each card, filter them the `copy-bank` way (counter, swap, payoff, picture, truth, banned, trademark), and show the builder two or three.

- **Research first, the `copy-bank` way.** Each hook is written from a buyer's or an owner's own words, logged in `hype-language.md` with the link. Reuse lines the owner already picked (`language-bank.md` §7) before writing new ones.
- **The shape that works:** a problem the owner has and hasn't named, said the way their buyers would say it, then the fix they can see on the card.
- **Loud is fine. The number is exact.** The energy comes from the hook and the picture. The number is what the source says, with the source, the year and the sample on the card. An owner who catches one wrong number stops believing the rest, and a local number is the kind they check.
- **No results promised.** "Found on Google and in ChatGPT" is a setup the builder delivers. "More customers" is a result nobody can promise.
- **Banned openers:** "Did you know" (the builder's rule), and everything in `copy-bank/banned.md`.
- Every line goes through `copywriting` and `antislop-copywriting`. No character a phone can turn into an emoji.

## The numbers

From the market read §2 and §4, each opened at its source.

- **Local:** `python scripts/census.py find "County, State"`, then `census.py county` with the two codes it prints: people, languages at home, households online and income for the county, each with the Census's own label and the source line for the card. It needs the builder's free key in the profile (`census_api_key`). Without one, the Census pages block automated readers: ask the builder to open QuickFacts and read the figure.
- **Trade and national:** the survey's own report, with its year and sample. Check it again before each new kit; these move fast. Last checked 2026-11-12: BrightLocal's Local Consumer Review Survey 2026 (1,002 US adults, published 2026-03-10) reports 45% of consumers using AI tools for local business recommendations, up from 6% the year before, and Google reviews use down from 83% to 71% ([source](https://www.brightlocal.com/research/lcrs-ai-trust/)).
- A number with no openable source doesn't get a card. Make the card about something else.

## Pictures, and Krea

- **Screens are real.** Every phone or browser on a card shows a real screenshot of the live pitch (`scripts/shots.py`), placed in the HTML. A generated picture of "their site" is a fabricated claim.
- **Their work is real.** Photos of the client's place, products or jobs come from their own files (`media-inventory.md`), upscaled if small. Never generated.
- **Krea makes the setting only:** a background or a texture in the brand's colors, never a device, a hand or a scene with a screen to fill. Write the brief with `krea-generate` and its model guide.
- **Words are never generated into the image.** All type is set in the HTML, so it stays sharp and correct.
- **One generation each** (the orchestrator's rule). Write the strongest prompt, quote the credits with a preflight, wait for the builder's yes, submit once, and fix small faults in code. Without credits or a yes, use the brand color and a real photo. The cards still work.

## Build and check

```bash
python scripts/shots.py <pitch url> deliverables/hype/src --state state.json --phone "/=phone"
python scripts/render_cards.py deliverables/hype deliverables/hype/src/soon.html deliverables/hype/src/stat-1.html
python scripts/render_cards.py deliverables/hype/story deliverables/hype/src/soon.html --size 1080x1920
```

`render_cards.py` writes one PNG per card at twice the size (2160 wide for a 1080 card) and fails when a card overflows its frame, an image didn't load, or a `{{placeholder}}` is still on it. Then open every PNG: a one-word last line, words sitting on top of the phone in a photo card, type over a busy part of a photo, or a phone cropped through its screen are fixed in the wording or the layout, never by shrinking the type. The script can't see any of those.

## Done when

- [ ] Each card carries one idea, and reads on a phone at arm's length
- [ ] `hype-language.md` traces every hook to a quote or an owner-picked line, and every number to a source opened that week
- [ ] Every screen on a card is a real screenshot of the live pitch
- [ ] Anything generated was quoted, approved and generated once, and holds no words, no client work and no people presented as theirs
- [ ] `render_cards.py` passes, and every PNG was opened
- [ ] The builder knows where the folder is and that nothing goes out until they say so
