---
title: Maple Preview (20B-A1B)
created: 2026-09-16
updated: 2026-09-16
type: model
tags: [model, moe, ternary, reasoning]
sources: [deepgrove/maple-preview, deepgrove/maple-preview-GGUF, stamsam/maple-preview-gguf]
---

# Maple Preview

> DeepGrove's 20B-A1B ternary-weight reasoning MoE — SOTA reasoning for its weight class, 218 tok/s on M4 Mac mini.

## Specifications

- **HuggingFace:** [deepgrove/maple-preview](https://huggingface.co/deepgrove/maple-preview) · [deepgrove/maple-preview-GGUF](https://huggingface.co/deepgrove/maple-preview-GGUF)
- **License:** MIT
- **Type:** Reasoning LLM (MoE)
- **Total Parameters:** 20.214B
- **Active Parameters per Token:** ~1.0B (20B-A1B)
- **Context Window:** 131,072 tokens (native)
- **Checkpoint Size (BF16):** ~40.4 GB
- **Checkpoint Size (GGUF):** 4.64–5.91 GiB (ternary), 12.33 GB (Q4_K_M)
- **Format:** GGUF, SafeTensors (BF16)
- **Release:** 2026-08-04

## Architecture

| Property | Value |
|----------|-------|
| Layers | 24 |
| Hidden Size | 2048 |
| Attention | GQA — 16 query heads, 4 KV heads, head_dim 128 |
| Attention Pattern | 3:1 hybrid — SWA-512 (sliding window 512) : Global Attention (GA) |
| RoPE | Partial (64/128 dims, theta 10000) on SWA layers; no RoPE on GA layers |
| QK Structure | Flash-head QK — per-head RMSNorm (q_norm/k_norm) on reshaped Q/K before RoPE; k_proj at 512 dims (4 KV heads × 128) |
| MoE | 256 experts, top-8 active |
| MoE Intermediate | 512 |
| MoE Gate | clamp-7 SwiGLU (`silu(min(gate, +7)) * clip(up, -7, +7)`) |
| Router | fp32 softmax + renormalized routing |
| KV Cache | Sliding-window KV cache (window 512) for SWA layers |
| Vocab Size | 151,936 (no weight tying; no bias terms) |
| RMSNorm eps | 1e-6 |
| Weight Format | Per-row-scaled ternary: `W ≈ alpha_row * T`, `T ∈ {-1, 0, +1}` (~39% exact zeros) for experts and q/o projections; k_proj, lm_head, embeddings, router, norms stored denser |

## Inference Performance

| Runtime | Platform | Prefill (pp512) | Decode (tg128) | Config |
|---------|----------|-----------------|----------------|--------|
| llama.cpp (fork) | M5 Pro MacBook Pro, 48GB RAM, CPU-only, 16 threads | 610.48 tok/s | 252.74 tok/s | TQ2_0 + Q4_K head, 5.50 GiB |
| llama.cpp (fork) | M5 Pro MacBook Pro, 48GB RAM, CPU-only, 16 threads | 513.33 tok/s | 231.13 tok/s | TQ1_0 + Q4_K head, 4.64 GiB |
| llama.cpp (fork) | M4 Mac mini, 16GB unified, CPU-only, 8 threads | — | 218 tok/s | TQ2_0 + Q4_K head |
| llama.cpp CUDA (stamsam fork) | NVIDIA H200, all layers GPU-offloaded | — | ~385 tok/s | F16, 40.5 GB |
| llama.cpp CUDA (stamsam fork) | NVIDIA RTX 4000 Ada | ~110 tok/s | ~97 tok/s | TQ2_0, 5.45 GB |
| llama.cpp CUDA (stamsam fork) | Jetson Xavier | — | ~14.8 tok/s | TQ2_0, 5.45 GB |

> **Note:** The official DeepGrove GGUF uses the `deepgrove-ai/llama.cpp` fork. The stamsam fork (`prism` branch) provides additional GPU kernels for `tq2_0` (GGML type 35). Mainline llama.cpp does not support the Maple architecture as of 2026-09-16.

## Benchmarks

> DeepGrove's official evaluation uses the dense output head. The model card states: "this preview is focused primarily on raw reasoning and, as such, may underperform on agentic benchmarks."

### Reasoning & Knowledge

| Benchmark | Score | Source |
|-----------|-------|--------|
| AIME 2026 | 87.5% | DeepGrove model card |
| HMMT 2026 | 78.8% | DeepGrove model card |
| LiveCodeBench v6 | 75.1% | DeepGrove model card |
| GPQA Diamond | 73.5% | DeepGrove model card |
| **Average (4 benchmarks)** | **78.7%** | Calculated |

### Agentic / SWE (Not Tested by DeepGrove)

| Benchmark | Score | Notes |
|-----------|-------|-------|
| TerminalBench v4.0 | — | Not on leaderboard; preview received minimal agentic post-training |
| DeepSWE | — | Not tested by DeepGrove |
| MMLU / MMLU-Pro | — | Not reported in official model card; third-party comparison tables show "—" |

> **Caveat:** DeepGrove's model card benchmark comparison is published as an embedded image (not extractable text), so underlying scores could not be independently verified. The model is competitive with larger models on reasoning tasks (Qwen3.5 35B-A3B, Gemma 4, gpt-oss).

## Optimal Quantization by Hardware Tier

| Tier | Recommended Quant | Size | Rationale |
|------|-------------------|------|-----------|
| **GPU** (13+ GB VRAM) | `maple-q4_k_m.gguf` (stamsam fork) | 12.33 GB | Uniform Q4_K_M, runs on NVIDIA H200 (~385 tok/s); quality-preserving, fits on 16 GB GPUs |
| **GPU** (6–8 GB VRAM) | `maple-tq2_0.gguf` (stamsam fork) | 5.45 GB | Tiered ternary + Q4_0 + F32; runs on RTX 4000 Ada (~97 tok/s), Jetson Xavier (~14.8 tok/s) |
| **CPU** (Apple Silicon / x86) | `maple-preview-TQ2_0-head-Q4_K.gguf` (DeepGrove) | 5.50 GiB | Official DeepGrove GGUF; 252 tok/s decode on M5 Pro (16 threads), 218 tok/s on M4 Mac mini |
| **Unified Memory** (Apple Silicon) | `maple-preview-TQ2_0-head-Q4_K.gguf` (DeepGrove) | 5.50 GiB | Same as CPU tier; entire model fits in unified memory; 218 tok/s on base M4 Mac mini |
| **Minimal CPU** (low RAM) | `maple-preview-TQ1_0-head-Q4_K.gguf` (DeepGrove) | 4.64 GiB | Smallest official GGUF; 231 tok/s decode on M5 Pro (16 threads) |

> **TQ1_0 vs TQ2_0:** TQ2_0 is generally faster but slightly higher memory footprint. TQ1_0 is smaller but slower.

## Runtime Configuration by Context Length

### 131K Context (Native)

- **Status:** Native training context — no scaling needed.
- **Memory:** ~5.5 GiB (TQ2_0 + Q4_K head) to ~12.3 GB (Q4_K_M).
- **Command:**
  ```bash
  ./llama-cli -m maple-preview-TQ2_0-head-Q4_K.gguf \
    -p "<prompt>" -n 512 -t 16 -ngl 999 -dev none \
    -c 131072
  ```
- **Notes:** Entire model fits in 16 GB unified memory on Apple Silicon. KV cache for 131K context adds ~1–2 GiB depending on batch size.

### 262K Context (Extended)

- **Status:** Requires RoPE scaling (model not trained beyond 131K).
- **Memory:** ~5.5 GiB model + ~2–4 GiB KV cache.
- **Quality:** Degraded beyond native context; accuracy on long-range dependencies will decrease.
- **Command:**
  ```bash
  ./llama-cli -m maple-preview-TQ2_0-head-Q4_K.gguf \
    -p "<prompt>" -n 512 -t 16 -ngl 999 -dev none \
    -c 262144 --rope-scaling linear --rope-scale 2
  ```
- **Notes:** Sliding-window attention (SWA-512) mitigates some long-context degradation, but global attention layers have no positional information beyond 131K. Not recommended for critical long-context tasks.

### 1M Context (Extrapolated)

- **Status:** Aggressive RoPE scaling; significant quality degradation expected.
- **Memory:** ~5.5 GiB model + ~8–16 GiB KV cache (depends on `--ctx-size`).
- **Quality:** Substantial degradation; SWA-512 window is only 0.05% of 1M context. Global attention layers rely on RoPE extrapolation which fails at this scale.
- **Command:**
  ```bash
  ./llama-cli -m maple-preview-TQ2_0-head-Q4_K.gguf \
    -p "<prompt>" -n 512 -t 16 -ngl 999 -dev none \
    -c 1048576 --rope-scaling linear --rope-scale 7.63
  ```
- **Notes:** Not recommended. If 1M context is needed, use a model natively trained for it (e.g., Qwen3.8 Max, Claude Fable 5.1). For Maple, stay at or near 131K for reliable results.

## System Availability

| System | Available | Path |
|--------|-----------|------|
| Omarchy | TBD | — |
| MacBook | TBD | — |

## Research Notes

- DeepGrove trained Maple-Preview natively in ternary format from scratch — not a post-hoc quantization. They argue ternary-from-scratch is "fundamentally superior" to post-training quantization.
- The model solves IMO-level math problems (e.g., IMO 2024 Problem 1) at 281.5 tok/s on M5 Pro.
- Runs on base M4 Mac mini (16 GB unified memory) at 218 tok/s — 5–16× faster than comparably-capable dense/MoE models (Gemma 4, Qwen3.5, gpt-oss).
- The official Transformers implementation depends on Triton and FlashAttention (CUDA-only). Apple Silicon performance comes from a separate on-device runtime (likely MLX).
- The 5.31 GB checkpoint is small enough to fit comfortably in RAM on most modern systems.
- Minimal agentic post-training — may underperform on SWE-bench-style tasks.
- No support for vLLM, SGLang, or mainline llama.cpp at release. Requires DeepGrove fork or stamsam fork.

## Aux-model evidence (absorbed from the entity page)

Maple-Preview is the auxiliary model Chris wants for Hermes compression and text aux tasks. It is a custom-architecture MoE model with no native support in stock llama.cpp and no vision projector ^[raw/inbox/2026-09-06.md].

### Artifacts on disk

- `~/Models/storage/gguf/Maple-Preview/maple-mlx` — deepgrove MLX download.
- `~/Models/storage/gguf/Maple-Preview/maple-tq2_0.gguf` — 5.4 GB, crashes on Metal warmup.
- `~/Models/storage/gguf/Maple-Preview/maple-q2_0.gguf` — tensor read failure under fork.
- `~/Models/storage/gguf/Maple-Preview/maple-f16.gguf` — 40.4 GB, completed download ^[raw/inbox/2026-09-06.md].

### Runtime compatibility

- **llama.cpp / GGUF**: incompatible. The `stamsam/llama.cpp` fork lacks Metal kernels for TQ2_0 and tensor layout mismatches for Q2_0. Final failure: `kernel_mul_mm_id_tq2_0_f32` missing in Metal compile pipeline.
- **MLX**: working via `deepgrove-ai/mlx-lm-deepgrove` with `--flash-head --trust-remote-code`.
- **Server mode**: unstable with prompt-cache growth; OOM after a handful of requests on 32 GB.
- **Generate mode**: stable for 100–5000 token prompts and tested to 130K tokens in 103 s without OOM ^[raw/inbox/2026-09-06.md].

### Performance

- ~62 tok/s warm.
- 130K compression workload completed in 103 s on this hardware.
- Uses ~7 GB at rest ^[raw/inbox/2026-09-06.md].

### Related

- [[turbofit|TurboFit]]
- [[mplx|MPLX]]
- [[aux-model-selection|Aux Model Selection]]
- [[compression-timeouts|Compression Timeouts]]


## Unverified 8B artifact note (absorbed 2026-10-28)

> Filed as a separate page ("Maple Preview 8B", `sources: []` — no raw evidence behind it) and merged here so there is one Maple page. Treat the 8B figures below as **unverified**; they conflict with the 20B-A1B figures above.

| Claim | Value |
| --- | --- |
| HuggingFace | `deepgrove/maple-preview-GGUF` |
| Parameters | 8B (claim) |
| Quantization / size | Q4_K_M / 22 GB on disk |
| Omarchy path | `/home/sovthpaw/Models/storage/gguf/deepgrove_maple-preview-GGUF/` |
| Reported speed | 12.4 tok/s (attributed to MLX on Mac in one cell and CUDA on Omarchy in another — internally inconsistent) |
