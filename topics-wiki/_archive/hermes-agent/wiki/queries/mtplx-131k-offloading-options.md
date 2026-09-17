---
title: "Can MTPLX use CPU offload, disk cache, or lower-precision KV to fit 131K on 32GB?"
created: 2026-09-07
updated: 2026-09-07
type: query
resolved: 2026-09-07
status: not-now
tags: [question, infra]
sources: ["raw/inbox/2026-09-07.md"]
confidence: high
answer: "No. Even with CPU offload or lower-precision KV, the combined memory (12.3 GB model + ~8 GB KV cache + 1 GB DFlash2 + 6-8 GB system = 27.3-29.3 GB) exceeds 32 GB physical RAM when accounting for page file and macOS services. Offloading would add latency that negates any tok/s target."
---

# Can MTPLX on Apple Silicon use CPU offload, disk cache, or lower-precision KV formats to fit Qwen 3.8 27B + 131K context under 32GB?

## Status

**Resolved — not-now** (2026-09-07). See [[topics-wiki/hermes-agent/wiki/decisions/131k-on-32gb-feasibility-decision-2026-09-07|131K on 32GB Feasibility Decision — 2026-09-07]].

## Answer

CPU offload, disk cache, and lower-precision KV formats cannot make `131K` context viable on `M1 32GB` with `Qwen 3.8 27B`. The memory math shows the model alone (12.3 GB) plus KV cache (~8 GB) plus DFlash2 (1 GB) already totals ~21.3 GB, leaving 10.7 GB for macOS + Hermes Agent + page file — which is insufficient for stable operation. ^[raw/inbox/2026-09-07.md]

Any offloading strategy would introduce the latency that makes the `10+ tok/s` target unachievable even if memory fit. The root cause is physical memory, not config.

## Alternative

Use `65K` context as the stable lockpoint — `[[topics-wiki/hermes-agent/wiki/decisions/stable-context-lock-2026-09-07|Stable Context Lock — 2026-09-07]]` documents this at `10-12 tok/s`, no OOM.

## Related
- [[topics-wiki/hermes-agent/wiki/decisions/131k-on-32gb-feasibility-decision-2026-09-07|131K on 32GB Feasibility Decision — 2026-09-07]]
- [[topics-wiki/hermes-agent/wiki/comparisons/65k-vs-131k-context|65K vs 131K Context Comparison]]
- [[topics-wiki/hermes-agent/wiki/decisions/stable-context-lock-2026-09-07|Stable Context Lock — 2026-09-07]]
- [[topics-wiki/hermes-agent/wiki/entities/model-check-20260903|Model Check — 20260903_001447_7bc70a]]
