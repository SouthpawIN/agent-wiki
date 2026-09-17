---
title: Qwen 27B MTPLX Optimized Speed
created: 2026-09-06
updated: 2026-09-07
type: entity
tags: [model, huggingface, mac, mtplx, qwen]
sources: [raw/inbox/2026-09-06.md, raw/inbox/2026-09-07.md]
confidence: high
---

# Qwen 27B MTPLX Optimized Speed

A Hugging Face model Chris asked about because it is advertised as specifically for Macs with 32 GB of RAM and up.^[raw/inbox/2026-09-06.md]

## Known facts

- Model size: ~20.4 GB.^[raw/inbox/2026-09-07.md]
- Peak memory on run: ~23.6 GB.^[raw/inbox/2026-09-06.md]
- Reported context: up to 262K tokens.^[raw/inbox/2026-09-06.md]
- Hardware target: Macs 32 GB and up.^[raw/inbox/2026-09-06.md]
- Hermes README-reported speed: 58 tok/s on an M5 Max under ideal conditions.^[raw/inbox/2026-09-06.md]^[raw/inbox/2026-09-07.md]

## Observed figures

- 8.7 tok/s at 131K was reported after cleanup on 2026-09-07, but only for prompts under 5K tokens in the observed session.^[raw/inbox/2026-09-07.md]
- A 5020-token prompt logged `remaining: 60526`, suggesting an effective 65K usable window under those conditions.^[raw/inbox/2026-09-07.md]
- 10.6 tok/s at 65K with reasoning off was reported on 2026-09-07, but that was from a 16-token prompt Hermes later called unrepresentative.^[raw/inbox/2026-09-07.md]
- After Chris explicitly overrode `MTPLX_SESSION_BANK_MAX_BYTES` and `MTPLX_SESSION_BANK_PER_SESSION_BYTES`, MTPLX warmed the model in 2.7s and reached 14.55 tok/s during prewarm; background warmup completed in 67.398s and exposed a local chat UI and OpenAI-compatible API.^[raw/inbox/2026-09-07.md]
- A clean large-prompt measurement at 65K returned 8.55 tok/s for 685 tokens; a separate 5010-token measurement returned 8.43 tok/s with cache shedding enabled.^[raw/inbox/2026-09-07.md]
- An override run with 1015 prompt tokens returned 9.43 tok/s for 100 completion tokens in 29.086s; end-to-end speed 3.44 tok/s.^[raw/inbox/2026-09-07.md]
- With `--paged-kv-quantization q8 --allow-swap`, 131K became stable for non-OOM operation at reduced speed: 6.9 tok/s on a 35-token prompt/800-token generation and 0.6 tok/s on a 5K prompt/100-token generation.^[raw/inbox/2026-09-07.md]
|- A 5010-token prompt under the second explicit override produced 8.43 tok/s generation; the active memory path was `active_bytes` 20.3GB, `cache_bytes` 1.5GB, `projected_bytes` 25.0GB, threshold 24.0GB, limit 25.8GB, with `cache_cleared: true` and cache reset to 0 after clearing.^[raw/inbox/2026-09-07.md]
|- A 1015-token prompt on the same override run returned 9.43 tok/s for 100 completion tokens in 29.086s; end-to-end speed was 3.44 tok/s, finish reason `length`.^[raw/inbox/2026-09-07.md]
|- The raw item records that 10+ tok/s at 131K on this M1 32GB box is impossible because 27B model + KV + macOS + Hermes needs 22-36GB against 32GB total, and the M5 Max README figure of 58 tok/s used a faster memory bus with almost nothing else running.^[raw/inbox/2026-09-07.md]
|- In the same raw slice, Hermes surveyed other 131K paths on this M1 32GB Mac and concluded 10+ tok/s at 131K is impossible for the Qwen 3.8 27B family on this hardware; the only path to materially higher throughput is a 64GB+ Mac.^[raw/inbox/2026-09-07.md]
|- Chris explicitly defined the test protocol as: short prompt 500 tokens, medium 5K prompt/100 tokens, long generation 1000 tokens; port 11613 was MTPLX with Qwen 3.8 27B MTPLX Optimized Speed, port 11606 was Unleashed + DFlash2.^[raw/inbox/2026-09-07.md]

## Why it matters

This is Chris's direct lookup request. Speed at the upper context length is still unresolved because later runs showed prompt-shape sensitivity, a possible 65K effective ceiling under observed conditions, and a new q8/swap path that changes the operating envelope again. See [[decisions/context-benchmark-request|Context benchmark request]], [[decisions/mtplx-session-budget-override|MTPLX session budget override]], [[decisions/qwen-27b-32g-mac-operating-mode|Qwen 27B 32GB Mac operating mode]], [[concepts/mtplx-65k-effective-context-cap|MTPLX 65K Effective Context Cap]], and [[concepts/mtplx-q8-kv-cache-swap|q8 KV cache + swap]].

## Related

- [[concepts/mtplx|MTPLX]]
- [[concepts/mt-speculative-decoding|MTP speculative decoding]]
- [[decisions/prefer-mtplx-over-unleashed|Prefer MTPLX over Unleashed]]
- [[decisions/mtplx-session-budget-override|MTPLX session budget override]]
- [[decisions/qwen-27b-32g-mac-operating-mode|Qwen 27B 32GB Mac operating mode]]
- [[comparisons/mtplx-65k-vs-131k|MTPLX 65K vs 131K]]
- [[comparisons/mtplx-131k-speed-report-comparison|MTPLX 131K Speed Report Comparison]]
- [[queries/mtplx-131k-systematic-retest|MTPLX 131K systematic retest]]
- [[queries/mtplx-131k-vs-unleashed-dflash2|MTPLX 131K vs Unleashed + DFlash2]]
- [[concepts/mtplx-65k-stable-benchmark|MTPLX 65K Stable Benchmark]]
- [[concepts/mtplx-131k-memory-overcommit|MTPLX 131K Memory Overcommit]]
