---
title: "2026-09-07 Candidate Narrowing"
created: 2026-09-07
updated: 2026-09-07
type: comparison
tags: [model, inference, benchmark, decision, turbofit, apple-silicon]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
---

# 2026-09-07 Candidate Narrowing

Chris narrowed the benchmark sweep from an open engine sweep for Qwen 3.8 27B to a focused model comparison among Bonsai, Colibri, and Ornith. ^[raw/inbox/2026-09-07.md]

## Shift in scope

- The initial 2026-09-07 05:36 request was open-ended: research all possible Apple Silicon engines for Qwen 3.8 27B and deliver model IDs, commands, and tok/s. ^[raw/inbox/2026-09-07.md]
- At 2026-09-07 08:17, Chris expanded the sweep to include Tiel Coder and Dirk 27B while keeping the warmup requirement. ^[raw/inbox/2026-09-07.md]
- At 2026-09-07 10:37, Chris redirected the effort: "cut Nail, Tiel Coder, and every. 27B besides Bonsai. Bonsai vs Maple Colibri vs Ornith 1.5 35A3B is where I am at." ^[raw/inbox/2026-09-07.md]
- This creates a contested intermediate state: Tiel Coder and Dirk 27B have recorded partial results and specific instructions, but those candidates are now deprioritized. ^[raw/inbox/2026-09-07.md]

## Remaining candidates

- Bonsai: Ternary Bonsai 27B MLX 2-bit, ~7.91 GB; 1.58-bit variant considered likely to "fly" on M1. ^[raw/inbox/2026-09-07.md]
- Colibri: Maple Colibri, ~4.6 GB total. ^[raw/inbox/2026-09-07.md]
- Ornith: Ornith 1.5 35A3B. ^[raw/inbox/2026-09-07.md]

## Test protocol

- Warmup required before every tok/s measurement. ^[raw/inbox/2026-09-07.md]
- Sequence: warmup, short prompt, 5K prompt. ^[raw/inbox/2026-09-07.md]
- Quote: "Run warmup, then short prompt (500 tokens), then 5K prompt (100 tokens). Report tok/s for each." ^[raw/inbox/2026-09-07.md]

## Housekeeping rule

- "Make sure to clear the old model off before testing the new one." ^[raw/inbox/2026-09-07.md]

## Partial results before narrowing

| Model | Context | Short tok/s | 5K tok/s | Notes |
|---|---:|---:|---:|:---|
| Tiel Coder | 65K | 23.1 | 4.2 | Q4 K XL; latest build; now deprioritized. ^[raw/inbox/2026-09-07.md] |
| Dirk 27B | 32K | 6.0 | 0.8 | 13 GB server load; OOM at 131K; now deprioritized. ^[raw/inbox/2026-09-07.md] |

## Related notes
- ACE-Step remains a separate run target, not part of this comparison. ^[raw/inbox/2026-09-07.md]
- A 2026-09-07 task running the finalized protocol was interrupted after 1944.94s with 50 API calls. ^[raw/inbox/2026-09-07.md]

## Links

- [[wiki-topics/try-again/wiki/entities/bonsai-27b|Bonsai 27B]]
- [[wiki-topics/try-again/wiki/entities/colibri|Colibri]]
- [[wiki-topics/try-again/wiki/entities/ornith-1.5-35a3b|Ornith 1.5 35A3B]]
- [[wiki-topics/try-again/wiki/decisions/benchmark-protocol|Benchmark Protocol]]
- [[wiki-topics/try-again/wiki/concepts/local-inference-benchmark-sweep|Local Inference Benchmark Sweep]]
