---
title: Dirk Qwen 3.8 27B GGUF
created: 2026-09-07
updated: 2026-09-07
type: entity
tags: [model, tool, plan, preference]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
---

# Dirk Qwen 3.8 27B GGUF

Chris requested Dirk GGUF downloads for local comparison. The actual repo is `peculiar-ragdoll/Dirk-Qwen3.8-27B-GGUF` because MTP is a model capability, not a repo suffix ^[raw/inbox/2026-09-07.md].

## Requested artifacts

- `Dirk-Qwen3.8-27B-UD-Q3_K_XL.gguf` (~12.24 GB) downloaded to `~/Models/storage/dirk-gguf/` and verified on disk ^[raw/inbox/2026-09-07.md].
- `Dirk-Qwen3.8-27B-GGUF-MTP` repo lookup returned 404 before the correction ^[raw/inbox/2026-09-07.md].

## Status

- Q3_K_XL downloaded; no speed evidence yet. 131K benchmark was deferred because larger candidates OOM on this box before Dirk was exercised.
- Chris wants GGUF vs MLX compared for each candidate, with a preference for Q3 when near base quality ^[raw/inbox/2026-09-07.md].

## Related

- [[dirk-gguf|Dirk GGUF Q3_K_XL]]
- [[candidate-quant-preference|Candidate Quant Preference]]
- [[apple-silicon-runtime-benchmark|Apple Silicon Runtime Benchmark]]
- [[unleashed-27b|Unleashed 27B]]
