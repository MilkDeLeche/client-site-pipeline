# Instagram mockups: the logo and the site, the way the owner will show them

A mockup is the picture an owner wants to post: their logo as the profile picture, their new site in the bio, a post announcing it, all looking like their own page. It says "look what's being built for me" in the place their customers already scroll. The logo leads; the site comes second.

Everything is drawn in code from HTML templates, so the screen always fits, the words stay sharp, and nothing costs credits. No generated phones, hands or scenes: a screenshot pasted onto a generated screen never lines up well enough to pass for real.

They live in `deliverables/instagram/`, with their sources in `src/` so any of them can be rebuilt. Nothing goes out until the builder says so.

## The three pieces

| Piece | Template | What it shows |
|---|---|---|
| The post image | `assets/ig-post-image.html` | The logo large, one owner-picked line, the news ("New website"), "Link in bio." A real post the client can put on their page |
| The post in the feed | `assets/ig-post-mockup.html` | That post as it appears in a feed: the logo mark as the profile picture, the handle, the place, the action row, a short caption |
| The profile page | `assets/ig-profile-mockup.html` | The page in a phone drawn in code: the logo mark as the profile picture, the name, a two-line bio and the new site's address, four highlights, and a grid of nine: the launch post first, then their real work and a screenshot of the site |

Render each with `scripts/render_cards.py` (4:5 posts; add `--size 1080x1920` for a story version). Render the post image first: it is also the picture in the post mockup and the first tile of the grid.

## What goes in them

- **The logo:** the real file (`brand-kit.md`, or the client's own). For the round profile picture, use the logo's mark alone on the brand color. If the logo has no mark that works in a circle, set the name's initials in the logo's typeface on the brand color, and say so in the report: it is a proposal until the owner sees it.
- **The handle and name:** the ones they have. If the page's name and the business name differ, show what they use today and put the question on the owner sheet.
- **The grid and highlights:** their real photos and real screenshots of the live pitch, cropped to 4:5. Never a generated picture of their work.
- **The bio and caption:** an owner-picked line, then plain facts. Researched the `copy-bank` way like every other line.

## Never on a mockup

- A follower, following, post or like count. A number nobody measured is a fabricated claim, and the templates leave them out.
- The platform's own logo or wordmark. The layout is generic: it reads as a social page without claiming to be one company's screen.
- Anything uncleared that becomes legible: client names, prices, a person's face they haven't agreed to.

## Before building: what's current

Check how agencies and brands are showing launch posts right now on **Pinterest and Reddit** (searches like "instagram post mockup", "brand reveal post", "website launch post"), dated, in `src/notes.md`. Take the layout idea, never someone's design.

## Check before it goes anywhere

- `render_cards.py` passes (nothing cut off, every image loaded, no `{{placeholder}}` left).
- Open every PNG: the logo is sharp, the handle and bio are right, no one-word last line in the caption, and nothing uncleared is legible in the grid or on the site screenshot.

## Done when

- [ ] The post image, the post mockup and the profile mockup are rendered, opened, and use only the real logo, real work and real screenshots
- [ ] No counts and no platform logo on any of them
- [ ] The builder knows where the folder is and that nothing goes out until they say so
