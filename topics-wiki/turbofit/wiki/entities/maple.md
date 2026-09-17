---
title: Maple
created: 2026-09-06
updated: 2026-09-06
type: entity
tags: [tool, model, pain, decision]
sources: [raw/inbox/2026-09-06.md]
confidence: high
---

# Maple

Maple-Preview is the auxiliary model Chris wants for Hermes compression and text aux tasks. It is a custom-architecture MoE model with no native support in stock llama.cpp and no vision projector ^[raw/inbox/2026-09-06.md].

## Artifacts on disk

- `~/Models/storage/gguf/Maple-Preview/maple-mlx` — deepgrove MLX download.
- `~/Models/storage/gguf/Maple-Preview/maple-tq2_0.gguf` — 5.4 GB, crashes on Metal warmup.
- `~/Models/storage/gguf/Maple-Preview/maple-q2_0.gguf` — tensor read failure under fork.
- `~/Models/storage/gguf/Maple-Preview/maple-f16.gguf` — 40.4 GB, completed download ^[raw/inbox/2026-09-06.md].

## Runtime compatibility

- **llama.cpp / GGUF**: incompatible. The `stamsam/llama.cpp` fork lacks Metal kernels for TQ2_0 and tensor layout mismatches for Q2_0. Final failure: `kernel_mul_mm_id_tq2_0_f32` missing in Metal compile pipeline.
- **MLX**: working via `deepgrove-ai/mlx-lm-deepgrove` with `--flash-head --trust-remote-code`.
- **Server mode**: unstable with prompt-cache growth; OOM after a handful of requests on 32 GB.
- **Generate mode**: stable for 100–5000 token prompts and tested to 130K tokens in 103 s without OOM ^[raw/inbox/2026-09-06.md].

## Performance

- ~62 tok/s warm.
- 130K compression workload completed in 103 s on this hardware.
- Uses ~7 GB at rest ^[raw/inbox/2026-09-06.md].

## Related

- [[topics-wiki/turbofit/wiki/entities/turbofit.md|TurboFit]]
- [[topics-wiki/turbofit/wiki/entities/mplx.md|MPLX]]
- [[topics-wiki/turbofit/wiki/decisions/aux-model-selection.md|Aux Model Selection]]
- [[topics-wiki/turbofit/wiki/concepts/compression-timeouts.md|Compression Timeouts]]
