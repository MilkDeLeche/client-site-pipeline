# Phase B: image prompts for true gaps

`intent-aware-rebrand.md` §4 says when an AI image may be used. This file is how to make one that looks like it belongs on the page, and how to keep a record of it. Generation runs through Krea (`krea-generate`: list the live models, read the model's prompting guide, then submit).

## 1. Find the gaps first

From `media-inventory.md` and the running page, list every image slot whose picture doesn't show what its text says. Typical gaps: a service with nothing to film (search, hosting, bookkeeping), a mood background, a texture, an empty-state illustration, an OG image backdrop.

A slot qualifies for an AI image only when **no real file can honestly fill it**. Write the slot, its claim, and why no real file fits. If a real file fits, use it. If the slot claims "this is our work", "this is our team" or "this is a result", it never gets an AI image: put the missing photo on the setup-list.

## 2. Write the prompt from the real footage

The image has to sit next to the client's real work without looking like a different company made it. Before writing, look at three or four of the client's real files from `media-inventory.md` and note their light, color grade, lens and time of day. Then write a narrative prompt (not a keyword list):

1. **Operation and subject:** "Create a candid night photograph of a hand holding a phone…"
2. **What it shows for the claim:** the idea of the slot in something you can see (a glowing map pin for "found in search"), never a fake result.
3. **Place:** the client's region, said concretely ("a sidewalk in a small South Texas border town, outside a family-run taqueria").
4. **Composition for the slot:** the slot's aspect ratio and crop (set the ratio in the model's field, not the prompt), where the subject sits, room for text if the slot has an overlay.
5. **Camera and light:** lens, aperture, focus point, film grain, the color grade copied from the real footage.
6. **Clean surfaces, said positively:** "every sign and surface is clean and unmarked, blurred into soft color" instead of "no text". No brand names, no logos, no readable UI, no recognizable faces.

Pick the model with `krea-generate`'s shortlist: a precise subject that has to look real goes to a high-fidelity model, while mood and illustration can use a faster, cheaper one. Make two variants that differ in one idea (place, angle), not ten.

## 3. Check it like a photo editor

Open every output before using it, at full size:

- Hands, fingers, phone shape, reflections, any letterforms (AI text renders as gibberish; it must be blurred or absent).
- Does it look like the client's footage, or like stock? If it looks like stock, retake with the grade and lens from step 2.
- Does it make a claim the client can't back (a five-star rating, a "#1" badge, a crowd that implies results)? Then it's out.
- Crop it to every slot that will use it and check the subject survives on desktop and phone.

Name a bad output plainly and retake with one correction at a time.

## 4. Use it, label it, log it

- Alt text describes it as an illustration ("Illustration: a phone showing a map pin outside a local storefront at night").
- Add it to `media-inventory.md` with origin `AI-generated` and the slots it may enter.
- Record it in the project's `image-prompts.md`: slot, claim, why no real file fits, model, the full prompt, aspect and resolution, date, which variant was used and why, the file path, and the alt text.
- The privacy page discloses AI imagery (`launch-audit` checks it). "Send us a real photo for this" goes on the setup-list when one could replace it later.
- When one service appears on several design options, they all use the same image, from the shared data file.
