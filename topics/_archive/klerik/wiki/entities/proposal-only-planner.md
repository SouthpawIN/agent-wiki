---
title: Proposal-only planner (existing engine)
created: 2026-09-05
updated: 2026-09-08
type: entity
tags: [tool, spec, plan]
sources: [raw/inbox/2026-09-05-legacy-inbox.md, raw/inbox/2026-09-08.md]
confidence: low
---
# Proposal-only planner (existing engine)

An already-existing planner in the vault that produces proposals only (no execution). It surfaced on 2026-09-05 while klerik's topic was being built: "This is the real engine — a proposal-only planner already exists. Let me see if it runs against our vault before writing anything of my own." ^[raw/inbox/2026-09-05-legacy-inbox.md]

**Why it matters for klerik.** The Senter operating model is conversation → interest → proposal → Chris approval → bot/loop creation. The planner is the "proposal" stage; klerik is the "creation" stage. The 2026-09-05 note's instruction is a reuse rule: *check whether the existing planner runs against the vault before writing new planning code.* This mirrors the fleet's anti-redundancy stance (anser gates duplicates) and klerik's own rule 2, "diagnose before you fix".

**Open question.** Whether it actually runs against the current vault is unconfirmed in the raw record — the message is a statement of intent to test, not a result. Tracked in [[topics/klerik/wiki/queries/does-the-proposal-only-planner-run-against-the-vault|Does the planner run against the vault?]]. Its output would feed the [[topics/klerik/wiki/concepts/bot-card-approval-wire|Bot-card approval wire]], which is where a proposal becomes a real profile via [[topics/klerik/wiki/entities/klerik|klerik]].

**Scan input quality (2026-09-08).** The planner, if it runs, consumes the same `scan_vault_agents()` output that feeds the live-data feed. That scan now detects proposed bots from `topics/*/agents/` — "vault agents ARE proposed bots" — producing 68 total against 11 real fleet bots: "The actual bot profiles are: anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver — that's 11 bots." ^[raw/inbox/2026-09-08.md] The noise-to-signal ratio of that feed is what the proposal stage must filter; see [[topics/klerik/wiki/concepts/vault-scan-live-data-cap|Vault scan live-data cap]].
