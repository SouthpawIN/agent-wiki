---
title: "2026-09-02 — Upstream PR policy: ledger for others' repos, ship on Chris's fork"
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, repo, bot]
sources: [raw/sources/knowledge/skill-senter-fleet-coordination.md]
confidence: high
---

# 2026-09-02 — Upstream PR policy: ledger for others' repos, ship on Chris's fork

**What.** [[wiki-topics/senter/wiki/entities/teknium|Teknium]] never opens PRs on repos Chris doesn't own during a session. Drafts go to the ledger `wiki-topics/hermes-agent/prs/`; Chris decides at session end. Chris's own repos (e.g. `SouthpawIN/hermes-agent`) ship immediately. ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

**Trigger.** A "submitted PR" report — verified with `gh pr list --author` / `git ls-remote --heads` — turned out to be two local unpushed branches. The deeper finding: the rule Chris had stated in chat "had never been written into the bot's SOUL and held by luck" → **every standing rule goes into the owning bot's SOUL the same turn** (via [[wiki-topics/senter/wiki/entities/klerik|klerik]]).

**Application.** When a core fix is needed NOW (approval-gate false positives; the preview→composer capability) ship it on the fork so the fleet runs on it today, and keep the upstream version as a draft in the ledger. Say which half is which. Chris works with the Hermes team and wants fleet-found core gaps upstreamed — through the ledger, not in-session.

**Also from this stretch.** Integration/feed sources are event-driven (webhooks/WebSub/ETag long-poll); timed polling only as a labeled fallback ([[wiki-topics/senter/wiki/concepts/live-data-contract|live-data contract]]). Verify an alleged action before reacting to it.
