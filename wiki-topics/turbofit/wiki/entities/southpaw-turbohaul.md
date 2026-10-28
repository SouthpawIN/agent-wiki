---
title: Southpaw Turbohaul
created: 2026-10-28
updated: 2026-10-28
type: entity
tags: [repo, turbofit, ecosystem]
sources: [raw/sources/2026-10-28-github-consolidation.md]
confidence: high
---

# Southpaw Turbohaul

> Curated fork of turbohaul-manager: AtomicBot llama.cpp (TQ3/TQ4 + MTP + NextN) and a hand-picked model set.

| | |
| --- | --- |
| **Repo** | [southpaw-turbohaul](https://github.com/SouthpawIN/southpaw-turbohaul) |
| **Status** | personal curated fork — model presets + AtomicBot runtime |

## What it adds over upstream

- **AtomicBot llama.cpp** build (TQ3/TQ4 quantized KV + MTP + NextN) in place of the stock TurboQuant fork.
- `bin/southpaw-models` model selector and `presets/southpaw-presets.yaml` / `presets/southpaw-setup.sh` hand-picked presets.
- Same queue / grace / IDLE_HOT / swap behaviour as [turbohaul-manager](turbohaul-manager.md).
- Docs inherited and extended: `docs/TURBOQUANT_FLAGS.md`, `docs/MULTI_AGENT_SHARING.md`, `docs/TOOL_CALL_HANDLING.md`, `docs/PERSISTENCE_CHECKLIST.md`.

## Reading it against TurboFit

`docs/TURBOQUANT_FLAGS.md` is the clearest written record of the TQ flag combinations; the MTP+quantized-KV composition claim lives here before any TurboFit rung used it.

## Related
- [[turbofit]] · [[ecosystem]] · [[fit-ladder]]
