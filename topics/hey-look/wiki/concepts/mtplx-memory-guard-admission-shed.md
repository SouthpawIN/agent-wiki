---
title: MTPLX memory_guard prefill_admission_shed
created: 2026-09-07
updated: 2026-09-07
type: concept
tags: [mtplx, mac, memory, context, benchmark, qwen]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---

# MTPLX memory_guard prefill_admission_shed

An exact memory-pressure event recorded during a 65K-context test on the 32GB Mac, showing that large prompts can trip MTPLX's admission shedder before generation begins.^[raw/inbox/2026-09-07.md]

## Recorded event

||- Prompt size: 5010 tokens
- Effective prompt length measured: 685 tokens generated before cache clearing; separate override run logged a 5010-token prompt with cached prefill after clearing.^[raw/inbox/2026-09-07.md]
- Observed action: `prefill_admission_shed`
- `active_bytes`: 20,477,462,598
- `cache_bytes`: 1,506,450,444
- `projected_bytes`: 25,533,473,874
- `threshold_bytes`: 24,996,709,662
- `limit_bytes`: 25,769,803,776
- `cache_cleared`: true
- `projected_bytes_after_cache_clear`: 24,027,023,430
- `active_bytes_after`: 20,477,462,598
- `cache_bytes_after`: 0

## Observed result after shedding

||- Generation event: `mtplx_openai_generation`
- Prompt tokens: 5010
- Completion tokens: 10
- max_tokens / effective_max_tokens: 10
- Finish reason: `length`
- Elapsed: 146.043496s
- Decode tok/s: 9.427712
- End-to-end tok/s: 0.068473
- Attempts: 1, blank retries: 0
||- A second override run logged a 1015-token prompt/100-completion-token generation with elapsed 29.086011s, decode tok/s 14.037647, and end-to-end tok/s 3.438079; finish reason `length`.^[raw/inbox/2026-09-07.md]
|- A second override run also recorded that 10+ tok/s at 131K on this M1 32GB box is impossible because 27B + KV + macOS + Hermes totals 22-36GB against 32GB total, and the M5 Max README 58 tok/s used a faster memory bus with almost nothing else running.^[raw/inbox/2026-09-07.md]

## Why it matters

This is not an OOM failure; it is a successful generation after cache clearing, which means speed numbers at large prompt sizes must include the admission-shed path. A 5010-token 65K prompt still completed, but the end-to-end speed dropped to 3.44 tok/s, far below the smaller-prompt 8-12 tok/s range.^[raw/inbox/2026-09-07.md]

## Related

- [[concepts/mtplx-65k-stable-benchmark|MTPLX 65K Stable Benchmark]]
- [[concepts/mtplx-131k-memory-overcommit|MTPLX 131K Memory Overcommit]]
- [[comparisons/mtplx-65k-vs-131k|MTPLX 65K vs 131K]]
- [[decisions/qwen-27b-32g-mac-operating-mode|Qwen 27B 32GB Mac operating mode]]
- [[entities/qwen-27b-mtplx-optimized-speed|Qwen 27B MTPLX Optimized Speed]]
- [[concepts/mtplx-q8-kv-cache-swap|q8 KV cache + swap]]