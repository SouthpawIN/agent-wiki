---
title: "Ornith performance metrics"
created: 2026-09-07
updated: 2026-09-07
type: concept
tags: [model, tool, preference]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---

# Ornith performance metrics

Observed throughput numbers for Ornith 1.5 local variants, captured during a multi-model comparison on 2026-09-07.

## DFlash2 initial result

^[raw/inbox/2026-09-07.md] At 08:39, Hermes reported Ornith results of **15.6 tok/s short** and **5.7 tok/s** at 5K context for the DFlash2 variant.

## MLX 4-bit results after cleanup

^[raw/inbox/2026-09-07.md] After cleanup and restarting with Ornith properly, Hermes observed:
- **29 tok/s short**
- **226 tok/s 5K**

These became the baseline used to judge the other candidates.

See also:
- [[wiki/entities/ornith-dflash2-artifacts|Ornith DFlash2 artifacts]]
- [[wiki/entities/ornith-mlx4b-artifacts|Ornith 1.5 model artifacts]]
- [[wiki/entities/mtplx-qwen38-27b-endpoint|mtplx-qwen38-27b endpoint]]
