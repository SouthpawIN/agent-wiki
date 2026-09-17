---
title: Umbrella (assets/umbrella.py — com.senter.umbrella, topic governance owner)
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [tool, loop, infra, decision, timeline]
sources: [raw/sources/2026-09-05-umbrella-still-runs.md, raw/inbox/2026-09-05.md, raw/inbox/2026-09-05-legacy-inbox.md]
confidence: high
---

# Umbrella (`assets/umbrella.py` · launchd `com.senter.umbrella`)

The **umbrella** is the one cross-topic job in the vault: a launchd service (`com.senter.umbrella`, **every 30 min**) running `~/Documents/Projects/Projects/assets/umbrella.py`. It **was not deleted** at 17:53 on 2026-09-05 — only the per-topic worker and wiki-compiler jobs were removed and replaced by `com.senter.topic-agent` ([[wiki-topics/senter/wiki/entities/topic-agent|topic agent]]). "`assets/umbrella.py` and `com.senter.umbrella` (every 30 min) were kept and still run." ^[raw/sources/2026-09-05-umbrella-still-runs.md]

## What it owns (topic governance)
- Merge/split proposals at the **locked thresholds** — propose ≥ .35, auto ≥ .50, calibrated by Chris 2026-09-02 ([[wiki-topics/senter/wiki/decisions/2026-09-02-governance-thresholds-calibrated|decision]]; 17:13: "The umbrella must use those thresholds, not mine").
- Cross-topic skill dedupe.
- Bot promotion.
- Stale-proposal reminders.
- `wiki-topics/_global` catalogs and every topic's `INDEX.md`.
- Syncing the topic-agent **WatchPaths** list when the [[wiki-topics/senter/wiki/concepts/watcher-as-cutter|watcher]] scaffolds a new topic — i.e. a new topic becomes agent-owned without anyone editing launchd by hand.
- Its proposals land in `wiki-topics/_global/.system/proposals.md` and as feed cards. ^[raw/sources/2026-09-05-umbrella-still-runs.md]

## History of the record (kept with dates)
- **16:37** — built as "one opinionated umbrella" alongside per-topic workers ([[wiki-topics/senter/wiki/comparisons/topic-pipeline-16-37-vs-17-46|comparison]]).
- **17:46** — Chris: "I don't like the separation." The *worker + compiler* roles collapsed into the topic agent ([[wiki-topics/senter/wiki/decisions/2026-09-05-one-agent-per-topic-no-separation|decision]]). Chris said nothing about the umbrella itself.
- **17:53 → 18:48** — this wiki recorded governance as **orphaned** ("the umbrella script was deleted at 17:53"). That was wrong: it inferred deletion from the collapse. The `senter` topic agent then pitched "governance has no owner" on every run, and a `topic-governance-rehome` loop was proposed. ^[raw/inbox/2026-09-05.md]
- **18:53** — Hermes: "The senter agent keeps pitching 'governance has no owner' — because the wiki (its memory) says the umbrella was deleted, when in fact it still runs. Fix the record, not the pitch." Correction filed to `raw/sources/2026-09-05-umbrella-still-runs.md`; this page is the fix. "Do not re-propose a governance loop; it exists. The pending `topic-governance-rehome` loop proposal is superseded by this fact." ^[raw/sources/2026-09-05-umbrella-still-runs.md]

## Relationship to the fleet
The umbrella is a script, not a bot; it runs under the `senter` profile's assets like the topic agent. Structural changes it *proposes* (merges/splits) are still executed the way [[wiki-topics/senter/wiki/entities/paladin|paladin]] ran the 63→19 merge — dry-run, rehearsal, snapshot — and gated by [[wiki-topics/senter/wiki/entities/anser|anser]] where redundancy is in question. The 30-min cadence is a timer; Chris's standing preference is event-driven ([[wiki-topics/senter/wiki/concepts/live-data-contract|live-data contract]]) — an open tension, not a bug, since governance is a cross-topic sweep rather than a per-message reaction.

See also [[wiki-topics/senter/wiki/concepts/fix-the-record-not-the-pitch|Fix the record, not the pitch]] for the lesson this episode produced.
