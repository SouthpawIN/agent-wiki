---
title: DeepSeek V4.1 Flash
created: 2026-09-16
updated: 2026-09-16
type: model
tags: [model, moe]
sources:
  - https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash
  - https://deepseekv4guide.org/guides/deepseek-v4-1-flash
  - https://antirez/deepseek-v4.1-flash-gguf
---

# DeepSeek V4.1 Flash

> DeepSeek's 552B backbone MoE with 8B/16B asymmetric activation, 1M context, and FP4 KV cache. Replaces V4 Pro entirely.

## Specifications

- **HuggingFace:** [deepseek-ai/DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- **GGUF (antirez):** [antirez/deepseek-v4.1-flash-gguf](https://huggingface.co/antirez/deepseek-v4.1-flash-gguf)
- **Type:** Multimodal LLM (MoE, Causal Encoder-Decoder)
- **Architecture:** Causal Encoder-Decoder (CED) MoE
- **Backbone Parameters:** 552B
- **Engram Parameters:** 196B (sparsely accessed conditional memory)
- **Total Weights:** ~763B
- **Active params per token:** 8B (prefill) / 16B (decode)
- **Layers:** 40 (20 encoder + 20 decoder)
- **Hidden Size:** 5120
- **MoE Experts:** 1 shared + 384 routed per layer, 6 activated per token
- **Context window:** Up to 1,000,000 tokens (native)
- **Max Output:** 384,000 tokens
- **KV Cache:** 890 bytes/token (FP4 E2M1, ~1/4 of V4 Flash)
- **Precision:** Native FP4 (MoE) + FP8 (attention/norm/router)
- **License:** MIT

## Architecture Details

DeepSeek-V4.1-Flash adopts a **Causal Encoder-Decoder (CED)** architecture — a 40-layer Transformer split into a 20-layer causal encoder and a 20-layer decoder. The decoder's global KV cache is projected from the final encoder hidden states rather than derived from each decoder layer's own hidden states. This asymmetric design halves prefill cost for input-heavy agentic workloads.

Key architectural components:

| Component | Description |
|-----------|-------------|
| **CED** | 20-layer encoder + 20-layer decoder; decoder KV projected from encoder output |
| **CSA2** | Compressed Sparse Attention 2 — Full/Reindex/Reuse modes share KV across layers |
| **Hierarchical Sparse Indexer** | Later indexers restricted to candidate pool from first Full-mode layer |
| **FP4 KV Cache** | E2M1 format, 890 bytes/token, always in HBM |
| **Single-Pass mHC** | Revised residual-stream mixing with Mega-mHC kernel |
| **Engram** | 196B conditional memory across two hash tables (layers 1 and 14) |
| **DSpark** | Semi-autoregressive speculative decoding head |
| **SWA Bounded Replay** | Reconstructs SWA KV from last n_win tokens only, 1/8 persistent KV footprint |

Trained from scratch on 45T multimodal tokens. Sparse attention trained at 64K, context extended to 1M at 34T tokens.

## Benchmarks

> DeepSeek-published scores. Agentic benchmarks use temperature=1.0, top_p=0.95, 1M context.

### Reasoning & Knowledge

| Benchmark | Score |
|-----------|-------|
| GPQA Diamond (Pass@1) | 90.9 |
| MMLU-Pro (EM, 5-shot) | 74.1 |
| AGIEval (EM, 3-5 shot) | 83.4 |
| C-Eval (EM, 5-shot) | 92.1 |
| SuperGPQA (EM, 5-shot) | 53.1 |
| BBH (EM, 3-shot) | 86.1 |
| HellaSwag (EM, 0-shot) | 87.2 |

### Coding & Math

| Benchmark | Score |
|-----------|-------|
| HumanEval (Pass@1, 0-shot) | 79.4 |
| BigCodeBench (Pass@1, 3-shot) | 60.6 |
| GSM8K (EM, 8-shot) | 93.0 |
| MATH (EM, 4-shot) | 61.1 |
| Codeforces (Rating) | 3471 |

### Agentic

| Benchmark | Score |
|-----------|-------|
| DeepSWE v1.1 (Resolved) | 74.2 |
| Terminal-Bench 2.1 (Pass@1) | 90.6 |
| Terminal-Bench 4.0 (Pass@1) | 31.2 |
| CyberGym (Pass@1) | 88.1 |
| SEC-Bench Pro (Pass@1) | 62.8 |
| AutomationBench (Pass@1) | 54.8 |
| Agents' Last Exam (Pass@1) | 31.8 |
| HLE w/ tools (Pass@1) | 63.9 |

## Optimal Quantization by Hardware Tier

### GPU (Dedicated VRAM: 80GB+)

| Quant | Weight Size | VRAM Needed | Notes |
|-------|-------------|-------------|-------|
| **FP8 (native)** | ~160 GB | 192 GB+ | Official DeepSeek deployment; 2x H200 or 2x RTX Pro 6000 |
| **Q4_K** | ~80 GB | 96-128 GB | Single high-VRAM GPU or 2x 4090 offload |
| **UD-Q4_K_XL** | 155 GB | 192 GB+ | Near-lossless (KLD 0.0102), experts bit-exact |

**Optimal:** FP8 native if hardware supports it (H200/B200); otherwise UD-Q4_K_XL at 192GB+.

### Unified (Apple Silicon / Shared Memory)

| Quant | Weight Size | Total Memory | Notes |
|-------|-------------|--------------|-------|
| **Q4 (antirez)** | 483 GB (294 GB main + 189 GB Engram) | 512 GB Mac | Resident on 512GB; SSD streaming on smaller |
| **Q2 (antirez)** | 341 GB (152 GB main + 189 GB Engram) | 128 GB Mac + SSD | SSD streaming on 128GB Macs; resident TP on 2x128GB with RDMA |
| **IQ2_XXS** | ~87 GB | 128 GB | Extreme compression; 30%+ weight rounding |

**Optimal:** Q4 for 512GB Macs (resident); Q2 for 128GB Macs with SSD streaming.

### CPU / Low Memory

| Quant | Weight Size | RAM Needed | Notes |
|-------|-------------|------------|-------|
| **Q2_K_XL** | ~97 GB | 128 GB + swap | Community GGUF; ~15 tok/s on consumer HW |
| **IQ2_XXS** | ~87 GB | 96-128 GB | Lowest usable; high quantization error |

**Optimal:** IQ2_XXS for 128GB-class systems; Q2_K_XL if fidelity matters more than size.

## Context Configuration

KV cache is 890 bytes/token. Memory planning:

| Context | KV Cache | Recommended Config | Use Case |
|---------|----------|-------------------|----------|
| **131K** (~128K) | ~110 MB | Any tier; fits easily | Standard agentic tasks, most workloads |
| **262K** (~256K) | ~220 MB | GPU: any; Unified: Q4+ | Long documents, multi-file repos |
| **1M** | ~850 MB | GPU: FP8/Q4; Unified: 512GB Mac | Full native context; million-token tasks |

### Recommended Runtime Flags

```
./llama-server --model DeepSeek-V4.1-Flash-Q4.gguf \
  --ctx-size 1048576 \
  --n-gpu-layers 999 \
  --flash-attn on \
  --temp 1.0 --top-p 0.95 \
  --reasoning off
```

- **131K:** `--ctx-size 131072` — minimal overhead on all tiers
- **262K:** `--ctx-size 262144` — ensure 16GB+ headroom for KV
- **1M:** `--ctx-size 1048576` — requires 850MB KV + Engram streaming from SSD

## System Availability

| System | Available | Path |
|--------|-----------|------|
| Omarchy | Yes | `/home/sovthpaw/Models/storage/gguf/vcruz305_DeepSeek-V4.1-Flash-GGUF/` |
| MacBook | No | `—` |

## Inference Performance

| Runtime | Platform | tok/s | Notes |
|---------|----------|-------|-------|
| llama.cpp CUDA | Omarchy RTX 3090×2 | — |  |
| llama.cpp Metal | MacBook M1 Pro | — |  |
| MLX | MacBook M1 Pro | — |  |

## Research Notes

- DeepSWE 74.2 and Terminal-Bench 2.1 90.6 place V4.1 Flash ahead of Claude Opus 5 and GPT-5.6 Sol on established agentic benchmarks.
- Terminal-Bench 3.0/4.0 scores (30.0/31.2) are weaker — strength is concentrated in established tasks, not frontier ones.
- GPQA Diamond 90.9 trails GPT-5.6 Sol (94.1) and Opus 5 (93.4).
- Not a "Flash" in the traditional sense — 552B backbone is larger than old V4 Pro (1.6T total but 49B active). The "Flash" label refers to asymmetric activation cost, not total weight.
- Engram (196B) is accessed via SSD streaming, not resident in RAM/VRAM.

## See Also

- [[concepts/benchmark-taxonomy|Benchmark Taxonomy]]
- [[topics/turbofit/wiki/index|Wiki Index]]
