---
title: "Is there a viable M-series Mac below 64GB RAM for Qwen 3.8 27B at 131K?"
created: 2026-09-07
updated: 2026-09-07
type: query
resolved: 2026-09-07
status: answered
tags: [question, infra]
sources: ["raw/inbox/2026-09-07.md"]
confidence: high
answer: "No. The 32GB M1 ceiling (12.3 GB model + ~8 GB KV cache + 1 GB DFlash2 + 6-8 GB system ≈ 27.3-29.3 GB) leaves no headroom. 64GB+ Mac (M4 Pro/Max) is the hardware floor for 131K at 10+ tok/s."
---

# Is there a viable M-series Mac configuration below 64GB RAM that can run Qwen 3.8 27B at 131K context without OOM?

## Status

**Resolved — answered** (2026-09-07). See [[wiki-topics/hermes-agent/wiki/decisions/131k-on-32gb-feasibility-decision-2026-09-07|131K on 32GB Feasibility Decision — 2026-09-07]].

## Answer

No sub-64GB M-series Mac can run `Qwen 3.8 27B` at `131K` context without OOM. The memory ceiling on `32GB` is hard: model weights (12.3 GB) + KV cache (~8 GB) + DFlash2 (1 GB) + macOS + Hermes Agent (6-8 GB) already totals 27.3-29.3 GB. No quantization path can reclaim the remaining 3-5 GB needed for stable operation at large prompt sizes. ^[raw/inbox/2026-09-07.md]

## Reference point

> "The M5 Max gets 58 tok/s because it has a faster memory bus and was tested with nothing else running."
> — 2026-09-07 00:35 ^[raw/inbox/2026-09-07.md]

The M5 Max achieves far higher throughput due to its faster memory bus — a hardware advantage that cannot be replicated on M1 via software configuration.

## Hardware floor

**64GB+ Mac** (M4 Pro/Max recommended) for `10+ tok/s at 131K` with `Qwen 3.8 27B`. The M1 32GB is suitable only for `65K` context as daily driver.

## Related
- [[wiki-topics/hermes-agent/wiki/decisions/131k-on-32gb-feasibility-decision-2026-09-07|131K on 32GB Feasibility Decision — 2026-09-07]]
- [[wiki-topics/hermes-agent/wiki/comparisons/65k-vs-131k-context|65K vs 131K Context Comparison]]
- [[wiki-topics/hermes-agent/wiki/decisions/stable-context-lock-2026-09-07|Stable Context Lock — 2026-09-07]]
- [[wiki-topics/hermes-agent/wiki/entities/model-check-20260903|Model Check — 20260903_001447_7bc70a]]
