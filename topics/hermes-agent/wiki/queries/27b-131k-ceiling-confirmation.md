---
title: "Can Qwen 3.8 27B achieve 10+ tok/s at 131K on M1 32GB with any combination?"
created: 2026-09-07
updated: 2026-09-07
type: query
resolved: 2026-09-07
status: not-now
tags: [question, infra, contested]
sources: ["raw/inbox/2026-09-07.md"]
confidence: high
answer: "No. 10+ tok/s at 131K is physically impossible on M1 32GB with a 27B model — it requires 64GB+ RAM or faster memory bus (M5 Max reference: 58 tok/s)."
---

# Can Qwen 3.8 27B achieve 10+ tok/s at 131K context on M1 32GB with any combination of quantization, speculative decoding, layer offloading, or alternative MTPLX providers?

## Status

**Resolved — not-now** (2026-09-07). See [[topics/hermes-agent/wiki/decisions/131k-on-32gb-feasibility-decision-2026-09-07|131K on 32GB Feasibility Decision — 2026-09-07]].

## Answer

No combination of quantization, speculative decoding, layer offloading, or alternative MTPLX providers can achieve `10+ tok/s at 131K` on `M1 32GB` with `Qwen 3.8 27B`. This is a hardware ceiling. ^[raw/inbox/2026-09-07.md]

## The requirement that cannot be met

> "Must be Qwen 3.8 27B variant. Target: 10+ tok/s at 131K context."
> — 2026-09-07 03:06 ^[raw/inbox/2026-09-07.md]

## Physical impossibility

> "The 10+ tok/s target at 131K is not happening on M1 32GB with a 27B model. It's like asking a Honda Civic to go 200mph. The engine isn't big enough."
> — 2026-09-07 05:35 ^[raw/inbox/2026-09-07.md]

### Memory breakdown

| Component | Size |
|-----------|------|
| Qwen 3.8 27B Q3_K_XL | 12.3 GB |
| 131K KV cache (q8) | ~8 GB |
| DFlash2 draft | 1 GB |
| macOS + Hermes Agent | 6-8 GB |
| **Total** | **27.3-29.3 GB** → exceeds 32 GB |

### Test results at 131K

| Prompt size | tok/s | Status |
|-------------|-------|--------|
| 44 tokens | 8.7 | Stable |
| 3K tokens | 1.0 | Stable |
| 4K tokens | 2.2 | Stable |
| 5K tokens | 0.3 | Stable |
| 8K tokens | 0.4 | Stable |
| 10K+ tokens | — | **OOM** |

## The interrupted session

Chris launched session `20260907_030601_6012ee` at `03:06` to pursue this target. It was interrupted at `05:38` after 20 API calls and 3400.36s without producing new measurement data. The attempt reinforced the same memory-cap conclusion. ^[raw/inbox/2026-09-07.md]

## Hardware path

**M5 Max reference**: 58 tok/s — achieved due to faster memory bus and idle system. Not replicable on M1 via software. ^[raw/inbox/2026-09-07.md]

**Upgrade requirement**: `64GB+` Mac for `10+ tok/s at 131K`.

## Related
- [[topics/hermes-agent/wiki/decisions/131k-on-32gb-feasibility-decision-2026-09-07|131K on 32GB Feasibility Decision — 2026-09-07]]
- [[topics/hermes-agent/wiki/decisions/stable-context-lock-2026-09-07|Stable Context Lock — 2026-09-07]]
- [[topics/hermes-agent/wiki/decisions/targeted-27b-131k-2026-09-07|Targeted 27B at 131K — 2026-09-07]]
- [[topics/hermes-agent/wiki/entities/session-20260907-030601|Session Check — 20260907_030601_6012ee]]
- [[topics/hermes-agent/wiki/comparisons/65k-vs-131k-context|65K vs 131K Context Comparison]]
