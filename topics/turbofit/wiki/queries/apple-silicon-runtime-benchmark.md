---
title: Apple Silicon Runtime Benchmark
created: 2026-09-07
updated: 2026-09-07
type: query
tags: [query, benchmark, runtime, ml, apple-silicon]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---

# Apple Silicon Runtime Benchmark

## Research Request

From [[raw/inbox/2026-09-07.md|2026-09-07 03:06]]: Chris asked to "Research and test ALL available Apple Silicon inference engines for Qwen 3.8 27B to find the fastest configuration: llama.cpp (different quants, KV cache types, speculative decoding), MLX (deepgrove fork), OMLX, FreeToken, and any other engines found. Report tok/s for each."

^[raw/inbox/2026-09-07.md]

## Tested Engines

### Ornith MLX 4-bit
- **Server**: `mlx_lm server --model ~/Models/storage/ornith --port 11613`
- **Context**: 131K
- **Speed**: 28.5 tok/s short, 5.7 tok/s at 5K, ~5 tok/s at 131K
- **Status**: Winner for short/medium context

### Tiel-Coder Q4_K_XL (llama.cpp)
- **Server**: `llama-server --model ~/Models/storage/tiel-coder-gguf/Tiel-Coder-35B-A3B-UD-Q4_K_XL.gguf --port 11622`
- **Context**: 65K
- **Speed**: 23.1 tok/s short, 4.2 tok/s at 5K
- **Status**: Working but slower than Ornith

### Dirk Q3_K_XL (llama.cpp)
- **Server**: `llama-server --model ~/Models/storage/dirk-gguf/Dirk-Qwen3.8-27B-UD-Q3_K_XL.gguf --port 11621`
- **Context**: 32K (OOM at 65K)
- **Speed**: 6.0 tok/s short, 0.8 tok/s at 5K
- **Status**: OOM above 32K context

### Nail Q4_K_XL (llama.cpp)
- **Server**: `llama-server --model ~/Models/storage/nail/Nail-Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf --port 11621`
- **Context**: 32K
- **Speed**: 23.4 tok/s short, 4.7 tok/s at 5K
- **Status**: MoE performs well at limited context

### MTPLX Qwen 3.8 27B Optimized Speed
- **Server**: `mtplx serve --model Youssofal/Qwen3.8-27B-MTPLX-Optimized-Speed`
- **Context**: 65K (stable), 131K (overcommitted)
- **Speed**: 8-12 tok/s at 65K, OOM at 131K with large prompts
- **Status**: Fast at 65K but problematic at 131K

### Unleashed + DFlash2 (llama.cpp fork)
- **Server**: `llama-server` with dflash2-llama.cpp fork
- **Context**: 131K (with q8 KV cache)
- **Speed**: ~5 tok/s stable
- **Issues**: DFlash2 flag incompatibilities, memory pressure
- **Status**: Slow but stable long-context option

## Speed Comparison Table

| Setup | Short (500t) | 5K Prompt | 131K | Status |
|-------|-------------|-----------|------|--------|
| **Ornith MLX 4-bit** | **28.5 tok/s** | 5.7 tok/s | ~5 tok/s | ✅ Best overall |
| Nail Q4_K_XL | 23.4 tok/s | 4.7 tok/s | - | ⚠️ 32K limit |
| Tiel-Coder Q4_K_XL | 23.1 tok/s | 4.2 tok/s | - | ⚠️ 65K limit |
| MTPLX 65K | 8-12 tok/s | - | - | ✅ Stable |
| Dirk Q3_K_XL | 6.0 tok/s | 0.8 tok/s | OOM | ❌ Fails |
| Unleashed+DFlash2 | 5 tok/s | - | **~5 tok/s** | ✅ Long-context |

## Hardware Reality Check

From [[raw/inbox/2026-09-07.md|2026-09-07 05:41]]:

> "**The hard truth:** On M1 MacBook 32GB with a 27B model at 131K context, **~5-6 tok/s is the ceiling.** You want 10+ tok/s. That's not happening with this hardware — it's like asking a Honda Civic to go 200mph."

## Key Findings

1. **MLX beats llama.cpp for 27B models on M1** - Native Metal acceleration is essential
2. **MoE architecture wins** - Models with ~3B active params outperform dense models
3. **65K is the practical limit** for fast inference on 32GB M1
4. **DFlash2 compatibility is runtime-specific** - Incompatible with MTPLX's MLX heads

## Related

- [[turbofit/queries/engine-research-request|Engine Research Request]]
- [[turbofit/entities/ornith-1-5-35b-a3b-mlx-4-bit|Ornith 1.5 35B-A3B MLX 4-bit]]
- [[turbofit/concepts/dflash2-mplx-incompatibility|DFlash2 MTPLX Incompatibility]]