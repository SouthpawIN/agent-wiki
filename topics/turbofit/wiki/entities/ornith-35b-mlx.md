---
title: Ornith 35B MLX
created: 2026-09-07
updated: 2026-09-07
type: entity
tags: [model, tool, decision]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
contested: true
---

# Ornith 35B A3B MLX

`Ornith-1.5-35B-A3B` MLX 4-bit is a MoE local candidate downloaded to `~/Models/storage/ornith/` with a companion DFlash2 draft package at `~/Models/storage/ornith-dflash2/` ^[raw/inbox/2026-09-07.md].

This page is a legacy entity record; see [[topics/turbofit/wiki/entities/ornith-1-5-35b-a3b-mlx-4-bit.md|Ornith 1.5 35B-A3B MLX 4-bit]] for measured throughput and config state after 2026-09-07 final lock-in ^[raw/inbox/2026-09-07.md].

## Tested speeds on M1 MacBook 32GB

|| Context | Tok/s |
||---------|-------|
|| Short (~500 tokens) | **28.5** |
|| 5K tokens | 5.7 |
|| 20K tokens | 1.5 |
|| 40K tokens | 0.7 |
|| 60K tokens | 0.4 |
|| 131K | ~0.5 |

These numbers were gathered in-session against downloaded artifacts ^[raw/inbox/2026-09-07.md].

## Model Facts

- **Architecture**: MoE 35B (3B active params per token)
- **Weight**: 18 GB via MLX 4-bit
- **Inference**: MLX via `mlx_lm` server

## Role

- Fastest observed short-context path on this box (28.5 tok/s)
- KV cache dominates throughput above ~20K context
- 131K path is unstable (~0.5 tok/s)

## Contested Evidence

Hermes summary claimed Ornith wins at 131K, but speed tests from 09:19 show:
- Ornith MLX 4-bit: 28.5 tok/s short, ~0.5 tok/s at 131K
- Nail Q4_K_XL: 23.4 tok/s short, 4.7 tok/s at 5K
- Tiel-Coder Q4_K_XL: 23.1 tok/s short, 4.2 tok/s at 5K
- Dirk Q3_K_XL: 6.0 tok/s at 32K, OOM above

**Conclusion**: Ornith is fastest at short context but drops sharply at long context. The "winner" designation depends on use case.

- **Current routed state**

Hermes `custom:turbofit` was retargeted to Ornith MLX on `http://127.0.0.1:11613/v1`, and session metadata confirms the provider changed to `ornith-1-5-35a3b-mlx via provider turbofit` at 14:25, but persistent `Connection error` timeouts recurred at 2026-09-07T19:26:47.525Z ^[raw/inbox/2026-09-07.md]. Until a verified post-restart Hermes completion is captured, the routed state remains contested.

- **Practical recommendation**

Use Ornith MLX 4-bit for short/medium-context daily work. Use Unleashed+DFlash2 for long-context fallback where stable throughput matters more than peak speed.

## Related

- [[topics/turbofit/wiki/entities/ornith-35b-dflash2.md|Ornith 35B DFlash2]]
- [[topics/turbofit/wiki/decisions/aux-model-selection.md|Aux Model Selection]]
- [[topics/turbofit/wiki/queries/apple-silicon-runtime-benchmark|Apple Silicon Runtime Benchmark]]