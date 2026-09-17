---
title: MTPLX 131K vs Unleashed + DFlash2
created: 2026-09-07
updated: 2026-09-07
type: query
tags: [benchmark, comparison, mtplx, unleashed, dflash2, qwen, mac]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
---

# MTPLX 131K vs Unleashed + DFlash2

Chris asked Hermes to research and test MTPLX versus Unleashed + DFlash2 at 131K on the 32GB Mac, and to check HuggingFace for a DFlash2 speculative decoder for the base Qwen 3.8 27B model.^[raw/inbox/2026-09-07.md]

## Request

- Test MTPLX at 131K with `--paged-kv-quantization q8 --allow-swap`.^[raw/inbox/2026-09-07.md]
- Compare head-to-head against Unleashed + DFlash2 running on port 11606.^[raw/inbox/2026-09-07.md]
- Search HuggingFace for `Qwen3.8-27B-DFlash2` or equivalent.^[raw/inbox/2026-09-07.md]
- Run speed tests: short prompt 500 tokens, medium 5K prompt/100 tokens, long generation 1000 tokens.^[raw/inbox/2026-09-07.md]

## Observed results

|| | Unleashed + DFlash2 | MTPLX |
||--|---------------------|-------|
|| Model size | 12.31 GB | 20.4 GB |
|| Draft/MTP | DFlash2 1.06 GB | MTP head |
|| Total model RAM | ~13 GB | ~20 GB |
|| Short prompt, ~1K tokens | 6.0 tok/s | 6.9 tok/s |
|| 5K prompt, 100 tokens | 0.8 tok/s | 0.6 tok/s |
|| Censorship | Uncensored / abliterated | Base Qwen |
|| Stability at 131K | Stable | Stable |
|| Medium-prompt advantage | 0.8 vs 0.6 tok/s | 6.9 vs 6.0 tok/s short |
|| RAM headroom | Leaves more headroom | Uses ~7GB more |

## Additional engine research on Apple Silicon 32GB

Hermes surveyed other local-serving paths for 131K on this hardware in the same raw slice:^[raw/inbox/2026-09-07.md]

- llama.cpp + DFlash2: reported ~5 tok/s at 131K.^[raw/inbox/2026-09-07.md]
- MTPLX (MTP): ~7 tok/s short prompts, OOM on a 507-token long generation.^[raw/inbox/2026-09-07.md]
- MLX deepgrove: OOM at 131K on this box.^[raw/inbox/2026-09-07.md]
- FreeToken: NVIDIA only, MoE only — not applicable.^[raw/inbox/2026-09-07.md]
- OMLX: estimated ~6 tok/s at 131K.^[raw/inbox/2026-09-07.md]
- Ornith-1.5-35B-A3B MLX 4-bit: achieved 28.5 tok/s on short prompts and 15.6 tok/s on a later 517-token/100-output test, but dropped to ~0.4 tok/s at 60K context and OOM'd at 131K with q8_0 KV cache; reduced GPU layers were explored but not confirmed as a stable fix.^[raw/inbox/2026-09-07.md]

The combined survey was used to argue that 10+ tok/s at 131K on an M1 32GB Mac is currently impossible for the Qwen 3.8 27B family, and that the only path to materially higher throughput is a 64GB+ RAM machine.^[raw/inbox/2026-09-07.md] The survey also recorded direct observations for llama.cpp + DFlash2 around ~5 tok/s, MLX deepgrove OOM, FreeToken as NVIDIA-only/MoE-only, and OMLX around ~6 tok/s estimated.^[raw/inbox/2026-09-07.md]

Ornith through llama.cpp + DFlash2 was proposed as a possible hybrid (short-prompt speed + better large-context KV behavior) but was not tested.^[raw/inbox/2026-09-07.md]

## Status

A same-day same-box comparison is on record, but the raw record does not include the explicit HuggingFace DFlash2 search outcome for the base Qwen model.^[raw/inbox/2026-09-07.md] The result is therefore incomplete: the speed comparison is known (MTPLX 6.9 tok/s vs Unleashed 6.0 tok/s short; 0.6 tok/s vs 0.8 tok/s medium at 131K), the availability of DFlash2 for the base MTPLX model path is not confirmed in the raw slice.^[raw/inbox/2026-09-07.md] A later Hermes turn also proposed testing Ornith-1.5-35B-A3B through llama.cpp + DFlash2 as a hybrid long-context path, but that was not executed.^[raw/inbox/2026-09-07.md]

## Why it matters

This is the first direct evidence that a smaller/uncensored path may be preferable on the 32GB Mac, and that q8/swap makes 131K usable for non-OOM workloads at reduced speed.^[raw/inbox/2026-09-07.md]

## Related

- [[decisions/prefer-mtplx-over-unleashed|Prefer MTPLX over Unleashed]]
- [[decisions/qwen-27b-32g-mac-operating-mode|Qwen 27B 32GB Mac operating mode]]
- [[comparisons/mtplx-131k-speed-report-comparison|MTPLX 131K Speed Report Comparison]]
- [[comparisons/mtplx-65k-vs-131k|MTPLX 65K vs 131K]]
- [[entities/qwen-27b-mtplx-optimized-speed|Qwen 27B MTPLX Optimized Speed]]
- [[entities/ornith-135b-mlx-35b-moe|Ornith-1.5-35B-A3B MLX 4-bit]]
- [[comparisons/131k-engine-survey-32gb-mac|131K engine survey — M1 32GB Mac]]
- [[queries/mtplx-dflash2-base-model-research|MTPLX DFlash2 base model research]]
- [[queries/ornith-llamacpp-long-context-viability|Ornith llama.cpp long-context viability]]