# Kickoff: one start, two pauses

How a job starts and how it runs to a finished pitch without stopping to ask what the builder has already answered.

## 1. Read the builder profile

`~/.client-site-pipeline/builder.json` (example: `assets/builder-profile.example.json`). It holds the builder's standing answers: the way of working (outbound or inbound), the antislop mode, the second language, the Krea credit budget per job, how cuts are approved, the prices, the tools that are never named to a client, and where to look for trends. **Never ask a question the profile answers.** If the file is missing, ask for those answers once, write the file, and carry on. Anything marked CONFIRM in it is the agent's reading: use it, and list it in the readiness report.

## 2. "Start the pipeline": find one, or have one in mind?

Ask one question:

> Do you want me to find a business to pitch, or do you have one in mind?

- **Find one:** ask where (a city, a neighborhood or a stretch of road) and, if they care, which trades. Then run `references/prospecting.md` and bring back a short list. The builder picks, and the pick becomes the brief.
- **Have one in mind:** take the brief below.

Skip the question when the builder already named a business or pasted a link.

## 3. The brief

Everything the run needs, asked once:

| | |
|---|---|
| The business | A link (their site, Instagram, Facebook or Google listing) or the name and city |
| City and area | Where they sell |
| Trade | In the owner's words |
| Template | A link if the builder already chose one; otherwise the design scout proposes the search |
| Anything known | A contact, a referral, something the owner said |

A link alone is enough. The rest is found in step 0.

## 4. Run, and stop only twice

Run steps 0 to 3 without stopping to confirm, deciding from the profile and the research. Write down every guess instead of asking about it.

1. **Pause 1, the template.** After the market read and the design scout, show the template search brief and the recommended direction. The builder picks the template (or says "you pick").
2. **Pause 2, before anything goes out.** With the pitch live and the deliverables built, hand over the readiness report. Nothing is sent, posted or printed until the builder says so.

These still stop the run, because they cost money or can't be undone: spending Krea credits beyond the profile's budget, buying a template, deploying to a real domain, anything a safety rule covers, and a template cut the profile says to ask about.

## 5. Keep the state file current

`pipeline-state.md` at the project root (template: `assets/pipeline-state-template.md`). Update it at the end of every step and before stopping for any reason. It is how the next session, or another tool, picks up without rediscovering anything: read it first on any project that has one, and trust the repo over it when they disagree.

## 6. End with the readiness report

`deliverables/readiness-report.md` (template: `assets/readiness-report-template.md`). One page for the builder: what's built, what's a guess, what was checked and how, what the owner still owes, what it cost. It is for the builder only. Then, when the builder approves, `references/outreach.md`.

## A new project folder

`node ~/.claude/skills/client-site-pipeline/scripts/scaffold.mjs <folder> --name "<Business>"` makes the folders, the gitignore entries, the state file, the capture Worker with its two tables, and the Cloudflare config. It prints the one command that adds Astro. It never overwrites a file that exists. After `git init`, run `node ~/.claude/skills/client-site-pipeline/scripts/guard_private.mjs` once so the pre-commit hook is in place before the first commit.
