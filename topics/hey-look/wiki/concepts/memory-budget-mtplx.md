---
title: MTPLX Memory Budget
created: 2026-09-06
updated: 2026-09-06
type: concept
tags: [mac, mtplx, memory, qwen, inference]
sources: [raw/inbox/2026-09-06.md]
confidence: medium
---

# MTPLX Memory Budget

A memory-control concept that emerged late in the raw record when Hermes corrected its throughput assumption and looked for a MTPLX-specific sizing control.^[raw/inbox/2026-09-06.md]

## What was learned

- Hermes initially misapplied memory math around the model's README peak-memory claim, then corrected it by rereading the README's claim that peak memory is 23.6 GB for 262K context on a 32GB Mac.^[raw/inbox/2026-09-06.md]
- Hermes then found a MTPLX-specific control, `--memory-budget`, intended to size KV-cache and allocator behavior against a total RAM envelope.^[raw/inbox/2026-09-06.md]
- The correction moved the project off an incorrect throughput assumption and onto a MTPLX-native sizing control.^[raw/inbox/2026-09-06.md]

## Why it matters

If MTPLX is meant to be the main serving path on a 32GB Mac, the memory-budget flag is one of the knobs that determines whether 131K or 262K actually stays within Chris's hardware.^[raw/inbox/2026-09-06.md]

## Related

- [[entities/qwen-27b-mtplx-optimized-speed|Qwen 27B MTPLX Optimized Speed]]
- [[decisions/mtplx-session-budget-override|MTPLX session budget override]]
- [[concepts/mtplx|MTPLX]]
- [[queries/mtplx-131k-benchmark-request|MTPLX 131K benchmark request]]
