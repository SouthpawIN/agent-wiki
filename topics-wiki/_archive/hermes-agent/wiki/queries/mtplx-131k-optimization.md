---
title: "What config flags, quantization, or offloading strategies run MTPLX 27B at 131K on 32GB?"
created: 2026-09-07
updated: 2026-09-07
type: query
resolved: 2026-09-07
status: not-now
tags: [question, infra]
sources: ["raw/inbox/2026-09-07.md"]
confidence: high
answer: "No combination of config flags, quantization paths, or offloading strategies can overcome the 32GB physical ceiling. The memory budget (12.3 GB model + ~8 GB KV cache + 1 GB DFlash2 + 6-8 GB system = 27.3-29.3 GB) leaves only 2.7-4.7 GB headroom, insufficient for page file and macOS services at 10K+ prompt sizes."
---

# What config flags, quantization paths, or offloading strategies let MTPLX Qwen 3.8 27B run at 131K context without OOM on 32GB unified memory?

## Status

**Resolved — not-now** (2026-09-07). See [[topics-wiki/hermes-agent/wiki/decisions/131k-on-32gb-feasibility-decision-2026-09-07|131K on 32GB Feasibility Decision — 2026-09-07]].

## Answer

No config flag, quantization path, or offloading strategy can make `131K` context stable for `Qwen 3.8 27B` on `M1 32GB`. The `10K+` prompt OOM is a hardware ceiling, not a config gap. ^[raw/inbox/2026-09-07.md]

## Evidence

The interrupted evaluation session (`20260907_030601_6012ee`) tested multiple approaches and produced no improvement:

> "ERROR: HTTP Error 507: Insufficient Storage" (MTPLX)
> "ERROR: Remote end closed connection without response" (llama.cpp Q3_K_XL + DFlash2)

Both servers ran out of memory at large prompt sizes despite different quantization and offloading configurations. ^[raw/inbox/2026-09-07.md]

## Recommendation

Accept `65K` context as the stable lockpoint at `10-12 tok/s` on this hardware, and plan for a `64GB+` Mac upgrade for the `131K / 10+ tok/s` target.

## Related
- [[topics-wiki/hermes-agent/wiki/decisions/131k-on-32gb-feasibility-decision-2026-09-07|131K on 32GB Feasibility Decision — 2026-09-07]]
- [[topics-wiki/hermes-agent/wiki/decisions/stable-context-lock-2026-09-07|Stable Context Lock — 2026-09-07]]
- [[topics-wiki/hermes-agent/wiki/entities/session-20260907-030601|Session Check — 20260907_030601_6012ee]]
- [[topics-wiki/hermes-agent/wiki/entities/model-check-20260903|Model Check — 20260903_001447_7bc70a]]
