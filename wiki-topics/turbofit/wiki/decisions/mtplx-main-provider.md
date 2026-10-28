---
title: MT_PlX Main Provider
created: 2026-09-07
updated: 2026-09-07
type: decision
tags: [decision, provider, configuration]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---

# MT_PlX Main Provider

Make `Youssofal/Qwen3.8-27B-MTPLX-Optimized-Speed` via `mtplx serve` the main TurboFit provider and remove Maple/Unleashed as co-resident models to reclaim disk space.

## Decision Context

Initial configuration used MTPLX at 131K context, but memory overcommit caused instability:
- `mtplx serve` with `--context-window 131072` prints `OVERCOMMITTED`
- Long prompts at 131K showed `507 Insufficient Storage` errors
- End-to-end throughput dropped to 0.39 tok/s

## Transition Path

1. Initial attempt: MTPLX at 131K → unstable under load
2. Cleanup: Removed Maple (53GB) and Unleashed Q3_K_XL (23GB)
3. Final config: MTPLX at 65K context (stable 7-12 tok/s)

## Final Configuration

```yaml
providers:
  turbofit:
    api: http://127.0.0.1:11613/v1
    default_model: mtplx-qwen38-27b-optimized-speed
    
model:
  default: ornith-1-5-35a3b-mlx  # Later switched to Ornith
  provider: custom:turbofit
```

## Status

- **2026-09-07 00:56**: MTPLX locked in as main provider at 65K context
- **2026-09-07 01:00**: Final state confirmed - MTPLX stable at 65K
- **2026-09-07 03:03**: Switched to Unleashed+DFlash2 after performance issues with MTPLX at 131K
- **2026-09-07 06:18**: Ornith MLX selected as winner and locked in

## The Ornith Override

After extensive testing comparing:
- Ornith MLX 4-bit: 28.5 tok/s short, 5.7 tok/s at 5K
- Nail Q4_K_XL: 23.4 tok/s short, 4.7 tok/s at 5K
- Tiel-Coder Q4_K_XL: 23.1 tok/s short, 4.2 tok/s at 5K

Ornith was selected as the main provider because:
1. Only model that works at 131K context
2. Best short-context speed (28.5 tok/s)
3. Good long-context throughput

## Related

- [[context-window-decision|Context Window Decision]]
- [[mtplx-qwen-38-27b-optimized-speed|MPLX Qwen 3.8 27B Optimized Speed]]
- [[ornith-35b-mlx|Ornith 35B MLX]]