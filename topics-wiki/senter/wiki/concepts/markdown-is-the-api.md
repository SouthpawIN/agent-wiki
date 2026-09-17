---
title: Markdown is the API
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [spec, preference]
sources: [raw/sources/knowledge/senter-SOUL.md, raw/sources/knowledge/skill-senter-fleet-coordination.md, raw/sources/knowledge/weaver-SOUL.md, raw/inbox/2026-09-05-legacy-inbox.md]
confidence: high
---

# Markdown is the API

Senter's hard rule: "every delegation, spawn, and outcome is written to the vault, not just chatted." The skill sharpens it: "Markdown is the API; unlogged work didn't happen." ^[raw/sources/knowledge/senter-SOUL.md] ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

## What it means in practice
- Every idea → `Ideas.md` verbatim; every outcome → topic `session.md` same turn; every fleet change → `log.md`; roster → `catalogs/agent-roster.md`.
- Bots log outcomes "the same turn (markdown-is-the-API)" — weaver's SOUL uses the phrase verbatim. ^[raw/sources/knowledge/weaver-SOUL.md]
- Decisions to Chris are cards *and* an `## AWAITING CHRIS` section in the plan file ([[topics-wiki/senter/wiki/decisions/2026-09-02-fleet-decisions-as-wiki-cards|decision]]).
- Repeat corrections become rules in `process/` docs, not just log lines ([[topics-wiki/senter/wiki/decisions/2026-09-02-process-artifacts-are-the-product|decision]]).
- Structural changes carry provenance in every touched file (`## Absorbed`, wikilinks).

## Doubles as transport
When DM bodies were dropped in transit (teammate says "sent you the plan", nothing arrives; confirmed via their `state.db`), the fix was to have them write the deliverable into `topics-wiki/<name>/.system/queue.md` and ack in one line — "Markdown-is-the-API doubles as the transport fallback."

## Why it matters to Chris
It is the mechanism behind [[topics-wiki/senter/wiki/concepts/cursor-for-markdown|Cursor for markdown]]: markdown files are "agentic context artifacts that can be set in the motion" — the same file that records a decision configures a bot. And it is the memory: "if it isn't in the wiki it isn't remembered" ([[topics-wiki/senter/wiki/concepts/progressive-disclosure|progressive disclosure]]). ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Constraint that follows
Vault/profile writes must use `write_file`/`patch` — never shell heredocs, `>>`/`tee`, or interpreter one-liners — because each of those trips the approval gate and costs Chris a click ([[topics-wiki/senter/wiki/entities/weaver|weaver]] rule 14; 96 cards in one day).
