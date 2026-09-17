---
title: MTPLX 65K Effective Context Cap
created: 2026-09-07
updated: 2026-09-07
type: query
tags: [benchmark, question, mtplx, context, mac, qwen]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
---

# MTPLX 65K Effective Context Cap

Hermes observed `remaining: 60526` for a 5020-token prompt, implying an effective ~65K usable window rather than the configured 131K.^[raw/inbox/2026-09-07.md] This raises the question: is MTPLX enforcing a 65K context limit on this 32GB Mac, or is this a configurable issue?

## What was observed

- With 131K configured, a 5020-token prompt logged `remaining: 60526`.^[raw/inbox/2026-09-07.md]
- This suggests the active KV cache window is closer to 65K tokens than 131K under those conditions.

## Why it matters

This changes how we interpret the 131K benchmark results. If the effective window is 65K, then the 8.7 tok/s and 10.6 tok/s readings are de facto 65K-speed results, not 131K-speed results. The hardware-constraint question shifts to whether a 64GB+ Mac can unlock true 131K throughput.

## Status

Contested: the measurement is derived from a single log line during active testing of both 131K and 65K modes. A controlled retest comparing config settings at both windows is needed to confirm or refute this cap hypothesis.

## Related

- [[concepts/mtplx-65k-effective-context-cap|MTPLX 65K Effective Context Cap]]
- [[concepts/mtplx-131k-memory-overcommit|MTPLX 131K Memory Overcommit]]
- [[decisions/qwen-27b-32g-mac-operating-mode|Qwen 27B 32GB Mac operating mode]]
- [[comparisons/mtplx-65k-vs-131k|MTPLX 65K vs 131K]]