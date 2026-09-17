---
title: umbrella (cross-topic opinion pass)
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [tool, loop, decision]
sources:
  - raw/inbox/2026-09-05-legacy-inbox.md
confidence: high
---

# umbrella

`assets/umbrella.py`, launchd `com.senter.umbrella`, every 30 min. Merges topics using the similarity thresholds Chris locked on 2026-09-02
(auto ≥0.50, propose ≥0.35; `name_contains` floors to 0.65; locked topics downgrade auto→propose), cross-topic skill dedupe, bot promotion
(`BOT_MIN=3` skills with no agent), stale reminders, `wiki-topics/_global` catalogs + every topic's INDEX.md refresh. Kanban-free first pass — proposals only. ^[raw/inbox/2026-09-05-legacy-inbox.md]

## First opinion (2026-09-05 17:13)
- **merge senter-wiki → senter (0.65, AUTO-tier by Chris's own calibration)** — the question the assistant had deferred; kept apart pending Chris
  ([[wiki-topics/senter-wiki/wiki/decisions/2026-09-05-keep-senter-and-senter-wiki-separate|keep senter / senter-wiki separate]]). Veto file: `wiki-topics/_global/.system/keep-separate.md`.
- 2 skill dedupes.
- `senter-wiki-bot` — 4 skills, no agent → proposed bot (`agents/senter-wiki-bot.md.proposed`). ^[raw/inbox/2026-09-05-legacy-inbox.md]

Chris's standing wish for it: *"opinionated in what it combines"* — propose boldly, apply nothing without him
([[wiki-topics/senter-wiki/wiki/concepts/approval-policy|approval policy]]).
