---
title: Context Window Decision
created: 2026-09-07
updated: 2026-09-07
type: decision
tags: [decision, hardware, context-window]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---

# Context Window Decision

**Decision**: Lock in 65K context as the stable daily driver on M1 MacBook 32GB, with 131K reserved for rare long-context needs where speed is not critical.

## Decision Evidence

From in-session testing on 2026-09-07:
- MTPLX at 131K shows `OVERCOMMITTED` and `requested context 131072 exceeds the machine fit`
- Long-context generation shows severe degradation: 0.39 tok/s end-to-end vs 8-12 tok/s at 65K
- Memory plan shows `engine budget 24.0G, weights 19.3G` leaving insufficient room for 131K KV cache

## Hardware Constraints

```
M1 MacBook 32GB unified memory:
- macOS + Hermes: ~8 GB
- Model weights (MTPLX): 19.3 GB  
- KV cache at 131K: ~8 GB
- Total needed: ~35 GB > 32 GB available
```

## Speed Comparison

|| Context | MTPLX | Unleashed+DFlash2 |
||---------|-------|-------------------|
|| 65K | 7-8 tok/s stable | ~5 tok/s |
|| 131K | 0.39 tok/s (observed) | 5 tok/s (with q8 KV) |

## Why 65K is Daily Driver

1. **Stable throughput**: 7-8 tok/s vs 0.39 tok/s at 131K
2. **No OOM risk**: Memory fits comfortably
3. **Fast enough**: Meets the 10+ tok/s target is not physically achievable at 131K on this hardware

## 131K as Fallback

131K context remains available for when long-context is essential (research, document summarization) and speed is not the priority.

## Chris's Words

> "Stable 65K is the safe daily context on this box; 131K remains a long-context fallback despite throughput collapse."

## Related

- [[topics/turbofit/wiki/entities/mplx-qwen-38-27b-optimized-speed.md|MPLX Qwen 3.8 27B Optimized Speed]]
- [[topics/turbofit/wiki/decisions/mtplx-main-provider.md|MPLX Main Provider]]
- [[topics/turbofit/wiki/entities/unleashed-27b.md|Unleashed 27B]]