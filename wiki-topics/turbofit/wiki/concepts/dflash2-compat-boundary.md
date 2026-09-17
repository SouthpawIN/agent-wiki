---
title: DFlash2 Compatibility Boundary
created: 2026-09-07
updated: 2026-09-07
type: concept
tags: [pain, tool, preference]
sources: [raw/inbox/2026-09-07.md, raw/inbox/2026-09-07-from-music.md]
confidence: medium
---

# DFlash2 Compatibility Boundary

DFlash2 draft models are not interchangeable across runtimes. On this box the boundary is concrete: MTPLX cannot use DFlash2, and Unleashed+DFlash2 only works through the dedicated `dflash2-llama.cpp` fork with a narrow valid flag set ^[raw/inbox/2026-09-07.md, raw/inbox/2026-09-07-from-music.md].

## MTPLX

MTPLX uses native MLX MTP heads. `z-lab/Qwen3.8-27B-DFlash2` is a CUDA/llama.cpp/vLLM/sglang diffusion draft model and is incompatible with MTPLX ^[raw/inbox/2026-09-07.md, raw/inbox/2026-09-07-from-music.md].

## Unleashed+DFlash2

Valid launch requires the `dflash2-llama.cpp` fork runtime at `~/.../runtimes/dflash2-llama.cpp-.../build-metal/bin/llama-server` and the flag `--model-draft` for the draft model path. Invalid flag attempts observed in this session:

- `--draft-ngl`
- `--draft-ctx-size`
- `--low-vram`
- `--draft-model`

These exited with `invalid argument` before binding the server ^[raw/inbox/2026-09-07.md].

## Port conflicts

At least one Unleashed+DFlash2 attempt failed with `couldn't bind HTTP server socket, hostname: 127.0.0.1, port: 11606` because port 11606 was already in use, not because of model incompatibility ^[raw/inbox/2026-09-07.md].

## Broken quant path

`Qwen3.8-27B-Unleashed-UD-IQ3_XXS.gguf` failed to load with `tensor 'blk.2.attn_qkv.weight' data is not within the file bounds` after a DFlash `dflash requires ctx_other to be set` warning. That artifact is not usable as a main model on this fork in current state ^[raw/inbox/2026-09-07.md].

## Related

- [[wiki-topics/turbofit/wiki/entities/dflash2-draft|DFlash2 Draft]]
- [[wiki-topics/turbofit/wiki/entities/unleashed-27b|Unleashed 27B]]
- [[wiki-topics/turbofit/wiki/entities/mplx-metal-load-failure|MPLX Metal Load Failure]]
- [[wiki-topics/turbofit/wiki/decisions/context-sizing|Context Sizing]]
