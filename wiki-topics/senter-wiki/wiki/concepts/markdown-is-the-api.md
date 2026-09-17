---
title: Markdown is the API — user edits are the steering wheel
created: 2026-07-07
updated: 2026-09-05
type: concept
tags: [spec, preference]
sources:
  - raw/sources/knowledge/agent-wiki-repo/spec.md
  - raw/sources/knowledge/agent-wiki-repo/README.md
  - raw/sources/knowledge/agent-wiki-repo/SENTER.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
  - raw/inbox/2026-09-05.md
confidence: high
---

# Markdown is the API — user edits are the steering wheel

## Principle
"Human → machine, machine → machine, machine → human. All via markdown files." "No chat command. No config file. No YAML wizard. Just edit markdown." The filesystem IS the database. ^[raw/sources/knowledge/agent-wiki-repo/spec.md] ^[raw/sources/knowledge/agent-wiki-repo/README.md]

## Steering table (spec)
| What to change | Where |
|---|---|
| "You misunderstood my goal" | `.system/continuity.md` |
| "I don't want that agent" | `agents/<agent>.md` — mark cancelled |
| "Change the cron frequency" | `triggers-loops/<loop>.md` |
| "Force-create a skill now" | `.system/queue.md` → `[SKILLS] my-skill` |
| "Show me what's running" | `README.md` | ^[raw/sources/knowledge/agent-wiki-repo/spec.md]

## Chris's corrections win
User corrections to `continuity.md` are never overwritten; queue items typed by the user are actionable work; in the LLM-wiki layer, lines marked `<!-- chris -->` are never rewritten ([[wiki-topics/senter-wiki/wiki/concepts/llm-wiki-topic-layout|LLM-wiki layout]]). ^[raw/sources/knowledge/skill-agent-wiki-vault.md] ^[raw/inbox/2026-09-05.md]

## All-caps modules
An all-caps filename (`MEDIA.md`, `WALLET.md`) is "an active system declaration rather than an ordinary note" — policy in Markdown, enforcement in Hermes ([[wiki-topics/senter-wiki/wiki/entities/senter-agent-sandbox|Senter Agent / SENTER.md]]). ^[raw/sources/knowledge/agent-wiki-repo/SENTER.md]

## In the UI
The [[wiki-topics/senter-wiki/wiki/entities/editor-card|editor card]] edits the row's markdown in place (bridge `/write`); the wiki's own files (README, lanes, `.system/`) are what the scanner renders — "The wiki documents itself — as ROWS Chris can see, not as a report." ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

Per-turn canvas contract (user-mandated): read `session.md` first; update session/queue/log every turn; ideas verbatim into `Ideas.md`. "Stale canvas = broken workflow; the user checks this." ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
