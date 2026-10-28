---
title: GSQ-RCO Qwen 3.8
created: 2026-09-16
updated: 2026-09-16
type: model
tags: [model, omarchy, quantization, gsq, rco, gguf]
sources:
  - https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF
  - https://huggingface.co/Qwen/Qwen3.8-27B
  - https://github.com/IST-DASLab/GSQ
  - https://github.com/IST-DASLab/RCO
confidence: high
---

# Qwen 3.8 27B GSQ-RCO

> ISTA-DASLab's non-uniform GGUF quantization — near-FP16 accuracy at Q3 via gradient-optimized per-tensor bit allocation.

## Model: Qwen3.8-27B

**Full name**: Qwen3.8-27B (GSQ-RCO quantization)
**Developer**: Alibaba Tongyi Lab (base) + ISTA Deep Algorithms and Systems Lab (quantization)
**License**: Apache 2.0

### Parameters
- **27.78 billion** (27,781,427,952 total)
- Hidden dimension: 5,120
- 64 transformer layers
- FFN intermediate: 17,408
- 24 query heads / 4 KV heads, head dim 256
- Token embedding: 248,320 (padded)

### Architecture
Dense hybrid-attention vision-language model built on Qwen3.5 backbone:
- **Hybrid attention (3:1 ratio)**: 48 layers Gated DeltaNet (linear attention) + 16 layers Gated Full Attention
- Layout: `16 × (3 × (Gated DeltaNet → FFN) → 1 × (Gated Attention → FFN))` — `full_attention_interval: 4`
- Multi-Token Prediction (MTP) draft head for speculative decoding
- Native multimodal: text, image, video via integrated vision encoder + projector (`mmproj`)
- BF16 size: ~55.6 GB (53.8 GiB)

### Context Windows
| Setting | Tokens | Notes |
|---------|--------|-------|
| Native | 262,144 | Full native context, no scaling needed |
| Agentic max | 131,072 | Qwen-recommended cap for final response in agentic workloads |
| Extended | 1,048,576 | YaRN scaling factor 4 — supported in vLLM, SGLang, TokenSpeed (not llama.cpp) |

## GSQ-RCO Quantization

**Method**: Non-uniform per-tensor quantization via two learned passes:
1. **GSQ** (Gumbel-Softmax Quantization, [paper](https://arxiv.org/abs/2604.18556)): learns per-coordinate grid assignments + per-group scales for each tensor at every candidate GGUF type
2. **RCO** (Riemannian Constrained Optimization, [paper](https://arxiv.org/abs/2605.00649)): gradient-based budget allocation — assigns one quantization type per tensor to hit exact size target while minimizing task loss

Result: standard GGUF files that run unmodified in llama.cpp, Ollama, LM Studio. Each tensor gets its own precision — sensitive layers get 4-5 bit, robust layers get 2-bit.

### Available Quantizations
| File | bpw | Size | Notes |
|------|-----|------|-------|
| `Qwen3.8-27B-GSQ-RCO-IQ2_XS.gguf` | 2.50 | 8.4 GB | Smallest; zero-shot above BF16 baseline |
| `Qwen3.8-27B-GSQ-RCO-IQ2_S.gguf` | 2.75 | 9.3 GB | Matches BF16 on AIME25; ZS avg exceeds BF16 |
| `Qwen3.8-27B-GSQ-RCO-IQ3_XXS.gguf` | 3.00 | 10.1 GB | Strong all-round; within ~1pt of BF16 on GPQA-D |
| `Qwen3.8-27B-GSQ-RCO-IQ3_S.gguf` | 3.50 | 11.8 GB | **Recommended; task-lossless** |
| `mmproj-Qwen3.8-27B-BF16.gguf` | 16 | 0.9 GB | Vision encoder + projector (shared across quants) |

Optional `-mtp` builds add ~0.35 GB for speculative decoding support in llama.cpp.

## Benchmark Scores

### Base Model (Qwen3.8-27B BF16) — Official
| Benchmark | Score | Notes |
|-----------|-------|-------|
| Terminal-Bench 2.1 (Terminus) | 73.0% | Agentic terminal coding |
| SWE-bench Pro | 61.7% | Claude Code harness, temp=1.0, 256K ctx |
| DeepSWE 1.1 | 42.2% | Claude Code harness, 256K ctx |
| NL2Repo-Bench | 42.3% | Repo-level code generation |
| QwenSWEBench | 79.0% | avg@3, 8hr timeout, 256K ctx |
| CoWorkBench | 70.7% | Long-horizon office work |
| JobBench | 33.4% | Professional job tasks |
| Agents' Last Exam | Pass@1 20.4 / Score 42.9 | Frontier agentic tasks |
| IFBench | 79.5% | Instruction following |
| GPQA Diamond | 89.2% | Graduate-level science |
| Humanity's Last Exam | 30.8% | No tools |
| LiveCodeBench v6 | 90.3% | Competitive coding |
| MMLU-Pro (5-shot CoT) | 76.71% | 12,032 questions |
| MMLU-Pro (Vals) | 84.3% | Independent eval |
| AIME 2025 | 100.00 | avg@3, 32K max tokens |

### GSQ-RCO Quantized Recovery
| Variant | bpw | Size | ZS avg | Recovery | AIME25 | GPQA-D | LCB v6 |
|---------|-----|------|--------|----------|--------|--------|--------|
| BF16 | 16.00 | 53.8 GB | 74.34 | 100.0% | 100.00 | 89.90 | 85.71 |
| **GSQ-RCO IQ2_XS** | 2.50 | 8.4 GB | 74.54 | 100.3% | 96.67 | 84.85 | 76.57 |
| **GSQ-RCO IQ2_S** | 2.75 | 9.3 GB | 75.70 | 101.8% | 100.00 | 86.36 | 82.29 |
| **GSQ-RCO IQ3_XXS** | 3.00 | 10.1 GB | 74.81 | 100.6% | 100.00 | 88.89 | 84.57 |
| **GSQ-RCO IQ3_S** | 3.50 | 11.8 GB | 74.47 | 100.2% | 100.00 | 89.39 | 85.71 |
| UD-IQ2_S (Unsloth) | 2.49 | 8.4 GB | 73.80 | 99.3% | 86.67 | 76.26 | 72.00 |
| UD-Q2_K_XL (Unsloth) | 2.88 | 9.8 GB | 74.37 | 100.0% | 100.00 | 86.87 | 82.28 |

**Key takeaway**: At matched 8.4 GB, IQ2_XS beats UD-IQ2_S by +10.0 AIME25, +8.6 GPQA-Diamond, +4.6 LiveCodeBench. IQ3_S at 11.8 GB is task-lossless (reproduces BF16 exactly on AIME25 and LCB v6, within 0.51pt on GPQA-Diamond).

## Optimal Quantization by Hardware Tier

### GPU (Dedicated VRAM) — e.g., RTX 3090×2 (48GB), RTX 4090 (24GB)
- **Best**: `IQ3_S` (3.50 bpw, 11.8 GB) — task-lossless, full GPU offload, ~28GB VRAM with KV cache at 262K
- **Alternative**: `IQ3_XXS` (3.00 bpw, 10.1 GB) — within 1pt of BF16, fits 24GB cards
- **Budget**: `IQ2_S` (2.75 bpw, 9.3 GB) — matches BF16 on AIME25, exceeds BF16 zero-shot avg
- **Flags**: `-ngl 99` (full GPU offload), `-c 262144` for native context

### Unified Memory (Apple Silicon, shared RAM)
- **Best**: `IQ3_XXS` (3.00 bpw, 10.1 GB) — balanced for shared memory bandwidth
- **Lighter**: `IQ2_S` (2.75 bpw, 9.3 GB) — for 16-32GB unified systems
- **Flags**: `-ngl 99` (Metal), suppress discrete split flags; KV cache shares system RAM

### CPU (Pinned RAM, AMX)
- **Best**: `IQ3_XXS` (3.00 bpw, 10.1 GB) — highest quality within RAM constraints
- **Lighter**: `IQ2_XS` (2.50 bpw, 8.4 GB) — smallest, zero-shot above BF16 baseline
- **Flags**: `-ngl 0` (CPU only), `--cpu-moe` not needed (dense model), pinned memory

## Runtime Configuration by Context

### 131K Context (Agentic Max)
- **Config**: `-c 131072 -ngl 99`
- **Use case**: Qwen-recommended cap for final response in agentic workflows; fits comfortably on 24GB+ GPUs with IQ3_S
- **VRAM estimate**: ~12 GB (weights) + ~4-8 GB (KV) = 16-20 GB total

### 262K Context (Native)
- **Config**: `-c 262144 -ngl 99`
- **Use case**: Full native context window; no scaling artifacts
- **VRAM estimate**: ~12 GB (weights) + ~8-16 GB (KV) = 20-28 GB total
- **Turbofit note**: On dual 3090×2, fits with IQ3_XXS or IQ3_S; KV cache may spill to host RAM if ≥32GB usable

### 1M Context (Extended via YaRN)
- **Config**: Requires vLLM or SGLang with `--rope-scaling yarn` (factor 4)
- **llama.cpp**: Not officially supported — YaRN in llama.cpp is limited; static scaling can hurt short-prompt quality
- **Use case**: Long documents, video, codebase-scale analysis
- **Turbofit note**: Use vLLM/SGLang backend for 1M; on llama.cpp, stay at 262K native
- **Quantization**: IQ2_S or IQ3_XXS recommended to leave headroom for extended KV cache

## Runtimes

### NVIDIA GPU (CUDA) — Omarchy RTX 3090×2
llama.cpp CUDA, GSQ-RCO tensors natively supported (standard GGUF IQ formats)

### AMD GPU (ROCm)
llama.cpp with ROCm (GSQ-RCO uses standard GGUF IQ types, ROCm compatible)

### Apple Silicon (Metal) — MacBook M1 Pro
llama.cpp Metal (Q4_K_M fallback if IQ types unsupported on older builds)

### CPU
llama.cpp AMX (AVX-512/AVX2) — dense model, no MoE offload needed

## Systems
- omarchy

## Notes
- Size: 8.4–11.8 GB depending on quant (plus 0.9 GB mmproj for multimodal)
- Cross-references: [[index|wiki index]]
- Reference implementations: [IST-DASLab/GSQ](https://github.com/IST-DASLab/GSQ), [IST-DASLab/RCO](https://github.com/IST-DASLab/RCO)
