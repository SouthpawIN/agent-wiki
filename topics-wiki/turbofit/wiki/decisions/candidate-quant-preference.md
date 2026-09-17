---
title: Candidate Quant Preference
created: 2026-09-07
updated: 2026-09-07
type: decision
tags: [decision, preference, model]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---

# Candidate Quant Preference

**Decision/Preference:** When comparing GGUF vs MLX for new local candidates, prefer the Q3 quant when model pages describe it as near base-model quality.

## Rationale

Chris said: "They also have a lot to say about their quants on their pages too, check GGUF vs MLX, I like the Q3 quant that they said is near base model quality" ^[raw/inbox/2026-09-07.md].

## Applies to

- Dirk: requested as `Dirk-Qwen3.8-27B-UD-Q3_K_XL.gguf` after GGUF repo correction.
- Nail: requested as `Nail-Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf`, but Chris wants GGUF vs MLX compared and would likely favor Q3 if near base quality.
- Tiel-Coder: queued as `Tiel-Coder-35B-A3B-UD-Q4_K_XL.gguf`; a Q3 path should be checked if the HuggingFace page supports it.
- Ornith: MLX 4-bit path was tested; no GGUF quant comparison completed.

## Open

A reusable quant-selection rule for candidate research: if page notes say "near base quality", default to Q3; otherwise compare Q3 vs Q4_K_XL explicitly.

## Related

- [[topics-wiki/turbofit/wiki/entities/dirk-qwen38-27b.md|Dirk Qwen 3.8 27B GGUF]]
- [[topics-wiki/turbofit/wiki/entities/nail-qwen36-35b.md|Nail Qwen 3.6 35B UD Q4_K_XL]]
- [[topics-wiki/turbofit/wiki/entities/tiel-coder.md|Tiel Coder]]
- [[topics-wiki/turbofit/wiki/entities/ornith-35b-mlx.md|Ornith 35B MLX]]
- [[topics-wiki/turbofit/wiki/queries/apple-silicon-runtime-benchmark|Apple Silicon Runtime Benchmark]]
