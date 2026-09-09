---
title: Qwen 27B 32GB Mac operating mode
created: 2026-09-07
updated: 2026-09-07
type: decision
tags: [decision, mtplx, mac, qwen, context, hardware, ornith]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---

# Qwen 27B 32GB Mac operating mode

Hermes presented three paths after logging `remaining: 60526` for a 5020-token prompt and obtaining 8.7 tok/s at 131K.^[raw/inbox/2026-09-07.md]

## What was decided

No final decision was recorded in the raw slice. The explicit options were:

1. Run MTPLX at 65K context — described as fast and stable, no OOM observed.
2. Keep saving for a Mac with 64GB+ RAM to run 131K+ properly.
3. The third option was left blank in the raw item.^[raw/inbox/2026-09-07.md]

## Ornith as a fourth context (from later same-day evidence)

The same raw slice adds a long-context alternative family: Ornith-1.5-35B-A3B MLX 4-bit tested on this 32GB Mac, reaching 28.5 tok/s on short prompts but dropping to ~0.4 tok/s at 60K context and OOM'ing at 131K with q8_0 KV cache, with Hermes exploring reduced GPU layers as a mitigation.^[raw/inbox/2026-09-07.md] This reframes the short/medium/long-context split rather than adding a clean 131K option.^[raw/inbox/2026-09-07.md]

## Current status on 2026-09-07
^[raw/inbox/2026-09-07.md]
- 8.7 tok/s at 131K was recorded after cleanup, but only under prompts shorter than 5K tokens; large prompts OOMed.^[raw/inbox/2026-09-07.md]
- 10.6 tok/s was reported at 65K with reasoning off; an earlier 16-token result was explicitly called unrepresentative.^[raw/inbox/2026-09-07.md]
- A larger-prompt retest at 65K produced 8.55 tok/s for 685 tokens and 8.43 tok/s for 5010 prompt tokens with cache shedding.^[raw/inbox/2026-09-07.md]
- Hermes presented three options for current operation: use the stable 65K path on this box; save for a 64GB+ Mac; or leave the third option blank pending Chris.^[raw/inbox/2026-09-07.md]
- MTPLX's memory plan showed 131K is overcommitted against the 24GB engine budget on this hardware, so choosing 65K is effectively choosing within hardware limits rather than choosing a slower mode.^[raw/inbox/2026-09-07.md]
- On the same day, Chris explicitly overrode `MTPLX_SESSION_BANK_MAX_BYTES` and `MTPLX_SESSION_BANK_PER_SESSION_BYTES` with size strings like `12G` or `12GiB`; MTPLX then warmed and exposed a local chat UI and OpenAI-compatible API.^[raw/inbox/2026-09-07.md]
- After q8/swap testing, 131K became non-OOM at reduced speed: 6.9 tok/s on a 35-token prompt/800-token generation and 0.6 tok/s on a 5K prompt/100-token generation.^[raw/inbox/2026-09-07.md]
- Chris defined the test protocol as short prompt 500 tokens, medium 5K prompt/100 tokens, long generation 1000 tokens; port 11613 = MTPLX, port 11606 = Unleashed + DFlash2.^[raw/inbox/2026-09-07.md] |
|- The same-day same-box survey also recorded Ornith-1.5-35B-A3B MLX 4-bit as a faster short-context path, but it OOM'd at 131K and dropped to ~0.4 tok/s at 60K in MLX server mode.^[raw/inbox/2026-09-07.md] |
|- A direct inference event from the q8/swap path produced 14.037647 tok/s decode and 3.438079 tok/s end-to-end for a 1015-token prompt/100-completion-token run; finish reason was `length`.^[raw/inbox/2026-09-07.md] |
|- The raw item records 10+ tok/s at 131K on this M1 32GB box as impossible for the Qwen 3.8 27B family, because 27B + KV + macOS + Hermes totals 22-36GB against 32GB total, while the M5 Max README 58 tok/s used a faster memory bus with almost nothing else running.^[raw/inbox/2026-09-07.md] |
|- A final Hermes turn recommended keeping prompts under ~2K tokens if 131K must be used, otherwise reducing context to 65K.^[raw/inbox/2026-09-07.md] |
- The same-day comparison showed Unleashed + DFlash2 at ~13GB total RAM versus MTPLX ~20GB, with Unleashed faster on medium prompts, uncensored/abliterated, and leaving more RAM headroom.^[raw/inbox/2026-09-07.md]
- Hermes also surveyed other 131K paths on this M1 32GB Mac and concluded 10+ tok/s at 131K is impossible for the Qwen 3.8 27B family on this hardware; the only path to higher throughput is a 64GB+ Mac.^[raw/inbox/2026-09-07.md]

## Next state

Open; still awaiting Chris's choice among the three options, including the currently blank third option, and whether to treat q8/swap as the preferred 131K path or accept lower throughput.^[raw/inbox/2026-09-07.md]

## Related

- [[entities/ornith-135b-mlx-35b-moe|Ornith-1.5-35B-A3B MLX 4-bit]]
- [[entities/qwen-27b-mtplx-optimized-speed|Qwen 27B MTPLX Optimized Speed]]
- [[decisions/prefer-mtplx-over-unleashed|Prefer MTPLX over Unleashed]]
- [[decisions/mtplx-session-budget-override|MTPLX session budget override]]
- [[comparisons/131k-engine-survey-32gb-mac|131K engine survey — M1 32GB Mac]]
- [[comparisons/mtplx-65k-vs-131k|MTPLX 65K vs 131K]]
- [[comparisons/mtplx-131k-speed-report-comparison|MTPLX 131K Speed Report Comparison]]
- [[queries/mtplx-131k-systematic-retest|MTPLX 131K systematic retest]]
- [[queries/mtplx-131k-vs-unleashed-dflash2|MTPLX 131K vs Unleashed + DFlash2]]
- [[concepts/mtplx-q8-kv-cache-swap|q8 KV cache + swap]]
