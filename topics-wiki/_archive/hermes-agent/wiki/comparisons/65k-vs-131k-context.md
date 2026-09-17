---
title: "65K vs 131K Context Comparison"
created: 2026-09-07
updated: 2026-09-07
type: comparison
tags: [preference, infra, comparison]
sources: ["raw/inbox/2026-09-07.md"]
confidence: high
---

# 65K vs 131K Context Comparison

## Summary

On `M1 MacBook 32GB` with `Qwen 3.8 27B` + `MTPLX` + `DFlash2`, the two context-length options are not interchangeable — `131K` is a hardware ceiling that triggers OOM, while `65K` is the stable operating point.

## Performance at 131K context

| Prompt size | tok/s | Status |
|-------------|-------|--------|
| 44 tokens | 8.7 | Stable |
| 3K tokens | 1.0 | Stable |
| 4K tokens | 2.2 | Stable |
| 5K tokens | 0.3 | Stable |
| 8K tokens | 0.4 | Stable |
| 10K+ tokens | — | **OOM (507)** |

> "MTPLX loads at ~20GB, KV cache at 131K needs ~12GB. That's 32GB total — zero room for macOS, Hermes Agent, or anything else."
> — 2026-09-07 00:25 ^[raw/inbox/2026-09-07.md]

## Performance at 65K context

| Metric | Value |
|--------|-------|
| tok/s | 10-12 |
| Stability | No OOM |
| Viable on M1 32GB | Yes ✅ |

> "MTPLX at 65K context — 10-12 tok/s, stable, no OOM"
> — 2026-09-07 00:25 ^[raw/inbox/2026-09-07.md]

## The memory math

| Component | 131K | 65K (estimated) |
|-----------|------|------------------|
| Model weights (Q3_K_XL) | 12.3 GB | 12.3 GB |
| KV cache | ~8 GB | ~4 GB |
| DFlash2 draft | 1 GB | 1 GB |
| macOS + Hermes Agent | 6-8 GB | 6-8 GB |
| **Total** | **27.3-29.3 GB** → OOM at 10K+ | **24.3-25.3 GB** → stable |

## Recommendation

- **Daily driver**: `65K context` — stable, fast enough (`10-12 tok/s`), no OOM.
- **Long-context work**: `131K context` — switch to `Unleashed` when needed; accept lower throughput and OOM risk at large prompt sizes.

> "Lock in 65K context as main provider; keep catalog entry for future 64GB+ Mac upgrade."
> — 2026-09-07 00:25 ^[raw/inbox/2026-09-07.md]

## Related
- [[topics-wiki/hermes-agent/wiki/decisions/stable-context-lock-2026-09-07|Stable Context Lock — 2026-09-07]]
- [[topics-wiki/hermes-agent/wiki/decisions/131k-on-32gb-feasibility-decision-2026-09-07|131K on 32GB Feasibility Decision — 2026-09-07]]
- [[topics-wiki/hermes-agent/wiki/entities/model-check-20260903|Model Check — 20260903_001447_7bc70a]]
- [[topics-wiki/hermes-agent/wiki/decisions/targeted-27b-131k-2026-09-07|Targeted 27B at 131K — 2026-09-07]]
