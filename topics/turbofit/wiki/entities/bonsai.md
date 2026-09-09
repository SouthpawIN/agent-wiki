---
title: Bonsai MLX
created: 2026-09-07
updated: 2026-09-07
type: entity
tags: [model, tool, candidate]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
contested: true
---

# Bonsai MLX

## What this is

Bonsai refers to models from `prism-ml`: `Bonsai-27B-mlx-1bit` (1-bit binary, 1.4M downloads) and `Ternary-Bonsai-27B-mlx-2bit` (2-bit ternary, 1.4M downloads). The Ternary 2-bit variant at 7.91 GB was downloaded to `~/Models/storage/bonsai-mlx/` for testing on the M1 32GB box ^[raw/inbox/2026-09-07.md].

A separate GGUF variant also exists but requires llama.cpp, not MLX.

## Status

- **Ternary Bonsai MLX 2-bit** — downloaded (7.91 GB), files intact, but server failed to start because `/bonsai-mlx/config.json` was missing ^[raw/inbox/2026-09-07.md]. The process exited with `FileNotFoundError` on `config.json`.
- **Bonsai MLX 1-bit** — downloaded from prism-ml but was "not the right variant" per Hermes assessment ^[raw/inbox/2026-09-07.md].
- **Bonsai GGUF** — requires llama.cpp runtime, incompatible with the active MLX turbofit engine.

## Chris's directive

Chris explicitly said "Don't worry about bonsai" — his priority was getting Ornith up as the main provider so he could continue working. Bonsai was deprioritized twice: at 2026-09-07 13:18 and again at 13:30, both times stating "It just needs to be configured into turbofit so I can continue with Ornith" ^[raw/inbox/2026-09-07.md].

## Memory fit

At 7.91 GB, Ternary Bonsai would fit within the 32 GB memory budget, but no verified speed tests were completed before Chris redirected focus to Ornith ^[raw/inbox/2026-09-07.md].

## Related

- [[topics/turbofit/wiki/entities/ornith-1-5-35b-a3b-mlx-4-bit|Ornith 1.5 35B-A3B MLX 4-bit]]
- [[topics/turbofit/wiki/queries/engine-research-request|Engine Research Request]]
- [[topics/turbofit/wiki/decisions/local-main-provider|TurboFit Local Main Provider Decision]]
