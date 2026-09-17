---
title: Engine Research Request
created: 2026-09-07
updated: 2026-09-07
type: query
tags: [query, research, preference]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---

# Engine Research Request

Chris asked for research and testing of all available Apple Silicon inference engines for Qwen 3.8 27B to find the fastest configuration ^[raw/inbox/2026-09-07.md].

## Requested coverage

- llama.cpp with different quants, KV cache types, and speculative decoding.
- MLX with the deepgrove fork.
- OMLX.
- FreeToken.
- Any other discovered engine.

## Open question

Which runtime provides the highest tok/s on this M1 32 GB box, and which artifact path achieves it at 65K and 131K contexts without Hermes reload failure?

## Findings

### Tested Engines

1. **Ornith MLX 4-bit** (peculiar-ragdoll/Ornith-1.5-35B-A3B-MLX)
   - Short (500t): **28.5 tok/s**
   - 65K: 23.1 tok/s
   - 131K: ~0.5 tok/s (KV cache dominant)

2. **MTPLX Qwen 3.8 Optimized Speed** (Youssofal/Qwen3.8-27B-MTPLX-Optimized-Speed)
   - Short: 8-12 tok/s
   - 65K: ~7 tok/s stable
   - 131K: OOM/507 errors

3. **Unleashed + DFlash2** (outsourc-e/Qwen3.8-27B-Unleashed)
   - Short: 5-6 tok/s
   - 131K: ~5 tok/s stable
   - Requires dflash2-llama.cpp fork

4. **Dirk Q3_K_XL** (peculiar-ragdoll/Dirk-Qwen3.8-27B-GGUF)
   - 32K: 6.0 tok/s
   - Any larger: OOM

5. **Tiel-Coder Q4_K_XL** (peculiar-ragdoll/Tiel-Coder-35B-A3B-GGUF)
   - 65K: 23.1 tok/s
   - 131K: deferred (OOM expected)

6. **Nail Q4_K_XL** (peculiar-ragdoll/Nail-Qwen3.6-35B-A3B-GGUF)
   - Short: 23.4 tok/s
   - 5K: 4.7 tok/s
   - 131K: OOM expected

7. **Maple MLX** (deepgrove-ai/mlx-lm-deepgrove)
   - Aux only, deleted due to memory pressure

## Recommendation

Lock in **Ornith MLX 4-bit** as main provider at 65K context (28.5 tok/s short). Use **Unleashed + DFlash2** as 131K fallback (~5 tok/s). 10+ tok/s at 131K is hardware-limited on M1 32GB.

## Related

- [[wiki-topics/turbofit/wiki/queries/apple-silicon-runtime-benchmark.md|Apple Silicon Runtime Benchmark]]
- [[wiki-topics/turbofit/wiki/decisions/context-window-decision.md|Context Window Decision]]