---
name: topic-wiki-compile
description: Use when compiling or reading a topic's two-layer LLM wiki. Raw is immutable, wiki pages are agent-owned with provenance, index.md IS the row context.
version: 0.1.0
distilled: 2026-09-05 17:49
topic: senter-wiki
---
# topic-wiki-compile
# topic-wiki-compile

Every topic under `wiki-topics/<slug>/` is a Karpathy-style LLM wiki driven by `assets/topic-wiki.py` (launchd `com.senter.topic-wiki`, every 15 min).

## Layers
1. `raw/` — Layer 1, IMMUTABLE. Watcher files Chris's messages to `raw/inbox/<day>.md`. Transcripts/specs/source live in `raw/sources/` (old `.system/` paths are symlinks — never break them). Never edit raw.
2. `wiki/{entities,concepts,decisions,comparisons,queries}` — Layer 2, agent-owned pages. Each page: frontmatter, >=2 wikilinks, `^[raw/...]` provenance on claims, contradictions KEPT with dates (do not resolve by deletion), any `<!-- chris -->` line never rewritten.
3. `SCHEMA.md` (per-topic taxonomy), `index.md` (one line per page, wikilinked, page/raw counts), `log.md`.

## Compile pass (per topic)
- Collect unprocessed raw items only. Do NOT compile full session transcripts — too big; grep them on demand.
- Create/update pages → rebuild `index.md` → append `log.md` → post a feed card and emit a `/stage` so the wiki visibly opens that topic.
- Skills, topics, continuity and wiki edits auto-apply. Only bots and loops are written as `.proposed`.

## UI contract
- The row's CONTEXT section renders the FULL `index.md`, not a 220-char summary. The context orb count = wiki page count. If CONTEXT looks like a summary line, the index is stale or the scanner is reading the wrong file — fix the root, not the text.

## Pitfalls
- launchd python under `~/Documents` is TCC-blocked: run from the venv outside Documents.
- A real compile of a 5 MB raw topic takes several minutes; report page counts only after it lands.

## Evidence
> Now the watcher files into `raw/inbox/<date>.md` (the immutable layer), and the scanner/UI read `index.md` as CONTEXT
> **The CONTEXT section of a row now renders the topic's full `index.md`** — every page, one line each, wikilinked — with page/raw counts; the context orb = page count. Not 220 characters.
> Compile loop every 15 min (`com.senter.topic-wiki`): one senter bot run per topic over unprocessed raw items → pages created/updated → index rebuilt → feed card + the wiki visibly opens that topic.
