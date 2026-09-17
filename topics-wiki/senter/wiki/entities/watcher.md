---
title: Watcher (per-message filer)
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [tool, loop, infra, timeline]
sources: [raw/inbox/2026-09-05-legacy-inbox.md, raw/inbox/2026-09-05.md]
confidence: high
---

# Watcher (per-message filer)

> **Superseded in part, 2026-09-05 17:46–17:53.** The watcher now *cuts* messages into per-topic pieces instead of routing whole messages, and the "every 12 filings → skill candidate" rule is gone (new subject → immediate research/bot cards). See [[topics-wiki/senter/wiki/concepts/watcher-as-cutter|Watcher as cutter]] and [[topics-wiki/senter/wiki/decisions/2026-09-05-one-agent-per-topic-no-separation|decision]]. The behaviour below is the 16:37 first form, kept for history. ^[raw/inbox/2026-09-05.md]

The **watcher** is the first moving piece of the [[topics-wiki/senter/wiki/concepts/five-part-architecture|five-part architecture]], live on **2026-09-05 ~16:37**. It replaces any hand-off from the sidebar: [[topics-wiki/senter/wiki/entities/chris|Chris]] wanted "a watcher watching the Hermes agent logs directly so there doesn't have to be a pass-off… programmically watch the logs as they're being populated and then sort all of those in the topics." ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Behavior (as built)
- Tails Hermes's message table **per message** (Chris: "not per session, I want to per message, just like when you talk to cursor" — [[topics-wiki/senter/wiki/decisions/2026-09-05-per-message-watcher|decision]]).
- Files each message under the best-fitting topic (`topics-wiki/<t>/.system/inbox.md`, now `raw/inbox/YYYY-MM-DD…md`) with a feed card; header per filing: timestamp · speaker · session id · TF-IDF similarity (e.g. `sim 0.12`).
- Parks misfits in `_inbox/unsorted.md` with a "new topic?" proposal.
- Every **12 filings** on a topic proposes a skill candidate from the recurring rules.
- Runs as a launchd service; reloads its corpus whenever the scanner rewrites the snapshot.
- Sorting uses the TF-IDF the wiki already had; thresholds must use the Chris-approved calibration (propose ≥ .35, auto ≥ .5) — "The umbrella must use those thresholds, not mine" ([[topics-wiki/senter/wiki/decisions/2026-09-02-governance-thresholds-calibrated|decision]]).

## Open questions Hermes raised (2026-09-05 16:30)
- Watcher granularity: every message vs session-end summaries + tool results → Chris answered: **per message**.
- Who runs topic loops: one `senter` profile iterating all topics, or a profile per topic once it has a bot → proposed: per-topic workers (`hermes -p senter <topic>`) + one opinionated umbrella cron, `hermes kanban` claims preventing collisions.
- Approvals: one card per proposal vs one digest card per topic per pass → unanswered; Chris then said wiki edits should need **no** approval at all ([[topics-wiki/senter/wiki/decisions/2026-09-05-no-approval-for-wiki-edits|decision]]).

## Chris's expansion (17:18)
"bots need to trigger a lot sooner… if I talk about a new subject then it should suggest maybe researching it or maybe scaffolding it… use maybe a bot that we've used before to research a different subject, or create a new one." The watcher's proposals are meant to feed the [[topics-wiki/senter/wiki/concepts/context-to-skills-to-bots-to-loops|context → skills → bots → loops flywheel]] constantly, not every 12 filings.

## Why it is still a custom daemon (19:12)
Chris's 19:06 direction is "just built in Hermes commands and markdown" ([[topics-wiki/senter/wiki/decisions/2026-09-05-backend-as-builtin-hermes-plus-markdown|decision]]). Hermes's inventory names the watcher as one of three custom pieces and gives the reason: "Hermes has no per-message hook" — the only native hook is `on_session_finalize`, and Chris locked per-message. A per-message hook is therefore the Hermes capability whose absence keeps the watcher (and the TF-IDF cutter) custom — see [[topics-wiki/senter/wiki/comparisons/native-hermes-vs-custom-backend|native vs custom backend]]. ^[raw/inbox/2026-09-05.md]

## Sources the watcher was mapped to
`hermes sessions export` / `agent.log` / bridge events; the `on_session_finalize` hook (Anser row 11) as the session-end complement. Related: [[topics-wiki/senter/wiki/concepts/progressive-disclosure|progressive disclosure]] (how the filed context is read back).
