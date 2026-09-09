---
title: Two-layer LLM wiki per topic (raw → wiki → index)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [spec, decision, infra]
sources:
  - raw/inbox/2026-09-05.md
  - raw/inbox/2026-09-05-legacy-inbox.md
confidence: high
---

# Two-layer LLM wiki

Chris corrected the assistant on 2026-09-05: *"You're right, and I'd been misreading 'context' as a summary line. Fixed at the root, using the `llm-wiki` skill as you said."*
Every topic is now a Karpathy-style LLM wiki (`assets/topic-wiki.py`). ^[raw/inbox/2026-09-05.md]

## Layers
1. **`raw/`** — immutable Layer 1. The [[topics/senter-wiki/wiki/entities/senter-watcher|watcher]] files Chris's messages into `raw/inbox/<day>.md`; transcripts/specs/source moved into
   `raw/sources/` (symlinked from the old `.system/` paths so nothing breaks).
2. **`wiki/{entities,concepts,decisions,comparisons,queries}`** — Layer 2, agent-owned pages with frontmatter, ≥2 wikilinks, `^[raw/…]` provenance, contradictions kept
   with dates, Chris's `<!-- chris -->` lines never rewritten.
3. **`SCHEMA.md`** (per-topic taxonomy), **`index.md`**, **`log.md`**. ^[raw/inbox/2026-09-05.md]

## UI contract
*"The CONTEXT section of a row now renders the topic's full `index.md` — every page, one line each, wikilinked — with page/raw counts; the context orb = page count.
Not 220 characters."* If CONTEXT looks like a summary line, the index is stale or the scanner reads the wrong file — fix the root. ^[raw/inbox/2026-09-05.md] ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Compile loop
Every 15 min (`com.senter.topic-wiki`), then superseded by `topic-agent` (every 5 min per topic with new raw): one senter run over unprocessed raw → pages → index →
feed card + `/stage` so the wiki visibly opens that topic. Full session transcripts are grepped on demand, never compiled per pass (too big).
([[topics/senter-wiki/wiki/decisions/2026-09-05-every-topic-is-an-llm-wiki|decision]]) ^[raw/inbox/2026-09-05.md]

## Progressive disclosure (older layer, still present)
`.system/INDEX.md` → file → section; the proposed sidebar SOUL *"reads INDEX first."* Durable knowledge homes: `.system/{concept,rules,context}.md` (concept = model;
rules = Chris's standing corrections as numbered law; context = files/knobs/contracts). *"A `.system/` file alone is invisible in the UI"* — lane files + README are what
render. ^[raw/inbox/2026-09-05-legacy-inbox.md]
