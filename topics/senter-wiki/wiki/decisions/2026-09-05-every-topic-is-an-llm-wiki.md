---
title: Decision 2026-09-05: every topic is a Karpathy-style LLM wiki; CONTEXT renders index.md
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, spec, tool, infra]
sources:
  - raw/inbox/2026-09-05.md
  - raw/inbox/2026-09-05-legacy-inbox.md
confidence: high
contested: true
aliases:
  - "Decision: every topic is a two-layer LLM wiki; CONTEXT renders index.md"
---

# Decision 2026-09-05: every topic is a Karpathy-style LLM wiki

> **Superseded in part, 19:06.** The two-layer wiki stands; the *rendering* half ("CONTEXT renders the full `index.md`; context orb = page count") was rejected by Chris the same evening — *"I don't want any numbers indicating what's in the wiki, I want to just see the wiki."* Current rule: [[topics/senter-wiki/wiki/decisions/2026-09-05-context-is-the-wiki-with-live-diffs|CONTEXT is the wiki itself with live diffs]]. ^[raw/inbox/2026-09-05.md]

## What
"You're right, and I'd been misreading 'context' as a summary line. Fixed at the root, using the `llm-wiki` skill as you said: **Every topic is now a Karpathy-style LLM wiki** (`assets/topic-wiki.py`)." (17:43) `raw/` immutable Layer 1 (watcher files `raw/inbox/<day>.md`; transcripts/specs/source moved to `raw/sources/`, symlinked from old `.system/` paths); `wiki/{entities,concepts,decisions,comparisons,queries}` Layer 2; `SCHEMA.md`, `index.md`, `log.md`. ^[raw/inbox/2026-09-05.md]

## Why
Chris corrected the 220-character summary notion of "context": the CONTEXT section must be the topic's whole compiled knowledge, browsable — "every page, one line each, wikilinked … Not 220 characters." ^[raw/inbox/2026-09-05.md]

## Effects
- Compile loop `com.senter.topic-wiki` every 15 min ([[topics/senter-wiki/wiki/entities/topic-wiki-compile-loop|entity]]); all 19 topics initialised; first compiles of senter + senter-wiki (5 MB raw) started in background. ^[raw/inbox/2026-09-05.md]
- UI: CONTEXT renders full `index.md`; context orb = page count. ^[raw/inbox/2026-09-05-legacy-inbox.md] — **superseded 19:06**: CONTEXT now renders the pages themselves with live diffs and no counts ([[topics/senter-wiki/wiki/decisions/2026-09-05-context-is-the-wiki-with-live-diffs|decision]]). ^[raw/inbox/2026-09-05.md]
- Watcher restarted for the new raw layer. ^[raw/inbox/2026-09-05.md]

Concept page: [[topics/senter-wiki/wiki/concepts/llm-wiki-topic-layout|LLM-wiki topic layout]]. Predecessor knowledge structure: [[topics/senter-wiki/wiki/entities/agent-wiki-repo|agent-wiki spec]] (`.system/continuity.md` as "raw understanding").

## Folded from `2026-09-05-topics-are-llm-wikis`
- Timing: decided 2026-09-05 17:42–17:43. Chris pushed back on "context" being a 220-char summary and pointed at the `llm-wiki` skill; the root fix is `raw/` (immutable inbox + sources) plus `wiki/` five sections with provenance and `SCHEMA.md`/`index.md`/`log.md`. ^[raw/inbox/2026-09-05.md] ^[raw/inbox/2026-09-05-legacy-inbox.md]
- Loop order: compile loop every 15 min, then `topic-agent`. ^[raw/inbox/2026-09-05.md] ^[raw/inbox/2026-09-05-legacy-inbox.md]
- Why (framing): Context is the outermost GOOP primitive — it must be the topic's structured understanding, not a blurb.
- Scope: all 19 topics initialised; transcripts grepped on demand, not compiled.
- See also: [[topics/senter-wiki/wiki/concepts/two-layer-llm-wiki|two-layer LLM wiki]], [[topics/senter-wiki/wiki/entities/topic-worker|compiler]].

## Absorbed
- `decisions/2026-09-05-topics-are-llm-wikis` — 2026-09-05 → archived at `topics/_archive/wiki-dedupe/senter-wiki/decisions/2026-09-05-topics-are-llm-wikis.md`
