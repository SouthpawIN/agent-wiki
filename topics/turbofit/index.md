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

# Turbofit Wiki

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

## WIKI

### CONTEXT

This section covers HOW TurboFit works: architecture, runtime selection, provider configuration, and the integration paths that make local inference stable.

#### Runtime Selection

TurboFit supports multiple inference backends. Selection depends on platform and model:

| Runtime | Platform | Models | Speed | Notes |
| --- | --- | --- | --- | --- |
| **llama.cpp** (dflash2 fork) | Omarchy, MacBook | Unleashed 27B, DeepSeek V4.1 | 70-85 tok/s (Omarchy GPU) | Full DFlash2 draft support |
| **llama.cpp** (stock) | Omarchy, MacBook | Most GGUF models | Varies | No DFlash2 support |
| **MTPLX** | MacBook (M1) | Qwen 3.8, Unleashed | 12.4 tok/s short, 7-12 tok/s at 65K | Memory guard at 131K |
| **MLX** | MacBook (M1) | Ornith 1.5, Maple | 28.5 tok/s short | Apple-native, fastest on M1 |

#### Hermes Provider Integration

TurboFit registers as `custom:turbofit` in Hermes Agent. Configuration is in `config.yaml`:

```yaml
provider: custom:turbofit
model: auto
```

**Auto mode** scans available hardware and selects the best model from the TurboFit List. Manual selection locks a specific model.

#### Model + Context Sizing

Local contexts are set to **131,072 tokens** as the stable sweet spot. Evidence:
- 262K+ pre-fills slowly on M1 32GB and stresses Metal heap
- Hermes compression timed out repeatedly at 270K+ tokens on main model
- 131K is the tested stable configuration on the MacBook

On Omarchy (256GB+ VRAM), 262K+ contexts are viable with DFlash2 draft models.

#### Provider Fallback Order

To prevent silent switching to cloud providers:

1. `model.default` must be first in the fallback chain
2. `auxiliary.compression.provider` pinned to local TurboFit route
3. Cloud fallback only for tasks exceeding local memory budget

This addresses the Hermes auto-route stability issue where `stepfun/step-3.7-flash:free` was selected without explicit choice.

#### DFlash2 Speculative Decoding

DFlash2 is a draft model for accelerating long-context inference. Key facts:

- **Only works with llama.cpp** (dflash2 fork), not MTPLX or MLX
- **Incompatible with MTPLX**: MTPLX uses native MLX MTP heads; DFlash2 is CUDA/llama.cpp only
- **Valid flags**: `--spec-draft-model`, `--spec-draft-ngl 999`, `--spec-draft-n-max 7`, `--spec-type draft-dflash`
- **Invalid flags** that fail: `--draft-model`, `--draft-ngl`, `--draft-ctx-size`, `--low-vram`, `--model-draft`

#### Memory Management

**MTPLX Memory Guard** — emits `prefill_admission_shed` events when a prompt would exceed memory threshold, clearing KV cache to stay under limit.

**Unleashed IQ3_XXS** — failed to load with `tensor 'blk.2.attn_qkv.weight' data is not within the file bounds`. This quant is not usable on the dflash2 fork.

**Crash pattern**: `mtplx serve` exits with code -9 when memory plan is marked `OVER`. Exit code 1 with `RuntimeError: [METAL] Command buffer execution failed: Insufficient Memory` during MTP injection.

#### Verifier Bridge

`turbofit-verifier` drives verification through `desktop_preview` on a real Hermes window instead of summary claims.

#### Model Zoo

> All models discovered during research. ★ = on TurboFit List.

| Model | Type | System | Parameters | AIME26 | GPQA-D | DeepSWE | LCBv6 | TB4.0 | HuggingFace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [[Maple Preview]] ★ | Aux LLM (Ternary MoE) | Omarchy | 20B-A1B | 87.5% | 73.5% | - | 75.1% | - | [maple-preview](https://huggingface.co/deepgrove/maple-preview) |
| [[Cyber Tiel Coder]] ★ | Code LLM (MoE) | Omarchy, MacBook | 35B-A3B | - | - | - | - | - | [Cyber-Tiel-Coder-GGUF](https://huggingface.co/peculiar-ragdoll/Cyber-Tiel-Coder-35B-A3B-GGUF-MTP) |
| [[Qwen 3.8 GSQ-RCO]] ★ | LLM (Quantized) | Omarchy | 27B | - | 89.2% | 42.2% | 90.3% | - | [GSQ-RCO-GGUF](https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF) |
| [[Qwen 3.8 Flash Next]] ★ | MoE (Qwen4 Preview) | Omarchy | 180B / 6B | - | 91.7% | 58.7% | 91.9% | - | [Flash-Next-GSQ-RCO](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF) |
| [[DeepSeek V4.1 Flash]] ★ | MoE | Omarchy | 763B / 16B | - | 90.9% | 74.2% | - | 31.2% | [V4.1-Flash-GGUF](https://huggingface.co/vcruz305/DeepSeek-V4.1-Flash-GGUF) |
| [[Ace Step 1.5]] | Music Generation | Omarchy | 4B | - | - | - | - | - | [ACE-Step-1.5-GGUF](https://huggingface.co/ACE-Step/ACE-Step-1.5-GGUF) |
| [[Bonsai 27B]] | LLM (Ternary) | Omarchy | 27B | - | - | - | - | - | [Bonsai-27B-gguf](https://huggingface.co/prism-ml/Bonsai-27B-gguf) |
| [[Cosmos 37B]] | LLM | Omarchy | 37B | - | - | - | - | - | [Cosmos-37b-BASE-i1-GGUF](https://huggingface.co/mradermacher/Cosmos-37b-BASE-i1-GGUF) |
| [[Cyber Tiel Coder MTP]] | Code LLM (MTP) | Omarchy | 35B-A3B | - | - | - | - | - | [Cyber-Tiel-MTP](https://huggingface.co/peculiar-ragdoll/Cyber-Tiel-Coder-35B-A3B-GGUF-MTP) |
| [[DAXZEIT GRM]] | Reasoning LLM (MTP) | Omarchy | 27B | - | - | - | - | - | [DAXZEIT-GRM-2.6-Plus-MTP](https://huggingface.co/mradermacher/DAXZEIT_GRM_2.6-Plus-0628-MTP-reasoning-i1-GGUF) |
| [[NVIDIA Nemotron 3.5]] | Enterprise LLM (MoE) | Omarchy | 30B-A3B | - | - | - | - | - | [NVIDIA-Nemotron-3.5-Lightning-30B-A3B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF) |
| [[Qwen 3.8 Unleashed]] | General LLM | Omarchy, MacBook | 27B | - | - | - | - | - | [Qwen3.8-Unleashed-GGUF](https://huggingface.co/outsourc-e/Qwen3.8-27B-Unleashed-GGUF) |
| [[Super Qwen]] | Uncensored LLM | Omarchy | 27B | - | - | - | - | - | [SuperQwen3.8-27b-abliterated](https://huggingface.co/Jiunsong/SuperQwen3.8-27b-abliterated-GGUF) |
| [[Qwen 2.5 Omni]] | Multimodal VLM | Omarchy | 3B | - | - | - | - | - | [Qwen2.5-Omni-3B](https://huggingface.co/unsloth/Qwen2.5-Omni-3B-GGUF) |
| [[Soprano]] | Creative Micro | Omarchy | 80M | - | - | - | - | - | [Soprano-1.1-80M](https://huggingface.co/WalkingCat/Soprano-1.1-80M-GGUF) |
| [[Qwen 3.8 Base]] | Base LLM | Omarchy, MacBook | 27B | - | - | - | - | - | [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) |
| [[Ornith 1.5]] | Code LLM (Legacy) | MacBook | 35B-A3B | - | - | - | - | - | [Ornith-1.5-35B-A3B](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B) |

> **Note:** GSQ-RCO IQ3_S scores shown (AIME25 100%, GPQA-D 89.2%, DeepSWE 42.2%, LCBv6 90.3%). Maple LCBv6 score is from LiveCodeBench v6.

#### TurboFit List

##### Agentic Model Lineup

| Model | Tok/s | Parameters | Best For |
| --- | --- | --- | --- |
| [[Maple Preview]] | 218 tok/s (MTPLX M4) | 20B-A1B | Aux/compression tasks |
| [[Cyber Tiel Coder]] | 23 tok/s (MacBook 65K) | 35B-A3B | Code generation |
| [[Qwen 3.8 GSQ-RCO]] | 85 tok/s (Omarchy GPU) | 27B | Daily driver, reasoning |
| [[Qwen 3.8 Flash Next]] | 70-85 tok/s (Omarchy GPU) | 180B / 6B | Maximum capability |
| [[DeepSeek V4.1 Flash]] | TBD | 763B / 16B | Next-gen capability |

##### Fit Calculation System

###### GPU (NVIDIA/AMD VRAM)

| Tier | Model | Quant | Context | Flags | Tok/s | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| <8 GB | Maple | IQ3_S | 131K | `--ctx-size 131072 --n-gpu-layers 999 --mlock` | ~10 tok/s | SSD streaming |
| 16-64 GB | GSQ-RCO | IQ3_S | 262K | `--ctx-size 262144 --n-gpu-layers 999 --mlock` | ~85 tok/s | Near-lossless |
| 96+ GB | Flash Next | IQ3_XXS | 524K | `--ctx-size 524288 --n-gpu-layers 999 --mlock` | TBD | |
| 256 GB | DeepSeek V4.1 | FP8 | 1M | `--ctx-size 1048576 --n-gpu-layers 999 --mlock` | TBD | |

###### CPU (System RAM)

| Tier | Model | Quant | Context | Flags | Tok/s | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| <8 GB | Maple | IQ3_S | 65K | `--ctx-size 65536 --no-mmap --mlock` | ~8 tok/s | Minimum viable |
| 16-48 GB | Cyber-Tiel | IQ3_S | 262K | `--ctx-size 262144 --no-mmap --mlock` | ~23 tok/s | MoE, 3B active |
| 64 GB | GSQ-RCO | IQ3_S | 262K | `--ctx-size 262144 --no-mmap --mlock` | ~12 tok/s | Low power |

###### Unified Memory (Apple Silicon)

| Tier | Model | Quant | Context | Engine | Tok/s | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| <8 GB | Maple | IQ3_S | 65K | MTPLX | 218 tok/s (M4) | |
| 16-48 GB | Cyber-Tiel | IQ3_S | 262K | MTPLX | ~23 tok/s (MacBook) | |
| 64 GB | GSQ-RCO | IQ3_S | 262K | MTPLX | ~8-12 tok/s (65K) | |

#### Key Concepts

##### 131K Deferred Candidates

Newly downloaded candidate artifacts not benchmarked at 131K because model-plus-KV exceeds 32GB Mac fit before testing begins.

##### Benchmark Taxonomy

| Tier | Use Case | Models |
| --- | --- | --- |
| Daily Driver | Short-context speed | Ornith MLX (28.5 tok/s) |
| Long Context | 131K stable | Unleashed + DFlash2 (~5 tok/s) |
| High Capability | Maximum quality | DeepSeek V4.1 Flash |
| Aux/Compression | Background tasks | Maple Preview |

##### Speculative Decoding Architectures

| Architecture | Runtimes | Draft Type | Speed Boost |
| --- | --- | --- | --- |
| DFlash2 | llama.cpp fork | Diffusion-based | ~1.5-2x |
| MTP (Multi-Token) | MLX, llama.cpp | Native heads | ~2x |
| MTPLX | MTPLX only | Native MLX MTP | ~2.5x |

##### Hermes Auto Route Stability

See Issues section for problem details and resolution.

##### Model Selection Decision Tree

```
Start
  ├─ Need vision? → Unleashed 27B (only model with projector)
  ├─ Need speed at 65K? → Ornith MLX 4-bit (28.5 tok/s)
  ├─ Need 131K long context? → Unleashed + DFlash2 on llama.cpp
  └─ Need max capability? → DeepSeek V4.1 Flash on Omarchy
```

#### Decisions

##### Aux Model Selection

**Maple Preview** selected for aux/compression tasks. Reasoning ON by default; token budgets sized for thinking models (4000+).

##### Candidate Quant Preference

**IQ3_S is the default recommendation** for all tiers where it fits (near-lossless, runs on less power). Only move to FP16 at 64GB+ when you have the VRAM and want every last %.

##### Context Sizing

Local TurboFit contexts are set to **131,072 tokens** for both main and aux.

**Why:** 262k pre-fills slowly on 32GB M1 and stresses Metal heap. Hermes compression timed out repeatedly at 270K+ tokens.

**Evidence:**
- "put Qwen 3.8 27B at 131K and Maple at 131K"
- "Context compression timed out before it could commit while the request was still approximately 270,285 tokens"
- "131k is the stable sweet spot for this 32 GB box"

##### Context Window Decision

**131K native, 262K native, 1M with YaRN extrapolation** depending on hardware tier.

##### Fallback Model Order

The active model preference order should preserve explicit user choice and avoid silently switching to `stepfun/step-3.7-flash:free`.

**Root cause:** `model.default` not first in fallback chain + `auxiliary.compression.provider: auto` selecting cloud.

**Fix:** Pin compression to local route; ensure `model.default` is first.

##### TurboFit Local Main Provider Decision

**Lock in Qwen 3.8 GSQ-RCO IQ3_S** as the recommended main provider for daily driver use on Omarchy and MacBook.

**Evidence:**
- Omarchy GPU: 85 tok/s at 262K context
- MacBook: 23 tok/s at 65K context
- Near-lossless IQ3_S quantization

##### Main Model Selection

Initial decision: Unleashed 27B + DFlash2 draft on `127.0.0.1:11606`, Metal, 131K context.

Updated 2026-09-07 after benchmark sweep: **Qwen 3.8 GSQ-RCO** is the recommended main provider for daily driver use.

**Evidence:**
- **Ornith MLX 4-bit**: 28.5 tok/s short-context
- **GSQ-RCO IQ3_S**: 85 tok/s on Omarchy GPU
- **Unleashed + DFlash2**: ~5 tok/s stable at 131K

##### MT_PlX Main Provider

MTPLX is an alternative runtime for M1 Macs. Use 65K context for stable operation. 131K triggers memory-guard events.

### CONTINUATION

#### Issues & Roadblocks

##### Hermes Model Switching

**Problem:** Hermes flips active model to StepFun 3.7 Flash without explicit user choice.

**Root cause:** `model.default` not first in fallback chain + `auxiliary.compression.provider: auto` selecting cloud.

**Fix:** Pin `auxiliary.compression.provider` to local TurboFit route; ensure `model.default` is first.

##### Compression Timeouts

At 262K+ tokens on the main model, Hermes compression timed out before committing. Resolved by capping context at 131K on M1 32GB.

##### MTPLX 131K Instability

MTPLX at 131K context triggers memory-guard events and crashes. Use 65K for stable MTPLX operation. 131K long-context needs llama.cpp + DFlash2 instead.

##### MPLX Service Args

`mtplx serve` does not accept `--memory-budget 32GB`. Only documented flags are accepted; undocumented flags exit with `unrecognized arguments`.

##### DFlash2 Port Conflicts

`couldn't bind HTTP server socket, hostname: 127.0.0.1, port: 11606` — port already in use. Not a model issue, a port conflict.

##### DFlash2 Flag Incompatibilities

Stock llama.cpp flags (`--draft-model`, `--draft-ngl`, `--low-vram`) do not work with the dflash2 fork. Use the spec-flagged variants instead.

##### Unleashed IQ3_XXS Corruption

`Qwen3.8-27B-Unleashed-UD-IQ3_XXS.gguf` failed to load with `tensor 'blk.2.attn_qkv.weight' data is not within the file bounds`. This quant is not usable on the dflash2 fork.

#### Visual Reference

`topics/turbofit/wiki/models/leaderboard.html` — live model benchmark charts.

#### Rules

1. **Model + KV Cache ≤ Tier Size** — never recommend a model that doesn't fit
2. **IQ3_S is the Default** — near-lossless, runs on less power
3. **Evidence Before Winner** — every claim needs a source

#### Absorbed Topics

Topics that have been fully resolved and merged into the wiki:
- Nail Qwen 3.6 35B — deprioritized for GSQ-RCO
- Colibri — incompatible custom architecture, deprioritized
- Bonsai MLX — research complete, no integration path forward

---

## SKILLS

Topic skills stored in this wiki at `topics/turbofit/skills/`:

- **[candidate-quant-comparison](skills/candidate-quant-comparison/SKILL.md)** — Use when evaluating new local TurboFit candidates. Compare GGUF vs MLX artifacts and prefer Q3 when page notes say near base quality.
- **[dflash2-fork-flag-boundary](skills/dflash2-fork-flag-boundary/SKILL.md)** — Use when testing DFlash2 speculative decoding with the dflash2-llama.cpp fork. Record the exact flag set that succeeds/fails to avoid retrying invalid combinations.
- **[maple-mlx-server-runtime](skills/maple-mlx-server-runtime/SKILL.md)** — Use when running or testing Maple MLX on Apple Silicon for Hermes aux or compression. Use deepgrove-ai fork flags and cache limits; avoid generic mlx_lm server mode.
- **[mtplx-32gb-macos-tuning](skills/mtplx-32gb-macos-tuning/SKILL.md)** — Use when tuning MTPLX on 32GB macOS. Check runtime config instead of unsupported CLI flags; validate context window against machine-bound memory plan before relying on tok/s claims.
- **[turbo-artifact-download-spec](skills/turbo-artifact-download-spec/SKILL.md)** — Use when downloading new TurboFit GGUF/MLX candidate artifacts. Build a reproducible curl-backed download record with size verification and wiki-ready evidence.
- **[turbo-fit-evidence-capture](skills/turbo-fit-evidence-capture/SKILL.md)** — Use when capturing TurboFit performance or behavior evidence. Capture from Chris's actual Hermes window using desktop_preview, never from process metadata or postcommit summaries.
- **[turbo-model-store-cleanup](skills/turbo-model-store-cleanup/SKILL.md)** — Use when freeing TurboFit storage. Delete only wiki-marked obsolete artifacts.

Related skills stored globally in `~/.hermes/skills/`:

- **[turbofit](https://github.com/NousResearch/hermes-agent)** — Rules for Turbofit Wiki
- **[turbofit-runtime-setup](https://github.com/NousResearch/hermes-agent)** — Use when setting up or fixing the Turbofit local runtime
- **[serving-llms-vllm](https://github.com/NousResearch/hermes-agent)** — vLLM: high-throughput LLM serving
- **[llama-cpp](https://github.com/NousResearch/hermes-agent)** — llama.cpp local GGUF inference + HF Hub model discovery
- **[huggingface-hub](https://github.com/NousResearch/hermes-agent)** — HuggingFace hf CLI: search/download/upload models, datasets

---

## BOTS

Bots stored in this wiki at `topics/turbofit/agents/`:

- **[candidate-benchmark-scout](agents/candidate-benchmark-scout.md.proposed)** — Proposed: Discovers and benchmarks new model candidates from HuggingFace
- **[mtplx-runtime-scout](agents/mtplx-runtime-scout.md.proposed)** — Proposed: Monitors MTPLX runtime stability and performance
- **[orchestrator](agents/orchestrator.md.proposed)** — Proposed: Coordinates multi-model TurboFit pipeline
- **[turbofit-benchmark](agents/turbofit-benchmark.md.proposed)** — Proposed: Automated benchmark runner for TurboFit models
- **[turbofit-bot](agents/turbofit-bot.md.proposed)** — Proposed: General-purpose TurboFit topic bot
- **[turbofit-evidence-capture](agents/turbofit-evidence-capture.md.proposed)** — Proposed: Captures performance evidence from live Hermes sessions
- **[turbofit-launcher](agents/turbofit-launcher.md.proposed)** — Proposed: Manages model launch and context sizing
- **[turbofit-route-stabilizer](agents/turbofit-route-stabilizer.md.proposed)** — Proposed: Prevents Hermes from switching to cloud providers
- **[turbofit-runtime-scout](agents/turbofit-runtime-scout.md.proposed)** — Proposed: Scouts runtime stability across platforms
- **[turbofit-verifier](agents/turbofit-verifier.md.proposed)** — Proposed: Verification bot using desktop_preview for evidence

---

## LOOPS

Loops stored in this wiki at `topics/turbofit/loops/`:

- **[131k-attempt-blocker](loops/131k-attempt-blocker.md.proposed)** — Proposed: Blocks 131K context attempts that would OOM
- **[candidate-65k-benchmark-sweep](loops/candidate-65k-benchmark-sweep.md.proposed)** — Proposed: Sweep benchmarks all candidates at 65K
- **[candidate-quant-comparator](loops/candidate-quant-comparator.md.proposed)** — Proposed: Compares quant variants for each candidate
- **[compression-timeout-watch](loops/compression-timeout-watch.md.proposed)** — Proposed: Watches for Hermes compression timeouts
- **[hermes-model-change-detector](loops/hermes-model-change-detector.md.proposed)** — Proposed: Detects and reports Hermes model switches
- **[mac-memory-watch](loops/mac-memory-watch.md.proposed)** — Proposed: Monitors memory usage on macOS
- **[mtplx-telemetry-watch](loops/mtplx-telemetry-watch.md.proposed)** — Proposed: Watches MTPLX memory-guard events
- **[turbo-context-budget-watch](loops/turbo-context-budget-watch.md.proposed)** — Proposed: Monitors context window vs memory budget
- **[turbofit-candidate-discovery](loops/turbofit-candidate-discovery.md.proposed)** — Proposed: Discovers new model candidates from HuggingFace
- **[turbofit-health-check](loops/turbofit-health-check.md.proposed)** — Proposed: Periodic health check of all TurboFit runtimes
- **[turbofit-memory-monitor](loops/turbofit-memory-monitor.md.proposed)** — Proposed: Monitors model memory usage across devices
- **[turbofit-memory-threshold-monitor](loops/turbofit-memory-threshold-monitor.md.proposed)** — Proposed: Alerts when memory approaches threshold
- **[turbofit-runtime-watch](loops/turbofit-runtime-watch.md.proposed)** — Proposed: Watches all runtime processes for crashes
