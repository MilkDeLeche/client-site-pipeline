# Update brochure

Every time a batch of work ships live after handoff (a dependency upgrade, a security round, a new feature, a fix), make a short brochure that shows the owner what changed behind the scenes. Most of this work is invisible: nobody sees a framework upgrade or a closed hole unless we show it. The brochure turns it into something the owner can read in a minute and is glad to pay for.

## When

- After the update is deployed **and verified live**, never before. The brochure reports what is true now.
- One brochure per update batch. Small fixes in the same week go into one.
- A security round (`client-site-security`) or a maintenance upgrade always gets one.

## Where

`deliverables/actualizaciones/<YYYY-MM-DD>-<short-name>.html`, exported next to it as `.pdf` (letter or A4) and one `.png` per page. Like everything in `deliverables/`, it goes to the owner only when the builder says so, and only as the PDF or images.

## Fixed wording (builder rule, every brochure)

- **Title:** "Your Cybersecurity Update", in the owner's language ("Tu actualización de ciberseguridad" in Spanish). Always this title, whatever the update contains.
- **Badge next to the title:** "This month" ("Este mes"), with a calendar icon.
- **Closing block, always:** "Why it matters" ("Por qué importa"), the last thing on the final page: one or two plain sentences on what this work protects in their business (customers who can book, a page that doesn't go down), in the owner's voice, with no scare statistics. The builder approved this closer on the first brochure (Nov 2026).

Everything else (the design, the illustrations, the points) is made for that client and that update.

## Look: that client's own design kit

Build it from the client's brand, not from a house template: read `creative-direction.md`, the site's design tokens (fonts, colors, radius, spacing) and the logo, and reuse the site's own imagery or illustrations. The brochure should look like a page of their site. Two clients' brochures should look nothing alike. Make it light and a little fun inside that brand (big numbers, before/after cards, a playful heading), never a dry report.

## Selling points: make the work look worth it

Every update becomes a few selling points, each one led by what the owner or their customers gain, with the proof right under it. Lead with the two or three strongest on the first page, big, each with its own visual, then put the rest as short cards.

- **Look for the win in every change, then measure it.** Measure what you can: bundle size before and after, load time on a throttled phone (median of 5), the number of checks that passed. A visitor-facing improvement (smoother page changes, fewer blank flashes) counts when you saw it in the browser.
- **Never sell a gain you didn't measure.** A newer version can be bigger or no faster. If the upgrade itself didn't make the site faster, say what it did do (security fixes, smoother navigation, still getting fixes) and don't write "faster". When you want a speed point, look for a real one in the same update (a heavy library out of the first load, a third-party script removed) and measure it.
- **Illustrate each point from the client's world**, in code from their brand, without spending credits. For example, a bike shop's router upgrade became a dotted cycling route between the site's pages, with a bike on it. Use generated images only with the builder's yes and a quoted cost.

## Voice: sound like a person

Before writing, look up how real owners and customers talk about the topic (Reddit threads, the `deep-research` or `copy-bank` research; when nothing turns up, say so and use what owners say in reviews and forums). Write the way the owner speaks: their language and country, short sentences, "you" and "your page". Then run the text through `humanizer` / `antislop-copywriting`. Cut every AI tell: "not just X but Y", lists of three, inflated words, em-dash asides, vague praise. One plain closing line on why it matters for their sales is fine; scare statistics without a source are not.

## Content: facts from this update only

Write in the owner's language, in plain words, one idea per card. Use only what the tool output from this update proves:

- **Before and after:** versions (for example "page navigation library: version 6, now version 7"), counts ("5 security warnings, now 0"), what a screen or permission did before and does now.
- **What it means for them:** one line each, about their business, not the technology ("your site keeps getting security fixes", "only the people you choose can change the gallery").
- **Tests run:** how many checks, how many passed, grouped simply (from outside, inside the database, the build). Exact numbers from the runs.
- **What they need to do**, if anything (a setting only they can change, a sign to repaint), short and kind.

Leave out:

- Secrets, keys, internal URLs, account IDs.
- Vendor account names. Say "your database" or "your server", not the hosting or tool brand. Library names are fine when they help ("React Router 7").
- How an attack works. Describe the protection, never the exploit or a payload.
- Any number that a run didn't produce. Write no number rather than an invented one.

## Build and check

1. Write the HTML with the client's fonts and colors, inline SVG icons (no emoji-able characters), sized for letter or A4 at print, readable on a phone as an image.
2. Render it with Playwright or Edge to PDF and PNG (`page.pdf`, `page.screenshot` per page).
3. Open the PNG and read it as the owner would: every number matches this update's output, nothing technical is left unexplained, text contrast passes, and it fits the page.
4. In the same session, bring the billable up to date (`billable.md`: new lines for what shipped, the comparison checked again; the price only changes when the builder says so), refresh the email previews if emails changed, and update `deliverables/pending-items-of-the-skill.md`.
5. Tell the builder where each one is, in one line each.

## Example, not a template

A bike shop's first brochure, Nov 2026: black-and-white editorial brand (DM Sans and Inter, condensed wordmark) with the door mural's yellow, green and red as accents. Two letter-size pages, in Mexican Spanish. React Router 7 measured bigger than 6, so the brochure didn't call it faster: it sold smoother page changes, and the speed point came from moving a heavy library out of the first load (960 KB down to 729 KB, the home page 0.3 s sooner on a throttled phone, median of 5 runs). Page 1:
- "Tu página ya corre con React Router 7", over a cycling-route illustration.
- "Abre con 24% menos peso", with before and after bars.
- "29 pruebas, las 29 pasaron", with a shield.
- 5 warnings now 0.

Page 2 had short cards (gallery roles, a fixed broken-photo bug, one opening time everywhere, what's new on screen), how it was tested, the owner's two to-dos, and one closing line on why it matters.

A different brand leads to a different brochure.
