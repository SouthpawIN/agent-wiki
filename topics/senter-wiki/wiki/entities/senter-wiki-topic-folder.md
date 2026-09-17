---
title: Senter-wiki topic folder — missing directory gap and creation
created: 2026-09-08
updated: 2026-09-09
type: entity
tags: [infra, repo, decision]
sources:
  - raw/inbox/2026-09-08.md
confidence: high
---

# Senter-wiki topic folder

## What happened
The `senter-wiki-bot` profile exists and serves topic `senter-wiki`, but there was **no `senter-wiki` topic folder** in the vault. The `scan-topics.py` scanner requires a topic directory to exist so it can map the profile to the topic.

> "There's no `senter-wiki` topic directory! ... The senter-wiki-bot profile serves the `senter-wiki` topic, but there's no `senter-wiki` topic folder."
> ^[raw/inbox/2026-09-08.md]

## The gap
- `senter-wiki-bot` AGENTS.md says it serves topic `senter-wiki`.
- The vault had `topics/senter/` but no `topics/senter-wiki/`.
- Without the folder, `scan_topics()` could not populate the `senter-wiki` topic's bots/skills/loops in `.system-live.json`.
  ^[raw/inbox/2026-09-08.md]

## Resolution
A `topics/senter-wiki/` directory was created with proper structure:
- `README.md`
- `index.md`
- `.system/`
- `wiki/`

> "Excellent! The scan now shows the `senter-wiki` topic with the correct bots including `senter-wiki-bot`."
> ^[raw/inbox/2026-09-08.md]

## Result
Post-fix scan shows: 20 skills, 4 bots (including the real `senter-wiki-bot`), 88 wiki pages for the `senter-wiki` topic.
^[raw/inbox/2026-09-08.md]

## See also
- [[topics/senter-wiki/wiki/entities/scan-topics|scan-topics.py]]
- [[topics/senter-wiki/wiki/entities/agent-wiki-repo|agent-wiki repo]]
- [[topics/senter-wiki/wiki/decisions/2026-09-08-senter-wiki-topic-structure-gap|Topic structure gap decision]]
