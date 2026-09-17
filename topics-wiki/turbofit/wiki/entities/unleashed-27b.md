---
title: Unleashed 27B
created: 2026-09-06
updated: 2026-09-06
type: entity
tags: [tool, repo, model, decision]
sources: [raw/inbox/2026-09-06.md]
confidence: high
---

# Unleashed 27B

Qwen3.8-27B-Unleashed in `UD-Q3_K_XL.gguf` with the Unleashed vision projector and DFlash2 draft. This is the main model in TurboFit ^[raw/inbox/2026-09-06.md].

## Served config

- **Runtime**: `llama.cpp` Metal build (`dflash2-llama.cpp-...`).
- **Port**: `11606`.
- **Context**: `131072`.
- **Draft**: `Qwen3.8-27B-DFlash2-Q4_K_M.gguf`, `--spec-type draft-dflash --spec-draft-n-max 7`.
- **KV cache**: `q4_0` k/v.
- **Batch**: `-b 512 -ub 256`.
- **Performance**: ~4.4–5.1 tok/s decode on this box ^[raw/inbox/2026-09-06.md].

## Role

- Main inference and vision provider.
- Stable under long context and large prompt ingest.
- Holds the DFlash2 draft path that earlier failed with wrong draft flags (`--draft-max`) and tensor mismatch before being aligned to the fork’s `--spec-draft-*` args ^[raw/inbox/2026-09-06.md].

## Related

- [[topics-wiki/turbofit/wiki/entities/turbofit.md|TurboFit]]
- [[topics-wiki/turbofit/wiki/entities/dflash2-draft.md|DFlash2 Draft]]
- [[topics-wiki/turbofit/wiki/decisions/main-model-selection.md|Main Model Selection]]
