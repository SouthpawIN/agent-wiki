---
name: turbo-model-store-cleanup
description: Use when freeing TurboFit storage. Delete only wiki-marked obsolete artifacts.
version: 0.1.0
distilled: 2026-09-07 17:12
topic: turbofit
---
# turbo-model-store-cleanup
## Steps
1. Read the topic wiki index and decision pages to identify obsolete or superseded candidates.
2. Match candidate names to directories under `~/Models/storage/`.
3. Remove only artifacts for candidates the wiki marks obsolete, deferred, or explicitly replaced.
4. Record freed space and exact paths removed in the candidate's wiki entity page.
5. Do not remove artifacts for candidates still in active testing or queued for comparison.

## Pitfalls
- Do not delete before the wiki decision page says the candidate is obsolete.
- Do not treat rerouted raw download bursts as cleanup; verify on-disk state.
- Do not clear a candidate that Chris has not yet approved removing.

## Evidence
> Must clear old models from `~/Models/storage/gguf/` before testing new ones to free RAM.
> Current immediate goal: clean up obsolete 27B model files (Nail, Tiel-Coder, etc.)

## Evidence
> "Must clear old models from `~/Models/storage/gguf/` before testing new ones to free RAM."
> "Current immediate goal: clean up obsolete 27B model files (Nail, Tiel-Coder, etc.)"
