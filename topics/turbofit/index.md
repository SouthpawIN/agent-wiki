---
title: Turbofit Wiki
created: 2026-09-16
updated: 2026-09-17
type: wiki
links:
  github: https://github.com/SouthpawIN/turbofit
  huggingface_turbofit: https://huggingface.co/SouthpawIN
  omarchy: https://github.com/SouthpawIN/omarchy
sources:
  - index.md
  - BRIEF.md
  - README.md
  - wiki/models/
---

## Overview

**TurboFit** is a first-class [Hermes Agent](https://github.com/NousResearch/hermes-agent) provider and adaptive local-inference runtime. It discovers what a machine can run, recommends an evidence-backed model ladder, launches a native backend, and exposes a single OpenAI-compatible endpoint.

**Design principles:**
- Local first, cloud fallback only when the task exceeds local capability
- Model choice is evidence-driven, not brand-driven
- Reasoning ON by default; token budgets sized for thinking models (4000+)
- Every model gets benchmarks, every claim gets a source

**Supported platforms:**
- **Omarchy** (RTX 3090 ×2, 377GB RAM) — primary GPU server
- **MacBook** (M1 32GB) — streaming + local inference
- Future: Surface Duo as mobile endpoint

```text
provider: custom:turbofit
model: auto
```

**TurboFit Check** scans the machine and applies Auto or a selected compatible lane.

---

## Implementation

This section covers HOW TurboFit works: architecture, runtime selection, provider configuration, and the integration paths that make local inference stable.

### Runtime Selection

TurboFit supports multiple inference backends. Selection depends on platform and model:

| Runtime | Platform | Models | Speed | Notes |
| --- | --- | --- | --- | --- |
| **llama.cpp** (dflash2 fork) | Omarchy, MacBook | Unleashed 27B, DeepSeek V4.1 | 70-85 tok/s (Omarchy GPU) | Full DFlash2 draft support |
| **llama.cpp** (stock) | Omarchy, MacBook | Most GGUF models | Varies | No DFlash2 support |
| **MTPLX** | MacBook (M1) | Qwen 3.8, Unleashed | 12.4 tok/s short, 7-12 tok/s at 65K | Memory guard at 131K |
| **MLX** | MacBook (M1) | Ornith 1.5, Maple | 28.5 tok/s short | Apple-native, fastest on M1 |

### Hermes Provider Integration

TurboFit registers as `custom:turbofit` in Hermes Agent. Configuration is in `config.yaml`:

```yaml
provider: custom:turbofit
model: auto
```

**Auto mode** scans available hardware and selects the best model from the TurboFit List. Manual selection locks a specific model.

### Model + Context Sizing

Local contexts are set to **131,072 tokens** as the stable sweet spot. Evidence:
- 262K+ pre-fills slowly on M1 32GB and stresses Metal heap
- Hermes compression timed out repeatedly at 270K+ tokens on main model
- 131K is the tested stable configuration on the MacBook

On Omarchy (256GB+ VRAM), 262K+ contexts are viable with DFlash2 draft models.

### Provider Fallback Order

To prevent silent switching to cloud providers:

1. `model.default` must be first in the fallback chain
2. `auxiliary.compression.provider` pinned to local TurboFit route
3. Cloud fallback only for tasks exceeding local memory budget

This addresses the Hermes auto-route stability issue where `stepfun/step-3.7-flash:free` was selected without explicit choice.

### DFlash2 Speculative Decoding

DFlash2 is a draft model for accelerating long-context inference. Key facts:

- **Only works with llama.cpp** (dflash2 fork), not MTPLX or MLX
- **Incompatible with MTPLX**: MTPLX uses native MLX MTP heads; DFlash2 is CUDA/llama.cpp only
- **Valid flags**: `--spec-draft-model`, `--spec-draft-ngl 999`, `--spec-draft-n-max 7`, `--spec-type draft-dflash`
- **Invalid flags** that fail: `--draft-model`, `--draft-ngl`, `--draft-ctx-size`, `--low-vram`, `--model-draft`

### Memory Management

**MTPLX Memory Guard** — emits `prefill_admission_shed` events when a prompt would exceed memory threshold, clearing KV cache to stay under limit.

**Unleashed IQ3_XXS** — failed to load with `tensor 'blk.2.attn_qkv.weight' data is not within the file bounds`. This quant is not usable on the dflash2 fork.

**Crash pattern**: `mtplx serve` exits with code -9 when memory plan is marked `OVER`. Exit code 1 with `RuntimeError: [METAL] Command buffer execution failed: Insufficient Memory` during MTP injection.

### Verifier Bridge

`turbofit-verifier` drives verification through `desktop_preview` on a real Hermes window instead of summary claims.

---

## Issues

Known problems, gotchas, and things to remember while building.

### Hermes Model Switching

**Problem**: Hermes flips active model to StepFun 3.7 Flash without explicit user choice.

**Root cause**: `model.default` not first in fallback chain + `auxiliary.compression.provider: auto` selecting cloud.

**Fix**: Pin `auxiliary.compression.provider` to local TurboFit route; ensure `model.default` is first.

### Compression Timeouts

At 262K+ tokens on the main model, Hermes compression timed out before committing. Resolved by capping context at 131K on M1 32GB.

### MTPLX 131K Instability

MTPLX at 131K context triggers memory-guard events and crashes. Use 65K for stable MTPLX operation. 131K long-context needs llama.cpp + DFlash2 instead.

### MPLX Service Args

`mtplx serve` does not accept `--memory-budget 32GB`. Only documented flags are accepted; undocumented flags exit with `unrecognized arguments`.

### DFlash2 Port Conflicts

`couldn't bind HTTP server socket, hostname: 127.0.0.1, port: 11606` — port already in use. Not a model issue, a port conflict.

---

## Model Zoo

> All models discovered during research. ★ = on TurboFit List.

| Model | Type | System | Parameters | AIME26 | GPQA-D | DeepSWE | LCBv6 | TB4.0 | HuggingFace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [[Maple Preview]] ★ | Aux LLM (Ternary MoE) | Omarchy | 20B-A1B | 87.5% | 73.5% | - | 75.1% | - | [maple-preview](https://huggingface.co/deepgrove/maple-preview) |
| [[Cyber Tiel Coder]] ★ | Code LLM (MoE) | Omarchy, MacBook | 35B-A3B | - | - | - | - | - | [Cyber-Tiel-Coder-GGUF](https://huggingface.co/peculiar-ragdoll/Cyber-Tiel-Coder-35B-A3B-GGUF-MTP) |
| [[Qwen 3.8 GSQ-RCO]] ★ | LLM (Quantized) | Omarchy | 27B | - | 89.2% | 42.2% | 90.3% | - | [GSQ-RCO-GGUF](https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF) |
| [[Qwen 3.8 Flash Next]] ★ | MoE (Qwen4 Preview) | Omarchy | 180B / 6B | - | 91.7% | 58.7% | 91.9% | - | [Flash-Next-GSQ-RCO](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF) |
| [[DeepSeek V4.1 Flash]] ★ | MoE | Omarchy | 763B / 16B | - | 90.9% | 74.2% | - | 31.2% | [V4.1-Flash-GGUF](https://huggingface.co/vcruz305/DeepSeek-V4.1-Flash-GGUF) |
| [[Ace Step 1.5]] | Music Generation | Omarchy | 4B | - | - | - | - | - | [ACE-Step-1.5-GGUF](https://huggingface.co/ACE-Step/ACE-Step-1.5-GGUF) |
| [[Bonsai 27B]] | LLM (Ternary) | Omarchy | 27B | - | - | - | - | - | [Bonsai-27B-gguf](https://huggingface.co/prism-ml/Bonsai-27B-gguf) |
| [[Cosmos 37B]] | LLM | Omarchy | 37B | - | - | - | - | - | [Cosmos-37b-BASE-i1-GGUF](https://huggingface.co/mradermacher/Cosmos-37b-BASE-i1-GGUF) |
| [[Cyber Tiel Coder MTP]] | Code LLM (MTP) | Omarchy | 35B-A3B | - | - | - | - | - | [Cyber-Tiel-MTP](https://huggingface.co/peculiar-ragdoll/Cyber-Tiel-Coder-35B-A3B-GGUF-MTP) |
| [[DAXZEIT GRM]] | Reasoning LLM (MTP) | Omarchy | 27B | - | - | - | - | - | [DAXZEIT-GRM-2.6-Plus-MTP](https://huggingface.co/mradermacher/DAXZEIT_GRM-2.6-Plus-0628-MTP-reasoning-i1-GGUF) |
| [[NVIDIA Nemotron 3.5]] | Enterprise LLM (MoE) | Omarchy | 30B-A3B | - | - | - | - | - | [NVIDIA-Nemotron-3.5-Lightning-30B-A3B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF) |
| [[Qwen 3.8 Unleashed]] | General LLM | Omarchy, MacBook | 27B | - | - | - | - | - | [Qwen3.8-Unleashed-GGUF](https://huggingface.co/outsourc-e/Qwen3.8-27B-Unleashed-GGUF) |
| [[Super Qwen]] | Uncensored LLM | Omarchy | 27B | - | - | - | - | - | [SuperQwen3.8-27b-abliterated](https://huggingface.co/Jiunsong/SuperQwen3.8-27b-abliterated-GGUF) |
| [[Qwen 2.5 Omni]] | Multimodal VLM | Omarchy | 3B | - | - | - | - | - | [Qwen2.5-Omni-3B](https://huggingface.co/unsloth/Qwen2.5-Omni-3B-GGUF) |
| [[Soprano]] | Creative Micro | Omarchy | 80M | - | - | - | - | - | [Soprano-1.1-80M](https://huggingface.co/WalkingCat/Soprano-1.1-80M-GGUF) |
| [[Qwen 3.8 Base]] | Base LLM | Omarchy, MacBook | 27B | - | - | - | - | - | [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) |
| [[Ornith 1.5]] | Code LLM (Legacy) | MacBook | 35B-A3B | - | - | - | - | - | [Ornith-1.5-35B-A3B](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B) |

> **Note:** GSQ-RCO IQ3_S scores shown (AIME25 100%, GPQA-D 89.2%, DeepSWE 42.2%, LCBv6 90.3%). Maple LCBv6 score is from LiveCodeBench v6.

---

## TurboFit List

> 5 models suitable for running Hermes Agent locally. Ordered by capability.

| Model | Tok/s | Parameters | Optimal Quant | Size | AIME26 | GPQA-D | DeepSWE | LCBv6 | TB4.0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Maple Preview** | 218 tok/s (MTPLX M4) | 20B-A1B | TQ2_0-head-Q4_K | 5.5 GiB | 87.5% | 73.5% | - | 75.1% | - |
| **Cyber Tiel Coder** | 23 tok/s (MacBook 65K) | 35B-A3B | UD-Q4_K_XL | 22.4 GiB | - | - | - | - | - |
| **Qwen 3.8 GSQ-RCO** | 85 tok/s (Omarchy GPU) | 27B | IQ3_S | 11.8 GiB | - | 89.2% | 42.2% | 90.3% | - |
| **Qwen 3.8 Flash Next** | 70-85 tok/s (Omarchy GPU) | 180B / 6B | IQ3_XXS | 47 GiB | - | 91.7% | 58.7% | 91.9% | - |
| **DeepSeek V4.1 Flash** | TBD | 763B / 16B | FP8 / UD-Q4_K_XL | 160 / ~40 GiB | - | 90.9% | 74.2% | - | 31.2% |

> **Note:** GSQ-RCO IQ3_S benchmark scores (AIME25 100%, GPQA-D 89.2%, DeepSWE 42.2%, LCBv6 90.3%) are from the model card. Maple LCBv6 score is from LiveCodeBench v6.

### Fit Calculation System

```
Required: model_size + KV_cache ≤ tier_size
KV_cache ≈ 2-4GB at 262K context (q8_0 KV)
Comfortable: model_size + 2GB ≤ tier_size
```

### GPU (NVIDIA/AMD VRAM — ≤16GB assumes system RAM available for MoE offload and KV cache)

| Tier | Model | Quant | Size | VRAM Used | Context | Engine | Flags | Tok/s | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <8 GB | Maple | TQ2_0 | 5.5 GiB | ~6 GiB | 131K native, 262K w/ RoPE | llama.cpp | `--ctx-size 262144 --n-gpu-layers 999 --mlock` | ~10 tok/s (est.) | SSD streaming via ssdmoe. System RAM for KV cache. |
| 16 GB | GSQ-RCO | IQ3_S | 11.8 GiB | ~12 GiB | 131K-262K | llama.cpp | `--ctx-size 262144 --n-gpu-layers 999 --mlock` | ~85 tok/s (Omarchy) | Near-lossless. Cyber-Tiel Q3_K_M also fits (~14 GiB). |
| 24 GB | GSQ-RCO | IQ3_S | 11.8 GiB | ~12 GiB | 262K | llama.cpp | `--ctx-size 262144 --n-gpu-layers 999 --mlock` | ~85 tok/s (Omarchy) | Same near-lossless model, more KV headroom |
| 32 GB | GSQ-RCO | IQ3_S | 11.8 GiB | ~12 GiB | 262K+ | llama.cpp | `--ctx-size 262144 --n-gpu-layers 999 --mlock` | ~85 tok/s (Omarchy) | Same. Bigger KV cache. Consider Cyber-Tiel for code |
| 48 GB | GSQ-RCO | IQ3_S | 11.8 GiB | ~12 GiB | 262K+ | llama.cpp | `--ctx-size 262144 --n-gpu-layers 999 --mlock` | ~85 tok/s (Omarchy) | Still IQ3_S. More context headroom |
| 64 GB | GSQ-RCO | IQ3_S | 11.8 GiB | ~16 GiB | 262K+ | llama.cpp | `--ctx-size 262144 --n-gpu-layers 999 --mlock` | ~85 tok/s (Omarchy) | Near-lossless. 52GB free for KV cache, DFlash2 draft. |
| 96 GB | Flash Next | IQ3_XXS | 47 GiB | ~48 GiB | 262K native, 1M w/ YaRN | llama.cpp | `--ctx-size 1048576 --n-gpu-layers 999 --mlock` | ~70-85 tok/s (Omarchy) | Qwen4 preview, beats Claude Opus 4.6 |
| 128 GB | Flash Next | IQ3_XXS | 47 GiB | ~48 GiB | 1M | llama.cpp | `--ctx-size 1048576 --n-gpu-layers 999 --mlock` | ~70-85 tok/s (Omarchy) | Max context for Flash Next |
| 256 GB | DeepSeek V4.1 Flash | FP8 | 160 GiB | ~162 GiB | 1M | llama.cpp | `--ctx-size 1048576 --n-gpu-layers 999 --mlock` | TBD | Top capability. SSD streaming for Engram |

> IQ3_S = near-lossless. Recommended for all tiers where it fits. Only move to FP16 at 64GB+.
> Flash Next QSA gives ~4.9x decode speedup vs dense attention at 262K. IQ3_XXS is the sweet spot for 96GB+.

### CPU (System RAM — model + KV must fit in RAM)

| Tier | Model | Quant | Size | RAM Used | Context | Engine | Flags | Tok/s | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <8 GB | Maple | TQ2_0 | 5.5 GiB | ~6 GiB | 131K native | llama.cpp | `--ctx-size 131072 --no-mmap --mlock` | ~8 tok/s (est.) | Minimum viable |
| 16 GB | Cyber-Tiel Coder | Q3_K_M | ~14 GiB | ~16 GiB | 262K native | llama.cpp | `--ctx-size 262144 --no-mmap --mlock` | ~23 tok/s (MacBook) | MoE, 3B active. Faster than GSQ-RCO on CPU. |
| 32 GB | Cyber-Tiel Coder | UD-Q4_K_XL | 22.4 GiB | ~23 GiB | 262K native | llama.cpp | `--ctx-size 262144 --no-mmap --mlock` | ~23 tok/s (MacBook) | MoE, 3B active, fast on CPU |
| 48 GB | Cyber-Tiel Coder | UD-Q4_K_XL | 22.4 GiB | ~23 GiB | 262K+ | llama.cpp | `--ctx-size 262144 --no-mmap --mlock` | ~23 tok/s | More KV headroom |
| 64 GB | GSQ-RCO | IQ3_S | 11.8 GiB | ~16 GiB | 262K+ | llama.cpp | `--ctx-size 262144 --no-mmap --mlock` | ~12 tok/s (65K ctx) | Near-lossless. Low power, high context headroom. |
| 96 GB | Flash Next | IQ3_XXS | 47 GiB | ~48 GiB | 262K native | llama.cpp | `--ctx-size 1048576 --no-mmap --mlock` | TBD | Flash Next entry tier |
| 128 GB | Flash Next | IQ3_XXS | 47 GiB | ~48 GiB | 1M w/ YaRN | llama.cpp | `--ctx-size 1048576 --no-mmap --mlock` | TBD | Max context |
| 256 GB | DeepSeek V4.1 Flash | FP8 | 160 GiB | ~162 GiB | 1M | llama.cpp | `--ctx-size 1048576 --no-mmap --mlock` | TBD | Max tier |

### Unified Memory (Apple Silicon — shared CPU/GPU RAM)

| Tier | Model | Quant | Size | RAM Used | Context | Engine | Flags | Tok/s | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <8 GB | Maple | TQ2_0 | 5.5 GiB | ~6 GiB | 131K native | MTPLX | `--context-length 131072` | 218 tok/s (M4 mini) | 218 tok/s on M4 Mac mini |
| 16 GB | Cyber-Tiel Coder | Q3_K_M | ~14 GiB | ~16 GiB | 262K native | MTPLX | `--context-length 262144` | ~23 tok/s (MacBook) | MoE, 3B active. Faster than GSQ-RCO on Apple Silicon. |
| 32 GB | Cyber-Tiel Coder | UD-Q4_K_XL | 22.4 GiB | ~23 GiB | 262K native | MTPLX | `--context-length 262144` | ~23 tok/s (MacBook) | 22+4=26GB ✓, fast MoE on Apple Silicon |
| 48 GB | Cyber-Tiel Coder | UD-Q4_K_XL | 22.4 GiB | ~23 GiB | 262K+ | MTPLX | `--context-length 262144` | ~23 tok/s | M2 Max/Ultra territory |
| 64 GB | GSQ-RCO | IQ3_S | 11.8 GiB | ~16 GiB | 262K+ | MTPLX | `--context-length 262144` | ~8-12 tok/s (65K) | Near-lossless. Low power, high context headroom. |
| 96 GB | Flash Next | IQ3_XXS | 47 GiB | ~48 GiB | 262K native | MTPLX | `--context-length 1048576` | TBD | M4 Ultra |
| 128 GB | Flash Next | IQ3_XXS | 47 GiB | ~48 GiB | 1M w/ YaRN | MTPLX | `--context-length 1048576` | TBD | Max Flash Next |
| 256 GB | DeepSeek V4.1 Flash | FP8 | 160 GiB | ~162 GiB | 1M | llama.cpp | `--ctx-size 1048576` | TBD | Max tier |

> ★ = on TurboFit List. Models without ★ are Model Zoo only.

---

---

## Concepts

### 131K Deferred Candidates

Newly downloaded candidate artifacts not benchmarked at 131K because model-plus-KV exceeds 32GB Mac fit before testing begins.

### Benchmark Taxonomy

| Tier | Use Case | Models |
| --- | --- | --- |
| Daily Driver | Short-context speed | Ornith MLX (28.5 tok/s) |
| Long Context | 131K stable | Unleashed + DFlash2 (~5 tok/s) |
| High Capability | Maximum quality | DeepSeek V4.1 Flash |
| Aux/Compression | Background tasks | Maple Preview |

### Speculative Decoding Architectures

| Architecture | Runtimes | Draft Type | Speed Boost |
| --- | --- | --- | --- |
| DFlash2 | llama.cpp fork | Diffusion-based | ~1.5-2x |
| MTP (Multi-Token) | MLX, llama.cpp | Native heads | ~2x |
| MTPLX | MTPLX only | Native MLX MTP | ~2.5x |

### Hermes Auto Route Stability

See [Issues](#issues) section for problem details and resolution.

### Model Selection Decision Tree

```
Start
  ├─ Need vision? → Unleashed 27B (only model with projector)
  ├─ Need speed at 65K? → Ornith MLX 4-bit (28.5 tok/s)
  ├─ Need 131K long context? → Unleashed + DFlash2 on llama.cpp
  └─ Need max capability? → DeepSeek V4.1 Flash on Omarchy
```

---

## Decisions

> All 10 decisions. Each entry preserves the full content of its source file.

### Aux Model Selection

Source: `wiki/decisions/aux-model-selection.md`

#### What

Auxiliary and compression routing is Maple MLX on `127.0.0.1:11612`, 131k context, served with `deepgrove-ai/mlx-lm-deepgrove` .

#### Why

Chris explicitly asked for Maple as the auxiliary model because it targets Apple Silicon with an MLX focus . Generic `mlx_lm` was rejected after repeated Metal OOMs; the deepgrove fork is the first working Apple-Silicon path.

#### When

Set 2026-09-06 after stock llama.cpp and generic MLX paths failed under load.

#### Contested

Multiple Hermes turns declared Maple MLX unstable or impossible before the deepgrove fork proved a working serverless-style path via `generate()` and later server-mode with `--flash-head --trust-remote-code`. Hermes also tried Ornith and Nous free-tier aux as fallback options, which Chris did not accept as permanent replacements .

#### Evidence

- "I would rather you use Maple which does have an MLX and does seem to have a focus for Apple development. I want that one to be my auxiliary model" .
- "Maple MLX is stable as aux with the deepgrove fork" .

#### Related

- [[topics/turbofit/wiki/entities/maple.md|Maple]]
- [[topics/turbofit/wiki/decisions/main-model-selection.md|Main Model Selection]]
- [[topics/turbofit/wiki/comparisons/aux-runtime-options.md|Aux Runtime Options]]

### Candidate Quant Preference

Source: `wiki/decisions/candidate-quant-preference.md`

**Decision/Preference:** When comparing GGUF vs MLX for new local candidates, prefer the Q3 quant when model pages describe it as near base-model quality.

#### Rationale

Chris said: "They also have a lot to say about their quants on their pages too, check GGUF vs MLX, I like the Q3 quant that they said is near base model quality" .

#### Applies to

- Dirk: requested as `Dirk-Qwen3.8-27B-UD-Q3_K_XL.gguf` after GGUF repo correction.
- Nail: requested as `Nail-Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf`, but Chris wants GGUF vs MLX compared and would likely favor Q3 if near base quality.
- Tiel-Coder: queued as `Tiel-Coder-35B-A3B-UD-Q4_K_XL.gguf`; a Q3 path should be checked if the HuggingFace page supports it.
- Ornith: MLX 4-bit path was tested; no GGUF quant comparison completed.

#### Open

A reusable quant-selection rule for candidate research: if page notes say "near base quality", default to Q3; otherwise compare Q3 vs Q4_K_XL explicitly.

#### Related

- [[topics/turbofit/wiki/entities/dirk-qwen38-27b.md|Dirk Qwen 3.8 27B GGUF]]
- [[topics/turbofit/wiki/entities/nail-qwen36-35b.md|Nail Qwen 3.6 35B UD Q4_K_XL]]
- [[topics/turbofit/wiki/entities/tiel-coder.md|Tiel Coder]]
- [[topics/turbofit/wiki/entities/ornith-35b-mlx.md|Ornith 35B MLX]]
- [[topics/turbofit/wiki/queries/apple-silicon-runtime-benchmark|Apple Silicon Runtime Benchmark]]

### Context Sizing

Source: `wiki/decisions/context-sizing.md`

#### What

Local TurboFit contexts are set to 131,072 tokens for both main and aux .

#### Why

262k pre-fills slowly on a 32 GB M1 and stresses the Metal heap. Hermes compression timed out repeatedly at 270k+ tokens on the main model. 131k is the stable local sweet spot on this box .

#### When

Set 2026-09-06 after multiple compression timeout errors during end-to-end testing.

#### Evidence

- "put Qwen 3.8 27B at 131K and Maple at 131K" .
- "Context compression timed out before it could commit while the request was still approximately 270,285 tokens" .
- "131k is the stable sweet spot for this 32 GB box" .

#### Related

- [[topics/turbofit/wiki/decisions/main-model-selection.md|Main Model Selection]]
- [[topics/turbofit/wiki/decisions/aux-model-selection.md|Aux Model Selection]]
- [[topics/turbofit/wiki/concepts/compression-timeouts.md|Compression Timeouts]]

### Context Window Decision

Source: `wiki/decisions/context-window-decision.md`

**Decision**: Lock in 65K context as the stable daily driver on M1 MacBook 32GB, with 131K reserved for rare long-context needs where speed is not critical.

#### Decision Evidence

From in-session testing on 2026-09-07:
- MTPLX at 131K shows `OVERCOMMITTED` and `requested context 131072 exceeds the machine fit`
- Long-context generation shows severe degradation: 0.39 tok/s end-to-end vs 8-12 tok/s at 65K
- Memory plan shows `engine budget 24.0G, weights 19.3G` leaving insufficient room for 131K KV cache

#### Hardware Constraints

```
M1 MacBook 32GB unified memory:
- macOS + Hermes: ~8 GB
- Model weights (MTPLX): 19.3 GB  
- KV cache at 131K: ~8 GB
- Total needed: ~35 GB > 32 GB available
```

#### Speed Comparison

|| Context | MTPLX | Unleashed+DFlash2 |
| --- | --- | --- | --- |
|| 65K | 7-8 tok/s stable | ~5 tok/s |
|| 131K | 0.39 tok/s (observed) | 5 tok/s (with q8 KV) |

#### Why 65K is Daily Driver

1. **Stable throughput**: 7-8 tok/s vs 0.39 tok/s at 131K
2. **No OOM risk**: Memory fits comfortably
3. **Fast enough**: Meets the 10+ tok/s target is not physically achievable at 131K on this hardware

#### 131K as Fallback

131K context remains available for when long-context is essential (research, document summarization) and speed is not the priority.

#### Chris's Words

> "Stable 65K is the safe daily context on this box; 131K remains a long-context fallback despite throughput collapse."

#### Related

- [[topics/turbofit/wiki/entities/mplx-qwen-38-27b-optimized-speed.md|MPLX Qwen 3.8 27B Optimized Speed]]
- [[topics/turbofit/wiki/decisions/mtplx-main-provider.md|MPLX Main Provider]]
- [[topics/turbofit/wiki/entities/unleashed-27b.md|Unleashed 27B]]

### Fallback Model Order

Source: `wiki/decisions/fallback-model-order.md`

#### What

The active model preference order should preserve explicit user choice and avoid silently switching to `stepfun/step-3.7-flash:free` .

#### Why

Chris’s project state keeps breaking because Hermes flips the active model to StepFun 3.7 Flash. Two causes appear in the transcript: `model.default` not being first in the fallback chain, and `auxiliary.compression.provider: auto` selecting StepFun for compression .

#### When

Diagnosed 2026-09-06 02:20–02:25 UTC; config correction attempted in-session but Chris still saw later switches, including to `longcat-2.0:free` and `muse-spark-1.3-contributor-free` .

#### Evidence

- "my model keeps switching the step 3.7 flash And that keeps screwing out my project" .
- "The config has `model.default: z-ai/glm-5.3-flash` but the system message shows `anthropic/claude-fable-5.1` is active" .

#### Related

- [[topics/turbofit/wiki/concepts/model-switching-pain.md|Model Switching Pain]]
- [[topics/turbofit/wiki/decisions/main-model-selection.md|Main Model Selection]]

### TurboFit Local Main Provider Decision

Source: `wiki/decisions/local-main-provider.md`

What Chris wanted: the smartest feasible local runtime as Hermes main, with verified evidence, not just Hermes internal logs.

#### The candidate field
| Candidate | Notes |
| --- | --- |
| Ornith MLX 4-bit | Short-context fastest; deepest long-context compatibility tested on this box |
| MTPLX Qwen 3.8 27B | Stable 65K fallback; explicit 131K overcommit warnings on 32GB |
| Unleashed Q3_K_XL + DFlash2 | Safe long-context backup; flag mismatches caused repeated failures |
| Nail Q4_K_XL | Faster at 32K than 27B dense, but not usable at 131K |
| Tiel-Coder Q4_K_XL | Works at 65K, not confirmed stable at 131K |
| Dirk Q3_K_XL | Dense 27B; OOMs above 32K |
| Bonsai | Incomplete for MLX; GGUF needs llama.cpp; custom formats blocked |
| Colibri | Custom Maple format, incompatible with standard MLX server |
| Maple | Stable at 65K; OOM at 131K under load |
| FreeToken | Optional CUDA-13 MoE candidate, no in-session promotion |

^[raw/inbox/2026-09-07-from-senter-wiki.md]

#### Chris's last intent
Repeated messages on 2026-09-07 say Ornith should be configured into turbofit and set as main so he can continue with a smarter local model instead of weaker free ones. He accepted hardware limits: "10+ tok/s at 131K is not happening on M1 32GB."

#### Verified state
Ornith is configured as default in Hermes via `custom:turbofit`, but Hermes connection timeouts were still observed after repoint. A full Hermes restart remains needed to confirm the live route. Until that restart and a successful completion are observed, final promotion is contested.

#### Evidence standard
Final TurboFit evidence requires a real Hermes window capture plus the primary viewport/approval path, not only server logs or Hermes postcommit artifacts.

#### Related pages
- [[ornith-1-5-35b-a3b-mlx-4-bit|Ornith 1.5 35B-A3B MLX 4-bit]]
- [[turbo-fit-evidence-capture|TurboFit Evidence Capture]]

### Main Model Selection

Source: `wiki/decisions/main-model-selection.md`

#### What

Initial decision: Main inference and vision is Unleashed 27B + DFlash2 draft on `127.0.0.1:11606`, Metal, 131k context .

Updated 2026-09-07 after benchmark sweep: **Ornith MLX 4-bit** is the recommended main provider for daily driver use.

#### Why

Chris wants local fast-lane inference with vision capability. Unleashed holds the vision projector, so vision cannot be split from it .

However, benchmark evidence shows:
- **Ornith MLX 4-bit**: 28.5 tok/s short, 5.7 tok/s at 5K, MoE 35B (much faster)
- **Unleashed + DFlash2**: ~5 tok/s stable at 131K, but only when DFlash2 integrates correctly
- **Dirk Q3_K_XL**: 6.0 tok/s at 32K, OOM above

#### Contested Evidence

Hermes summary later claimed MTPLX is the locked main provider on `:11613`, while command evidence showed repeated 131K overcommit warnings and `-9` exits .

Multiple provider switches occurred during the session:
1. MTPLX Qwen 3.8 Optimized Speed locked in at 65K (unstable at 131K)
2. Reverted to Unleashed+DFlash2 after MTPLX crashes
3. Final recommendation: Ornith MLX 4-bit as primary

#### Final Recommendation

**Lock in Ornith MLX 4-bit** as main provider at 65K context:
- Speed: 28.5 tok/s short-context
- Stability: No OOM at 65K
- Fallback: Unleashed + DFlash2 at 131K for long-context needs

#### Related

- [[topics/turbofit/wiki/entities/unleashed-27b.md|Unleashed 27B]]
- [[topics/turbofit/wiki/entities/ornith-35b-mlx.md|Ornith 35B MLX]]
- [[topics/turbofit/wiki/entities/mplx.md|MPLX]]
- [[topics/turbofit/wiki/entities/mtplx-qwen-38-27b-optimized-speed.md|MPLX Qwen 3.8 27B]]
- [[topics/turbofit/wiki/decisions/context-window-decision.md|Context Window Decision]]

### MT_PlX Main Provider

Source: `wiki/decisions/mtplx-main-provider.md`

Make `Youssofal/Qwen3.8-27B-MTPLX-Optimized-Speed` via `mtplx serve` the main TurboFit provider and remove Maple/Unleashed as co-resident models to reclaim disk space.

#### Decision Context

Initial configuration used MTPLX at 131K context, but memory overcommit caused instability:
- `mtplx serve` with `--context-window 131072` prints `OVERCOMMITTED`
- Long prompts at 131K showed `507 Insufficient Storage` errors
- End-to-end throughput dropped to 0.39 tok/s

#### Transition Path

1. Initial attempt: MTPLX at 131K → unstable under load
2. Cleanup: Removed Maple (53GB) and Unleashed Q3_K_XL (23GB)
3. Final config: MTPLX at 65K context (stable 7-12 tok/s)

#### Final Configuration

```yaml
providers:
  turbofit:
    api: http://127.0.0.1:11613/v1
    default_model: mtplx-qwen38-27b-optimized-speed
    
model:
  default: ornith-1-5-35a3b-mlx  # Later switched to Ornith
  provider: custom:turbofit
```

#### Status

- **2026-09-07 00:56**: MTPLX locked in as main provider at 65K context
- **2026-09-07 01:00**: Final state confirmed - MTPLX stable at 65K
- **2026-09-07 03:03**: Switched to Unleashed+DFlash2 after performance issues with MTPLX at 131K
- **2026-09-07 06:18**: Ornith MLX selected as winner and locked in

#### The Ornith Override

After extensive testing comparing:
- Ornith MLX 4-bit: 28.5 tok/s short, 5.7 tok/s at 5K
- Nail Q4_K_XL: 23.4 tok/s short, 4.7 tok/s at 5K
- Tiel-Coder Q4_K_XL: 23.1 tok/s short, 4.2 tok/s at 5K

Ornith was selected as the main provider because:
1. Only model that works at 131K context
2. Best short-context speed (28.5 tok/s)
3. Good long-context throughput

#### Related

- [[topics/turbofit/wiki/decisions/context-window-decision.md|Context Window Decision]]
- [[topics/turbofit/wiki/entities/mplx-qwen-38-27b-optimized-speed.md|MPLX Qwen 3.8 27B Optimized Speed]]
- [[topics/turbofit/wiki/entities/ornith-35b-mlx.md|Ornith 35B MLX]]

## Visual Reference

![Model Ladder](assets/scaling-ladder.png)

![Provider Integration](assets/provider-integration.png)

![Hermes Settings](assets/hermes-desktop-turbofit-settings.png)

![Speculative Decode](assets/turbofit-2.4-spec-decode.png)

## Rules

### Rule 1: Model + KV Cache ≤ Tier Size

**The fit equation:** `model_size (quant) + KV_cache ≤ tier_size`

- KV cache at 262K context with q8_0 KV ≈ 2-4GB for most models
- Comfortable fit: `model_size + 2GB ≤ tier_size`
- If model doesn't fit in a tier, drop to smaller quant or mark as "doesn't fit"

### Rule 2: IQ3_S is the Default

**Near-lossless quantization:** IQ3_S is recommended for all tiers where it fits.

- Only move to FP16 at 64GB+ when you have the VRAM and want every last %
- FP16 only at 64GB+ — never recommend FP16 at lower tiers
- GPU tiers ≤16GB assume system RAM for MoE offload and KV cache

### Rule 3: Evidence Before Winner

**No model is a TurboFit winner without physical campaign proof.**

- Catalog entries are **candidates** until the physical campaign passes
- Compile, download, or estimated fit is NOT a winner
- Evidence must come from actual benchmark runs on the target hardware
- Hermes window capture required for contested results (not just internal logs)

---

## Skills

### Hermes Skills for Turbofit

| Skill | Location | Description |
| --- | --- | --- |
| turbofit | `skills/turbofit/SKILL.md` | Rules for Turbofit Wiki - use when editing |
| turbofit-runtime-setup | `skills/turbofit-runtime-setup/SKILL.md` | Setting up or fixing Turbofit local runtime |
| turbo-model-store-cleanup | `skills/turbo-model-store-cleanup/SKILL.md` | Freeing storage before/after candidate sweeps |
| candidate-quant-comparison | `skills/candidate-quant-comparison/SKILL.md` | Comparing candidate model quantizations |
| turbo-artifact-download-spec | `skills/turbo-artifact-download-spec/SKILL.md` | Artifact download specifications |
| maple-mlx-server-runtime | `skills/maple-mlx-server-runtime/SKILL.md` | Maple MLX server runtime management |
| dflash2-fork-flag-boundary | `skills/dflash2-fork-flag-boundary/SKILL.md` | DFlash2 fork flag compatibility |
| mtplx-32gb-macos-tuning | `skills/mtplx-32gb-macos-tuning/SKILL.md` | MTPLX 32GB macOS memory tuning |
| turbofit-macos-setup | `skills/turbofit-macos-setup.md` | Turbofit macOS setup |
| speedometer-menu-design | `skills/speedometer-menu-design.md` | Speedometer menu UI design |
| turbo-fit-evidence-capture | `skills/turbo-fit-evidence-capture/SKILL.md` | Evidence capture for TurboFit |

### Related Hermes Skills

| Skill | Description |
| --- | --- |
| agent-wiki-vault | Agent-wiki Obsidian vault workflow |
| hermes-agent | Hermes Agent usage and configuration |
| hermes-fleet-ops | Bot fleet operations |
| hermes-update | Updating Hermes |
| github | GitHub via gh CLI |
| github-pr-workflow | GitHub PR lifecycle |
| github-repo-management | Repo management |
| xlsx | Excel/CSV operations |
| pdf | PDF operations |
| docx | Word document operations |
| weekly-review-planning | Weekly review and planning |

---

## Absorbed Topics

- `turbohaul-llmfit` — Generate optimized llama-server launch strings (absorbed 2026-09-02; was DORMANT)
- `turbohaul-manager` — Ollama-shape inference manager (absorbed 2026-09-02; was DORMANT)
- `southpaw-turbohaul` — Curated model server for Nous Research (absorbed 2026-09-02; was DORMANT)
- `sirvir` — GitHub-current TurboFit support for Hermes (absorbed 2026-09-02; was ACTIVE)

