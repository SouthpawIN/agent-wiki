---
title: MTPLX 65K Stable Benchmark
created: 2026-09-07
updated: 2026-09-07
type: concept
tags: [benchmark, mtplx, mac, context, qwen, hardware]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
---

# MTPLX 65K Stable Benchmark

This is the first repeated, same-context measurement from 2026-09-07 showing 65K as the stable operating window for Qwen 3.8 27B on a 32GB Mac.^[raw/inbox/2026-09-07.md]

## Observed figures

- 8.55 tok/s for 685 tokens at 65K context.^[raw/inbox/2026-09-07.md]
||- 8.43 tok/s generation for a 5010-token prompt with a 146.043s elapsed and a 10-completion-token `length` finish; decode tok/s 9.427712, end-to-end tok/s 0.068473.^[raw/inbox/2026-09-07.md] |
||- A second override run produced 9.43 tok/s for 100 completion tokens with a 1015-token prompt; elapsed 29.086011s, decode tok/s 14.037647, end-to-end tok/s 3.438079.^[raw/inbox/2026-09-07.md] |
- 65K stability was maintained for at least 42 minutes in one session before a larger-prompt recheck.^[raw/inbox/2026-09-07.md]
- A 16-token measurement from the same day was explicitly called unrepresentative; 10.6 tok/s with reasoning off was later reported before the larger-prompt 8.55 tok/s measurement locked the figure.^[raw/inbox/2026-09-07.md]
- A separate warmup run reached 14.55 tok/s at 512 context and 16.73 tok/s at 2560 context in 67.398s.^[raw/inbox/2026-09-07.md]

## Memory behavior during larger prompts

||- A 5010-token prompt triggered `memory_guard` `prefill_admission_shed`: `active_bytes` 20,477,462,598, `cache_bytes` 1,506,450,444, `projected_bytes` 25,533,473,874, `threshold_bytes` 24,996,709,662, `limit_bytes` 25,769,803,776, with `cache_cleared: true` and post-clear `projected_bytes_after_cache_clear` 24,027,023,430.^[raw/inbox/2026-09-07.md] |
||- A 1015-token prompt returned 100 completion tokens in 29.086011s, decode tok/s 14.037647, end-to-end tok/s 3.438079; finish reason `length`.^[raw/inbox/2026-09-07.md]

## Why it matters

This measurement makes 65K the only currently proven usable large-prompt context on the 32GB Mac. It also explains why the 131K figure was so variable: 65K-speed numbers were sometimes reported as if they were 131K-speed numbers. See [[comparisons/mtplx-65k-vs-131k|MTPLX 65K vs 131K]], [[comparisons/mtplx-131k-speed-report-comparison|MTPLX 131K Speed Report Comparison]], and [[entities/qwen-27b-mtplx-optimized-speed|Qwen 27B MTPLX Optimized Speed]].

## Related

- [[concepts/mtplx-65k-effective-context-cap|MTPLX 65K Effective Context Cap]]
- [[concepts/mtplx-q8-kv-cache-swap|q8 KV cache + swap]]
- [[decisions/mtplx-session-budget-override|MTPLX session budget override]]
- [[decisions/qwen-27b-32g-mac-operating-mode|Qwen 27B 32GB Mac operating mode]]
- [[queries/mtplx-131k-systematic-retest|MTPLX 131K systematic retest]]
