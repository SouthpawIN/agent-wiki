---
title: topic-wiki compile loop (com.senter.topic-wiki)
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [loop, infra, tool]
sources:
  - raw/inbox/2026-09-05.md
  - raw/inbox/2026-09-05-legacy-inbox.md
confidence: high
---

# topic-wiki compile loop (com.senter.topic-wiki)

## What it is
`assets/topic-wiki.py` + launchd `com.senter.topic-wiki`, every 15 min: one senter bot run per topic over unprocessed raw items → pages created/updated under `wiki/` → `index.md` rebuilt → a feed card, and the wiki visibly opens that topic. Established by [[topics/senter-wiki/wiki/decisions/2026-09-05-every-topic-is-an-llm-wiki|every topic is an LLM wiki]]. ^[raw/inbox/2026-09-05.md]

## Rules it enforces (the `llm-wiki` skill)
`raw/` immutable; `wiki/{entities,concepts,decisions,comparisons,queries}` with frontmatter, ≥2 wikilinks, `^[raw/…]` provenance; contradictions kept with dates; Chris's `<!-- chris -->` lines never rewritten; `SCHEMA.md` per-topic taxonomy; `index.md` rebuilt programmatically; `log.md` appended. ^[raw/inbox/2026-09-05.md]

## State at 2026-09-05 17:43
"All 19 topics initialised. The first two real compiles (senter, senter-wiki — the ones with 5 MB of raw) are running now in the background." Full session transcripts are not compiled per pass (too big) — grepped on demand; everything else in `raw/` is. ^[raw/inbox/2026-09-05.md]

The `init` entry in this topic's own `log.md` (`topic-wiki.py init`) is this loop's footprint. Layout details: [[topics/senter-wiki/wiki/concepts/llm-wiki-topic-layout|LLM-wiki topic layout]]; scheduling siblings in [[topics/senter-wiki/wiki/entities/launchd-services|launchd services]].

## First results (18:14–18:15)
Exit 0; senter → 60 pages, senter-wiki → 55; rows read `CONTEXT · 60 WIKI PAGES · 26 RAW`, context orbs 60 / 55. One page spot-checked against the bar in [[topics/senter-wiki/wiki/concepts/wiki-page-quality-bar|wiki page quality bar]]; full account in [[topics/senter-wiki/wiki/queries/first-compile-results-2026-09-05|first compile results]]. Known defect: no slug-collision guard, so a second pass over the same raw set produced near-duplicates ([[topics/senter-wiki/wiki/queries/duplicate-page-candidates|candidates]]). ^[raw/inbox/2026-09-05.md]
