---
title: Context benchmark request
created: 2026-09-06
updated: 2026-09-06
type: decision
tags: [benchmark, context, decision, speed, mtplx]
sources: [raw/inbox/2026-09-06.md]
confidence: high
---

# Context benchmark request

Chris asked for the speed of the Qwen 27B MTPLX setup at ~131K context, after Hermes had already reported 58 tok/s.^[raw/inbox/2026-09-06.md]

## What was decided

No benchmark at 131K was completed in this raw slice; only the request exists.

## Why it matters

If speed drops sharply at longer context, it affects whether this model path is usable for long-context workflows on a 32GB Mac.

## Next state

Open measurement; superseded by [[queries/mtplx-131k-benchmark-request|MTPLX 131K benchmark request]]. The active local configuration now includes Chris's explicit override of `MTPLX_SESSION_BANK_MAX_BYTES` and `MTPLX_SESSION_BANK_PER_SESSION_BYTES`; MTPLX is reachable at a local chat UI and OpenAI-compatible API, but a stable large-prompt 131K measurement is still missing.^[raw/inbox/2026-09-07.md]

## Related

- [[entities/qwen-27b-mtplx-optimized-speed|Qwen 27B MTPLX Optimized Speed]]
- [[queries/mtplx-131k-benchmark-request|MTPLX 131K benchmark request]]
- [[queries/mtplx-131k-systematic-retest|MTPLX 131K systematic retest]]
- [[comparisons/mtplx-131k-speed-report-comparison|MTPLX 131K Speed Report Comparison]]
