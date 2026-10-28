---
title: Qwen 3.8 Flash Next
created: 2026-09-16
updated: 2026-09-16
type: model
tags: [model, moe, qwen4-preview]
sources:
  - https://huggingface.co/Qwen/Qwen3.8-Flash-Next
  - https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF
  - https://github.com/QwenLM/Qwen3.8-Flash-Next
  - https://arxiv.org/html/2608.30320
  - https://gist.github.com/ryan4yin/48617bbddacc7067f10799770b7cc33f
confidence: high
---

# Qwen 3.8 Flash Next (Qwen4 Preview)

> 125B-parameter MoE backbone + 51B n-gram embedding table + 4B MTP head = ~180B total on disk. Only 6B parameters activated per token. Gated DeltaNet + Qwen Sparse Attention hybrid, 512 experts (10 routed + 1 shared active).

## Architecture

| Component | Detail |
|---|---|
| **Total params** | ~180B (125B main + 51B n-gram + 4B MTP) |
| **Activated params** | 6B per token |
| **Hidden dimension** | 2560 |
| **Layers** | 48 |
| **Layer layout** | 12 × [3×(Gated DeltaNet → MoE) → 1×(Qwen Sparse Attention → MoE)] |
| **Attention heads (QSA)** | 24 Q / 2 KV, head dim 256 |
| **Attention heads (GDN)** | 48 V / 16 QK, head dim 128 |
| **QSA indexer** | MQA, 4 query heads + 1 shared key head, budget 512 blocks / 2048 tokens |
| **MoE** | 512 experts, 10 routed + 1 shared active, expert intermediate dim 640 |
| **N-gram embedding** | 20,000,000 bigrams/trigrams at layer 2, 51B params |
| **Gated Residual** | 4 branches, bottleneck rank 320 |
| **MTP** | 1 layer, multi-step trained (native NEXTN speculative decode in SGLang) |
| **Native context** | 262,144 tokens (extensible to 1,000,000 via YaRN) |
| **Training tokens** | ~1/3 of Qwen3.7-Plus (~1/9 training FLOPs) |
| **Optimizer** | Muon (with AdamW for non-2D params) |

## Benchmarks

Qwen-reported scores from HuggingFace model card:

| Benchmark | Score | vs Claude Opus 4.6 |
|---|---|---|
| **DeepSWE 1.1** (agentic coding) | **58.7** | — |
| **SWE-bench Pro** | **62.5** | +9.1 (Opus 53.4) |
| **SWE-bench Multilingual** | **81.0** | +3.5 (Opus 77.5) |
| **GPQA Diamond** | **91.7** | +0.4 (Opus 91.3) |
| **LiveCodeBench v6** | **91.9** | +3.1 (Opus 88.8) |
| **IFBench** (instruction following) | **81.3** | +18.8 (Opus 62.5) |
| **CoWorkBench** (long-horizon office) | **73.9** | +5.7 (Opus 68.2) |
| **JobBench** (professional tasks) | **55.7** | +19.1 (Opus 36.6) |
| **HLE** (GPT-4o judged) | **35.9** | -4.1 (Opus 40.0) |
| **Toolathlon Verified** (Pass@1) | **73.5** | — |
| **NL2Repo-Bench** | 48.1 | +0.5 (Opus 47.6) |
| **Agents' Last Exam** | Pass@1 24.3 / Score 51.2 | — |

**TerminalBench v4.0**: Not in published leaderboard (Sep 2026). Benchmark dominated by GPT-6 Astra (58.2%), Claude Fable 5.1 (57.9%), Claude Opus 5 (51.8%).

**MMLU / MMLU-Pro**: Not separately reported on HF model card benchmark table. Evaluated during architecture ablation (25B-A3B stage) but not published for the 125B production model.

## GSQ-RCO Quantization (ISTA-DASLab)

Gumbel-Softmax Quantization + Riemannian Constrained Optimization — per-tensor, non-uniform, gradient-based search under exact size budget.

| Variant | bpw | Shard 1 (resident) | Shard 2 (n-gram, disk) | Total | Notes |
|---|---|---|---|---|---|
| **Q2_0** | 2.40 | 37.6 GB | 28.8 GB | 66.4 GB | Fastest; avoids lookup-table formats |
| **IQ2_XS** | 2.50 | 39.2 GB | 28.8 GB | 68.0 GB | Smallest at equal quality |
| **IQ3_XXS** | 3.00 | 47.0 GB | 28.8 GB | 75.8 GB | **Recommended** — matches base on AIME25 (100.00), within 0.51 GPQA-D, 1.14 LCB v6 |
| **mmproj-BF16** | 16 | 0.91 GB | — | 0.91 GB | Vision encoder + projector |

**Recovery vs BF16:**
- IQ3_XXS: 99.4% task average recovery, 92.57 task avg vs 93.12 base
- IQ2_XS: 95.7% task average recovery
- Q2_0: 96.67 AIME25, 89.39 GPQA-D, 81.14 LCB v6

**Memory requirements:**
- Only Shard 1 must be resident (VRAM or system RAM).
- Shard 2 (n-gram table) is memory-mapped on disk, read sparsely (one row per token).
- Use `-lm mmap --lazy-mode on` in llama.cpp to keep shard 2 off VRAM.

## Optimal Quantization by Hardware Tier

### NVIDIA GPU (CUDA)
| VRAM | Optimal quant | Resident (shard 1) | Notes |
|---|---|---|---|
| 80GB+ (A100/H100) | IQ3_XXS | 47 GB | Full model on GPU, large KV headroom |
| 48GB (A6000/A5000) | IQ3_XXS | 47 GB | Fits with ~1 GB headroom; KV in system RAM if needed |
| 32GB (A10G/RTX A5500) | IQ3_XXS (offload) or IQ2_XS | 47 / 39.2 GB | IQ3_XXS needs ~7 GB offload; IQ2_XS fits natively |
| 24GB (RTX 3090/4090) | IQ3_XXS (offload) or IQ2_XS | 47 / 39.2 GB | IQ3_XXS with `--fit on --fit-target 256`; IQ2_XS lighter offload |
| 16GB (RTX 4080/4070 Ti) | IQ2_XS or Q2_0 | 39.2 / 37.6 GB | Heavy offload needed; KV in system RAM |

**Reference config (RTX 4090 24GB, from gist):**
```bash
llama-server \
  --model Qwen3.8-Flash-Next-GSQ-RCO-IQ3_XXS-00001-of-00002.gguf \
  --mmproj mmproj-F16.gguf \
  --ctx-size 120000 \
  --fit on --fit-target 256 \
  -t 20 -tb 24 \
  -b 6144 -ub 6144 \
  --temp 1.0 --top-p 0.95 --top-k 20 --min-p 0.0 \
  --flash-attn on --cache-type-k q8_0 --cache-type-v q8_0 \
  --reasoning-budget 4000 \
  --chat-template-kwargs '{"reasoning_effort": "medium"}' \
  --reasoning-preserve \
  --cont-batching --metrics -np 1
```

### Apple Silicon (Metal / Unified Memory)
| Unified Memory | Optimal quant | Notes |
|---|---|---|
| 128GB (M4 Ultra) | IQ3_XXS (47 GB resident + KV) | Comfortable headroom |
| 64GB (M4 Max) | IQ2_XS (39.2 GB) or Q2_0 (37.6 GB) | IQ3_XXS at 47 GB leaves only ~17 GB for KV |
| 32GB (M1/M2/M3 Pro) | IQ2_XS with n-gram on disk | 39.2 GB > 32 GB; needs some KV spillover |
| 16GB–24GB | Not practical | Model exceeds available memory |

**Notes:**
- N-gram shard (28.8 GB) stays on SSD via mmap; only Shard 1 needs unified memory.
- `--cache-type-k/v q8_0` recommended to save ~1.5 GB vs F16 KV.
- MTP head unsupported by llama.cpp Metal backend; speculative decode unavailable.

### CPU (x86/ARM, no discrete GPU)
| System RAM | Optimal quant | Notes |
|---|---|---|
| 128GB+ | IQ3_XXS | Both shards in RAM; mmap n-gram from SSD |
| 64GB | IQ2_XS or Q2_0 | Shard 1 (37–39 GB) fits; n-gram on disk |
| 48GB | Q2_0 (37.6 GB shard 1) | Minimum for acceptable throughput |

**Notes:**
- llama.cpp with `-lm mmap --lazy-mode on` keeps n-gram shard off RAM when possible.
- Flash-attn on CPU: use `--flash-attn on` if compiled with appropriate backend.
- Prefer IQ3_XXS for quality; Q2_0 for maximum throughput on memory-constrained systems.

### Unified Tier Summary
- **GPU** (high VRAM): IQ3_XXS
- **GPU** (24GB): IQ3_XXS with `--fit on --fit-target 256`
- **GPU** (16GB): IQ2_XS or Q2_0 with heavy offload
- **Apple Silicon** (64GB+): IQ2_XS or Q2_0; IQ3_XXS at 128GB
- **CPU** (64GB+): IQ2_XS or Q2_0; IQ3_XXS at 128GB

## Runtime Config by Context Length

### 131K (131,072 tokens)
- **VRAM needed:** Shard 1 (47 GB for IQ3_XXS) + KV cache (~2–4 GB for q8_0 at 131K context)
- **Suitable for:** 48GB GPUs, 64GB+ unified memory
- **Config:** `--ctx-size 131072 --fit on --flash-attn on --cache-type-k q8_0 --cache-type-v q8_0`
- **With vision (mmproj):** Max stable ~150K with mmproj on 48GB card; plan compaction before 131K
- **Prefill:** ~982 tok/s @ 131K with -b 6144 -ub 6144 on 24-core CPU
- **Decode:** ~22–30 tok/s with -t 20 -tb 24 on 24-core CPU

### 262K (262,144 tokens — native context)
- **VRAM needed:** Shard 1 + KV cache (~4–8 GB q8_0 at 262K)
- **Suitable for:** 80GB+ GPUs, 128GB+ unified memory
- **Config:** `--ctx-size 262144 --fit on --flash-attn on --cache-type-k q8_0 --cache-type-v q8_0`
- **Note:** KV at 262K is substantial; on 48GB GPU, use `--no-kv-offload` to spill KV to system RAM
- **QSA speedup:** ~4.9× decode speedup vs dense attention at 1M tokens

### 1M (1,000,000 tokens — extended via YaRN)
- **VRAM needed:** Shard 1 + KV cache (~15–30 GB q8_0 at 1M context)
- **Suitable for:** Multi-GPU (2×24GB+), 128GB+ unified memory, or heavy offload
- **Config:** `--ctx-size 1000000 --fit on --flash-attn on --cache-type-k q8_0 --cache-type-v q8_0`
- **Note:** QSA prefill ~7.6× faster than dense attention at 1M tokens
- **Inference framework:** SGLang, vLLM, or TokenSpeed recommended for YaRN support
- **llama.cpp:** Limited YaRN support; prefer SGLang/vLLM for 1M context

## Key Flags Reference

| Flag | Purpose |
|---|---|
| `--fit on` | Auto-fit weights to available VRAM |
| `--fit-target 256` | Offload granularity in MB; don't go below 256 |
| `-lm mmap --lazy-mode on` | Keep n-gram shard on disk, not in RAM |
| `--cache-type-k q8_0 --cache-type-v q8_0` | KV cache quantization; q4_0 dequant overhead cancels gain |
| `--flash-attn on` | Enable FlashAttention |
| `--reasoning-budget 4000` | Cap thinking tokens (xhigh wastes tokens; medium better) |
| `--reasoning_effort medium` | Avoid self-doubt loops at xhigh |
| `--tensor-split` | For multi-GPU (e.g., 2×RTX 3090) |
| `--no-kv-offload` | Spill KV to system RAM when VRAM full |

## Systems
- omarchy (RTX 3090×2)
- macOS (Metal) — limited to 32GB unified for IQ2_XS/Q2_0; 64GB+ for IQ3_XXS

## Notes
- Model ships MTP head but llama.cpp doesn't support it yet (`--spec-type draft-mtp` OOMs)
- `--ctx-size 131072` may OOM with mmproj on 24GB cards; max stable ~120K
- IQ3_XXS is the best quality/size tradeoff: matches base on AIME25, 0.51 behind on GPQA-D
- Q2_0 fastest but 2–3 points behind on reasoning benchmarks
- N-gram shard is read sparsely; SSD-backed mmap has negligible latency impact

## Cross-references
- [[index|wiki index]]
- [[Qwen 3.8 27B Base|Qwen3.8-27B]] — non-MoE sibling
