---
title: Loop apply path (approve a loop card → real Hermes cron on the owning bot)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [loop, infra, bot, spec, timeline]
sources: [raw/inbox/2026-09-05.md, raw/sources/2026-09-05-umbrella-still-runs.md]
confidence: medium
---

# Loop apply path (approve → real cron)

The **loop apply path** is what happens when Chris approves a *loop* pitch from a [[topics-wiki/senter/wiki/entities/topic-agent|topic agent]]: the card's approval becomes a **real Hermes cron job on the bot that owns the loop**, not a note in a queue. Proven end to end at 18:20 on 2026-09-05: "Loop apply path proven end-to-end: approve → real cron `e6e20c22e1b9` on klerik. Clean the probe and verify the wiki picks it up." ^[raw/inbox/2026-09-05.md]

## Shape
1. Topic agent pitches a loop (`{"name","pitch","agent","cadence","prompt"}`) — agent = an existing fleet bot where one fits ([[topics-wiki/senter/wiki/concepts/proactive-suggestion-doctrine|bots first, then loops]]).
2. The wiki shows it as a card ([[topics-wiki/senter/wiki/entities/senter-bridge|senter-bridge]] carries approvals).
3. Approve → a cron job is created in the **named bot's profile** (here klerik; job id `e6e20c22e1b9`) with the loop's cadence and prompt.
4. The result is written back so the wiki reflects the live loop — "verify the wiki picks it up" is part of done, per [[topics-wiki/senter/wiki/concepts/markdown-is-the-api|markdown is the API]] and the [[topics-wiki/senter/wiki/concepts/live-data-contract|spawn = visible]] rule.
5. The probe loop used to prove the path is removed ("clean the probe") so no test artifact lingers as a fake running loop.

## Why this matters
Under the 2026-08-30 model, loops were "suggested to Chris, never spawned silently." This path is the first mechanism where the suggestion and the spawn are one click apart and land as a real, inspectable cron — the *Loops* lane of [[topics-wiki/senter/wiki/concepts/context-to-skills-to-bots-to-loops|the flywheel]] finally has a wire. It was completed under the 18:16 ruling to stop asking and finish the incomplete ([[topics-wiki/senter/wiki/decisions/2026-09-05-preempt-decisions-complete-the-incomplete|decision]]). ^[raw/inbox/2026-09-05.md]

## Generalised (18:0x decision, recorded 18:53)
The loop path is one row of a table: bot cards → `hermes profile create` + SOUL/AGENTS (klerik finishes voice/skin/alias); research cards → looker writes the answer into the page. See [[topics-wiki/senter/wiki/concepts/approval-apply-paths|approval apply paths]]. ^[raw/sources/2026-09-05-umbrella-still-runs.md]

## Known limits (as of 18:20)
- Only the klerik path has been exercised; other bots' profiles are unproven.
- A cron created from a CLI-scheduled context is local-only in delivery; whether the loop's output reaches the wiki (not just the cron log) is exactly what "verify the wiki picks it up" checks — the raw item ends before the verification result is recorded, so this is *proven created*, not yet *proven visible*.
- Cadence-based loops are timers; Chris's preference is event-driven ("no timed loaders"). Loops whose cadence can be "on new inbox" should use that.
