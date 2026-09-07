# Contributing

## Skill anatomy

Every skill is a folder under `skills/` containing a `SKILL.md`:

```markdown
---
name: skill-name              # kebab-case, must match the folder name
description: >                 # one paragraph — this is what the agent
  When to use this skill and   # matches against, so lead with triggers
  what it produces.
---

# Human-readable title

The instructions the agent follows.
```

Supporting files live alongside it in conventional subfolders:

- `assets/` — templates the skill copies into a project (e.g. a setup-list)
- `scripts/` — runnable helpers the skill invokes
- `references/` — deeper documentation the skill loads on demand

## Editing rules

- **The `description` is load-bearing.** An agent decides whether to open a
  skill from its description alone. Front-load the trigger phrases; be concrete
  about the artifact it produces.
- **Keep each `SKILL.md` short.** If a topic needs depth, move it to
  `references/` and link to it — the agent loads references only when needed.
- **Cross-references use the skill name**, e.g. "`clone-intake`", not a path.
  The orchestrator (`client-site-pipeline`) owns the ordering; individual
  skills state their step number and their neighbours.
- **The pipeline order is a contract.** If you change what a step produces or
  requires, update `client-site-pipeline/SKILL.md` and the "Done when" column
  in the README in the same change.

## Testing a change

1. Copy the edited skill into your agent's skills directory (`./install.sh`).
2. Run the relevant step on a real project and confirm the gate still fires
   when its input is missing.
3. Update `CHANGELOG.md`.
