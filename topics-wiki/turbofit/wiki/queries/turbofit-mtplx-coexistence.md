---
title: TurboFit MTPLX Coexistence
created: 2026-09-07
updated: 2026-09-07
type: query
tags: [query, infra, model, pain]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---

# Can MTPLX serve as a live TurboFit provider on this box without being killed by memory limits or forcing co-resident main-model eviction?

## Evidence: No — MTPLX cannot coexist at 131K on this 32GB box

| Scenario | Result | Notes |
|----------|--------|-------|
| MTPLX 131K with 500-token prompt | 8–12 tok/s | Stable |
| MTPLX 131K with 5K+ prompt | OOM / 507 Insufficient Storage | Memory overcommit |
| MTPLX 131K with DFlash2 draft | Not available | DFlash2 incompatible with MLX MTP |
| Unleashed + DFlash2 131K | ~5 tok/s | Stable but slower than 65KMTPLX |
| Ornith 35B MLX 4-bit 131K | ~0.5 tok/s | KV cache dominates |

## Key Constraint

**32GB physical RAM limitation:** 27B model weights (19.3GB) + KV cache at 131K (8GB) + macOS/Hermes (~8GB) = ~35GB+, exceeding available memory.

The memory plan explicitly shows `OVERCOMMITTED` before any generation:
```
Memory plan: 32G Mac: engine budget 24.0G, weights 19.3G, context 131072 (machine-bound) (OVERCOMMITTED)
requested context 131072 exceeds the machine fit 8192: KV at the full window needs 8.0 GiB
```
^[raw/inbox/2026-09-07.md].

## Pattern: Stable vs Overcommitted

- **65K context:** Stable across all runtimes (MTPLX ~7 tok/s, Unleashed+DFlash2 ~5 tok/s)
- **131K context:** Consistent OOM/kill on 5K+ prompts regardless of runtime

## Related

- [[topics-wiki/turbofit/wiki/concepts/mtplx-context-overcommit|MPLX Context Overcommit]]
- [[topics-wiki/turbofit/wiki/entities/turbofit-memory-crash|TurboFit Memory Crash]]
- [[topics-wiki/turbofit/wiki/entities/turbofit-mtp-performance|TurboFit MTP Performance]]
- [[topics-wiki/turbofit/wiki/decisions/context-window-decision|Context Window Decision]]