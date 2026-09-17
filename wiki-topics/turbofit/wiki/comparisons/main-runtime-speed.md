---
title: Main Runtime Speed Comparison
created: 2026-09-07
updated: 2026-09-07
type: comparison
tags: [comparison, decision, preference, pain]
sources: [raw/inbox/2026-09-07.md, raw/inbox/2026-09-07-from-music.md, raw/inbox/2026-09-06.md]
confidence: medium
---

# Main Runtime Speed Comparison

Evidence-observed main-runtime candidates for Qwen 3.8 27B-class workloads on this 32 GB M1 Mac. Numbers are in-session measurements against downloaded/observed artifacts, not all confirmed live Hermes routes ^[raw/inbox/2026-09-07.md, raw/inbox/2026-09-07-from-music.md, raw/inbox/2026-09-06.md].

|| Runtime / setup | Short context | Long context / 131K | Failure mode |
|-----------------|--------------|---------------------|--------------|
|| MTPLX `Youssofal/Qwen3.8-27B-MTPLX-Optimized-Speed` | 7–12 tok/s | 0.6–1.0 tok/s at 5K+, 131K `OVERCOMMITTED` | exit `-9`, `prefill_admission_shed`, cache clear, swap |
|| Unleashed Q3_K_XL + DFlash2 | 5–6 tok/s | ~5 tok/s at 131K | Metal `Insufficient Memory`, port conflicts, draft flag mismatches |
|| Unleashed IQ3_XXS + DFlash2 | not measured | failed to load | `tensor ... not within the file bounds` |
|| Ornith-1.5-35B-A3B MLX 4-bit | 28.5 tok/s | ~0.5 tok/s | drops sharply with KV growth; no stable 131K path on 32GB |
|| Dirk Q3_K_XL | not measured | 131K deferred | 13 GB + 8 GB KV = OOM on 32GB before benchmark ^[raw/inbox/2026-09-07.md] |
|| Tiel-Coder Q4_K_XL | not measured | 131K deferred | 22 GB + 8 GB KV = OOM on 32GB before benchmark ^[raw/inbox/2026-09-07.md] |
|| Nail Q4_K_XL | not measured | 131K deferred | 20.8 GB + 8 GB KV = OOM on 32GB before benchmark ^[raw/inbox/2026-09-07.md] |
|| Maple MLX via `deepgrove-ai` | aux only | aux only | deleted from box after memory pressure |
|| Nous free tier | works | works | zero local memory pressure; not a main local runtime |

## Honest ceiling

On this hardware, 10+ tok/s at 131K with a 27B-class load is not achievable without more RAM. A more useful target is a split policy: fastest short-context local runtime for daily work, plus a stable long-context fallback that stays resident ^[raw/inbox/2026-09-07.md].

## Related

- [[wiki-topics/turbofit/wiki/entities/mplx.md|MPLX]]
- [[wiki-topics/turbofit/wiki/entities/unleashed-27b|Unleashed 27B]]
- [[wiki-topics/turbofit/wiki/entities/ornith-35b|Ornith 35B A3B]]
- [[wiki-topics/turbofit/wiki/entities/dflash2-draft|DFlash2 Draft]]
- [[wiki-topics/turbofit/wiki/queries/apple-silicon-runtime-benchmark|Apple Silicon Runtime Benchmark]]
- [[wiki-topics/turbofit/wiki/comparisons/aux-runtime-options|Aux Runtime Options]]
