---
title: 131K Deferred Candidates
created: 2026-09-07
updated: 2026-09-07
type: concept
tags: [concept, memory, oom, deferred, candidates]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---

# 131K Deferred Candidates

## The Problem

A number of newly downloaded candidate artifacts were not benchmarked at 131K because model-plus-KV size exceeds the stable 32 GB Mac fit before testing begins.

From [[raw/inbox/2026-09-07.md|2026-09-07 08:36]]:

> "Several downloaded candidates were deferred from 131K testing because their size plus KV cache exceeds stable 32 GB fit before benchmark."

## Why They're Deferred

The M1 MacBook 32GB has hard memory limits:

```
M1 MacBook 32GB unified memory:
- macOS + Hermes: ~8 GB
- Model weights: varies by model
- KV cache at 131K: ~8 GB (q8_0)
- Total needed: ~35+ GB > 32 GB available
```

### Candidate Analysis

| Model | Weights | KV @ 131K | Total | Fits? |
|-------|---------|-----------|-------|-------|
| **Ornith MLX 4-bit** | 18 GB | ~8 GB | ~26 GB | ✅ Yes |
| **Unleashed Q3_K_XL** | 12.31 GB | ~8 GB | ~20 GB | ✅ Yes |
| **Nail Q4_K_XL** | 20.8 GB | ~8 GB | ~29 GB | ⚠️ Marginal |
| **Tiel-Coder Q4_K_XL** | 22.4 GB | ~8 GB | ~30 GB | ⚠️ Marginal |
| **Dirk Q3_K_XL** | 13.1 GB | ~8 GB | ~21 GB | ✅ But slow/OOM |

## Memory Guard Evidence

From [[raw/inbox/2026-09-07.md|2026-09-07 00:56]]:

```json
{
  "event": "prefill_admission_shed",
  "prompt_tokens": 8014,
  "projected_bytes": 26306738710,
  "threshold_bytes": 24996709662,
  "limit_bytes": 25769803776,
  "cache_cleared": true
}
```

This shows MTPLX's memory guard: prefill_admission_shed clears KV cache to stay under ~24.99 GB threshold on a 25.77 GB limit, corroborating existing 32GB/131K overcommit findings.

## The Reality Check

From [[raw/inbox/2026-09-07.md|2026-09-07 09:20]]:

> "**The hard truth:** On M1 MacBook 32GB with a 27B model at 131K context, **~5-6 tok/s is the ceiling.** You want 10+ tok/s. That's not happening with this hardware — it's like asking a Honda Civic to go 200mph."

## Testing Strategy

**Working at 131K:**
- Ornith MLX 4-bit (18 GB)
- Unleashed Q3_K_XL (12.31 GB) + DFlash2 draft (1 GB)

**Deferred to smaller contexts:**
- Dirk Q3_K_XL - tested at 32K only (OOM at 65K)
- Nail Q4_K_XL - testing incomplete due to OOM risk
- Tiel-Coder Q4_K_XL - tested at 65K

## Key Insight

The winner for 131K must balance:
1. Model weights under ~18-20 GB
2. Efficient quantization (Q3/Q4)
3. MoE architecture OR small enough dense model

Ornith MLX 4-bit wins because it's MoE (~3B active params) with MLX backend for native Metal acceleration.

## Related

- [[turbofit/concepts/mtplx-32gb-memory-and-evidence-reliability|MPLX 32GB Memory and Evidence Reliability]]
- [[turbofit/entities/turbofit-memory-crash|TurboFit Memory Crash]]
- [[turbofit/entities/mplx-memory-guard|MPLX Memory Guard]]