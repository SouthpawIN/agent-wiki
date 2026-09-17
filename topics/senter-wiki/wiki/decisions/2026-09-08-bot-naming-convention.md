---
title: Bot naming convention — remove .md extension from display names
created: 2026-09-08
updated: 2026-09-09
type: decision
tags: [ui, bug, resolved, spec]
confidence: high
sources:
  - raw/inbox/2026-09-08.md
---

# Decision 2026-09-08: Bot naming convention — remove .md extension

## The problem

Bot names were displaying with `.md` extensions in the UI: `librarian-bot.md` instead of `librarian-bot`.

**Raw Chris observation:**
"1. Remove `.md` extension from bot names in the senter-wiki topic (e.g., `librarian-bot.md` should be `librarian-bot`)" (2026-09-08 09:59) ^[raw/inbox/2026-09-08.md]

## Resolution

The scanner's `scan_bots()` and `scan_vault_agents()` functions were updated to strip the `.md` extension from bot
display names. The underlying file remains `librarian-bot.md`, but the rendered name in SKILLS/BOTS/LOOPS rows, orb tooltips,
card displays, and all other bot name presentations now shows `librarian-bot` without the extension.

**Evidence of fix:** The 2026-09-09 scan confirmed the bot names are now clean — hero meta shows "skills ×6 · bots ×3" without
`.md` artifacts. ^[raw/inbox/2026-09-09.md]

## Related

- [[topics/senter-wiki/wiki/entities/fleet-bots|Fleet bots]]
- [[topics/senter-wiki/wiki/entities/senter-bridge|senter-bridge]]
- [[topics/senter-wiki/wiki/concepts/approval-policy|Approval policy]]
