---
title: DFlash2 Fork Flag Boundary
created: 2026-09-07
updated: 2026-09-07
type: concept
tags:
  - turbofit
  - dflash2
  - llama-cpp
  - compatibility
  - pain
sources:
  - raw/inbox/2026-09-07.md
  - raw/inbox/2026-09-07-from-senter-wiki.md
confidence: high
---

# DFlash2 Fork Flag Boundary

DFlash2 draft models are not interchangeable across runtimes. On this box the boundary is concrete: MTPLX cannot use DFlash2, and Unleashed+DFlash2 only works through the dedicated `dflash2-llama.cpp` fork with a narrow valid flag set.

## MTPLX Incompatibility

MTPLX uses native MLX MTP heads. `z-lab/Qwen3.8-27B-DFlash2` is a CUDA-only diffusion-based draft model for llama.cpp/vLLM/sglang — incompatible with MTPLX's native MLX MTP heads.

**Key insight**: The DFlash2 draft path cannot be used with Ornith MLX because MLX uses native speculative decoding architectures, while DFlash2 is a llama.cpp/vLLM feature.

## Unleashed+DFlash2 Flag Requirements

Valid launch flags for the `dflash2-llama.cpp` fork:

```bash
llama-server -m <main-model> \
  --spec-draft-model <draft-model>.gguf \
  --spec-draft-ngl 999 \
  --spec-draft-n-max 7 \
  --spec-type draft-dflash
```

**Invalid flags** that failed before binding (from `raw/inbox/2026-09-07.md`):

| Flag | Status |
|------|--------|
| `--draft-model` | invalid argument |
| `--draft-ngl` | invalid argument |
| `--draft-ctx-size` | invalid argument |
| `--low-vram` | invalid argument |
| `--model-draft` | invalid argument |

## Port conflict evidence

At least one Unleashed+DFlash2 attempt failed with:

```
couldn't bind HTTP server socket, hostname: 127.0.0.1, port: 11606
```

Because port 11606 was already in use, not because of model incompatibility.

## Broken quant path

`Qwen3.8-27B-Unleashed-UD-IQ3_XXS.gguf` failed to load with:

```
tensor 'blk.2.attn_qkv.weight' data is not within the file bounds, model is corrupted or incomplete
```

After a DFlash warning: `dflash requires ctx_other to be set`. That artifact is not usable as a main model on this fork.

## Recommendation

- **Use Ornith MLX 4-bit** as primary local provider (fastest at short context)
- **Use Unleashed Q3_K_XL + DFlash2** as long-context fallback (stable ~5 tok/s)
- **Do not attempt DFlash2 with MTPLX** — architecture incompatibility is fundamental

## Related

- [[topics-wiki/turbofit/wiki/entities/dflash2-draft.md|DFlash2 Draft]]
- [[topics-wiki/turbofit/wiki/entities/unleashed-27b.md|Unleashed 27B]]
- [[topics-wiki/turbofit/wiki/entities/ornith-35b-dflash2.md|Ornith 35B DFlash2]]
- [[topics-wiki/turbofit/wiki/entities/ornith-1-5-35b-a3b-mlx-4-bit.md|Ornith 1.5 35B-A3B MLX 4-bit]]