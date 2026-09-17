---
title: MTPLX
created: 2026-09-06
updated: 2026-09-07
type: concept
tags: [model-serving, mac, huggingface, mtplx, speculative-decoding]
sources: [raw/inbox/2026-09-06.md, raw/inbox/2026-09-07.md]
confidence: high
---

# MTPLX

A serving/setup path Hermes used while installing and testing the Qwen 27B model Chris asked about.^[raw/inbox/2026-09-06.md]

## What was done

- MTPLX was installed.
- The Qwen 27B model was downloaded through MTPLX.
- A first MTPLX run failed near completion at 19G/20.4G, then completed after restart.
- MTPLX was brought up with MTP depth 3.
- Speed was tested after server start.
- Maple and Unleashed were deleted, leaving MTPLX as the main local serving path on this box.^[raw/inbox/2026-09-07.md]

## Current operating understanding

On 2026-09-07, Hermes noted:

- MTPLX at 65K context was stable, fast, and fit within memory on the 32GB Mac.^[raw/inbox/2026-09-07.md]
- MTPLX at 131K worked only for short prompts under 5K tokens in observed conditions, and large prompts OOMed.^[raw/inbox/2026-09-07.md]
- A 5020-token prompt logged `remaining: 60526`, suggesting an effective 65K usable window rather than 131K.^[raw/inbox/2026-09-07.md]
- Chris defined the explicit test protocol as: short prompt 500 tokens, medium 5K prompt/100 tokens, and long generation 1000 tokens.^[raw/inbox/2026-09-07.md]
- On a 5010-token 65K prompt, `memory_guard` logged `prefill_admission_shed` with `active_bytes` 20.3GB, `cache_bytes` 1.5GB, `projected_bytes` 25.0GB, threshold 24.0GB, limit 25.8GB, `cache_cleared: true`, post-clear `projected_bytes_after` 24.0GB.^[raw/inbox/2026-09-07.md]
- A 1015-token 65K prompt returned 9.43 tok/s for 100 completion tokens in 29.086s; end-to-end speed 3.44 tok/s, finish reason `length`.^[raw/inbox/2026-09-07.md]
- MTPLX's own memory plan showed 19.3GB weights + ~8GB KV at 131K = 27.3GB, against a 24GB engine budget, making 131K overcommitted on this box.^[raw/inbox/2026-09-07.md]
- At 65K, ~4GB KV keeps total use near 23.3GB and avoids the overcommit path.^[raw/inbox/2026-09-07.md]
- Chris later explicitly overrode `MTPLX_SESSION_BANK_MAX_BYTES` and `MTPLX_SESSION_BANK_PER_SESSION_BYTES`, so the budget is now actively tunable rather than only a README-derived observation.^[raw/inbox/2026-09-07.md]
- Stable 65K operation now has a reachable chat UI and OpenAI-compatible API exposed on this box.^[raw/inbox/2026-09-07.md]
- The README M5 Max claim of 58 tok/s was explained as from a different machine with a faster memory bus and idle memory; it should not be treated as a target for this 32GB Mac.^[raw/inbox/2026-09-07.md]
- `--paged-kv-quantization q8 --allow-swap` made 131K stable for non-OOM operation at reduced speed: 6.9 tok/s on a 35-token prompt/800-token generation, and 0.6 tok/s on a 5K prompt/100-token generation.^[raw/inbox/2026-09-07.md]
- A same-day head-to-head with Unleashed + DFlash2 showed MTPLX slightly faster on short prompts but Unleashed faster on medium prompts and using less RAM; Unleashed was also noted as uncensored/abliterated.^[raw/inbox/2026-09-07.md]

## Integration touchpoints

Hermes mentioned updating auxiliary compression to use MTPLX and adding it to a model catalog. This suggests MTPLX is intended to be part of a local model catalog or compression pipeline, not just a one-off test.^[raw/inbox/2026-09-06.md]

## Related

- [[entities/qwen-27b-mtplx-optimized-speed|Qwen 27B MTPLX Optimized Speed]]
- [[concepts/mt-speculative-decoding|MTP speculative decoding]]
- [[concepts/mtplx-q8-kv-cache-swap|q8 KV cache + swap]]
- [[decisions/prefer-mtplx-over-unleashed|Prefer MTPLX over Unleashed]]
- [[decisions/qwen-27b-32g-mac-operating-mode|Qwen 27B 32GB Mac operating mode]]
- [[decisions/mtplx-session-budget-override|MTPLX session budget override]]
- [[queries/mtplx-131k-benchmark-request|MTPLX 131K benchmark request]]
- [[queries/mtplx-131k-systematic-retest|MTPLX 131K systematic retest]]
- [[queries/mtplx-131k-vs-unleashed-dflash2|MTPLX 131K vs Unleashed + DFlash2]]
- [[queries/mtplx-65k-effective-context-cap|MTPLX 65K Effective Context Cap]]
