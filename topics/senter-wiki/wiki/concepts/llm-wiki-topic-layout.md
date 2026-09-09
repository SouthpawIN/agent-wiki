---
title: Every topic is a Karpathy-style LLM wiki (raw / wiki / SCHEMA / index / log)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [spec, decision, tool]
sources:
  - raw/inbox/2026-09-05.md
  - raw/inbox/2026-09-05-legacy-inbox.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
confidence: high
---

# Every topic is a Karpathy-style LLM wiki

## Why (Chris, 2026-09-05 17:43)
Senter had been "misreading 'context' as a summary line." Chris pointed at the `llm-wiki` skill; the fix went to the root: every topic became a three-layer LLM wiki (`assets/topic-wiki.py`). See [[topics/senter-wiki/wiki/decisions/2026-09-05-every-topic-is-an-llm-wiki|decision]]. ^[raw/inbox/2026-09-05.md]

## Layout
```
topics/<t>/
├── raw/                 Layer 1, immutable
│   ├── inbox/<day>.md   watcher filings, per message, with similarity
│   └── sources/         transcripts / specs / source (symlinked from old .system paths)
├── wiki/{entities,concepts,decisions,comparisons,queries}   Layer 2, agent-owned
├── SCHEMA.md            per-topic taxonomy + thresholds (Layer 3)
├── index.md             one line per page — rendered as the row's CONTEXT
└── log.md               append-only
```
Page rules: frontmatter (title, created, updated, type, tags, sources, confidence), ≥2 wikilinks, `^[raw/…]` provenance, contradictions kept with dates (`contested: true`), Chris's `<!-- chris -->` lines never rewritten; pages > 200 lines split. ^[raw/inbox/2026-09-05.md]

## Relationship to the GOOP lanes
`skills/ agents/ loops/` and `.system/{continuity,queue,injections}` stay as the spec's lanes; `raw/` and `wiki/` add the memory layers. `.system/knowledge/` became `raw/sources/knowledge/`. ^[raw/inbox/2026-09-05-legacy-inbox.md] ^[raw/inbox/2026-09-05.md]

## UI effect
"The CONTEXT section of a row now renders the topic's full `index.md` — every page, one line each, wikilinked — with page/raw counts; the context orb = page count. Not 220 characters." ^[raw/inbox/2026-09-05.md]

## Compile
[[topics/senter-wiki/wiki/entities/topic-wiki-compile-loop|com.senter.topic-wiki]] every 15 min; index rebuilt programmatically (never hand-edited); a feed card and a stage event per compile. Full transcripts excluded (grepped on demand). ^[raw/inbox/2026-09-05.md]

Related: [[topics/senter-wiki/wiki/concepts/progressive-disclosure|progressive disclosure]] (how the sidebar reads it), [[topics/senter-wiki/wiki/concepts/markdown-is-the-api|Markdown is the API]].
