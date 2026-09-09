---
title: Topic-agent `--all` pass (launchd WatchPaths job over all topics, incl. the 17 thin ones)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [infra, loop, tool, pain, timeline, question]
sources: [raw/inbox/2026-09-05.md]
confidence: medium
---
# Topic-agent `--all` pass

**Definition.** The topic-agent job is the launchd-triggered process that runs one TOPIC AGENT per topic in the vault (this page is written by one such agent). It has an `--all` mode that sweeps every topic in a single pass, and it is fired by a launchd `WatchPaths` trigger rather than a fixed cadence: "The agent job is running its first `--all` pass right now (WatchPaths fired). Log is buffered until it exits." ^[raw/inbox/2026-09-05.md] Its first ever `--all` pass began at 18:21 on 2026-09-05, while klerik's own build was in flight.

**The 17 thin topics.** The vault holds ~23 topic dirs (`_archive`, `_global`, `_inbox` plus ~20 real topics — anser, burner-phone, crow, dev-tooling, evolutionary, hermes-agent, kashik, klerik, legacy-bots, memento, music, nous-community, omnisenter-models, pirouette-framework-core-003, pocket-shop, senter, senter-wiki, turbofit, youtube …). Only a handful (senter, klerik, senter-wiki, anser) were built out to the full [[topics/klerik/wiki/concepts/topic-build-out-spec|Topic build-out spec]]; the remaining "17 thin topics" have SCHEMA/index/log scaffolding but little or no raw. The stated gap at 18:20: "the topic agents are running on the 17 thin topics too — check the log for failures, and check the watcher is actually cutting live" ^[raw/inbox/2026-09-05.md]. Two risks are named:
1. **Agent failures on thin topics** — an agent handed a topic with an empty inbox or malformed SCHEMA may error, and because the log is buffered until exit, failures are invisible until the whole `--all` pass finishes.
2. **Watcher not cutting live** — the watcher (which cuts Chris's messages into per-topic `raw/inbox/YYYY-MM-DD.md` blocks, per [[topics/klerik/wiki/decisions/2026-09-05-per-message-inbox-filing|per-message inbox filing]]) may be filing only on batch, not as he speaks. Evidence in this very inbox: every block is `hermes`-sender (assistant side) at sim 0.08–0.13 — Chris's own lines about klerik have not landed here, which is either correct routing (he said little about klerik directly) or a symptom of the watcher missing him.

**Operational facts (observed at compile time, 18:32).**
- `.system/agent.lock` = `1365` (a pid) and `.system/agent.cursor` lists three processed raw hashes — the agent job is single-instance per topic and cursor-based, so re-runs do not re-compile old items.
- The `--all` pass and klerik's build ran concurrently by design: "Let me check klerik's bot build and the fleet feed while that runs" ^[raw/inbox/2026-09-05.md].
- Buffered logging is the pain: nothing can be verified live while the pass runs, which is the opposite of Chris's "watch it land" standard.

**Why it lives in klerik's wiki.** klerik is the bot that fixes other bots' profiles; if the thin-topic agents fail systematically, the fix is a profile/prompt change klerik owns. And the queue-drain loop ([[topics/klerik/wiki/entities/klerik-queue-drain-loop|klerik-queue-drain]]) and the `--all` pass share one failure surface: both are launchd/cron-triggered background jobs whose only proof of life is a log Chris cannot see until they exit. Open question: [[topics/klerik/wiki/queries/did-the-first-all-pass-fail-on-thin-topics|Did the first `--all` pass fail on the thin topics?]].
