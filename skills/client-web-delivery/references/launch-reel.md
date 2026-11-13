# The launch reel

Fifteen seconds an owner wants to post: their real site moving inside a phone, then one or two animated cards. Nothing in it is generated video. The site on the screen is the real site, recorded, and the cards are animations written in code, so every word stays sharp.

It is built from pieces the job already has: the live pitch and the hype cards (`hype-set.md`). It costs no credits. It lives in `deliverables/reel/`.

## Before building: what's moving right now

Reel styles turn over in weeks. Check **Pinterest and Reddit every time** (the builder's standing rule), plus the trade's own corner of Instagram or TikTok when the builder can show it:

- Pinterest: search the kind of reel plus the trade ("website launch reel", "coming soon reel bakery"). Note the opening second, the pace, how words come in, the shapes in use.
- Reddit: the trade's subreddit and the social media ones (r/socialmedia, r/smallbusiness, r/InstagramMarketing) for what owners say is working and what they're tired of seeing.
- Write the date and what was seen in `deliverables/reel/src/notes.md`. Take the structure of what works (the first-second hook, the rhythm). Never copy someone's line, sound or footage.

These sites need a logged-in browser: use the builder's, and stop at any wall.

## The pieces

1. **The site, moving.** `reel.py record <pitch url> src/scroll-phone.mp4 --size 412x952 --seconds 10 --scroll` films the live pitch in Chrome at a phone's shape: a short hold, a glide down the page, a hold.
2. **In a phone drawn in code.** Copy `assets/reel-phone-frame.html` next to the recording, put one line above the phone, and film it: `reel.py record src/phone-frame.html src/part-site.mp4 --size 1080x1920 --seconds 10`. The recording plays inside the phone, so the screen always fits.
3. **Animated cards.** A hype card with its lines arriving in order and its number counting up to the real value: `assets/reel-stat-card.html`. Film it with `reel.py record src/reel-stat.html src/part-stat.mp4 --size 1080x1920 --seconds 6`. Any card can be animated the same way: one movement, used in reading order, and the finished frame is the still card. People who turn motion off see it finished.
4. **Joined.** `reel.py join <client>-launch-reel.mp4 src/part-site.mp4 src/part-stat.mp4`.

## Writing an animation in code

- One idea per card and one kind of movement per reel. Lines rise in as the eye reaches them; a number counts up and stops exactly on the sourced value.
- The words follow the hype set's rules: a researched hook, an exact number, the source on the card.
- Keep it under seven seconds a card. The whole reel runs 12 to 20 seconds.
- The first second has to work with the sound off and no context: the phone in the hand, or the hook already on screen.
- A logo that builds itself is `motion-template` → `references/logo-loader.md`. It can open or close the reel.

## What it doesn't have

Sound. Add music inside Instagram or TikTok when posting, from their own library, so the licence is theirs to give. The builder or the owner does that step.

## Check before it goes anywhere

- Play it on a phone, sound off. The first second reads.
- Pause on three frames: the words on the screen are sharp, and nothing unapproved is legible (client names, prices). A long scroll passes a lot of the page: record a section without them if they aren't cleared.
- Every number is the one on its still card, and the source is on screen long enough to read.

## Done when

- [ ] The trend note is dated, from Pinterest and Reddit
- [ ] The screen recording is of the live pitch, and the framed clip was checked on paused frames
- [ ] Each animated card ends on its still version, with the source visible
- [ ] One file, 12 to 20 seconds, 1080 by 1920, played on a phone
- [ ] The builder knows it has no sound yet and that nothing was posted
