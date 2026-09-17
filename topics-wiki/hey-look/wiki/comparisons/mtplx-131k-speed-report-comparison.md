---
title: MTPLX 131K Speed Report Comparison
created: 2026-09-06
updated: 2026-09-07
type: comparison
tags: [benchmark, comparison, mtplx, speed, mac, qwen]
sources: [raw/inbox/2026-09-06.md, raw/inbox/2026-09-07.md]
confidence: medium
contested: true
---

# MTPLX 131K Speed Report Comparison

This page keeps the competing 131K figures on record, because Hermes later contradicted its own earlier benchmark while testing a larger prompt.^[raw/inbox/2026-09-06.md]

## Reported measurements

- 14-19 tok/s decode, 46 tok/s prefill at 131K with `--no-ssd-session-cache`.^[raw/inbox/2026-09-06.md]
- 8.2 tok/s at 131K when testing with a larger 131K prompt.^[raw/inbox/2026-09-06.md]
- 5000-prompt test took 158s, described as reasoning mode burning the budget before a larger meaningful prompt could be used.^[raw/inbox/2026-09-06.md]

## New observations — 2026-09-07

Hermes deleted Maple and Unleashed, then checked logs for a 5020-token prompt and observed `remaining: 60526` for a 5020-token prompt — implying an effective 65K usable window rather than 131K. This remains unresolved.
- 8.7 tok/s was reported at 131K after cleanup, but only for prompts under 5K tokens in the observed session; large prompts OOMed.^[raw/inbox/2026-09-07.md]
- 10.6 tok/s was reported at 65K with reasoning off; an earlier 16-token reading was explicitly called unrepresentative.^[raw/inbox/2026-09-07.md]
- Clean 65K figures from the same raw slice: 8.55 tok/s for 685 tokens and 8.43 tok/s for 5010 prompt tokens with cache shedding; an override run returned 9.43 tok/s for 1015 prompt tokens.^[raw/inbox/2026-09-07.md]
- Chris explicitly overrode `MTPLX_SESSION_BANK_MAX_BYTES` and `MTPLX_SESSION_BANK_PER_SESSION_BYTES`; MTPLX warmed the model in 2.7s and reached 14.55 tok/s during prewarm, with background warmup completing in 67.398s and exposing a local chat UI and OpenAI-compatible API.^[raw/inbox/2026-09-07.md]
- A second override run warmed in 3.5s at 14.54 tok/s prewarm and produced 9.43 tok/s on a 1015-token prompt.^[raw/inbox/2026-09-07.md]
- MTPLX's own memory plan showed 19.3GB weights + ~8GB KV at 131K = 27.3GB against a 24GB engine budget, making 131K overcommitted on this hardware.^[raw/inbox/2026-09-07.md]
- A 5010-token prompt logged `remaining: 60526`, implying an effective ~65K usable window; Chris defined the retest protocol as short 500 tokens, medium 5K prompt/100 tokens, and long generation 1000 tokens on port-mapped servers.^[raw/inbox/2026-09-07.md]
- The raw item records that 10+ tok/s at 131K on this M1 32GB box is impossible because 27B + KV + macOS + Hermes totals 22-36GB against 32GB total; the M5 Max README 58 tok/s used a faster memory bus with almost nothing else running.^[raw/inbox/2026-09-07.md]
- With `--paged-kv-quantization q8 --allow-swap`, 131K became stable for non-OOM operation at reduced speed: 6.9 tok/s on a 35-token prompt/800-token generation and 0.6 tok/s on a 5K prompt/100-token generation.^[raw/inbox/2026-09-07.md]
- The same raw slice also records the hardware bound for 131K: 10+ tok/s at 131K on this M1 32GB box is impossible for the Qwen 3.8 27B family because 27B + KV + macOS + Hermes totals 22-36GB against 32GB total, and the M5 Max README 58 tok/s used a faster memory bus with almost nothing else running.^[raw/inbox/2026-09-07.md]

## Why it matters

These numbers suggest the measurement method materially changes the reported speed at long context. For Chris's goal of knowing whether the chosen MTPLX path is fast enough at 131K, the current state is contested: there is not yet one stable benchmark.^[raw/inbox/2026-09-06.md] Hermes later resumed testing speed and large-prompt behavior at 131K, but no stable figure was produced in the next turn either.^[raw/inbox/2026-09-07.md] The q8/swap path changed the operating envelope again and should be treated as a separate sub-path rather than proof that 131K is stable at prior speed levels.^[raw/inbox/2026-09-07.md]

## Dispute handling

These figures conflict, so they are not merged into a single claim. Retain both with the 8.2 tok/s result as the later/large-prompt measurement, and flag the page `contested: true` until a single retest protocol is chosen.^[raw/inbox/2026-09-06.md]

## Related

- [[queries/mtplx-131k-benchmark-request|MTPLX 131K benchmark request]]
- [[entities/qwen-27b-mtplx-optimized-speed|Qwen 27B MTPLX Optimized Speed]]
- [[decisions/prefer-mtplx-over-unleashed|Prefer MTPLX over Unleashed]]
- [[comparisons/mtplx-65k-vs-131k|MTPLX 65K vs 131K]]
- [[queries/mtplx-131k-vs-unleashed-dflash2|MTPLX 131K vs Unleashed + DFlash2]]
- [[entities/ornith-135b-mlx-35b-moe|Ornith-1.5-35B-A3B MLX 4-bit]]
- [[comparisons/131k-engine-survey-32gb-mac|131K engine survey — M1 32GB Mac]]