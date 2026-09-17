---
title: "Ornith performance metrics"
created: 2026-09-07
updated: 2026-09-13
type: concept
tags: [model, tool, pain, plan]
sources: [raw/inbox/2026-09-07.md, raw/inbox/2026-09-13.md]
confidence: high
---

# Ornith performance metrics

Observed throughput numbers for Ornith 1.5 local variants, captured across local-inference runs on 2026-09-07 and 2026-09-13.

## DFlash2 initial result

^[raw/inbox/2026-09-07.md] At 08:39, Hermes reported Ornith results of **15.6 tok/s short** and **5.7 tok/s** at 5K context for the DFlash2 variant.

## MLX 4-bit results after cleanup

^[raw/inbox/2026-09-07.md] After cleanup and restarting with Ornith properly, Hermes observed:
- **29 tok/s short**
- **226 tok/s 5K**

These became the baseline used to judge the other candidates.

## Q4_K_M result — Ornith now routing (2026-09-13)

^[raw/inbox/2026-09-13.md] At 16:39 Hermes reported: **"Ornith 1.5 is alive and routing. 14.5 tok/s on an M1 with Q4_K_M."** This is a different quantizer (Q4_K_M) than the earlier DFlash2/MLX-4b figures and a different machine class (M1) — so it is not directly comparable to the 09-07 numbers, which were measured on the primary (non-M1) local model. The 14.5 tok/s figure is the M1-on-Q4_K_M data point.

See also:
- [[wiki/entities/ornith-dflash2-artifacts|Ornith DFlash2 artifacts]]
- [[wiki/entities/ornith-mlx4b-artifacts|Ornith 1.5 model artifacts]]
- [[wiki/entities/mtplx-qwen38-27b-endpoint|mtplx-qwen38-27b endpoint]]
- [[wiki/concepts/ornith-routing-config|Ornith 1.5 routing config (8091)]]
