---
title: Ornith 35B A3B DFlash2
created: 2026-09-07
updated: 2026-09-07
type: entity
tags: [model, tool, pain, decision]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
---

# Ornith 35B A3B DFlash2

`jzinno/Ornith-1.5-35B-A3B-DFlash2` was inspected on HuggingFace and downloaded as a local draft artifact for speculative-decode experiments ^[raw/inbox/2026-09-07.md].

## Status

- Community uptake is small (~840 downloads at observation time)
- No usable MTPLX integration path: MTPLX uses native MLX MTP heads rather than llama.cpp draft models
- DFlash2 is a CUDA-only diffusion-based draft model for llama.cpp/vLLM/sglang, incompatible with MLX MTP

## Benchmark Evidence

The DFlash2 draft model is **not viable for this hardware configuration**. From the speed tests:

| Setup | Short | 131K |
|-------|-------|------|
| **Ornith MLX 4-bit** | **28.5 tok/s** | ~0.5 tok/s |
| Ornith + DFlash2 | N/A | Cannot test |

The DFlash2 draft path cannot be used with Ornith MLX because:
1. MTPLX cannot use DFlash2 (native MLX MTP heads vs CUDA diffusion draft)
2. llama.cpp DFlash2 integration failed with invalid argument errors (`--draft-ngl`, `--draft-ctx-size`, `--low-vram` not supported)

## Contested Recommendation

Hermes recommended pairing Ornith MLX 4-bit with Unleashed+DFlash2 for 131K coverage; that pairing is contested because:
- DFlash2 cannot be integrated with Ornith MLX (different runtimes)
- Ornith MLX alone drops to ~0.5 tok/s at 131K due to KV cache dominance

## Final Recommendation

**Ornith MLX 4-bit solely as main provider** for short/medium context (28.5 tok/s at 500 tokens). For long context, use **Unleashed + DFlash2** at 131K (~5 tok/s) or **Nail Q4_K_XL** at 32K (23.4 tok/s).

## Related

- [[topics-wiki/turbofit/wiki/entities/ornith-35b-mlx.md|Ornith 35B MLX]]
- [[topics-wiki/turbofit/wiki/concepts/dflash2-mplx-incompatibility|MPLX DFlash2 Incompatibility]]
- [[topics-wiki/turbofit/wiki/entities/dflash2-draft.md|DFlash2 Draft]]
- [[topics-wiki/turbofit/wiki/queries/apple-silicon-runtime-benchmark|Apple Silicon Runtime Benchmark]]