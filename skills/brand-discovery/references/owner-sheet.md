# The owner sheet

Moved here word for word from `SKILL.md` section 8 (v1.25.0).

One PDF the owner fills in once. It carries everything only they can decide, so nothing is asked piecemeal and nothing waits on a question nobody sent. `packages.md`, the setup-list and `creative-direction.md` stay with the builder: an owner never gets Markdown, a vendor name or a key to paste. Nothing is hosted, uploaded or stored online: the builder sends the file through their own channel and reads the returned copy on their own machine.

Three parts, in this order:

1. **What you sell.** The plans from `packages.md` in buyer words: what a client gets, a suggested price, and a blank for the owner's own (`"type": "prices"`). Owners react to their offer on one page before they react to any design. A site that never shows what the buyer gets is the usual reason an owner stalls on a build that looks fine.
2. **The site.** The recommended design with its link and a veto question (section 5), then the ask-first questions still open. When the owner used a word that could mean several things ("the output", "simpler", "amateur"), quote it back and offer what it could mean.
3. **Only you can answer these.** Who gets the requests, whether a phone and email show, permission to name clients, a photo of the owner, and the name on the social page when it differs from the site (the front door, section 1).

Rules:

- **Twelve numbered items at most,** ticks wherever a tick will do. Anything more waits for a second sheet, after the first comes back.
- **Every tick question has a fallback** (`default` per question): the option that makes no new claim and changes nothing the owner didn't ask for, such as no prices shown, no clients named, the form only. A question about something only the owner can do, like renaming their Instagram, has none.
- **A date when they owe an answer** (`decide_by`). A client or a partner gets one date for the whole sheet. An owner who was pitched and hasn't bought owes nothing by Friday: leave the date off, and the sheet reads "No answer? We'll go with: …".
- **A fallback that takes effect is the builder's decision.** Log it in §3 as `default, owner silent` with the date. It lets the job move. It never counts as the owner's approval of the alignment statement.
- **Answerable by text.** `reply_by_text` letters the options, so "4C 5A" in a message is a complete answer. Transcribe it with `answers-template`.
- **The builder checks every suggested price before the sheet goes out.** Each stays labeled a suggestion until the person who does that work sets it.
- **In the owner's words.** Write the lines through `copywriting` and `antislop-copywriting`. No design words, and no "packages": say plans, or the trade's own word (menu, services, memberships).
- **When.** On an outbound pitch it goes with the pitch kit or right after the owner has seen the site, as the way to steer it. For an inbound client it goes before the build. After any pushback it is the cheapest next move.
- **Where.** `deliverables/owner-sheet/<client>-owner-sheet.pdf`, with its `src/` beside it. The builder opens it, fixes what's wrong and sends it. Nothing goes out until they say so. Returned copies and answers go in `discovery/`.

Start from `assets/owner-sheet.example.json`. A sheet with only the questions (no plans, nothing to hand over yet) starts from `assets/questions.example.json` and builds the same way.

```
node ~/.claude/skills/client-site-pipeline/scripts/setup.mjs   # installs reportlab and pypdf if missing; it prints the Python to use
python scripts/discovery_pdf.py build deliverables/owner-sheet/src/questions.json --agency ~/.client-site-pipeline/agencies/<slug>.json --out deliverables/owner-sheet/<client>-owner-sheet.pdf
python scripts/discovery_pdf.py read discovery/returned.pdf --questions deliverables/owner-sheet/src/questions.json --out discovery/answers.json
python scripts/discovery_pdf.py answers-template deliverables/owner-sheet/src/questions.json --out discovery/answers.json   # text or call answers, no dependencies
```

- **Questions:** keep only what the homework left open, and rewrite the options from the research. Not sure and Other are added automatically (`"not_sure": false` and `"other": false` drop them where a veto or a yes/no needs neither); `note: true` adds room to explain; `links` puts a link under the prompt; `conflicts` flags answers that pull apart. A `"type": "section"` item starts a part and takes no number. `locale: "es"` switches the built-in text to Spanish.
- **Open the PDF before it goes anywhere.** Render the pages and look: a question split across two pages, a price that runs into its field, a long label that wraps to one word. Fix the wording, not the type size.
- **Agencies:** one profile per sending agency, from `assets/agency-profile.example.json`, kept outside any public repo (suggested `~/.client-site-pipeline/agencies/<slug>.json`). The logo is optional (PNG or JPG). Without one, or when it can't be read, the PDF sets the agency name in type and prints a note.
- **Privacy:** questions, returned PDFs and answers live in the project's `discovery/` folder, which is gitignored. Agency profiles and client answers never go into this skills repo.
- **Reading it back:** `read` flags blanks (with the fallback that will stand after the date), Other without text, too many picks, Not sure mixed with answers, and conflicts. A price left blank keeps the suggestion and isn't flagged. A copy that was printed, scanned or flattened has no fields left: `read` says `flattened`, and the answers are typed into an `answers-template` file by hand with provenance `transcribed`. Every flag becomes a follow-up question, not a guess.
- **Dependencies are the agent's job.** Before the first `build`, run the setup above yourself (or `python -m pip install --user -r scripts/requirements.txt`); never ask the owner or the user to install anything. If it still can't install, the rest of the pipeline is unaffected: ask by text or call. Tests: `python -m unittest test_discovery_pdf` from `scripts/`.

A returned PDF fills §3 and §4. It never fills §8's approval.
