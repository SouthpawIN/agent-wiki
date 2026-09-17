---
title: "Can 131K context with Qwen 3.8 27B be made stable on M1 32GB?"
created: 2026-09-07
updated: 2026-09-07
type: query
resolved: 2026-09-07
status: not-now
tags: [question, infra]
sources: ["raw/inbox/2026-09-07.md"]
confidence: high
answer: "No. Physical memory math (12.3 GB model + ~8 GB KV cache + 1 GB DFlash2 + 6-8 GB system = 27.3-29.3 GB) leaves no headroom on 32 GB. OOM at 10K+ prompt tokens is a hardware ceiling, not a config gap."
---

# Can 131K context with Qwen 3.8 27B be made stable on M1 32GB by changing KV cache quantization, offloading, or draft-model memory usage?

## Status

**Resolved — not-now** (2026-09-07). See [[topics-wiki/hermes-agent/wiki/decisions/131k-on-32gb-feasibility-decision-2026-09-07|131K on 32GB Feasibility Decision — 2026-09-07]].

## Answer

No. The `10+ tok/s at 131K` target with `Qwen 3.8 27B` is physically impossible on `M1 32GB` regardless of quantization, offloading, or draft-model configuration. The memory budget is exhausted by model weights + KV cache + DFlash2 + system overhead, leaving zero headroom for the page file or macOS services. ^[raw/inbox/2026-09-07.md]

## Recommendation

- Use `65K` context as the daily driver (stable, `10-12 tok/s`, no OOM).
- Upgrade to `64GB+` Mac for the `131K` target.

## Related
- [[topics-wiki/hermes-agent/wiki/decisions/131k-on-32gb-feasibility-decision-2026-09-07|131K on 32GB Feasibility Decision — 2026-09-07]]
- [[topics-wiki/hermes-agent/wiki/comparisons/65k-vs-131k-context|65K vs 131K Context Comparison]]
- [[topics-wiki/hermes-agent/wiki/decisions/stable-context-lock-2026-09-07|Stable Context Lock — 2026-09-07]]
- [[topics-wiki/hermes-agent/wiki/entities/model-check-20260903|Model Check — 20260903_001447_7bc70a]]
