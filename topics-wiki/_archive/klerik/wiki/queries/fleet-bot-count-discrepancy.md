---
title: Query — does the scan live-data reflect true fleet bot counts?
created: 2026-09-08
updated: 2026-09-08
type: query
tags: [question, bot, infra, fleet]
sources: [raw/inbox/2026-09-08.md]
confidence: high
---
# Query — does the scan live-data reflect true fleet bot counts?

**Status: open.** On 2026-09-08 the live-data feed reported 68 bots, but the actual fleet has only 11: "The actual bot profiles are: anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver — that's 11 bots. But the data shows 68 bots." ^[raw/inbox/2026-09-08.md]

**Why the discrepancy.** The `scan_vault_agents()` function includes proposed vault agents from `topics-wiki/*/agents/` as if they were real bots: "The `scan_vault_agents()` function is actually working as designed - it's detecting proposed bots from `topics-wiki/*/agents/` directory. The issue is that these vault agents are being included in the live data, which adds a lot of noise." ^[raw/inbox/2026-09-08.md]

**What needs verification.** The live-data export is capped at 2MB, and the 2026-09-08 block reports a 2.8MB file blowing past that cap due to `scan-topics.py` accumulating `text` fields (up to 120KB each) for wiki pages plus `.system` files across ~20+ topics. Whether the 68 count is truncated, inflated, or both depends on how the cap interacts with the aggregation logic. See [[topics-wiki/klerik/wiki/concepts/vault-scan-live-data-cap|Vault scan live-data cap]].

**How to answer.** Compare the raw `scan_vault_agents()` output against the directory listing of `~/.hermes/profiles/` (real fleet bots) and `topics-wiki/*/agents/*.proposed` (proposed bots in flight). The key metric: do the 11 fleet bots have correct counts in the live-data feed, and is the 68 count purely the sum of real bots + proposed agents? Log the result to `.system/session.md`.