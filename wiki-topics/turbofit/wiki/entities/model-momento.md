---
title: Model Momento
created: 2026-10-28
updated: 2026-10-28
type: entity
tags: [repo, turbofit, ecosystem]
sources: [raw/sources/2026-10-28-github-consolidation.md]
confidence: high
---

# Model Momento

> SQLite-backed model database: HF metadata, benchmark runs and notes — FastAPI backend + single-file web UI, installable as a Hermes skill.

| | |
| --- | --- |
| **Repo** | [model-momento](https://github.com/SouthpawIN/model-momento) |
| **Status** | active side tool — model metadata + benchmark history store |

## What it is

- `schema.sql` + `server.py` (FastAPI) + single-file web UI under `web/`.
- `import_hf.py` pulls HuggingFace metadata; `model-momento/SKILL.md` installs as a Hermes skill so an agent can `memento <hf-url>` to import a model and open its notes.
- Stores: HF metadata, benchmark runs, free-form notes.

## Relation to TurboFit

TurboFit's own catalog is the shipped subset (`model-catalog.json`: 62 artifacts in 13 families) and its intel lives in [model-intel](../../references/model-intel.md) / [benchmark-leaderboard](../../references/benchmark-leaderboard.md). Model Momento is the *long-tail* store — everything benchmarked but not shipped. Two stores, one question: whether Model Momento should ingest `benchmark-results.json` so model history has a single home (open, see [source map](../../raw/sources/2026-10-28-github-consolidation.md)).

## Related
- [[turbofit]] · [[ecosystem]] · [[fit-ladder]]
