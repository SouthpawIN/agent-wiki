---
title: Aux Runtime Options
created: 2026-09-06
updated: 2026-09-06
type: comparison
tags: [comparison, tool, pain, decision]
sources: [raw/inbox/2026-09-06.md]
confidence: high
---

# Aux Runtime Options

## Options tested for Maple aux on this box

| Runtime | Result | Reason |
|---------|--------|--------|
| `llama.cpp` stock | Failed | `unknown model architecture: 'maple'` |
| `stamsam/llama.cpp` fork + TQ2_0 | Failed | Missing Metal kernel `kernel_mul_mm_id_tq2_0_f32`; warmup crash and load crash |
| `stamsam/llama.cpp` fork + Q2_0 | Failed | `gguf_init_from_reader: failed to read tensor data` |
| `mlx_lm` server generic | Failed | `Insufficient Memory` after prompt-cache growth beyond ~1K tokens |
| `deepgrove-ai/mlx-lm-deepgrove` generate | Works | 100–5000 tokens: 2–9 s; 130K tokens: 103 s, no OOM |
| `deepgrove-ai/mlx-lm-deepgrove` server | Partial | Works but prompt-cache growth causes repeated OOM |
| Nous free tier | Works | Handles 270K tokens, zero local memory pressure |

## Selected path

Maple MLX via deepgrove fork with Hermes compression routing configured locally. If server-mode instability returns, fallback to Nous for heavy compression and keep Maple for short aux only ^[raw/inbox/2026-09-06.md].

## Related

- [[topics-wiki/turbofit/wiki/entities/maple.md|Maple]]
- [[topics-wiki/turbofit/wiki/decisions/aux-model-selection.md|Aux Model Selection]]
- [[topics-wiki/turbofit/wiki/queries/maple-metal-compat.md|Maple Metal Compatibility]]
