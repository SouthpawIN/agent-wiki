---
title: MTPLX 65K Effective Context Cap
created: 2026-09-07
updated: 2026-09-07
type: concept
tags: [mtplx, mac, context, qwen, hardware, benchmark]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
contested: true
---

# MTPLX 65K Effective Context Cap

A log-derived observation that MTPLX may be enforcing an effective ~65K usable context window on this setup, even though 131K was configured.^[raw/inbox/2026-09-07.md]

## Observation

Hermes checked logs after deleting Maple and Unleashed and observed `remaining: 60526` for a 5020-token prompt.^[raw/inbox/2026-09-07.md] This implies the active window is closer to 65K than 131K under those conditions. The observation is not yet proven to be a hard cap; it could also reflect config, prompt-shape sensitivity, cache settings, or measurement artifact. The same raw slice also records a 5010-token 65K prompt surviving `memory_guard` cache shedding rather than failing outright, which suggests the ceiling is a usable-context/memory-pressure behavior, not a simple max-tokens setting.^[raw/inbox/2026-09-07.md]

## Why it matters

If the current 32GB Mac can only comfortably use 65K, it changes the long-context plan from a benchmarking question into a hardware-choice question. It also means the 8.7 tok/s and 10.6 tok/s readings may be best understood as 65K-speed results rather than 131K-speed results. The same raw slice also surveyed other 131K paths and concluded 10+ tok/s at 131K on this M1 32GB box is impossible for the Qwen 3.8 27B family; the only path to materially higher throughput is a 64GB+ RAM machine.^[raw/inbox/2026-09-07.md]

## Dispute handling

The cap interpretation is contested because the measurement is derived from a single log line and a single prompt, and Hermes was actively testing both 131K and 65K in the same turn. Keep this page `contested: true` until a direct config/retest comparison confirms or refutes the effective cap.

## Related

- [[comparisons/mtplx-131k-speed-report-comparison|MTPLX 131K Speed Report Comparison]]
- [[queries/mtplx-131k-systematic-retest|MTPLX 131K systematic retest]]
- [[queries/mtplx-65k-effective-context-cap|MTPLX effective context ceiling]]
- [[decisions/qwen-27b-32g-mac-operating-mode|Qwen 27B 32GB Mac operating mode]]
- [[entities/qwen-27b-mtplx-optimized-speed|Qwen 27B MTPLX Optimized Speed]]
- [[concepts/mtplx|MTPLX]]