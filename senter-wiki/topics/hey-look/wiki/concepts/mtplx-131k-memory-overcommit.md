---
title: MTPLX 131K Memory Overcommit
created: 2026-09-07
updated: 2026-09-07
type: concept
tags: [mtplx, mac, context, qwen, hardware, benchmark]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---

# MTPLX 131K Memory Overcommit

Hermes derived this explanation directly from MTPLX's own memory plan after Chris set explicit session-budget overrides: 19.3GB weights + ~8GB KV cache at 131K = 27.3GB, while MTPLX budgets only ~24GB for the engine.^[raw/inbox/2026-09-07.md]

## Observed math

- 65K context: ~4GB KV cache, total ~23.3GB — fits the 24GB budget.^[raw/inbox/2026-09-07.md]
- 131K context: ~8GB KV cache, total ~27.3GB — overcommitted by ~3GB against the engine budget.^[raw/inbox/2026-09-07.md]
- With `--paged-kv-quantization q8`, the 131K KV cache drops to ~4GB, which makes stable non-OOM operation possible at reduced speed.^[raw/inbox/2026-09-07.md]
- A same-day survey noted llama.cpp + DFlash2 around ~5 tok/s at 131K, MLX deepgrove OOM, FreeToken inapplicable, and OMLX around ~6 tok/s estimated.^[raw/inbox/2026-09-07.md]

## Behavior

When overcommitted without q8/swap, MTPLX tries cache shedding and swap, which matches the OOM failures observed on large prompts at 131K.^[raw/inbox/2026-09-07.md] A 5010-token prompt under the second explicit override produced 8.43 tok/s generation; the active memory path was `active_bytes` 20.3GB, `cache_bytes` 1.5GB, `projected_bytes` 25.0GB, threshold 24.0GB, limit 25.8GB, with `cache_cleared: true` and cache reset to 0 after clearing.^[raw/inbox/2026-09-07.md] A same-day survey also noted llama.cpp + DFlash2 around ~5 tok/s at 131K, MLX deepgrove OOM, FreeToken inapplicable, and OMLX around ~6 tok/s estimated.^[raw/inbox/2026-09-07.md]

## Why it matters

This moves the 131K question from "maybe a config bug" to "known memory overcommit unless hardware changes or q8/swap is used". It also explains why the M5 Max README figure of 58 tok/s is not relevant here: that benchmark used nothing else running and a faster memory bus, while this box has 32GB total and already hits the budget with KV.^[raw/inbox/2026-09-07.md]

## Related

- [[concepts/mtplx-65k-stable-benchmark|MTPLX 65K Stable Benchmark]]
- [[concepts/mtplx-65k-effective-context-cap|MTPLX 65K Effective Context Cap]]
- [[concepts/mtplx-q8-kv-cache-swap|q8 KV cache + swap]]
- [[concepts/mtplx-memory-guard-admission-shed|MTPLX memory_guard prefill_admission_shed]]
- [[decisions/mtplx-session-budget-override|MTPLX session budget override]]
- [[entities/qwen-27b-mtplx-optimized-speed|Qwen 27B MTPLX Optimized Speed]]
- [[comparisons/mtplx-65k-vs-131k|MTPLX 65K vs 131K]]