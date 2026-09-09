---
title: Bot naming convention — remove .md extension from display names
created: 2026-09-08
updated: 2026-09-08
type: decision
tags: [ui, bug, spec]
sources:
  - raw/inbox/2026-09-08.md
confidence: high
---

# Decision 2026-09-08: Bot naming convention — remove .md extension

## The problem

Bot names were displaying with `.md` extensions in the UI: `librarian-bot.md` instead of `librarian-bot`.

**Raw Chris observation:**
"1. Remove `.md` extension from bot names in the senter-wiki topic (e.g., `librarian-bot.md` should be `librarian-bot`)" (2026-09-08 09:59) ^[raw/inbox/2026-09-08.md]

## The fix

Remove the `.md` extension from bot names when rendering in:
- SKILLS/BOTS/LOOPS rows
- Orb tooltips
- Card displays
- Any other bot name presentation

The underlying file remains `librarian-bot.md`, but the display name should be `librarian-bot`.

## Related
- [[topics/senter-wiki/wiki/entities/fleet-bots|Fleet bots]]
- [[topics/senter-wiki/wiki/entities/senter-bridge|senter-bridge]]
- [[topics/senter-wiki/wiki/concepts/approval-policy|Approval policy]]