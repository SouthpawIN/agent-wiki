---
title: DFlash2 Draft
created: 2026-09-06
updated: 2026-09-06
type: entity
tags: [tool, model, spec]
sources: [raw/inbox/2026-09-06.md]
confidence: high
---

# DFlash2 Draft

DFlash2 is the speculative-draft model paired with Unleashed 27B in TurboFit. It requires the `dflash2-llama.cpp` fork, not stock llama.cpp ^[raw/inbox/2026-09-06.md].

## Artifact

- `~/Models/storage/gguf/Qwen3.8-27B/Qwen3.8-27B-DFlash2-Q4_K_M.gguf` ^[raw/inbox/2026-09-06.md].

## Flag corrections

- Wrong: `--draft-max`, `--draft-min`, `--draft-p-min`, `--model-draft`.
- Correct for this fork: `--spec-draft-model <path>`, `--spec-draft-n-max 7`, `--spec-draft-n-min 5`, `--spec-draft-p-min 0.75`, `--spec-type draft-dflash` ^[raw/inbox/2026-09-06.md].

## Related

- [[topics-wiki/turbofit/wiki/entities/unleashed-27b.md|Unleashed 27B]]
- [[topics-wiki/turbofit/wiki/entities/turbofit.md|TurboFit]]
- [[topics-wiki/turbofit/wiki/comparisons/aux-runtime-options.md|Aux Runtime Options]]
- [[topics-wiki/turbofit/wiki/entities/ornith-35b-dflash2.md|Ornith 35B DFlash2]]
