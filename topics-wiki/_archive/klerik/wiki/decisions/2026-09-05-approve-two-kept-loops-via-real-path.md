---
title: Decision — approve the two kept loops through the real path (paladin wiki-dedupe-sweep, looker player-regression-check; 2026-09-05 18:55)
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, loop, bot, infra, timeline]
sources: [raw/inbox/2026-09-05.md]
confidence: high
---
# Decision — approve the two kept loops through the real path

**What.** At 18:55 on 2026-09-05, right after the nine-loop sweep, the session approved the two loop cards that survived triage — and did it through the bridge's approve wire rather than by hand: "Approve the two kept loops through the real path (this also exercises the gateway check on looker/paladin):" ^[raw/inbox/2026-09-05.md] The two are `wiki-dedupe-sweep` (owner paladin, every 30m, card in `topics-wiki/senter-wiki/triggers-loops/`) and `player-regression-check` (owner looker, every 2h, card in `topics-wiki/youtube/triggers-loops/`). Neither is a klerik loop; they matter here because they were the second and third proofs of the loop branch klerik's own [[topics-wiki/klerik/wiki/entities/klerik-queue-drain-loop|klerik-queue-drain]] was the first of.

**Why "the real path".** The earlier 18:18 decision ([[topics-wiki/klerik/wiki/decisions/2026-09-05-prove-apply-path-with-one-real-approval|Prove the apply path with one real approval]]) had established that an approval is only proven when the artifact runs. Approving two more loops on two *different* bots tested the part klerik-queue-drain could not: that the fix for the "loop never ticks" root cause — a bot with no gateway can never fire a cron — was general, not a one-off for klerik. Hence "this also exercises the gateway check on looker/paladin". Concept: [[topics-wiki/klerik/wiki/concepts/gateway-was-the-missing-ticker|Gateway was the missing ticker]].

**Result claimed (18:58).** "Loop cards → `hermes cron create` on the owning bot, gateway auto-installed if that profile had none. Live: `klerik-queue-drain` (klerik), `wiki-dedupe-sweep` (paladin, 30m), `player-regression-check` (looker, 2h)." ^[raw/inbox/2026-09-05.md]

**Result verified on disk (19:07, this compile).**
- paladin: `~/.hermes/profiles/paladin/cron/jobs.json` holds `9e70db5cfa27 wiki-dedupe-sweep every 30m`; `~/Library/LaunchAgents/ai.hermes.gateway-paladin.plist` exists and `launchctl list` shows it running (pid 5635). `cron runs` → "No cron execution attempts recorded" — registered, not yet ticked.
- looker: `95e13093ff26 player-regression-check every 120m`; gateway plist present, running (pid 5634). Zero runs yet.
- klerik: gateway plist present, running (pid 5306); `klerik-queue-drain` has **executed** (18:50:25 completed, 18:56:40 output file) — the first of the three to actually tick.
So "Live" is accurate in the sense the wire is complete and the gateways run; only klerik's has yet produced a tick. Whether the other two fire is tracked in [[topics-wiki/klerik/wiki/queries/did-the-kept-loops-tick|Did the two kept loops tick?]].

**What this means for klerik.** klerik is no longer the only bot with a gateway, and loop ownership is spread across the fleet as designed. klerik's own role in a loop approval is nil — the bridge creates the cron on the owner directly. Its role stays the bot branch: [[topics-wiki/klerik/wiki/concepts/deterministic-apply-path|Deterministic apply path]].
