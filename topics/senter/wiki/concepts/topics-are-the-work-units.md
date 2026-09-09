---
title: Topics are the work units (GOOP spec)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [spec, plan]
sources: [raw/sources/knowledge/senter-SOUL.md, raw/sources/knowledge/skill-senter-fleet-coordination.md, raw/sources/knowledge/weaver-AGENTS.md, raw/sources/knowledge/paladin-SOUL.md, raw/inbox/2026-09-05-legacy-inbox.md]
confidence: high
---

# Topics are the work units (GOOP spec)

A vault topic `topics/<name>/` is the thing a bot "absorbs". When Chris's idea maps to an existing topic, the bot that owns that topic owns the idea; a new domain means a new topic *and* a new bot, created together via klerik. ^[raw/sources/knowledge/senter-SOUL.md]

## Layout (GOOP spec, `[[agent-wiki-spec]]`)
- `README.md` = dashboard (frontmatter: title/updated/type/repo/status/tags; owner, spec, files, version).
- `.system/` = machine internals: `session.md` (append-only dated outcomes — "write it as if handing off to a stranger"), `queue.md` (work items; sections `[FIXES] → [FEATURES] → [LOOPS]`; the LOG, not the lock), `claims/` ([[topics/senter/wiki/concepts/claim-v2-protocol|CLAIM v2]]), `continuity`, `injections`, `INDEX.md` (progressive-disclosure index), `inbox.md` → now `raw/inbox/` (watcher filings), `selfmodel/` (senter only), `architecture.md`.
- `skills/`, `agents/`, `loops/`, `plans/`, `process/`, `prs/` as the topic needs them.
- Since 2026-09-05 each topic is also an LLM wiki: `SCHEMA.md`, `index.md`, `log.md`, `raw/`, `wiki/{entities,concepts,decisions,comparisons,queries}` ([[topics/senter/wiki/decisions/2026-09-05-context-section-is-a-full-llm-wiki|decision]]). ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Who lives where
- `topics/senter/` — Senter + [[topics/senter/wiki/entities/paladin|paladin]] (plans, process docs, loops/reflect.md, selfmodel).
- `topics/senter-wiki/` — [[topics/senter/wiki/entities/weaver|weaver]] + [[topics/senter/wiki/entities/looker|looker]]; the UI queue and 7.4 MB of exported sessions.
- `topics/klerik/process/agent-authoring-rules.md`; `topics/hermes-agent/prs/` (PR ledger).
- Structure changes (merges, renames, index regen) belong to paladin; content to the owning bot. The 63→19 merge (2026-09-02) is the reference structural run; nothing deleted — `topics/_archive/`.

## Working model
Bots work OUT OF topics: an ephemeral instance wakes with only the topic's `.system/` as memory ([[topics/senter/wiki/concepts/meeseeks-model|Meeseeks model]]), claims one item, logs to session.md, posts a [[topics/senter/wiki/concepts/done-signal|done signal]]. "Activating work = kick off owning bot, record outcome in topic session.md + queue.md, log in log.md, keep `catalogs/agent-roster.md` matching reality." Per-topic loops (`hermes cron` / `hermes -p senter <topic>`) run the [[topics/senter/wiki/concepts/context-to-skills-to-bots-to-loops|flywheel]]. ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]
