# Pending items of the skill

Every client project keeps one list for the builder of what the pipeline can still do for that client and hasn't done yet, with how to get each one done. It exists so the builder can step away for weeks, open the project, and know in a minute what's missing and how they've been doing it.

**File:** `deliverables/pending-items-of-the-skill.md` (gitignored, never sent to the owner). Written in the builder's language, plain, as a checklist.

## When to update it

- At the end of every session that changed the project, before the final message.
- When a step finishes (tick it, with the date) or a new one becomes possible.
- At the start of a session on an existing project, read it right after `pipeline-state.md`, and mention the top two open items in one line.

## What it holds

Start from the full menu below and keep only what applies to that client. For each open item: what it is, why it matters for this client, the next concrete step, and who does it (the builder, the owner, or "say the word and I do it").

1. **Pipeline steps:** brand discovery, PRD, architecture plan, clone intake, build (Phase A, B, C), launch audit, security round (`client-site-security`), SEO. A step that was done once but should be rechecked after big changes says so ("security: recheck after the email marketing update").
2. **Extras** (`references/extras.md`): logo loading animation, the loader-to-hero transition, motion-site template, social videos.
3. **Email marketing** (`client-web-delivery` → `references/email-marketing.md`): domain verified in Resend, key set with `wrangler secret put`, automations set up, **"Time to design or bring the email template: pick one in Copymail and I'll adapt it to the brand"**, the first monthly newsletter, the owner's perk for the signup (if any).
4. **Deliverables:** update brochure for the last update, billable up to date, handoff, pitch kit, mockups, hype set, launch reel, ads.
5. **The owner's to-dos:** things only they can do (a domain, a Google Business Profile change, a photo, a sign to repaint), copied from the setup-list.
6. **Rechecks:** dependency updates (`npm audit`), the responsive audit after design changes, the launch audit after the home page changes.

## Shape

```markdown
# Pending items of the skill: <client>
Updated: <date>

## Next up
- [ ] <the one or two things to do next, with the first step>

## Open
### Email marketing
- [ ] Bring the email template from Copymail. Why: the newsletter still uses the plain base. Next: pick one, send me the link or a screenshot.
...

## Done
- [x] Security round 3, 29/29 checks (2026-11-27)
```

Keep it short enough to read in a minute. Done items move to the bottom with their date and are trimmed after a few months.
