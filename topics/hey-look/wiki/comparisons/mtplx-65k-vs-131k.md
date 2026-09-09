---
title: MTPLX 65K vs 131K
created: 2026-09-07
updated: 2026-09-07
type: comparison
tags: [benchmark, comparison, mtplx, speed, mac, qwen, context]
sources: [raw/inbox/2026-09-07.md]
confidence: high
contested: false
---

# MTPLX 65K vs 131K

This comparison uses the same box and model from the same raw slice to separate proven 65K results from the still-contested 131K results.^[raw/inbox/2026-09-07.md]

## 65K — proven usable

|| Prompt size | Speed | Stability | Notes ||
||-------------|-------|-----------|-------||
|| 16 tokens | 10.6 tok/s | Unrepresentative | Hermes later rejected it as too small.^[raw/inbox/2026-09-07.md] ||
|| 685 tokens | 8.55 tok/s | Stable | First clean large-prompt measurement.^[raw/inbox/2026-09-07.md] ||
||| 1015 tokens | 9.43 tok/s | Stable | After explicit session-budget override; 100 completion tokens in 29.086s, end-to-end 3.44 tok/s, finish reason `length`.^[raw/inbox/2026-09-07.md] ||
||| 5010 tokens with cache shed | 8.43 tok/s | Stable | Same override run; decoded 8.43 tok/s but generation event was a 10-token `length` finish in 146.043s, so end-to-end dropped to 0.068 tok/s.^[raw/inbox/2026-09-07.md] ||
|| 5010 tokens | 8.43 tok/s | Stable, memory shed | `memory_guard` cleared cache; `active_bytes` 20.3GB, `cache_bytes` 1.5GB, `projected_bytes` 25.0GB, threshold 24.0GB, limit 25.8GB, `cache_cleared: true`, post-clear `projected_bytes_after` 24.0GB; result still completed.^[raw/inbox/2026-09-07.md] ||

## 131K — contested / qualified

|| Prompt | Generation | Speed | Stability | Notes ||
||--------|-----------|-------|-----------|-------||
|| <5K tokens | — | 8.7 tok/s | Unverified | Observed once after cleanup; not a stable large-prompt figure.^[raw/inbox/2026-09-07.md] ||
|| 35 tokens | 800 tokens | 6.9 tok/s | Stable | After `--paged-kv-quantization q8 --allow-swap` with q8 KV cache.^[raw/inbox/2026-09-07.md] ||
|| 5K tokens | 100 tokens | 0.6 tok/s | Stable | Same q8 path; prompt-bound.^[raw/inbox/2026-09-07.md] ||
|| Large prompt | — | OOM | Fails | Without q8/swap; weights + KV overcommit the 24GB engine budget.^[raw/inbox/2026-09-07.md] ||

**Note:** the 8.7 tok/s figure predates the q8/swap path and should not be treated as the final 131K ceiling.^[raw/inbox/2026-09-07.md]

## Memory math

- 65K: ~4GB KV + 19.3GB weights ≈ 23.3GB — fits in 24GB engine budget.^[raw/inbox/2026-09-07.md]
- 131K: ~8GB KV + 19.3GB weights ≈ 27.3GB — overcommitted by ~3GB against the engine budget without q8/swap.^[raw/inbox/2026-09-07.md]
- With `--paged-kv-quantization q8`, the 131K KV cache drops from ~8GB to ~4GB, making stable non-OOM operation possible at reduced speed.^[raw/inbox/2026-09-07.md]

## Why it matters

This comparison shows why the same box cannot fairly present 131K and 65K speeds as equivalent options without a larger-RAM machine. The earlier benchmark confusion came from 65K-speed numbers being reported as if they were 131K-speed numbers and from the 58 tok/s README claim, which used a faster memory bus and empty memory loadout.^[raw/inbox/2026-09-07.md]

## Related

- [[concepts/mtplx-65k-stable-benchmark|MTPLX 65K Stable Benchmark]]
- [[concepts/mtplx-131k-memory-overcommit|MTPLX 131K Memory Overcommit]]
- [[concepts/mtplx-65k-effective-context-cap|MTPLX 65K Effective Context Cap]]
- [[comparisons/mtplx-131k-speed-report-comparison|MTPLX 131K Speed Report Comparison]]
- [[entities/qwen-27b-mtplx-optimized-speed|Qwen 27B MTPLX Optimized Speed]]
- [[decisions/qwen-27b-32g-mac-operating-mode|Qwen 27B 32GB Mac operating mode]]