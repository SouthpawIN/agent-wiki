---
ingested: 2026-09-05
source: Hermes (builder) correction, verbatim
---
# Correction: the umbrella was NOT deleted — governance has an owner

At 17:53 the topic-worker and topic-wiki launchd jobs were removed and replaced by `com.senter.topic-agent` (one agent per topic).
`assets/umbrella.py` and `com.senter.umbrella` (every 30 min) were kept and still run. The umbrella owns topic governance:
merge/split proposals at the LOCKED thresholds (propose ≥ .35, auto ≥ .50, calibrated by Chris 2026-09-02), cross-topic skill dedupe,
bot promotion, stale-proposal reminders, `topics-wiki/_global` catalogs, every topic's INDEX.md, and syncing the topic-agent WatchPaths list
when the watcher scaffolds a new topic. Its proposals land in `topics-wiki/_global/.system/proposals.md` and as feed cards.

Do not re-propose a governance loop; it exists. The pending `topic-governance-rehome` loop proposal is superseded by this fact.

Also decided (Chris 18:0x, "stop asking me for so many decisions"): approvals APPLY — a loop card → `hermes cron create`, a bot card →
profile create + SOUL/AGENTS from the spec (klerik finishes voice/skin/alias), a research card → looker writes the answer into the page.
