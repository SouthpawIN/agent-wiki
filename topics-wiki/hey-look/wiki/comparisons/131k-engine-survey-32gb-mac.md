---
title: 131K engine survey — M1 32GB Mac
created: 2026-09-07
updated: 2026-09-07
type: comparison
tags: [benchmark, comparison, mtplx, unleashed, mlx, mac, qwen, moe, context]
sources: [raw/inbox/2026-09-07.md]
confidence: high
contested: false
---

# 131K engine survey — M1 32GB Mac

A same-day same-box survey of local-serving paths at 131K context on the M1 MacBook with 32GB RAM.^[raw/inbox/2026-09-07.md]

## Constraint summary

- 10+ tok/s at 131K on this M1 32GB box is considered impossible for the Qwen 3.8 27B family under the surveyed configurations. The same raw slice records that 27B model + KV + macOS + Hermes needs 22-36GB against 32GB total, and that the M5 Max README 58 tok/s used a faster memory bus with almost nothing else running.^[raw/inbox/2026-09-07.md] The only path to materially higher throughput is a 64GB+ RAM machine. This survey replaces earlier single-engine estimates with a same-day same-box evidence set, and adds Ornith as a short-context alternative.
- Chris's port-mapped protocol for the comparison used port 11613 for MTPLX and port 11606 for Unleashed + DFlash2, with explicit prompt shapes: short prompt 500 tokens, medium 5K prompt/100 tokens, long generation 1000 tokens.^[raw/inbox/2026-09-07.md]

## Port-mapped test protocol

Chris defined an explicit test protocol for the same-day comparison:
- Port 11613 = MTPLX Qwen 3.8 27B optimized speed
- Port 11606 = Unleashed + DFlash2
- Test shapes: short prompt 500 tokens, medium 5K prompt/100 tokens, long generation 1000 tokens^[raw/inbox/2026-09-07.md]

## Qwen 3.8 27B family

|| Engine | Total model RAM | Short prompt speed | Medium prompt speed | Stability | Notes ||
||--------|-----------------|-------------------|---------------------|-----------|-------||
|| MTPLX | ~20 GB | 6.9 tok/s | 0.6 tok/s | Stable with q8/swap | Base Qwen; slightly faster short prompt; heavier RAM use. Port 11613.^[raw/inbox/2026-09-07.md] ||
|| Unleashed + DFlash2 | ~13 GB | 6.0 tok/s | 0.8 tok/s | Stable with q8_0 | Uncensored/abliterated; leaves more RAM headroom. Port 11606.^[raw/inbox/2026-09-07.md] |

## Alternative model families

|| Engine / model | Disk footprint | Short prompt speed | Long-context behavior | Availability ||
||----------------|----------------|-------------------|-----------------------|--------------||
|| Ornith-1.5-35B-A3B MLX 4-bit | ~18 GB | 28.5 tok/s initial, 15.6 tok/s later short prompt, 5.7 tok/s 5K | 131K OOM with q8_0; reduced GPU layers explored but not confirmed as a stable fix. Warmup 68.2s on later test. | DFlash2 draft available: `jzinno/Ornith-1.5-35B-A3B-DFlash2`. Tested on port 11620.^[raw/inbox/2026-09-07.md] ||

## Other surveyed paths

- llama.cpp + DFlash2: reported ~5 tok/s at 131K.^[raw/inbox/2026-09-07.md]
- MTPLX (MTP): ~7 tok/s short prompts, OOM on a 507-token long generation.^[raw/inbox/2026-09-07.md]
- MLX deepgrove: OOM at 131K on this box.^[raw/inbox/2026-09-07.md]
- FreeToken: NVIDIA only, MoE only — not applicable.^[raw/inbox/2026-09-07.md]
- OMLX: estimated ~6 tok/s at 131K.^[raw/inbox/2026-09-07.md]
- Ornith-1.5-35B-A3B through llama.cpp + DFlash2: proposed as a possible hybrid (short-prompt speed + better large-context KV behavior); not tested.^[raw/inbox/2026-09-07.md]

## Why it matters

This survey replaces earlier single-engine estimates with a same-day same-box evidence set. It adds Ornith-1.5-35B-A3B as a short-context alternative that is materially faster than the 27B paths but OOMs at 131K in MLX server mode on this hardware. It also preserves the negative results so future hardware upgrades can be measured against the same protocol.^[raw/inbox/2026-09-07.md]

## Related

- [[entities/qwen-27b-mtplx-optimized-speed|Qwen 27B MTPLX Optimized Speed]]
- [[entities/unleashed-dflash2-131k-path|Unleashed + DFlash2 131K Path]]
- [[entities/ornith-135b-mlx-35b-moe|Ornith-1.5-35B-A3B MLX 4-bit]]
- [[comparisons/mtplx-65k-vs-131k|MTPLX 65K vs 131K]]
- [[queries/mtplx-131k-vs-unleashed-dflash2|MTPLX 131K vs Unleashed + DFlash2]]
- [[decisions/qwen-27b-32g-mac-operating-mode|Qwen 27B 32GB Mac operating mode]]