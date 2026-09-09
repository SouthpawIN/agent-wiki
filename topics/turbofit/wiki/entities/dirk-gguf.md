---
title: Dirk GGUF Q3_K_XL
created: 2026-09-07
updated: 2026-09-07
type: entity
tags: [model, tool, preference]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
---

# Dirk GGUF Q3_K_XL

`Dirk-Qwen3.8-27B-UD-Q3_K_XL.gguf` (12.24 GB) is the requested Q3 Dirk artifact at `~/Models/storage/dirk-gguf/`, selected because Chris prefers Q3 when it is described as near base-model quality and because 13 GB fits the short-context candidate path better than heavier quants on this 32 GB box ^[raw/inbox/2026-09-07.md].

## Status

- Downloaded and verified on disk (12.24 GB, GGUF magic number confirmed)
- No benchmark evidence yet; 131K testing deferred because Dirk is a dense 27B model
- Chris explicitly wanted GGUF vs MLX compared, with preference for Q3 when near base quality

## Memory Impact

Dirk is a **dense 27B model** (not MoE), so:
- Model weights: 12.24 GB (Q3_K_XL)
- KV cache at 131K (q8): ~8 GB
- Total: ~20 GB + macOS/Hermes (~8 GB) = ~28 GB at 32K context

**Result**: OOM expected above 32K context window.

## Repo Correction

- Requested: `peculiar-ragdoll/Dirk-Qwen3.8-27B-GGUF-MTP` (returned 404)
- Actual: `peculiar-ragdoll/Dirk-Qwen3.8-27B-GGUF` (MTP is a model capability, not repo name)

## Runtimes Tested

| Runtime | Status | Notes |
|---------|--------|-------|
| llama.cpp stock | ❌ Incompatible | `unknown model architecture: 'maple'` (Maple only) |
| llama.cpp Qwen branch | ✅ | Works with Q3_K_XL |
| MLX | 🔄 Pending | Would need 131K streaming verification |

## Related

- [[topics/turbofit/wiki/entities/dirk-qwen38-27b.md|Dirk Qwen 3.8 27B GGUF]]
- [[topics/turbofit/wiki/decisions/candidate-quant-preference.md|Candidate Quant Preference]]
- [[topics/turbofit/wiki/queries/apple-silicon-runtime-benchmark|Apple Silicon Runtime Benchmark]]
- [[topics/turbofit/wiki/entities/unleashed-27b.md|Unleashed 27B]]