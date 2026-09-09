---
title: MTPLX 131K benchmark request
created: 2026-09-06
updated: 2026-09-07
type: query
tags: [benchmark, mtplx, speed, question]
sources: [raw/inbox/2026-09-06.md, raw/inbox/2026-09-07.md]
confidence: high
---

# MTPLX 131K benchmark request

Chris asked for the speed of the MTPLX-backed Qwen 27B setup at about 131K tokens, after an initial faster figure was reported at a shorter context.^[raw/inbox/2026-09-06.md]

## Request chain

- Chris first asked for speed at 131K if it is lower than the number already reported.^[raw/inbox/2026-09-06.md]
- He then clarified that he wants the speed-optimized MTPLX build he already selected, not Unleashed.^[raw/inbox/2026-09-06.md]
- He wants to remove Unleashed if it is slower or adds confusion.^[raw/inbox/2026-09-06.md]
- On 2026-09-07, Chris asked for a head-to-head test of MTPLX vs Unleashed + DFlash2 at 131K on the 32GB Mac, including q8/swap and a HuggingFace search for DFlash2 availability for the base Qwen 3.8 27B model.^[raw/inbox/2026-09-07.md] He specified short prompt 500 tokens, medium 5K prompt/100 tokens, and long generation 1000 tokens, with port 11613 for MTPLX and port 11606 for Unleashed + DFlash2.^[raw/inbox/2026-09-07.md]

## What was measured

- After fixing context-flag issues and bringing MTPLX up with 262K context, Hermes tested at 131K with `--no-ssd-session-cache`.^[raw/inbox/2026-09-06.md]
- Reported figures from the raw record: 14-19 tok/s decode, 46 tok/s prefill.^[raw/inbox/2026-09-06.md]
- Later, at 131K, Hermes reported 8.2 tok/s while testing with a large 131K prompt.^[raw/inbox/2026-09-06.md]
- 8.7 tok/s at 131K was reported after cleanup, but only for prompts under 5K tokens.^[raw/inbox/2026-09-07.md]
- With `--paged-kv-quantization q8 --allow-swap`, 131K became stable for smaller/medium prompts: 6.9 tok/s on a 35-token prompt/800-token generation and 0.6 tok/s on a 5K prompt/100-token generation.^[raw/inbox/2026-09-07.md]
- Head-to-head with Unleashed + DFlash2: MTPLX 6.9 tok/s vs 6.0 tok/s on short prompts, and 0.6 tok/s vs 0.8 tok/s on medium prompts.^[raw/inbox/2026-09-07.md]

## Status

There is a 131K result on record, but the reported figures are not consistent in the raw item, and a larger-prompt retest was in progress.^[raw/inbox/2026-09-06.md] This remains an open measurement rather than a stable benchmark. On 2026-09-07, Chris explicitly overrode `MTPLX_SESSION_BANK_MAX_BYTES` and `MTPLX_SESSION_BANK_PER_SESSION_BYTES`, which changed the active configuration but did not produce a stable large-prompt 131K measurement until the q8/swap path restored non-OOM behavior at lower speed.^[raw/inbox/2026-09-07.md]

## Related

- [[queries/mtplx-131k-vs-unleashed-dflash2|MTPLX 131K vs Unleashed + DFlash2]]
- [[comparisons/mtplx-131k-speed-report-comparison|MTPLX 131K Speed Report Comparison]]
- [[entities/qwen-27b-mtplx-optimized-speed|Qwen 27B MTPLX Optimized Speed]]
- [[decisions/prefer-mtplx-over-unleashed|Prefer MTPLX over Unleashed]]
- [[decisions/qwen-27b-32g-mac-operating-mode|Qwen 27B 32GB Mac operating mode]]
- [[decisions/mtplx-session-budget-override|MTPLX session budget override]]
- [[concepts/mtplx-65k-stable-benchmark|MTPLX 65K Stable Benchmark]]
- [[concepts/mtplx-131k-memory-overcommit|MTPLX 131K Memory Overcommit]]
- [[concepts/mtplx-q8-kv-cache-swap|q8 KV cache + swap]]
- [[queries/mtplx-131k-systematic-retest|MTPLX 131K systematic retest]]
- [[comparisons/mtplx-65k-vs-131k|MTPLX 65K vs 131K]]
