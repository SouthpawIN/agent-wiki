---
title: DFlash2 MTPLX Incompatibility
created: 2026-09-07
updated: 2026-09-07
type: concept
tags: [concept, incompatibility, dflash2, mplx, cuda, apple-silicon]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---

# DFlash2 MTPLX Incompatibility

## The Incompatibility

DFlash2 draft models are incompatible with MTPLX's native MLX MTP heads. This is a fundamental architecture mismatch.

From 2026-09-07 02:20:

> "DFlash2 is not available for MTPLX. `z-lab/Qwen3.8-27B-DFlash2` exists on HuggingFace but is a CUDA-only diffusion draft model for llama.cpp/vLLM/sglang — incompatible with MTPLX's native MLX MTP heads."

## Technical Details

| Aspect | DFlash2 | MTPLX |
|--------|---------|-------|
| **Target runtime** | CUDA (llama.cpp/vLLM/sglang) | Apple Silicon MLX |
| **Draft architecture** | Diffusion-based speculative decoding | Native MTP (Machine-specific Parallelization Transfer) heads |
| **Hardware support** | NVIDIA GPU only | Apple Silicon Metal |

## Evidence of Failure

Multiple DFlash2-related commands failed:

1. **MTPLX rejection**:
   ```
   mtplx serve --model ... --memory-budget 32GB
   mtplx: error: unrecognized arguments: --memory-budget 32GB
   ```

2. **DFlash2 fork flag incompatibilities** (for llama.cpp):
   ```
   error: invalid argument: --draft-model
   error: invalid argument: --draft-ngl
   error: invalid argument: --draft-ctx-size
   error: invalid argument: --low-vram
   ```

3. **DFlash2 cannot load with MTPLX**:
   ```
   RuntimeError: [METAL] Command buffer execution failed: Insufficient Memory
   ```

## Model Sizes

From 2026-09-07 01:27:

| Model | Size |
|-------|------|
| Unleashed Q3_K_XL | 12.31 GB |
| DFlash2 Q4_K_M (draft) | 1.06 GB |

With q8 KV cache at 131K: ~17 GB total fits in 32GB, but DFlash2 cannot be paired with MTPLX.

## Workarounds

1. **Use MTPLX standalone** - Fast at 65K context (7-12 tok/s), but not with DFlash2
2. **Use Unleashed + DFlash2** - via llama.cpp fork at 131K (~5 tok/s)
3. **Use Ornith MLX** - MoE architecture with native speculative decoding

## Why This Matters

The incompatibility explains why:
- MTPLX at 131K OOMed or crashed when users tried to add DFlash2
- The "memory budget" flag didn't work as expected
- Long-context inference without cloud fallback required choosing between incompatible options

## Related

- [[dflash2-arg-failures|DFlash2 Arg Failures]]
- [[mtplx-service-arg-validation|MPLX Service Arg Validation]]
- [[dflash2-draft|DFlash2 Draft]]
- [[dflash2-compat-boundary|DFlash2 Compatibility Boundary]]