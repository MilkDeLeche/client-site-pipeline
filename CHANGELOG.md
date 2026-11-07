# Changelog

All notable changes to this pipeline are recorded here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.21.0] — 2026-11-07

- **Authorship mark on every client site** (`client-web-delivery`, orchestrator; requested by the builder). The builder is credited as the author out of sight: a `designer` meta tag, `/humans.txt`, a copyright notice in the page source, and a hidden easter egg where 20 quick clicks on the footer show "Original author · Miguel Sanchez". New assets: `author-mark.astro`, `humans.txt`. It goes on client page layouts, not the options picker. The notice asks people and AI agents to keep the credit and never asks anyone to hide it.

## [1.20.2] — 2026-11-07

- **Removed** the two `clone-workflow` gotchas added in 1.20.0 (scoped styles vs `set:html`, iPhone swipe selection). The builder kept the fixes on that site but didn't want them as pipeline rules.

## [1.20.1] — 2026-11-07

- **Social videos are opt-in** (builder: niche, not every client has TikTok). The orchestrator now has a "Finishing touches" step near the end of Phase B that asks the builder which extras the client wants: a logo loading animation, and the client's social videos. `client-web-delivery`'s social-video rules apply only after a yes.

## [1.20.0] — 2026-11-07

- **`client-web-delivery`, social videos:** autoplay muted with the platform's own unmute (no sound a visitor didn't ask for). Start players one at a time, about 1.5 s apart, after simultaneous loads returned "Player error". Reload a stalled player once. Keep players only for the cards showing. Start loading them behind a home page's loading screen. This replaces the earlier tap-to-play rule.
- **`clone-workflow` gotchas:** Astro's scoped styles don't reach `set:html` markup (use `:global()`). Swipe-driven pages need `user-select: none` and no tap highlight on iPhone.

## [1.19.1] — 2026-11-07

- **`logo-loader.md` rewritten around understanding, not a style list.** Read the logo's construction (geometry, stroke or fill, meaningful pieces, color roles, type), the client's craft and how they want to come across, and the design's own motion and what follows the loader. Finish the sentence "this mark is ___, so it should come together by ___". Then design one idea: structure, then form, then color; the logo's own geometry for every guide and move; choreography; a typographic frame tied to the real load; an exit with the page's energy. The first job's loaders are kept only as an example of that reasoning. The check asks whether the motion would make sense for a different client; if it would, it's generic.

## [1.19.0] — 2026-11-07

Coded logo loaders. On the building-designer pitch the builder rejected two generated loader clips (ink, glossy spheres) as making no sense for the brand, and liked coded ones much better.

- **`logo-loader.md` rewritten:** study the brand first (the logo's construction, exact colors, trade, each design's look), then ask the builder **coded or video**, with a recommendation and a comparison table. The coded workflow: trace the logo into SVG (OpenCV contours from the largest file), draw-on strokes with `pathLength`, a pure-CSS 00→100 count, clipped pieces for assemblies, leaving after the mark and the page load (fade or curtain). Three worked ideas: blueprint construction, outline draw-on, isometric assembly. The video workflow stays as the second option.
- **Orchestrator and `motion-template`** point to the ask-first step.
- **`intent-aware-rebrand`:** the leftover check covers attributes that only show in view-source (builder layer names), after a Framer layer name kept the template author's copyright line.

## [1.18.0] — 2026-11-07

- **Logo loading animation workflow** (`motion-template/references/logo-loader.md`): pick a loader idea per design look, build the start frame from the real logo, prompt the mark coming apart and reverse the clip, encode, page code, checks. The orchestrator and `motion-template`'s description now point to it, so it's found when a builder asks for a loader.
- **One generation per image or video, pipeline-wide** (orchestrator). The rule was already in `motion-template` and the image-prompt reference; it now covers every generated asset. Preflight the cost, submit once, fix small faults in code, and make a second generation only when the builder asks. It keeps credit spending low without lowering quality.

## [1.17.0] — 2026-11-07

- **`motion-template` technique F, a logo loading animation:** start a short image-to-video clip on the real logo, prompt the mark coming apart in the design's look, then reverse the clip, so it builds the mark and ends on the exact logo file. Includes encoding, poster, timing and background matching. From the building-designer pitch: three loaders (blueprint lines, ink on paper, soft 3D spheres), one generation each.

## [1.16.0] — 2026-11-07

The client's social videos on a pitch. The building designer's old site played TikToks through iframes that showed "overload-protect triggered"; the pitch puts them back so they play.

- **`client-web-delivery` live showcase standard:** social video rules. Use ids from the client's own site; show local covers and load the player on tap, one at a time (TikTok's `player/v1` plays where `embed/v2` and the profile embed hit the rate limit). A muted background loop loads only while visible and stops when closed. Auto-updating to the newest uploads needs the platform's API and the client's authorization, so it goes on the setup-list. The privacy page names the platform.
- **`copy-bank/approved.md`:** the builder's hero pick for the building-design pitch.
- **Unchanged:** the steps and their order, the hook method, the ban on invented facts.

## [1.15.1] — 2026-11-06

Spanish that reads as written, not translated. A native speaker reviewing the building-designer pitch said the Spanish "no tiene sentido… es muy IA": dictionary words, English word order and literal UI labels.

- **`copy-bank` §2:** when second-language buyer threads are gated, build a glossary of the trade's everyday words in that language from open sources (local government pages, classifieds, freelance listings, regional peers) in `language-bank.md` §2b. Write from the meaning, not the English sentence, and read every line aloud, labels and form fields included.
- **`copy-bank` anti-patterns, `banned.md` §4:** the rejected Spanish lines and what replaced them.
- **`industries/home-design.md`:** a Spanish trade glossary for RGV home design.
- **Unchanged:** the steps and their order, the hook method, the ban on invented facts.

## [1.15.0] — 2026-11-06

Language and the pages every pitch needs. On the building-designer pitch the designs had gone up in English only, without a privacy page or a 404. The builder asked for Spanish on every page, served automatically by the visitor's system language with no button. A native Spanish speaker on the builder's side flagged missing accents and word-for-word translations as the thing that makes Spanish copy cringe.

- **Language follows the system language** (`client-web-delivery` live showcase standard, orchestrator):
  - A head script reads `navigator.languages[0]` and sends second-language systems to `/<code>/`.
  - `?lang=` overrides it for previews and is remembered for the visit.
  - There's no language button or popup, and no geolocation. This replaces the earlier "language switch in the nav" rule.
  - The 404 picks its language in place.
- **Spanish spelled and written natively** (`client-web-delivery`, `copy-bank`):
  - every accent, tilde, `¿` and `¡`
  - formal `usted` by default
  - rewritten, never word for word
  - read by a native speaker before it goes to the owner
  - client reviews stay in the reviewer's own language
- **Privacy page and custom 404 from the first pitch deploy,** in both languages, before the forms or email tool exist. The privacy page describes only what the site does that day.
- **Unchanged:** the steps and their order, the forms and D1 capture in Phase C, the ban on invented facts.

## [1.14.0] — 2026-11-06

A skill for motion-site prompt templates. The builder has many "recreate this page exactly" prompts for motion sites, each tied to one fictional brand's hosted assets, and had never used them for a client. On a building designer's design picker, one such prompt (five cut-out scenes for a Nordic cabin brand) was rebuilt with three of the client's houses. The builder asked for the method to be kept.

- **New `motion-template` skill** (not a step). Written as general rules, because no two templates are the same: study how the template works, work out what assets it needs, produce the same kind of assets from the client's work, clone the template as given and check it against the template. The first job is kept only as a worked example.
  - **Reading the template:** it reads the prompt and lists every asset and the motion spec, names the technique, and studies the template's art for style only.
  - **Mapping and approval:** it maps each asset to a real client file, an AI image made from a client file, or code. It swaps the place and the copy (the client's published words first), puts a different client project in each scene, and hands the builder an asset plan with a credit quote before anything is generated.
  - **References:**
    - `references/techniques.md`: how to spot layered cut-out scenes, scroll-scrubbed frame sequences (one image-to-video clip from the cheapest suitable model, such as Kling 4.0 Flash, cut into frames with ffmpeg), video heroes, stills with effects, and shader or 3D, with the assets and models each needs and a prompt order that gets the flat style right the first time.
    - `references/build-and-check.md`: the scene engine (transitions as pure functions of t that play backwards, `settle`, input, nav tone, return flow), the layout lessons (ground band, then trees, then the subject in front so it stands on its lawn; portrait sizing; per-scene contrast; parallax layers trimmed to their frames), copy rules, and the verification list.
    - `assets/asset-plan-template.md`: the plan the builder approves.
- **One generation per AI image** across the pipeline: `clone-workflow/references/image-prompts.md` no longer suggests two variants. The builder asks for a retake when one is wanted.
- **Wired in:** `design-options-shelf.md` (a shelf built from a motion template), the orchestrator note, the README.
- **Unchanged:** the steps and their order, Phase A, the ban on invented facts and on AI images in "this is our work" slots.

## [1.13.1] — 2026-11-05

Copy-bank additions from a residential building-design pitch, and skill descriptions that fit claude.ai uploads.

- **New `copy-bank/industries/home-design.md`:** buyer words for custom-home design from published client reviews and a Houzz thread (being heard and guided, the dream in their heads, not like the neighbors, cost fear), the hidden problems with honest payoffs, and the RGV competitor read. Building designers in Texas are never called architects.
- **`banned.md`:** home-design category clichés in English and Spanish ("Build your dream home", "Designed around you", "La casa de tus sueños"), two RGV competitor lines, and four lines the owner rejected (a swap-test hero, a staccato hook, buyer situations as service titles, a three-beat tagline).
- **Descriptions under 1,024 characters** for `brand-discovery` and `client-web-delivery`, the Agent Skills limit claude.ai enforces on upload. Same triggers, fewer words.

## [1.13.0] — 2026-11-05

A second poster page that sells the plan, and the setup now installs everything the pitch kit uses. The builder read page 1 as "the introduction" and asked for one more page with selling points ("one page is good, two pages is perfect, three is too boring"). They also asked that the setup install the kit's tools like everything else in the pipeline.

- **Page 2 of the plan poster** (`assets/pitch-poster-page2-template.html`, "Page 2" in `references/pitch-kit.md`). It shows the owner a problem they haven't noticed yet: sites built once and then left behind, and social pages that search can't find. Then it shows the plan already handling it. It has one stat card from a primary source that was opened and cited on the page, six to eight service cards (SEO + GEO, updates every month, email marketing, Google reviews, secure and private, a monthly growth report, every request right away, and AI chat only when the builder offers it to this client), two more sections of the live site (the work gallery on desktop and the primary form on a phone), and a "One competitive monthly price" bar naming the bills it replaces, with the QR again. Two pages at most. Page footers read "Page 1 of 2" and "Page 2 of 2".
- **Scripts:** `scripts/shots.py` takes desktop, phone (Pixel 7) and single-section screenshots. Section shots hide fixed and sticky bars and wait for reveal animations. `scripts/render_pages.py` renders each page to a 2550x3300 PNG and a one-page PDF, merges them, and fails on a second sheet or a QR that doesn't decode. Both were tested on the first kit. In Git Bash, set `MSYS_NO_PATHCONV=1` before passing site paths.
- **Setup installs the pitch kit:** `setup.mjs` checks for Google Chrome and installs it if missing (winget or Homebrew), along with the Python packages in `client-web-delivery/scripts/requirements.txt` (qrcode, pillow, numpy, opencv, playwright, pypdf). It tries a user install first and falls back to a private environment. Python is now installed even with `--no-optional`, because the kit needs it.
- **Copy bank:** `industries/creative-agency.md` gets the research for a monthly website plan (owners' worries: a designer who disappears, a fee for a site that never changes, whether a flat fee is fair, "Facebook is enough"), marked as notes until opened, plus the opened BrightLocal 2026 stat.
- **Unchanged:** page 1, the steps and their order, Phase A, the ban on invented facts and results, AI chat as opt-in.

## [1.12.0] — 2026-11-05

A pitch kit, so a near-final pitch can be sold in one meeting. On a home-builder pitch the builder needed something the person doing the selling could put in front of the owner. A one-page plan poster with a QR to the live pitch, plus a contract-questions sheet, was what made it "easy to present to the client".

- **New `client-web-delivery/references/pitch-kit.md`**, with a short "Pitch kit" section in the skill and a note in the orchestrator. It is not a step and does not replace the launch audit.
  - **Plan poster** (`assets/pitch-poster-template.html`): the client's logo, "Your new website is already built.", a real photo of their work (upscaled, never generated) with desktop and phone screenshots of the live pitch, one proof chip from the data file, the price and what's included, opt-in add-ons in a separate box, a QR card, and a three-row "what changes" comparison, each "today" claim checked on the client's current site. No results promised (rankings, sales), no capability a vendor hasn't confirmed, no seller details unless asked. Includes the render commands (2550x3300 PNG, one-page letter PDF) and the screenshot recipe (storage state to hide the banner and popup; Pixel 7, because the iPhone devices fail with the Chrome channel).
  - **QR** (`scripts/make_qr.py`): error correction H, logo at most 24% wide, brand color; it decodes the result at four sizes and exits 1 on any failure. Decode it on the rendered poster as well, then scan the print with a phone.
  - **Contract-questions sheet** (`assets/contract-questions-template.md`): money, edits, canceling, ownership, what's not included, getting started, and the line for anything not on the sheet. Terms are the builder's. The agent drafts defaults only where the builder hasn't said, and lists each one as a suggestion to confirm. A buyout that hands over site files is promised only if the template license allows it.
- **`deliverables/` is gitignored** in every client project (setup-list, pitch kit, handoff), so prices, terms and owner details never reach the repo. A tracked folder is ignored and untracked with `git rm -r --cached`. Sources of truth and the README updated.
- **Copy bank:** `banned.md` §5 logs six lines cut in a builder-site wording pass: question hooks as service and feature titles, a "tradition of excellence" line, dream-home clichés, a pun headline, and "easier than you think".
- **Unchanged:** the steps and their order, Phase A, the ban on invented facts, AI chat as an opt-in add-on, antislop and copywriting.

## [1.11.0] — 2026-11-04

Putting the options in front of the owner, and the fixes a real handover turned up. On the same agency pitch the owner had turned down build after build, so the builder put the four finished designs on one page for him to choose from, and asked for one more pass to cut anything generic.

- **New `clone-workflow/references/design-options-shelf.md`.** One page with the finished options, for an owner who can't pick from descriptions. It shows finished designs only: the Phase A template baselines are never shown and come off the deployed site, and template code ships only once its licence is bought. Each option gets a plain name, the owner's own words for the direction and a few facts, written to the owner as "you", never template product names. The page is unlisted (`noindex`, out of the sitemap) and shows one language per visit, picked from the browser. Opening a design goes to the real page. Every design gets a way back, shown only to visitors who came from the shelf, clear of the page's own buttons and reachable by keyboard. Verification covers real clicks with an `elementFromPoint` check (a full-width logo band had covered a Close button), state checks instead of mid-animation screenshots in throttled automation browsers, and a clean-clone build. Linked from the rebrand reference and the folder conventions.
- **Image prompts:** no real app logos or look-alikes, even when the copy names the app and the owner asks for them: use generic icons and let the copy name the apps. The rating rule is narrowed: a rating or result attributed to the client is out, while a generic, unnamed interface labeled as an illustration may show what the service does. Crop to each slot's real shape (a short, wide card cut the subject out of a tall image).
- **Wordmark swaps:** when the client's name replaces a full-width wordmark, the box takes its height from the type, the fit adds back the letter-spacing after the last letter, and a longer name stays on one line at a smaller size. A fixed-height box had clipped the letters, and the fit had cut off the last one.
- **Copy bank:** `banned.md` §5 logs the lines cut in a generic-wording pass and why (staccato steps, shot descriptions as titles, a tease as a heading, a false range). Two new anti-patterns: a copy pass that overwrites an approved line (diff against `approved.md` first, because an owner-approved heading had been replaced), and stunts as work titles or step titles where plain labels read as chosen.

## [1.10.0] — 2026-11-03

A copy bank, so hooks come from research instead of the agent's head. On the same agency pitch the owner rejected the hero lines twice ("they make no sense", "so generic") even though they followed every v1.9.0 rule. The rules block bad patterns; they don't supply good material. Working copywriters get it from the buyer's own words, from a swipe file of patterns, from writing many lines and cutting hard, and from the owner's ear.

- **New `copy-bank` skill** (not a step): the method plus a shared library that grows with every client.
  - `patterns.md`: 17 hook structures, each with real credited examples (study only, never shipped), the buyer awareness level it fits (Schwartz), and when it works and fails.
  - `banned.md`: category clichés in English and Spanish, competitor lines seen in the market with sources and dates, the AI tells in one place, and every line an owner rejected with the reason.
  - `approved.md`: lines owners picked, with the pattern, trade, region, source and date. No client names.
  - `industries/creative-agency.md`: the first trade file, with verbatim buyer quotes from public threads (marked secondary), the hidden problem and the honest payoff, buyer-side research labeled as notes, the RGV competitor read, and a reference brand's argument map.
  - `assets/language-bank-template.md`: the per-client file. §1–4 (buyer situations and awareness, buyer words, the avoid list, the owner's words) start at step 0; §5–7 (30+ candidates, the shortlist, the owner's answer and the log) are written in Phase B.
- **The filter** every candidate passes before the owner sees it: counter test (would the owner say it at the counter?), swap test (could a competitor sign it?), payoff, picture, truth, banned and trademark checks.
- **The loop closes.** Picks go to `approved.md`, rejections to `banned.md` with the owner's reason, new buyer words and competitor lines to the trade file, written in the source checkout so a reinstall doesn't erase them.
- **Image prompts for true gaps.** New `clone-workflow/references/image-prompts.md`, linked from the existing AI-image rule. It covers four things. A gap audit: an AI image only where no real file can honestly fill the slot, and never in a "this is our work" slot. A prompt recipe written from the client's own footage: its light, grade and lens, the region said concretely, clean surfaces described positively. A photo-editor check of every output: hands, gibberish letterforms, stock look, implied claims. A per-project `image-prompts.md` log with the alt label, privacy disclosure and inventory row. First used on the same pitch for the one slot every design got wrong (the search service, shown with a house, a store opening and a clothing tag). Two variants, one rejected because it read as phone use while driving, and one edit pass to remove gibberish street names.
- **Wired in, minimal edits:** `brand-discovery` homework starts `language-bank.md`; the Phase B copywriter writes the hook bank from it and offers a shortlist; one new gate (hero lines are the owner's picks from the shortlist, logged) and one anti-pattern; the orchestrator's step 0 and 3 rows, companion notes and sources of truth; the README. **The steps, their order, Phase A, the hook voice rules, the ban on invented facts, antislop and copywriting are unchanged.**

## [1.9.0] — 2026-11-03

Sell the offer, keep the template. Found on an agency pitch weeks after Phase B shipped: the owner compared the Phase A clone with the live site and found sections that had been simplified or cut without his knowledge (an image mosaic turned into five text cards, the pricing block removed because there were no prices, case-study details dropped), and no report had told him. He also found the "Got a bar?" service cards corny once he saw a reference agency that simply named its services and listed what each includes, and he wanted that on every design.

- **Hooks in the hero, named services in the cards.** The v1.4 rule "headlines and card titles name the buyer's situation" is split. The hero speaks to a buyer situation or a hidden problem and pays it off. Service cards use the plain name a buyer would search for ("Video & Reels", "Social Media Management", "Websites"), a body that shows the result, and what's included. What fails is a vague department title with nothing under it. The gate and anti-patterns changed to match.
- **Hooks must pay off.** A hook that only names the problem reads as a downer, and one that scolds the owner reads as a lecture. Three real failed lines and their fixes were added to the hook voice table.
- **Offer and packages before copy.** New `packages.md` step in `client-web-delivery` (template: `assets/packages-template.md`) for businesses that sell packaged services: tiers that stack, local published prices with links and the date checked, national benchmarks labeled as such, owner-unset prices labeled suggestions, builder tools and costs kept out. It feeds the pricing slot and the service names on every design option. A missing price is no longer a reason to cut Pricing.
- **No silent cuts.** Every template slot is refilled with real material first. Simplifying a rich section counts as a removal. A removal needs the user's approval and goes in a cut log, and Phase B ends by handing over a template-vs-site report, section by section. Template text hardcoded in a shared component moves into the data file with the template's wording as fallback, so the Phase A baseline still renders unchanged.
- **Argument maps for reference brands.** When a reference is admired for how it sells, step 0 maps its argument (hidden problem, proof, system, offer structure, objections, CTA) and marks which points the client can honestly make today. Phase B follows the map with the client's facts; the reference's wording and numbers never transfer.
- **One services list across design options.** Every design reads services from one shared source; no design borrows another's card copy by title lookup.
- Minimal edits elsewhere: the orchestrator's step 1 and 3 rows and sources of truth, the README step table, the rebrand plan (now lists the named services and packages), two acceptance scenarios (pricing with no prices yet, stats the client can't back). **Phase A, the grammar rules, the ban on invented proof, antislop, copywriting and the approval gates are unchanged.**

## [1.8.0] — 2026-10-24

Client alignment. Step 0 now works for any trade, can be skipped on a cold pitch without losing anything, and ends with something the client actually approves. Everything is an edit to `brand-discovery` in place: no second discovery skill, no second PRD, no separate proof inventory.

- **Yes / Skip for now.** Step 0 opens with a choice. A skip saves `creative-direction.md` as `deferred` with the homework, any directions and the reason; it resumes from that file when the pitch becomes paid work, the owner replies or pushes back, or the client returns. A deferred direction never counts as approved.
- **Adaptive questions for any industry.** New `references/question-bank.md`: core decisions every business has (who it's for, the 10-second takeaway, the main action, which offer leads, what leads, proof, feel, too much, references, hard limits), two or three add-ons each for restaurants, contractors, appointment businesses, retail, licensed professionals, creative agencies, gyms and real estate, and Spanish notes. Questions are picked from what the homework left open; multiple-choice questions carry Not sure, Other and room to explain. The fourth always-settled topic changed from "your best three to five pieces of work" to "what should people see first, and what can you show for it", because the old wording assumed a portfolio business.
- **What leads vs. the evidence.** "Show our work" is split into products, craft, deliverables, verified results, credibility, how the service works, the place and the people. `creative-direction.md` §4 records the owner's desired emphasis and the evidence that exists apart, with the gap going to the setup-list. Results need a source, a date and permission.
- **Reference decoding.** Each reference records the quality admired (visual design, positioning, content hierarchy, credibility, customer experience, volume of work, or other) and only that quality transfers.
- **Alignment statement and approval record** in `creative-direction.md` §8: who approved, role, date, channel, their words or where the evidence is kept, statement version. A returned questionnaire, silence or an unrelated "looks good" is not approval.
- **Feedback diagnosis.** New `references/feedback-diagnosis.md`: when a client rejects or questions a design, write down what they said, map it to a layer (promise, audience, offer order, what leads, proof, feel, density and motion, navigation, technical quality, one element), ask one locating question, size the change, keep the previous direction in the new §9 change log, and re-approve the statement when strategy changed. Then rebuild.
- **Optional discovery PDF kit.** `scripts/discovery_pdf.py` builds a branded, fillable PDF from the same questions (`build`), reads a returned copy into answers with flags for blanks, Other without text, too many picks, Not sure mixed with answers, conflicts and flattened copies (`read`), and writes an empty answers file for text or call answers (`answers-template`). Multiple sending agencies via private profile files, an optional PNG/JPG logo with a typography fallback, optional TrueType brand fonts, English and Spanish built in, tooltips on every field. Nothing is hosted or uploaded; agency profiles and client answers stay out of the repo (projects keep them in a gitignored `discovery/` folder). Needs `reportlab` and `pypdf` (`scripts/requirements.txt`); without them the command says so and points to the text-or-call path. Radio buttons draw their own circle, because reportlab's is only correct at 20pt and otherwise lands in the corner of its box in real viewers. 27 unit tests (`python -m unittest test_discovery_pdf`), including a render through pdfium's form layer that checks chosen answers show where they were made, when the test-only `pypdfium2` is installed.
- **Dependencies install themselves.** New `client-site-pipeline/scripts/setup.mjs` checks Node 18+, the `copywriting` and `antislop` companion packs, ffmpeg and the PDF kit's Python packages, and installs what's missing (`npx skills add … -g -a claude-code -y`, winget or Homebrew, `pip --user`, or a private venv where user installs are blocked). `install.sh` / `install.ps1` run it after copying the skills (`--no-setup` / `-NoSetup` to skip) and install Node first if needed. The orchestrator now has the agent run the setup itself at the start of a job instead of stopping and handing the user commands; it stops only when a required item still fails. The README lists every dependency and why.
- A `creative-direction.md` approved under v1.7.0, before alignment statements existed, keeps its approval; the statement is written from it and confirmed at the next client touchpoint.
- Minimal edits elsewhere: the orchestrator's step 0 row, creative direction gate (deferred, resume triggers, questionnaire is not approval, pushback goes to diagnosis) and sources of truth; the PRD template's §5 gains "What leads" and §6 the `deferred` status; the rebrand reference's prerequisites, art director row and one anti-pattern. The creative-direction template keeps its sections and the template-fit table now sits under §7, so existing `§7` references still land. **Phase A, the PRD gate, cloning safeguards, the pitch workflow, antislop, copywriting and the approval gates are unchanged.** The install scripts already copy every skill folder.

## [1.7.0] — 2026-10-21

Direction before template. Found on an agency pitch: the build was clean and on-brand for the owner's trendy social edits, and the owner still pushed back. He wanted a much simpler site that his non-technical buyers could follow, sized to the amount of work he actually had, and he had been measuring himself against a competitor with a much deeper portfolio. Nobody had asked him how the business should come across.

- **New step 0, `brand-discovery`.** Before the PRD, the agent does the homework (site, socials, Google profile, any brand the owner looks up to) and writes a **vibe read** that keeps confirmed, observed, guessed and unknown apart, with where the client is now next to where they want to be. Then a short **ask-first list**: three to five questions the builder can text the owner, each tied to what was found, naming what the answer decides, ordered so template-changing questions come first. It uses open techniques (this or that, reacting to real versions, plain-word questions, asking why, "never this", unpacking vague words such as "simpler"), never hidden steering. Two or three named directions follow (plain name plus the designer term), and the result is saved to `creative-direction.md` from the new `assets/creative-direction-template.md`. On a pitch with no interview, the builder approves a labeled guess and takes the questions to the meeting.
- **Templates vs. reference brands.** Every link is sorted: a template is a clone candidate once licensed; a real company's site is studied for its niche, promise, proof and buying path, and is never cloned or quoted for claims.
- **`clone-intake` vets the template first:** template or real company, license, look against the direction, size, how much work it needs to look full, navigation in plain words, motion, claim slots, phone, and clone cost (Webflow vs. Framer). A poor fit the user keeps is recorded and still cloned faithfully.
- **Creative direction gate.** Client-facing Phase B needs an approved PRD and an approved creative direction (client for production, builder for a pitch). A draft of either blocks settling the look, not the research, media inventory or rebrand plan. `reference-only` skips step 0.
- Phase B's room checks the direction: the strategist against the intended impression, the copywriter in the approved voice, the art director owning compliance, the UX lead on whether the buyer can picture their own result. Every redline checks the page against `creative-direction.md`; direction clashes use the existing `CONFLICT` / `NEEDS_APPROVAL` states.
- The orchestrator now treats `creative-direction.md` as the strategy and the cloned template as how it looks (antislop gets both). The PRD template points to the direction in §5 and §6 and adds an acceptance item. Step headers now read "steps 0–5". **Phase A, the grammar limits and the ban on fake proof are unchanged.** The install scripts already copy every skill folder and needed no change.

## [1.6.1] — 2026-10-19

Audit fixes found running v1.6 on a two-language pitch (Kasocri Construction, English + Spanish at `/es`).

- `launch-audit/scripts/audit.sh` check [13] counts privacy links with a locale prefix (`/es/privacy`, `/pt-br/privacy`) and reports how many language versions of the privacy page exist. Before, every Spanish page showed as unlinked (21 of 40 instead of 40 of 40).
- Check [9] reports `<html lang>` on every page, grouped by language, and fails on pages with none. When the build has two or more languages it also requires `hreflang` alternates with `x-default` on every non-404 page. Before, it read only `index.html`.

## [1.6.0] — 2026-10-18

Lessons from shipping the Timeless Media pitch.

- `clone-workflow` Phase B adds **hook voice: finesse, not corn**. The payoff half of a hook is the owner's outcome in an everyday phrase (about five words), section headings are confident labels, and there's no forced slang, stunt lines or instructions as headings. Includes the real before/after rewrites the client chose, and offering two or three options when a hook carries the page.
- `client-web-delivery`: add-ons such as an AI sales chat are opt-in per client, never part of the standard offer; renamed or deleted media keep their old URLs alive through `public/_redirects`; the share image is recaptured whenever hero copy changes (1200x630, under ~300 KB, cache-busted).
- `launch-audit`: the OG check confirms the share image shows the current hero and stays under ~300 KB.

## [1.5.0] — 2026-10-17

- **Required companion skills.** `client-site-pipeline` now checks, before step 1, for `copywriting` (`coreyhaines31/marketingskills`) and the `antislop` pack (`miqdadbadjuber/anti-slop`). If either is missing it stops, names them, and gives the install commands. `install.sh` / `install.ps1` print the same reminder.
- Phase B's copywriter drafts with `copywriting` and filters every line, in both languages, through `antislop-copywriting`; the redline uses `antislop-ui`, `antislop-layoutmobile` and `antislop-human` as the checklist for what Phase B/C added.
- The cloned template is antislop's design direction: it filters additions and never restyles the Phase A clone (findings against the template become rebrand-plan proposals). Neither skill overrides the ban on invented facts.
- `launch-audit` runs antislop's contrast checker and Delivery Gate.
- Phase B runs antislop in **DURING** mode: the copywriter and UX lead write with these skills from the first draft, and Phase B closes with the Delivery Gate report. They are not an after-the-fact rewrite.

## [1.4.0] — 2026-10-15

Phase B is judged by the buyer, not by the slots. Found running v1.3.1 on an agency pitch (Timeless Media): every image and heading was replaced, the page still spoke to nobody, and real client reels sat in a folder while AI mood images held the hero and the service cards.

- `clone-workflow` Phase B (`references/intent-aware-rebrand.md`) defines **done**: someone in the target buyer group sees, on the first screen, that the site is for them, what they'd get, and real proof. Swapping content is the method, not the goal.
- **The room:** Phase B runs as four senior roles, each writing its part before the build: strategist/analyst (buyers by situation, research), copywriter (a hook bank in the buyer's words), art director (media truth and slot assignment), UX/front-end lead (grammar, funnel gaps, build). After the build, each role **redlines** the running page and the misses get fixed.
- **Media-truth inventory** (`media-inventory.md`): every client file is opened and logged by what's actually in frame, its origin (real, AI-generated, stock) and the slots it may enter. Filenames are not evidence. Claim slots (hero, services, proof) take real work whenever it exists; AI images fill true gaps only.
- **Headlines name the buyer's situation** ("Got a bar?"); service titles named after departments are a failed Phase B. Punchy lines are fine; invented reviews, prices, contact details and results are still banned.
- Research has a floor: three peer sites, the industry guidance, the client's best-performing posts, and, for agencies, their buyers' industries.
- The rebrand plan must answer what the page still fails to do and whether an existing section pattern should be duplicated to do it.
- A **draft** PRD blocks an invented positioning, not the research, the media inventory or the plan.
- **Lead capture is a Phase B decision per site type:** the money action (call, order, booking, directions or a form), qualifying fields only where the owner uses them, D1 capture so no lead is lost, and a failure message that hands the visitor a working channel instead of a dead end.
- **Cloudflare Workers is the standard host for every project.** A site already on Vercel or Netlify moves over as a named step with its old URL redirected, never silently.
- **Every site ships a second language** as part of the live showcase standard (Spanish for RGV / Texas clients): `/<code>/` via Astro i18n, one copy file per locale over the same facts, written natively (not translated word for word), `hreflang` + `x-default`, locale stored with each signup and inquiry, and a fluent client review on the setup-list. The PRD, architecture-plan and setup-list templates and the launch audit's lang check follow.
- New gates and anti-patterns to match. **Phase A, the grammar limits and the ban on fake proof are unchanged.**

## [1.3.1] — 2026-10-15

Fixes found by running v1.3 on a real near-final pitch (Kasocri Construction).

- `launch-audit/scripts/audit.sh` checks every built page whichever layout the build uses. With Astro `build.format: "file"` (`dist/about.html`, the static + API Worker default) it used to see only `index.html`/`404.html`, report false duplicate titles and miss `/privacy`. Check [13] now also counts the pages that link to `/privacy`.
- `clone-workflow` Phase B (`references/intent-aware-rebrand.md`): re-measure the fixed header after the logo swap; a taller client logo hides inner-page headings under the template's hardcoded offset.
- `client-web-delivery`: moving a project off the Astro Cloudflare adapter, delete the stale `.wrangler/deploy/config.json`.

## [1.3.0] — 2026-10-14

Intent-aware rebranding. Phase A is unchanged; Phase B now knows what the business needs the site to do.

- `client-site-pipeline` adds a **PRD gate** to step 1: read a supplied PRD and never overwrite it, or draft and approve one. A **seed PRD** (just the client's current website link in a text file) is researched and expanded into the full PRD, never mistaken for one. `reference-only` PRDs allow Phase A only. `PRD.md`, `section-purpose-map.md` and `conversion-acceptance.md` join the sources of truth. Unsold showcase sites are now **near-final pitches**: about 99% done, nothing labeled preview or prototype, every form really captures.
- `client-web-delivery` starts Stage 1 from the PRD (intent: audience, proof, the action that makes money, who answers it) and reconciles the architecture plan with it. The standing D1 exception adds an `inquiries` table when the primary action is a form. New `assets/prd-template.md`.
- `clone-workflow` adds a Phase B strategy gate and the on-demand `references/intent-aware-rebrand.md`: a design-grammar inventory (only the template's buttons, where it places them; its fonts, spacing and section patterns), a section-purpose map, editorial media rules (Krea images as labeled illustrative fill only), funnels by business type, and a **first-screen test** (on phone and desktop the first screen must say what is sold, where, why trust them, and what to do next), one label for the primary CTA everywhere, and the near-final pitch standard. The "PRD first" step now reads a supplied PRD instead of rewriting it. **No Phase A text changed.**
- `launch-audit` adds conditional **conversion journey checks**: a real browser submission, proof the submission was stored or delivered, failure paths, a named owner, server-side conversion counts, and `conversion-acceptance.md`. The existing 17 checks are unchanged.
- `architecture-plan-template.md` records `primary_action`, `completion_route` and `destination_owner` from the PRD (the PRD template uses the same names).
- Inquiry capture is fully specified: `POST /api/inquiries` (columns, honeypot, same-origin, honest success message) joins `/api/subscribe` behind the API Worker, which now serves `/api/*`. The setup-list asks who receives new inquiries, and its numbering is fixed.
- Near-final pitches deploy to `*.workers.dev` with `noindex`; it is removed in step 5 after the sale. A missing fact is hidden, never shown as a placeholder. Fonts stay the template's unless the user directs a brand font.
- Conversion checks read the database the form actually wrote to (local for `wrangler dev`, remote for `workers.dev`), prove `tel:` and external order/booking links by following them, accept pending delivery on a pitch, and check a challenge only when the plan names one.

## [1.2.0] — 2026-10-14

Live showcase standard: client sites are often built before the client pays, so every site ships feeling live.

- `client-site-pipeline` adds the live showcase standard to Phase C and to the launch-audit summary. The architecture gate keeps static sites static, with one standing exception: the email-capture API Worker + D1 subscribers table.
- `client-web-delivery` adds a third Cloudflare mode, **static + API Worker** (`run_worker_first: ["/api/*"]`, no Astro adapter, `build.format: "file"`). It also defines the standard: a signup popup + inline signup saved to D1 via `/api/subscribe`, a cookie banner that actually gates analytics, and a privacy page that matches. It includes a signup-hook table by business type, D1 deploy steps (no `database_id`, schema run by the Worker, clean-clone dry run) and Git-connected Workers deploy settings.
- `architecture-plan-template.md` records `api_worker`, the D1 subscribers table, consent-gated analytics, and the newsletter/cookie feature flags.
- `setup-list-template.md` asks what the signup promises and which email tool will send it, and the privacy item now covers newsletter data, the cookie banner and AI-made images.

## [1.1.0] — 2026-10-06

Architecture planning, without changing the five-step order or the clone gates.

- `client-web-delivery` writes `architecture-plan.md` at intake and `deliverables/client-handoff.md` after SEO. New projects default to Astro on Cloudflare Workers. Database is none, Supabase, or Convex, each with a reason. D1 and KV are not auto-selected. R2 is only for files uploaded after launch.
- `clone-workflow` adds Phase C after the existing Phase A verify and Phase B rebrand. Phase C connects only what the architecture plan selected and does not redesign layout.
- `launch-audit` keeps the existing technical and legal checklists, then checks only the systems the plan turned on (including a two-window test when Convex was chosen for realtime).
- `seo` states that a content strategy is required and a blog is not. The existing “a juice bar does not need a blog” rule stays.
- Legacy hosts (Vercel, Netlify) remain valid when the architecture plan names them. They are no longer the default for a new project.

## [1.0.0] — 2026-09-07

Initial release. Six skills:

- `client-site-pipeline` — orchestrator; enforces the five-step order and refuses to skip ahead.
- `client-web-delivery` — intake, the client setup-list, pre-launch gate, deploy. Includes `assets/setup-list-template.md`.
- `clone-intake` — the checklist that gates cloning: live URL + repo `.txt` DOM dumps + motion video.
- `clone-workflow` — the non-negotiable Phase A (verbatim clone, verified against the screenshot/video) → Phase B (content-only rebrand) gate; `ffmpeg` motion-reading; content-integrity rules.
- `launch-audit` — technical + legal ship-readiness on the production build. Includes `scripts/audit.sh`.
- `seo` — SEO / local / GEO-AEO practice with seven reference docs and `scripts/google-index.js`.
