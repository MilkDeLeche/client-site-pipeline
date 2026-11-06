# Presenting design options: the shelf

Use this when an owner can't choose from descriptions, or keeps turning down one build after another. Put the finished options on one page they can open on their phone, side by side, and let them pick.

First used on an agency pitch: four finished designs on a shelf of VHS boxes, one cover per design. The format is free. The rules below are what mattered.

## What goes on it

- **Finished designs only.** Each one is a Phase B build with the client's real content. The Phase A template baselines (the template's own copy and images) are never shown, on the shelf or on the deployed site. Gitignore their routes and keep them locally for fidelity checks.
- **Licensed code only.** A design built on a bought template ships once the licence is bought. Until then, show it on your screen.
- **Names the owner reads.** A plain name per option (Bold, Minimal, Noir, Editorial), the owner's own words for the direction ("Calm and spacious", from `creative-direction.md`), one line on what the site is like, and facts (fewest sections, quote form on the page, languages). Template product names and platform names mean nothing to the owner, so leave them out.
- **Written to the owner.** They are the reader: "the businesses you've worked with", not "the owner asked for".
- **Cover art can be AI.** It labels an option, not the client's work. Log it in the project's `image-prompts.md`, give each cover that design's palette and a scene from its own content, and check every output for real brand logos the model invented (one cover came out with a retailer's logo on a store wall).
- **Built from a motion-site template.** When the builder supplies a motion-site prompt (scroll scenes, frame sequences) for the shelf, use `motion-template`: it names the technique, maps the template's assets to the client's work, and gets the asset plan and its credit cost approved before generating anything.

## How it behaves

- **Unlisted.** `noindex`, out of the sitemap (check the sitemap filter: `/design-` does not match `/designs`), and not in the site's navigation. You send the owner the link.
- **One language per visit.** The browser's first preferred language picks it, and `?lang=` overrides it for previews. Never both languages side by side.
- **Opening a design** goes to the real page in the same tab. A transition into it is optional polish. If you build one, preload the page in a hidden frame and grow the frame to full screen before navigating, so the swap shows no jump. Ctrl-click and middle-click still open a new tab, reduced motion goes straight to the page, and Back restores the shelf, including any text the transition hid.
- **A way back from every design.** A small "All designs" control, shown only to visitors who came from the shelf: the shelf sets a session flag, and each design page checks it. Regular visitors to the live site never see it. Keep it clear of each page's own buttons. On the pitch it covered a hero's quote button on phones, so it now slides in once the visitor scrolls past the first screen. It stays reachable by keyboard: moved off-screen, not hidden.

## Verify

- **Click every control for real**, and check that `document.elementFromPoint` at each button's centre returns that button. On the pitch a full-width decorative band (the centred logo strip in the top bar) sat over the Close button, so only Escape worked.
- **Judge motion by state, not by screenshots.** Automation browsers can throttle `requestAnimationFrame` to a couple of frames a second, so mid-animation screenshots lag behind the page. Wait, then read the page's state.
- **Check phone width** for every design with the return control showing.
- **Build from a clean clone of the commit**, which is what the host builds. Confirm the template routes are gone, the shelf and every design are present, and the shelf isn't in the sitemap.
