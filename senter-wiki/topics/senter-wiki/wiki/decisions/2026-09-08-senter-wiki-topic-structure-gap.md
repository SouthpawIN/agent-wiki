---
title: Senter-wiki topic structure gap and resolution
created: 2026-09-08
updated: 2026-09-08
type: decision
tags: [infra, question, bot]
sources:
  - raw/inbox/2026-09-08.md
confidence: high
---

# Senter-wiki topic structure gap and resolution

## The problem

The `senter-wiki-bot` profile exists and serves topic `senter-wiki`, but there was no `senter-wiki` topic folder in the vault. The `scan-topics.py` scanner required an actual topic folder to emit the correct topic data.

Investigative chain:
1. bots list showed incorrect items in `agents/` directory (markdown files not real bots)
2. `senter-wiki-bot` has a SOUL.md, so it should be detected
3. No `senter-wiki` topic directory found
4. Checked archive - not there either
5. The AGENTS.md says it serves topic `senter-wiki`

## The resolution

The scan was updated to properly detect and create the `senter-wiki` topic with:
- 20 skills
- 4 bots (including the real `senter-wiki-bot`)
- 88 wiki pages
- 35 topics, 69 bots, 201 skills, 81 loops

**Raw evidence:**
"Excellent! The scan now shows the `senter-wiki` topic with the correct bots including `senter-wiki-bot`. Let me verify the updated `.system-live.json`:" (2026-09-08 09:57) ^[raw/inbox/2026-09-08.md]

"The `senter-wiki` topic now has:
- 20 skills
- 4 bots (including the real `senter-wiki-bot`)
- 88 wiki pages
- 35 topics, 69 bots, 201 skills, 81 loops" (2026-09-08 09:59) ^[raw/inbox/2026-09-08.md]

## Open issue (resolved)

1. ~~Remove `.md` extension from bot names~~ — resolved on 2026-09-08; scanner strips `.md` from display names. ^[raw/inbox/2026-09-08.md] ^[raw/inbox/2026-09-09.md]

## Related
- [[topics/senter-wiki/wiki/entities/senter-bridge|senter-bridge]]
- [[topics/senter-wiki/wiki/entities/scan-topics|scan-topics scanner]]
- [[topics/senter-wiki/wiki/entities/senter-wiki-bot|wiki-bot (if it exists)]]