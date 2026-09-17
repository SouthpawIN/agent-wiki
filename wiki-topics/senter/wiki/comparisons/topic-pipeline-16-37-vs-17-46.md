---
title: Topic pipeline shapes — worker + umbrella + compiler (16:37) vs one topic agent (17:46)
created: 2026-09-05
updated: 2026-09-05
type: comparison
tags: [spec, loop, decision, infra]
sources: [raw/inbox/2026-09-05-legacy-inbox.md, raw/inbox/2026-09-05.md, raw/sources/2026-09-05-umbrella-still-runs.md]
confidence: high
contested: true
---

# Topic pipeline shapes — 16:37 vs 17:46 (2026-09-05)

Two designs for "how does a topic turn Chris's talk into wiki + action", both from the same afternoon. The second replaced the first within ~70 minutes after [[wiki-topics/senter/wiki/entities/chris|Chris]] said "I don't like the separation." ^[raw/inbox/2026-09-05-legacy-inbox.md] ^[raw/inbox/2026-09-05.md]

| | 16:37 — workers + umbrella (+ compiler) | 17:46 → 17:53 — one topic agent |
|---|---|---|
| Intake | Watcher routes each **whole message** to its best topic (`.system/inbox.md`) | Watcher **cuts** each message at subject changes; each piece filed to its topic's `raw/inbox/<day>.md` ([[wiki-topics/senter/wiki/concepts/watcher-as-cutter|cutter]]) |
| Wiki rewrite | Separate "wiki compiler" pass | Same run as proposals — step 1 of [[wiki-topics/senter/wiki/entities/topic-agent|topic-agent.py]] |
| Skills | Per-topic worker: `inbox.md` → `skills-capabilities/<name>/SKILL.md.proposed`; watcher proposes a candidate **every 12 filings** | Fall out of the bot's work; written when a repeatable procedure is evident, no approval |
| Bots | After skills cluster (`BOT_MIN=3` umbrella rule — see `agents/senter-bot.md.proposed`, 17:43) | **Proposed first**, on first appearance of a subject; reuse a fleet bot when one fits |
| Loops | Umbrella cron per vault: merge/split proposals, cross-topic skill dedupe | Proposed after bots, per topic; the [[wiki-topics/senter/wiki/entities/umbrella|umbrella]] **kept running** (30 min) for cross-topic governance — corrected 18:53, earlier "home is open" was wrong |
| Collision control | `hermes kanban` claims between workers | One agent per topic; `.system/agent.lock` |
| Cadence | Workers async; umbrella cron | Every 5 min per topic (a timer — tension with "per message" / "no timers") |
| Approvals | Cards for every artifact (skill, bot, loop, merge) | Cards for bots-profiles/loops; none for wiki edits or skills ([[wiki-topics/senter/wiki/decisions/2026-09-05-no-approval-for-wiki-edits|decision]]) |
| Chris's verdict | "I don't like the separation… the bots has taken a little slow to be created or used" | "Understood. One agent per topic owns the whole lifecycle" (Hermes) — not contradicted |

## What carried over unchanged
Per-message intake ([[wiki-topics/senter/wiki/decisions/2026-09-05-per-message-watcher|decision]]); raw/ immutable, wiki compiled; the locked .35/.50 thresholds for any merge/split (17:13: "The umbrella must use those thresholds, not mine"); reuse before create.

## What the second shape lost — corrected
*Written 17:53–18:48:* The 16:37 umbrella carried the "opinionated" cross-topic jobs — merge/split proposals and skill dedupe. Nothing in the 17:53 build names an owner for them. Nearest existing owner: paladin (vault structure; ran the 63→19 merge on 09-02). Recorded as open on [[wiki-topics/senter/wiki/queries/senter-timeline|the timeline]] and in [[wiki-topics/senter/wiki/decisions/2026-09-05-one-agent-per-topic-no-separation|the decision]].

*Corrected 18:53:* Nothing was lost. Only the worker and compiler jobs were removed; `com.senter.umbrella` was kept and still runs every 30 min — governance, skill dedupe, bot promotion, `_global` catalogs, INDEX.md regeneration, and WatchPaths sync for new topics ([[wiki-topics/senter/wiki/entities/umbrella|umbrella]]). The 17:46 shape is therefore **watcher (cuts) + one agent per topic + one umbrella**, not two roles. ^[raw/sources/2026-09-05-umbrella-still-runs.md]
