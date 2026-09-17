---
title: TurboFit
created: 2026-09-06
updated: 2026-09-06
type: entity
tags: [tool, bot, infra, decision]
sources: [raw/inbox/2026-09-06.md]
confidence: high
---

# TurboFit

TurboFit is the adaptive local-inference path for Hermes on this 32 GB M1 Mac. It loads local models first and falls back to cloud providers when compression or context load exceeds what the box can sustain ^[raw/inbox/2026-09-06.md].

## Current topology

- **Main**: Qwen3.8-27B-Unleashed + DFlash2 draft on `127.0.0.1:11606`, Metal, 131k context.
- **Aux / Compression**: Maple MLX on `127.0.0.1:11612`, served with the `deepgrove-ai/mlx-lm-deepgrove` runtime.
- **Vision**: routed to Unleashed; Maple has no projector.
- **Cloud fallback**: Nous free tier when local context exceeds memory/compression limits ^[raw/inbox/2026-09-06.md].

## Runtimes on disk

- `llama.cpp-1c3c9674de4d455f1e571bed808252af54932767` — Unleashed + DFlash2 Metal build.
- `dflash2-llama.cpp-1deefcca395743049c3820ab8f9b15043f3e9446` — DFlash2 fork with Metal build.
- `maple-llama.cpp-9ee03eec62d088a117ab916bbe489e7a3872a21f` — Maple llama.cpp fork from `stamsam/llama.cpp` (CUDA-first).
- `/tmp/mlx-lm-deepgrove` — custom MLX runtime for Maple on Apple Silicon ^[raw/inbox/2026-09-06.md].

## Related

- [[wiki-topics/turbofit/wiki/entities/unleashed-27b.md|Unleashed 27B]]
- [[wiki-topics/turbofit/wiki/entities/maple.md|Maple]]
- [[wiki-topics/turbofit/wiki/entities/dflash2-draft.md|DFlash2 Draft]]
- [[wiki-topics/turbofit/wiki/entities/mplx.md|MPLX]]
