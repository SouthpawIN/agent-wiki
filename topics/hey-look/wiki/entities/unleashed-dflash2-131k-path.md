---
title: Unleashed + DFlash2 131K Path
created: 2026-09-07
updated: 2026-09-07
type: entity
tags: [model, mac, qwen, dflash2, unleashed, speculative-decoding]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
---

# Unleashed + DFlash2 131K Path

An alternate Apple Silicon path tested head-to-head with MTPLX on 2026-09-07, running on port 11606 during Chris's specified retest protocol.^[raw/inbox/2026-09-07.md]

- Model file size: ~12.31 GB.^[raw/inbox/2026-09-07.md]
- DFlash2 draft model: ~1.06 GB.^[raw/inbox/2026-09-07.md]
- Total model RAM footprint: ~13 GB.^[raw/inbox/2026-09-07.md]
- KV cache type: q8_0.^[raw/inbox/2026-09-07.md]
- Censorship status: uncensored / abliterated.^[raw/inbox/2026-09-07.md]
- Stability: reported stable at 131K on the same 32GB Mac with q8 KV cache.^[raw/inbox/2026-09-07.md]
- Port: 11606 during the port-mapped 2026-09-07 comparison.^[raw/inbox/2026-09-07.md]

## Observed 131K figures

|| Test | Speed |
||------|-------|
|| Short prompt, ~1K tokens | 6.0 tok/s |
|| 5K prompt, 100 tokens | 0.8 tok/s |
|| Stability | Stable |

## Raw-chain evidence

Hermes recorded multiple near-duplicate comparison tables on 2026-09-07; the key stable figures are 6.0 tok/s short and 0.8 tok/s medium.^[raw/inbox/2026-09-07.md]

## Additional test paths and constraints

- Maple was deleted and then re-added during testing, but was removed again for the final head-to-head; the deletion was re-applied after comparison testing completed.^[raw/inbox/2026-09-07.md]
- The port-mapped test protocol specified port 11606 for Unleashed + DFlash2 and port 11613 for MTPLX during the 2026-09-07 comparison.^[raw/inbox/2026-09-07.md]
- A 5000-token warmup in reasoning mode was observed to take 158s before meaningful speed measurements could begin, so warmup cost is now a tracked factor in retest design.^[raw/inbox/2026-09-07.md]

## Why it matters

This is the smaller-RAM alternative Chris asked Hermes to research for the base Qwen 3.8 27B family. Same-day same-box comparison showed it leaves more RAM headroom than MTPLX, is faster on medium prompts, and is uncensored; the raw item records 10+ tok/s at 131K on this M1 32GB box as impossible for either path.^[raw/inbox/2026-09-07.md] The unresolved part of Chris's original request is whether a DFlash2 speculative decoder exists for the base MTPLX Qwen model path; that HuggingFace search outcome is not confirmed in the raw slice.^[raw/inbox/2026-09-07.md]

## Related

- [[queries/mtplx-131k-vs-unleashed-dflash2|MTPLX 131K vs Unleashed + DFlash2]]
- [[decisions/prefer-mtplx-over-unleashed|Prefer MTPLX over Unleashed]]
- [[decisions/qwen-27b-32g-mac-operating-mode|Qwen 27B 32GB Mac operating mode]]
- [[comparisons/mtplx-65k-vs-131k|MTPLX 65K vs 131K]]
- [[entities/qwen-27b-mtplx-optimized-speed|Qwen 27B MTPLX Optimized Speed]]
