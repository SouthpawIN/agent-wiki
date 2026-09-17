---
title: Vault scan live-data cap (scan-topics.py 2MB overflow and the .system-live.json bypass)
created: 2026-09-08
updated: 2026-09-08
type: concept
tags: [infra, tool, pain, bot, spec]
sources: [raw/inbox/2026-09-08.md]
confidence: medium
---
# Vault scan live-data cap

**Definition.** A 2026-09-08 failure where the live-data export endpoint was producing payloads far over its own size cap: "The file is 2.8MB — way over the 2MB cap. The root cause is in `scan-topics.py`: the `text` field of each topic can be up to 120KB, and it includes all wiki pages plus .system files. With ~20+ topics, this easily blows past 2MB." ^[raw/inbox/2026-09-08.md]

**The two issues and the bypass.** The same hermes block reports two distinct problems and an attempted workaround: the per-file cap itself is exceeded by the aggregated topic `text` field (wiki pages + `.system` files for 20+ topics), and the `/file` route is being patched "directly" to let `.system-live.json` bypass the `FILE_CAP` limit because "it's the server's own live data output." ^[raw/inbox/2026-09-08.md]

**Why it matters for klerik.** klerik is the profile that reviews and corrects other Hermes profiles. The proposal/apply pipeline ([[topics/klerik/wiki/concepts/proposal-apply-path|Proposal apply path]]) depends on topic scans surfacing proposed agents, skills, and loops. If the scan payload is capped and certain files (`.system-live.json`) are being special-cased to bypass that cap, then what klerik sees (and what Chris approves in the wiki feed) may be silently truncated or, conversely, polluted by `.system` files that should stay internal. The "bypass the FILE_CAP" move is the same class of workaround reflex as the config-write case ([[topics/klerik/wiki/comparisons/config-write-workaround-vs-deterministic-path|Config workaround vs deterministic path]]) — a direct write-path change instead of routing through the approval surface.

**Bot-counting signal.** A follow-on block in the same inbox distinguishes real fleet bots from vault-proposed ones: "The actual bot profiles are: anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver — that's 11 bots. But the data shows 68 bots." ^[raw/inbox/2026-09-08.md] The 2026-09-08 block then identifies `scan_vault_agents()` as "actually working as designed" — it detects proposed bots from `topics/*/agents/`, which is exactly the proposal stage feed klerik consumes ([[topics/klerik/wiki/entities/proposal-only-planner|Proposal-only planner]]; [[topics/klerik/wiki/concepts/proposal-apply-path|Proposal apply path]] proof table). The concern is not that the function is wrong but that it adds "a lot of noise" to the live data, inflating the bot count and making it harder to see whether the 11 real fleet bots have correct counts. "The real fleet bots … should have their counts and data correct."

**Relation to other concepts.** The scan cap is the read-side sibling to the [[topics/klerik/wiki/concepts/deterministic-apply-path|Deterministic apply path]]: if the apply path needs correct card text, the scan path must deliver it untruncated. The 68-vs-11 split is a direct input to [[topics/klerik/wiki/queries/does-the-proposal-only-planner-run-against-the-vault|Does the proposal-only planner run against the vault?]] — if the planner runs against the same `scan_vault_agents()` output, it is proposing for all 68, and the signal-to-noise ratio against klerik's queue ([[topics/klerik/wiki/entities/klerik-queue-drain-loop|klerik-queue-drain loop]]) is the operational question.
