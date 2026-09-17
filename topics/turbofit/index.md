---
title: Turbofit Wiki
created: 2026-09-16
updated: 2026-09-16
type: wiki
sources:
  - index.md
  - BRIEF.md
  - README.md
  - wiki/models/
  - wiki/entities/
  - wiki/concepts/
  - wiki/decisions/
  - wiki/comparisons/
  - wiki/queries/
---

---

## Overview

**Turbofit** is a first-class [Hermes Agent](https://github.com/NousResearch/hermes-agent) provider and adaptive local-inference runtime.

> **GitHub:** [SouthpawIN/Turbofit](https://github.com/SouthpawIN/turbofit) · ACTIVE · MIT License

It inventories physical compute and total usable memory, recommends an evidence-backed ladder, launches a native backend, and exposes one OpenAI-compatible endpoint.

```text
provider: custom:turbofit
model: auto
```

**TurboFit Check** scans the machine — dedicated VRAM, unified/integrated memory, or RAM-only — and applies Auto or a selected compatible lane.

## Integrations

### Repositories

| Repo | Link | Status | Stars |
| --- | --- | --- | --- |
| turbofit | [github.com/SouthpawIN/turbofit](https://github.com/SouthpawIN/turbofit) | ACTIVE | 83 |
| turbohaul-llmfit | [github.com/SouthpawIN/turbohaul-llmfit](https://github.com/SouthpawIN/turbohaul-llmfit) | DORMANT | 2 |
| turbohaul-manager | [github.com/SouthpawIN/turbohaul-manager](https://github.com/SouthpawIN/turbohaul-manager) | DORMANT | 1 |
| southpaw-turbohaul | [github.com/SouthpawIN/southpaw-turbohaul](https://github.com/SouthpawIN/southpaw-turbohaul) | DORMANT | 7 |
| sirvir | [github.com/SouthpawIN/sirvir](https://github.com/SouthpawIN/sirvir) | ACTIVE | 27 |

### HuggingFace Models

| Model | Repository |
| --- | --- |
| Maple Preview | [deepgrove/maple-preview](https://huggingface.co/deepgrove/maple-preview) |
| Cyber Tiel Coder | [peculiar-ragdoll/...](https://huggingface.co/peculiar-ragdoll/Cyber-Tiel-Coder-35B-A3B-GGUF-MTP) |
| Qwen 3.8 GSQ-RCO | [ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF](https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF) |
| Qwen 3.8 Flash Next | [ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF) |
| DeepSeek V4.1 Flash | [vcruz305/DeepSeek-V4.1-Flash-GGUF](https://huggingface.co/vcruz305/DeepSeek-V4.1-Flash-GGUF) |

---



---

## Model Zoo

> All models discovered during research. ★ = on TurboFit List.

| Model | Type | System | Parameters | AIME26 | GPQA-D | DeepSWE | LCBv6 | TB4.0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [[Maple Preview]] ★ | Aux LLM (Ternary MoE) | Omarchy | 20B-A1B | 87.5% | 73.5% | - | 75.1% | - |
| [[Cyber Tiel Coder]] ★ | Code LLM (MoE) | Omarchy, MacBook | 35B-A3B | - | - | - | - | - |
| [[Qwen 3.8 GSQ-RCO]] ★ | LLM (Quantized) | Omarchy | 27B | - | 89.2% | 42.2% | 90.3% | - |
| [[Qwen 3.8 Flash Next]] ★ | MoE (Qwen4 Preview) | Omarchy | 180B / 6B | - | 91.7% | 58.7% | 91.9% | - |
| [[DeepSeek V4.1 Flash]] ★ | MoE | Omarchy | 763B / 16B | - | 90.9% | 74.2% | - | 31.2% |
| [[Ace Step 1.5]] | Music Generation | Omarchy | 4B | - | - | - | - | - |
| [[Bonsai 27B]] | LLM (Ternary) | Omarchy | 27B | - | - | - | - | - |
| [[Cosmos 37B]] | LLM | Omarchy | 37B | - | - | - | - | - |
| [[Cyber Tiel Coder MTP]] | Code LLM (MTP) | Omarchy | 35B-A3B | - | - | - | - | - |
| [[DAXZEIT GRM]] | Reasoning LLM (MTP) | Omarchy | 27B | - | - | - | - | - |
| [[NVIDIA Nemotron 3.5]] | Enterprise LLM (MoE) | Omarchy | 30B-A3B | - | - | - | - | - |
| [[Qwen 3.8 Unleashed]] | General LLM | Omarchy, MacBook | 27B | - | - | - | - | - |
| [[Super Qwen]] | Uncensored LLM | Omarchy | 27B | - | - | - | - | - |
| [[Qwen 2.5 Omni]] | Multimodal VLM | Omarchy | 3B | - | - | - | - | - |
| [[Soprano]] | Creative Micro | Omarchy | 80M | - | - | - | - | - |
| [[Qwen 3.8 Base]] | Base LLM | Omarchy, MacBook | 27B | - | - | - | - | - |
| [[Ornith 1.5]] | Code LLM (Legacy) | MacBook | 35B-A3B | - | - | - | - | - |

> **Note:** GSQ-RCO IQ3_S scores shown (AIME25 100%, GPQA-D 89.2%, DeepSWE 42.2%, LCBv6 90.3%). Maple LCBv6 score is from LiveCodeBench v6.

---

## TurboFit List

> 5 models suitable for running Hermes Agent locally. Ordered by capability.

| Order | Model | Type | Parameters | Optimal Quant | Size | AIME26 | GPQA-D | DeepSWE | LCBv6 | TB4.0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | **Maple Preview** | Ternary MoE | 20B-A1B | TQ2_0-head-Q4_K | 5.5 GiB | 87.5% | 73.5% | - | 75.1% | - |
| 2 | **Cyber Tiel Coder** | Code LLM (MoE) | 35B-A3B | UD-Q4_K_XL | 22.4 GiB | - | - | - | - | - |
| 3 | **Qwen 3.8 GSQ-RCO** | LLM (Quantized) | 27B | IQ3_S | 11.8 GiB | - | 89.2% | 42.2% | 90.3% | - |
| 4 | **Qwen 3.8 Flash Next** | MoE (Qwen4 Preview) | 180B / 6B | IQ3_XXS | 47 GiB | - | 91.7% | 58.7% | 91.9% | - |
| 5 | **DeepSeek V4.1 Flash** | MoE | 763B / 16B | FP8 / UD-Q4_K_XL | 160 / ~40 GiB | - | 90.9% | 74.2% | - | 31.2% |

> **Note:** GSQ-RCO IQ3_S benchmark scores (AIME25 100%, GPQA-D 89.2%, DeepSWE 42.2%, LCBv6 90.3%) are from the model card. Maple LCBv6 score is from LiveCodeBench v6.

### Fit Calculation System

```
Required: model_size + KV_cache ≤ tier_size
KV_cache ≈ 2-4GB at 262K context (q8_0 KV)
Comfortable: model_size + 2GB ≤ tier_size
```

### GPU (NVIDIA/AMD VRAM — ≤16GB assumes system RAM available for MoE offload and KV cache)

| Tier | Model | Quant | Size | VRAM Used | Context | Engine | Flags | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <8 GB | Maple | TQ2_0 | 5.5 GiB | ~6 GiB | 131K native, 262K w/ RoPE | llama.cpp | `--ctx-size 262144 --n-gpu-layers 999 --mlock` | SSD streaming via ssdmoe. System RAM for KV cache. |
| 16 GB | GSQ-RCO | IQ3_S | 11.8 GiB | ~12 GiB | 131K-262K | llama.cpp | `--ctx-size 262144 --n-gpu-layers 999 --mlock` | Near-lossless. Cyber-Tiel Q3_K_M also fits (~14 GiB). |
| 24 GB | GSQ-RCO | IQ3_S | 11.8 GiB | ~12 GiB | 262K | llama.cpp | `--ctx-size 262144 --n-gpu-layers 999 --mlock` | Same near-lossless model, more KV headroom |
| 32 GB | GSQ-RCO | IQ3_S | 11.8 GiB | ~12 GiB | 262K+ | llama.cpp | `--ctx-size 262144 --n-gpu-layers 999 --mlock` | Same. Bigger KV cache. Consider Cyber-Tiel for code |
| 48 GB | GSQ-RCO | IQ3_S | 11.8 GiB | ~12 GiB | 262K+ | llama.cpp | `--ctx-size 262144 --n-gpu-layers 999 --mlock` | Still IQ3_S. More context headroom |
| 64 GB | GSQ-RCO | IQ3_S | 11.8 GiB | ~16 GiB | 262K+ | llama.cpp | `--ctx-size 262144 --n-gpu-layers 999 --mlock` | Near-lossless. 52GB free for KV cache, DFlash2 draft. |
| 96 GB | Flash Next | IQ3_XXS | 47 GiB | ~48 GiB | 262K native, 1M w/ YaRN | llama.cpp | `--ctx-size 1048576 --n-gpu-layers 999 --mlock` | Qwen4 preview, beats Claude Opus 4.6 |
| 128 GB | Flash Next | IQ3_XXS | 47 GiB | ~48 GiB | 1M | llama.cpp | `--ctx-size 1048576 --n-gpu-layers 999 --mlock` | Max context for Flash Next |
| 256 GB | DeepSeek V4.1 Flash | FP8 | 160 GiB | ~162 GiB | 1M | llama.cpp | `--ctx-size 1048576 --n-gpu-layers 999 --mlock` | Top capability. SSD streaming for Engram |

> IQ3_S = near-lossless. Recommended for all tiers where it fits. Only move to FP16 at 64GB+.
> Flash Next QSA gives ~4.9x decode speedup vs dense attention at 262K. IQ3_XXS is the sweet spot for 96GB+.

### CPU (System RAM — model + KV must fit in RAM)

| Tier | Model | Quant | Size | RAM Used | Context | Engine | Flags | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <8 GB | Maple | TQ2_0 | 5.5 GiB | ~6 GiB | 131K native | llama.cpp | `--ctx-size 131072 --no-mmap --mlock` | Minimum viable |
| 16 GB | Cyber-Tiel Coder | Q3_K_M | ~14 GiB | ~16 GiB | 262K native | llama.cpp | `--ctx-size 262144 --no-mmap --mlock` | MoE, 3B active. Faster than GSQ-RCO on CPU. |
| 32 GB | Cyber-Tiel Coder | UD-Q4_K_XL | 22.4 GiB | ~23 GiB | 262K native | llama.cpp | `--ctx-size 262144 --no-mmap --mlock` | MoE, 3B active, fast on CPU |
| 48 GB | Cyber-Tiel Coder | UD-Q4_K_XL | 22.4 GiB | ~23 GiB | 262K+ | llama.cpp | `--ctx-size 262144 --no-mmap --mlock` | More KV headroom |
| 64 GB | GSQ-RCO | IQ3_S | 11.8 GiB | ~16 GiB | 262K+ | llama.cpp | `--ctx-size 262144 --no-mmap --mlock` | Near-lossless. Low power, high context headroom. |
| 96 GB | Flash Next | IQ3_XXS | 47 GiB | ~48 GiB | 262K native | llama.cpp | `--ctx-size 1048576 --no-mmap --mlock` | Flash Next entry tier |
| 128 GB | Flash Next | IQ3_XXS | 47 GiB | ~48 GiB | 1M w/ YaRN | llama.cpp | `--ctx-size 1048576 --no-mmap --mlock` | Max context |
| 256 GB | DeepSeek V4.1 Flash | FP8 | 160 GiB | ~162 GiB | 1M | llama.cpp | `--ctx-size 1048576 --no-mmap --mlock` | Max tier |

### Unified Memory (Apple Silicon — shared CPU/GPU RAM)

| Tier | Model | Quant | Size | RAM Used | Context | Engine | Flags | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <8 GB | Maple | TQ2_0 | 5.5 GiB | ~6 GiB | 131K native | MTPLX | `--context-length 131072` | 218 tok/s on M4 Mac mini |
| 16 GB | Cyber-Tiel Coder | Q3_K_M | ~14 GiB | ~16 GiB | 262K native | MTPLX | `--context-length 262144` | MoE, 3B active. Faster than GSQ-RCO on Apple Silicon. |
| 32 GB | Cyber-Tiel Coder | UD-Q4_K_XL | 22.4 GiB | ~23 GiB | 262K native | MTPLX | `--context-length 262144` | 22+4=26GB ✓, fast MoE on Apple Silicon |
| 48 GB | Cyber-Tiel Coder | UD-Q4_K_XL | 22.4 GiB | ~23 GiB | 262K+ | MTPLX | `--context-length 262144` | M2 Max/Ultra territory |
| 64 GB | GSQ-RCO | IQ3_S | 11.8 GiB | ~16 GiB | 262K+ | MTPLX | `--context-length 262144` | Near-lossless. Low power, high context headroom. |
| 96 GB | Flash Next | IQ3_XXS | 47 GiB | ~48 GiB | 262K native | MTPLX | `--context-length 1048576` | M4 Ultra |
| 128 GB | Flash Next | IQ3_XXS | 47 GiB | ~48 GiB | 1M w/ YaRN | MTPLX | `--context-length 1048576` | Max Flash Next |
| 256 GB | DeepSeek V4.1 Flash | FP8 | 160 GiB | ~162 GiB | 1M | llama.cpp | `--ctx-size 1048576` | Max tier |

> ★ = on TurboFit List. Models without ★ are Model Zoo only.


---

## Entities

> All 26 entities from the entity catalog. Each entry preserves the full content of its source file.

### Bonsai MLX

Source: `wiki/entities/bonsai.md`


#### What this is

Bonsai refers to models from `prism-ml`: `Bonsai-27B-mlx-1bit` (1-bit binary, 1.4M downloads) and `Ternary-Bonsai-27B-mlx-2bit` (2-bit ternary, 1.4M downloads). The Ternary 2-bit variant at 7.91 GB was downloaded to `~/Models/storage/bonsai-mlx/` for testing on the M1 32GB box .

A separate GGUF variant also exists but requires llama.cpp, not MLX.

#### Status

- **Ternary Bonsai MLX 2-bit** — downloaded (7.91 GB), files intact, but server failed to start because `/bonsai-mlx/config.json` was missing . The process exited with `FileNotFoundError` on `config.json`.
- **Bonsai MLX 1-bit** — downloaded from prism-ml but was "not the right variant" per Hermes assessment .
- **Bonsai GGUF** — requires llama.cpp runtime, incompatible with the active MLX turbofit engine.

#### Chris's directive

Chris explicitly said "Don't worry about bonsai" — his priority was getting Ornith up as the main provider so he could continue working. Bonsai was deprioritized twice: at 2026-09-07 13:18 and again at 13:30, both times stating "It just needs to be configured into turbofit so I can continue with Ornith" .

#### Memory fit

At 7.91 GB, Ternary Bonsai would fit within the 32 GB memory budget, but no verified speed tests were completed before Chris redirected focus to Ornith .

#### Related

- [[topics/turbofit/wiki/entities/ornith-1-5-35b-a3b-mlx-4-bit|Ornith 1.5 35B-A3B MLX 4-bit]]
- [[topics/turbofit/wiki/queries/engine-research-request|Engine Research Request]]
- [[topics/turbofit/wiki/decisions/local-main-provider|TurboFit Local Main Provider Decision]]

### Colibri

Source: `wiki/entities/colibri.md`


#### What this is

Colibri is a custom-architecture model with `base_model: deepgrove/maple-preview`. It requires custom Maple MLX training/inference code and is incompatible with the standard `mlx_lm` server .

#### Status

- **Incompatible with standard MLX server**: The `mlx_lm` server from the deepgrove-ai fork failed to start because it could not find `config.json` at `/Users/sovthpaw/Models/storage/colibri/config.json` . The model uses a custom Maple format that generic MLX servers cannot load.
- **Removed**: Chris's subagents removed Colibri from the candidate set because its custom format is incompatible with standard MLX server execution paths.

#### Why it failed

Colibri's `base_model: deepgrove/maple-preview` means it requires the Maple-specific MLX codepath, not the generic mlx_lm server. The custom code that trains and runs Maple models is not present in standard mlx_lm distributions .

#### Chris's directive

Chris explicitly redirected focus from Bonsai and Colibri to Ornith: "Don't worry about bonsai" and "I said the model that we're using is too dumb, okay? So we need to focus entirely on getting Ornith up" .

#### Related

- [[topics/turbofit/wiki/entities/maple.md|Maple]]
- [[topics/turbofit/wiki/entities/ornith-1-5-35b-a3b-mlx-4-bit|Ornith 1.5 35B-A3B MLX 4-bit]]
- [[topics/turbofit/wiki/decisions/local-main-provider|TurboFit Local Main Provider Decision]]

### DFlash2 Arg Failures

Source: `wiki/entities/dflash2-arg-failures.md`


All attempted llama.cpp DFlash2 integration commands failed with invalid/unrecognized argument errors. The `dflash2-llama.cpp` fork has a different flag set than stock llama.cpp.

#### Failed Commands and Errors

|| Command | Error |
| --- | --- | --- |
| `llama-server -m ... --draft-model <path> --draft-ngl 999 --draft-ctx-size 131072 --low-vram 0` | `error: invalid argument: --draft-model` |
| `llama-server -m ... --draft-ngl 999 --low-vram 0` | `error: invalid argument: --draft-ngl` |
| `llama-server -m ... --draft-ctx-size 131072 --low-vram 0` | `error: invalid argument: --draft-ctx-size` |
| `llama-server -m ... --low-vram 0` | `error: invalid argument: --low-vram` |
| `mtplx serve --model ... --memory-budget 32GB` | `error: unrecognized arguments: --memory-budget 32GB` |

#### Root Cause

The `dflash2-llama.cpp` fork uses different argument names than stock llama.cpp:
- `--draft-model` → not supported; use `--spec-draft-model`
- `--draft-ngl` → not supported; use `--spec-draft-ngl`
- `--draft-ctx-size` → not supported
- `--low-vram` → not supported

MTPLX's `--memory-budget` flag is also rejected; use `MTPLX_MEMORY_BUDGET` environment variable instead.

#### Workarounds

For stock llama.cpp with DFlash2:
```bash
llama-server -m <main-model> --model-draft <draft-model> --spec-draft-ngl 999
```

For the dflash2-llama.cpp fork:
```bash
llama-server -m <main-model> --spec-draft-model <draft-model> --spec-draft-ngl 999 --spec-draft-n-max 7
```

#### Related

- [[topics/turbofit/wiki/entities/dflash2-draft.md|DFlash2 Draft]]
- [[topics/turbofit/wiki/entities/mplx-service-arg-validation.md|MPLX Service Arg Validation]]
- [[topics/turbofit/wiki/concepts/dflash2-compat-boundary.md|DFlash2 Compatibility Boundary]]

### DFlash2 Draft

Source: `wiki/entities/dflash2-draft.md`


DFlash2 is the speculative-draft model paired with Unleashed 27B in TurboFit. It requires the `dflash2-llama.cpp` fork, not stock llama.cpp .

#### Artifact

- `~/Models/storage/gguf/Qwen3.8-27B/Qwen3.8-27B-DFlash2-Q4_K_M.gguf` .

#### Flag corrections

- Wrong: `--draft-max`, `--draft-min`, `--draft-p-min`, `--model-draft`.
- Correct for this fork: `--spec-draft-model <path>`, `--spec-draft-n-max 7`, `--spec-draft-n-min 5`, `--spec-draft-p-min 0.75`, `--spec-type draft-dflash` .

#### Related

- [[topics/turbofit/wiki/entities/unleashed-27b.md|Unleashed 27B]]
- [[topics/turbofit/wiki/entities/turbofit.md|TurboFit]]
- [[topics/turbofit/wiki/comparisons/aux-runtime-options.md|Aux Runtime Options]]
- [[topics/turbofit/wiki/entities/ornith-35b-dflash2.md|Ornith 35B DFlash2]]

### Dirk GGUF Q3_K_XL

Source: `wiki/entities/dirk-gguf.md`


`Dirk-Qwen3.8-27B-UD-Q3_K_XL.gguf` (12.24 GB) is the requested Q3 Dirk artifact at `~/Models/storage/dirk-gguf/`, selected because Chris prefers Q3 when it is described as near base-model quality and because 13 GB fits the short-context candidate path better than heavier quants on this 32 GB box .

#### Status

- Downloaded and verified on disk (12.24 GB, GGUF magic number confirmed)
- No benchmark evidence yet; 131K testing deferred because Dirk is a dense 27B model
- Chris explicitly wanted GGUF vs MLX compared, with preference for Q3 when near base quality

#### Memory Impact

Dirk is a **dense 27B model** (not MoE), so:
- Model weights: 12.24 GB (Q3_K_XL)
- KV cache at 131K (q8): ~8 GB
- Total: ~20 GB + macOS/Hermes (~8 GB) = ~28 GB at 32K context

**Result**: OOM expected above 32K context window.

#### Repo Correction

- Requested: `peculiar-ragdoll/Dirk-Qwen3.8-27B-GGUF-MTP` (returned 404)
- Actual: `peculiar-ragdoll/Dirk-Qwen3.8-27B-GGUF` (MTP is a model capability, not repo name)

#### Runtimes Tested

| Runtime | Status | Notes |
| --- | --- | --- |
| llama.cpp stock | Incompatible | `unknown model architecture: 'maple'` (Maple only) |
| llama.cpp Qwen branch | | Works with Q3_K_XL |
| MLX | 🔄 Pending | Would need 131K streaming verification |

#### Related

- [[topics/turbofit/wiki/entities/dirk-qwen38-27b.md|Dirk Qwen 3.8 27B GGUF]]
- [[topics/turbofit/wiki/decisions/candidate-quant-preference.md|Candidate Quant Preference]]
- [[topics/turbofit/wiki/queries/apple-silicon-runtime-benchmark|Apple Silicon Runtime Benchmark]]
- [[topics/turbofit/wiki/entities/unleashed-27b.md|Unleashed 27B]]

### Dirk Qwen 3.8 27B GGUF

Source: `wiki/entities/dirk-qwen38-27b.md`


Chris requested Dirk GGUF downloads for local comparison. The actual repo is `peculiar-ragdoll/Dirk-Qwen3.8-27B-GGUF` because MTP is a model capability, not a repo suffix .

#### Requested artifacts

- `Dirk-Qwen3.8-27B-UD-Q3_K_XL.gguf` (~12.24 GB) downloaded to `~/Models/storage/dirk-gguf/` and verified on disk .
- `Dirk-Qwen3.8-27B-GGUF-MTP` repo lookup returned 404 before the correction .

#### Status

- Q3_K_XL downloaded; no speed evidence yet. 131K benchmark was deferred because larger candidates OOM on this box before Dirk was exercised.
- Chris wants GGUF vs MLX compared for each candidate, with a preference for Q3 when near base quality .

#### Related

- [[topics/turbofit/wiki/entities/dirk-gguf.md|Dirk GGUF Q3_K_XL]]
- [[topics/turbofit/wiki/decisions/candidate-quant-preference.md|Candidate Quant Preference]]
- [[topics/turbofit/wiki/queries/apple-silicon-runtime-benchmark|Apple Silicon Runtime Benchmark]]
- [[topics/turbofit/wiki/entities/unleashed-27b.md|Unleashed 27B]]

### Maple

Source: `wiki/entities/maple.md`


Maple-Preview is the auxiliary model Chris wants for Hermes compression and text aux tasks. It is a custom-architecture MoE model with no native support in stock llama.cpp and no vision projector .

#### Artifacts on disk

- `~/Models/storage/gguf/Maple-Preview/maple-mlx` — deepgrove MLX download.
- `~/Models/storage/gguf/Maple-Preview/maple-tq2_0.gguf` — 5.4 GB, crashes on Metal warmup.
- `~/Models/storage/gguf/Maple-Preview/maple-q2_0.gguf` — tensor read failure under fork.
- `~/Models/storage/gguf/Maple-Preview/maple-f16.gguf` — 40.4 GB, completed download .

#### Runtime compatibility

- **llama.cpp / GGUF**: incompatible. The `stamsam/llama.cpp` fork lacks Metal kernels for TQ2_0 and tensor layout mismatches for Q2_0. Final failure: `kernel_mul_mm_id_tq2_0_f32` missing in Metal compile pipeline.
- **MLX**: working via `deepgrove-ai/mlx-lm-deepgrove` with `--flash-head --trust-remote-code`.
- **Server mode**: unstable with prompt-cache growth; OOM after a handful of requests on 32 GB.
- **Generate mode**: stable for 100–5000 token prompts and tested to 130K tokens in 103 s without OOM .

#### Performance

- ~62 tok/s warm.
- 130K compression workload completed in 103 s on this hardware.
- Uses ~7 GB at rest .

#### Related

- [[topics/turbofit/wiki/entities/turbofit.md|TurboFit]]
- [[topics/turbofit/wiki/entities/mplx.md|MPLX]]
- [[topics/turbofit/wiki/decisions/aux-model-selection.md|Aux Model Selection]]
- [[topics/turbofit/wiki/concepts/compression-timeouts.md|Compression Timeouts]]

### MPLX Metal Load Failure

Source: `wiki/entities/mplx-metal-load-failure.md`


A `mtplx serve --download` background process exited with code `1` after 42.2 s because model loading failed with `RuntimeError: [METAL] Command buffer execution failed: Insufficient Memory (00000008:***)` during MTP injection .

#### Evidence

- Command path: `~/turbofit/.venv/bin/mtplx serve --model Youssofal/Qwen3.8-27B-MTPLX-Optimized-Speed --download --port 11613 --host 127.0.0.1` .
- Failure site: `mtplx/runtime.py:762 load()` → `inject_mtp_support(...)` → `mx.eval(mtp.parameters())` .
- Sidecar note in MTPLX output: `"[mtp norms] sidecar gains are delta-encoded; restoring the +1.0 convention"` .

#### Note

- The same model earlier caused an exit code `-9`, which points to OS memory-limit preemption under MTPLX serving and Metal allocation pressure. This load failure is a separate stop at the runtime/Metal boundary.

#### Related

- [[topics/turbofit/wiki/entities/turbofit-memory-crash.md|TurboFit Memory Crash]]
- [[topics/turbofit/wiki/entities/turbofit-mtp-performance.md|TurboFit MTP Performance]]

### MPLX

Source: `wiki/entities/mplx.md`


MPLX is an experimental additional local runtime discovered late in the session. It was downloaded and measured at 12.4 tok/s, roughly 2.5x faster than Unleashed Q3_K_XL on this hardware, but testing stopped before serving or integration .

#### Observed behavior

- 26 GB used during download, 5.7 GB free, heavy swapping with Unleashed also resident.
- Tested by temporarily removing Unleashed to free RAM.
- Measured speeds:
  - 300 tokens in 61 s → ~5.1 tok/s
  - 350 tokens in 80 s → ~4.4 tok/s
  - MPLX MTP path: 12.4 tok/s reported .
- `--memory-budget 32GB` is not a valid `mtplx serve` argument; MTPLX exits with usage error when that flag is passed ^[raw/inbox/2026-09-07-from-senter-wiki.md].

#### Open questions

- Can it coexist with Unleashed on 32 GB?
- What is its real memory ceiling with MTP enabled?
- Is there a first-class Hermes provider definition for it, or only manual path config?

#### Related

- [[topics/turbofit/wiki/entities/turbofit.md|TurboFit]]
- [[topics/turbofit/wiki/entities/unleashed-27b.md|Unleashed 27B]]
- [[topics/turbofit/wiki/queries/mplx-integration.md|MPLX Integration]]

### MTPLX Memory Guard

Source: `wiki/entities/mtplx-memory-guard.md`


MTPLX emits a memory-guard `prefill_admission_shed` event when a prompt would push the active process above its memory threshold, clearing the KV cache before admission to keep the projected bytes under the threshold ^[raw/inbox/2026-09-07-from-senter.md].

#### Evidence

- Event: `{"action": "prefill_admission_shed", ...}` triggered for a 5016-token prompt ^[raw/inbox/2026-09-07-from-senter.md].
- Pre-admission values: `active_bytes: 20.70 GB`, `cache_bytes: 2.00 GB`, `projected_bytes: 26.26 GB`, `threshold_bytes: 24.99 GB`, `limit_bytes: 25.77 GB` ^[raw/inbox/2026-09-07-from-senter.md].
- Behavior: `cache_cleared: true`, then projected dropped to `24.25 GB` and was admitted against the `24.99 GB` threshold ^[raw/inbox/2026-09-07-from-senter.md].

#### Note

- This is a live runtime safeguard, not an application prefetch guarantee. It shows that long-prompt admission is actively shedding cache to stay under the memory budget, which can stall throughput and explain apparent cache-hit variability.

#### Related

- [[topics/turbofit/wiki/entities/turbofit-mtp-performance.md|TurboFit MTP Performance]]
- [[topics/turbofit/wiki/entities/turbofit-memory-crash.md|TurboFit Memory Crash]]
- [[topics/turbofit/wiki/queries/turbofit-mtplx-coexistence.md|MTPLX Coexistence]]

### MTPLX Qwen 3.8 27B Optimized Speed

Source: `wiki/entities/mtplx-qwen-38-27b-optimized-speed.md`


`Youssofal/Qwen3.8-27B-MTPLX-Optimized-Speed` is the candidate Hermes TurboFit provider discovered on 2026-09-07. It is served via `~/turbofit/.venv/bin/mtplx serve` and exposes an OpenAI-compatible endpoint on this box .

#### Runtime facts

- Weights: 19.3 GB.
- Engine budget: 24.0 GB.
- Stable observed context: 65,536 tokens.
- 131,072-token context prints `OVERCOMMITTED`, warns `requested context 131072 exceeds the machine fit 8192`, and then exits under generation pressure .
- Memory guard clears KV cache when projected bytes exceed threshold .
- `--memory-budget` is not a valid CLI flag; the supported path is env/runtime config .

#### Performance

| Context | Throughput | Notes |
| --- | --- | --- |
| 500 tokens | 8–12 tok/s | Stable short context |
| 65K | ~7 tok/s | Stable daily-driver target |
| 131K | 6–7 tok/s short | Hermes summary claim |
| 5K+ prompts at 131K | 507 Insufficient Storage | Observed failure |
| End-to-end @ 131K 2005-token history | 0.39 tok/s | `end_to_end_tok_s` observed |

#### Artifacts

- Hermes summary claimed config locked to `custom:turbofit-mtplx` as main provider, but that state is contested because later command evidence reverted to Unleashed+DFlash2 after repeated instability .

#### Related

- [[topics/turbofit/wiki/entities/mplx.md|MPLX]]
- [[topics/turbofit/wiki/decisions/mtplx-main-provider.md|MPLX Main Provider]]
- [[topics/turbofit/wiki/decisions/context-window-decision.md|Context Window Decision]]
- [[topics/turbofit/wiki/entities/mtplx-memory-guard.md|MPLX Memory Guard]]
- [[topics/turbofit/wiki/entities/mtplx-service-arg-validation.md|MPLX Service Arg Validation]]
- [[topics/turbofit/wiki/concepts/mtplx-32gb-memory-and-evidence-reliability.md|MPLX 32GB Memory and Evidence Reliability]]

### MT_PlX Service Arg Validation

Source: `wiki/entities/mtplx-service-arg-validation.md`


`mtplx serve` with `--memory-budget 32GB` exits with an error:

```
usage: mtplx [-h] [--no-color] [--version] {help,advanced,...}
mtplx: error: unrecognized arguments: --memory-budget 32GB
```

#### Accepted Arguments

MTPLX's CLI does not accept `--memory-budget` as a flag. According to the model family documentation, memory management should be handled via:

1. **Environment variables**: `MTPLX_MEMORY_BUDGET` for memory budget control
2. **Native runtime config**: Per-model memory planning is automatic

#### Working Command Pattern

```bash
### Correct: Environment variable for memory budget
MTPLX_MEMORY_BUDGET=34359738368 mtplx serve --model <model-id> --port 11613

### Or let MTPLX auto-calculate based on available memory
mtplx serve --model <model-id> --port 11613
```

#### Related

- [[topics/turbofit/wiki/entities/mplx-qwen-38-27b-optimized-speed.md|MPLX Qwen 3.8 27B Optimized Speed]]
- [[topics/turbofit/wiki/entities/mplx.md|MPLX]]
- [[topics/turbofit/wiki/concepts/mtplx-32gb-memory-and-evidence-reliability.md|MPLX 32GB Memory and Evidence Reliability]]

### Nail Qwen 3.6 35B UD Q4_K_XL

Source: `wiki/entities/nail-qwen36-35b.md`


`Nail-Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf` (~20.82 GB) and its `mmproj-F16.gguf` (~858 MB) were downloaded to `~/Models/storage/nail/` for testing. This is a MoE architecture model (3B active params per token).

#### Benchmark Results (M1 MacBook 32GB)

|| Model | Type | Context | Warmup | Short | 5K | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
|| **Nail Q4_K_XL** | MoE 35B | 32K | ~3s | **23.4 tok/s** | **4.7 tok/s** | Winner |

#### Key Findings

- **Best measured at 32K**: 23.4 tok/s short-context, 4.7 tok/s at 5K prompt.
- **Long-context status**: deferred from 131K testing because 20.8 GB weights plus ~8 GB KV at full window exceeds stable 32 GB fit before benchmark .
- **MoE advantage**: only 3B active params per token keeps memory footprint lower than dense 27B rivals, but it is not enough for 131K on this box.

#### Why It Won

`Nail` and `Tiel-Coder` are both MoE 35B models with 3B active parameters, making them far more memory-efficient than dense 27B models like Dirk. Combined with the Q4_K_XL quantization, Nail achieved the best balance of speed and stability on this hardware.

#### Vision Support

The `mmproj-F16.gguf` file (858 MB) provides vision capability. Test verification:
```
- Nail-Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf: 22,360,465,312 bytes (20.82 GB)
- mmproj-F16.gguf: 899,283,680 bytes (858 MB)
```

#### Related

- [[topics/turbofit/wiki/queries/apple-silicon-runtime-benchmark|Speed Test Results]]
- [[topics/turbofit/wiki/decisions/candidate-quant-preference|Candidate Quant Preference]]
- [[topics/turbofit/wiki/entities/ornith-35b-mlx.md|Ornith 35B MLX]]

### Ornith 1.5 MLX 4-bit

Source: `wiki/entities/ornith-1-5-35b-a3b-mlx-4-bit.md`


Local candidate for TurboFit main on the M1 32GB box, owned by MLX, tested from `~/Models/storage/ornith/`.

#### What this is

Ornith is a Mixture of Experts (MoE) model with 35B total parameters and roughly 3B active parameters per token. The tested artifact here is the MLX 4-bit build served by `mlx_lm server` on `http://127.0.0.1:11613/v1`. This is the variant Chris repeatedly wanted running on TurboFit so he could switch Hermes off weaker free models.

#### Provenance

Ornith is owned by TurboFit routing, not the wiki itself. See `[[turbofit-runtime-providers|TurboFit Runtime Providers]]` and `[[turbo-fit-evidence-capture|TurboFit Evidence Capture]]` for how service health should be checked when Hermes can't reach it.

^[raw/inbox/2026-09-07-from-senter-wiki.md]

#### Status

- **Local server:** MLX deepgrove fork via `mlx_lm server --model ~/Models/storage/ornith --port 11613 --host 127.0.0.1` 
- **Config:** Hermes provider `custom:turbofit`; `providers.turbofit.api: http://127.0.0.1:11613/v1`; `model.default: ornith-1-5-35a3b-mlx` 
- **Context supported:** 131K claimed from server logs; throughput at that window drops sharply under prompt load 
- **Q3 preference note:** Chris wants GGUF vs MLX compared for new candidates and prefers the Q3 quant when page notes place it near base model quality; this page records the MLX run only .
- **Final configuration locked:** 2026-09-07 — Ornith MLX 4-bit configured as main provider at 131K context .

#### Measured throughput

|| Test | Measured value |
| --- | --- | --- |
|| Warmup | ~68s first run; much faster on restarts |
|| Short prompt | 15.6 tok/s at ~517 tokens in / 100 out |
|| 5K prompt | 5.7 tok/s at ~3519 tokens in / 100 out |
|| 131K-loaded server | short-context benchmark also reported at ~28-29 tok/s under lighter conditions |
|| After restart verification | 29 tok/s short prompt, 226 tok/s 5K prompt |

#### Benchmark Results (vs competitors)

|| Benchmark | Ornith 1.5 | Ornith 1.0 | Qwen3.6 35B | Gemma 4 31B | Muse Glimmer 30B | Qwen3.5 397B |
| --- | --- | --- | --- | --- | --- | --- | --- |
|| **Terminal-Bench (Terminus-2)** | **67.8** | 64.2 | 52.5 | 42.1 | 51.7 | 53.5 |
|| **Terminal-Bench (Claude Code)** | **68.5** | 62.8 | 49.2 | - | - | 48.6 |
|| **SWE-bench Verified** | **79.0** | 75.6 | 73.4 | 52.0 | - | 76.4 |
|| **SWE-bench Pro** | **59.6** | 50.4 | 49.5 | 35.7 | 51.2 | 51.6 |
|| **SWE-bench Multilingual** | **71.4** | 69.3 | 67.2 | 51.7 | - | 69.3 |

#### Why It Feels Smarter Than Free Models

1. **Agentic coding**: Outperforms 35B+ models on coding tasks by wide margins
2. **Continuous self-improvement**: Uses reinforcement learning to optimize task generation and solution rollouts
3. **Efficient MoE**: Gets 35B-level reasoning with 3B active parameters = faster, smarter than dense models

#### Behavioral notes

Chris repeatedly asked to ignore Bonsai, Maple Colibri, and music generation noise and focus on getting Ornith up as the main provider. Three near-duplicate raw messages on 2026-09-07 at 13:18/13:20/13:30 show his exact framing: "It just needs to be configured into turbofit so I can continue with Ornith. Don't worry about bonsai."

#### Decision trail

Hermes-side `custom:turbofit` was retargeted to `http://127.0.0.1:11613/v1`, but Hermes timeouts occurred until restart. Chris switched his active provider to `ornith-1-5-35a3b-mlx via provider turbofit` at 14:25, and session metadata confirms the provider change; however, provider `timeout` errors (`code: timeout`, `provider: turbofit`, `model: ornith-1-5-35a3b-mlx`, `error: Connection error.`) recurred at 2026-09-07T19:26:47.525Z . A full Hermes restart remains needed to confirm the live route. Until that restart and a successful completion are observed, final promotion is contested .

Chris's final directive at 14:25: "It just needs to be configured into turbofit so I can continue with Ornith" .

#### Related pages

- [[turbo-fit-evidence-capture|TurboFit Evidence Capture]]
- [[mtplx-main-provider|MPLX Main Provider]]
- [[unleashed-backup|Unleashed Backup]]

### Ornith 35B A3B DFlash2

Source: `wiki/entities/ornith-35b-dflash2.md`


`jzinno/Ornith-1.5-35B-A3B-DFlash2` was inspected on HuggingFace and downloaded as a local draft artifact for speculative-decode experiments .

#### Status

- Community uptake is small (~840 downloads at observation time)
- No usable MTPLX integration path: MTPLX uses native MLX MTP heads rather than llama.cpp draft models
- DFlash2 is a CUDA-only diffusion-based draft model for llama.cpp/vLLM/sglang, incompatible with MLX MTP

#### Benchmark Evidence

The DFlash2 draft model is **not viable for this hardware configuration**. From the speed tests:

| Setup | Short | 131K |
| --- | --- | --- |
| **Ornith MLX 4-bit** | **28.5 tok/s** | ~0.5 tok/s |
| Ornith + DFlash2 | N/A | Cannot test |

The DFlash2 draft path cannot be used with Ornith MLX because:
1. MTPLX cannot use DFlash2 (native MLX MTP heads vs CUDA diffusion draft)
2. llama.cpp DFlash2 integration failed with invalid argument errors (`--draft-ngl`, `--draft-ctx-size`, `--low-vram` not supported)

#### Contested Recommendation

Hermes recommended pairing Ornith MLX 4-bit with Unleashed+DFlash2 for 131K coverage; that pairing is contested because:
- DFlash2 cannot be integrated with Ornith MLX (different runtimes)
- Ornith MLX alone drops to ~0.5 tok/s at 131K due to KV cache dominance

#### Final Recommendation

**Ornith MLX 4-bit solely as main provider** for short/medium context (28.5 tok/s at 500 tokens). For long context, use **Unleashed + DFlash2** at 131K (~5 tok/s) or **Nail Q4_K_XL** at 32K (23.4 tok/s).

#### Related

- [[topics/turbofit/wiki/entities/ornith-35b-mlx.md|Ornith 35B MLX]]
- [[topics/turbofit/wiki/concepts/dflash2-mplx-incompatibility|MPLX DFlash2 Incompatibility]]
- [[topics/turbofit/wiki/entities/dflash2-draft.md|DFlash2 Draft]]
- [[topics/turbofit/wiki/queries/apple-silicon-runtime-benchmark|Apple Silicon Runtime Benchmark]]

### Ornith 35B A3B MLX

Source: `wiki/entities/ornith-35b-mlx.md`


`Ornith-1.5-35B-A3B` MLX 4-bit is a MoE local candidate downloaded to `~/Models/storage/ornith/` with a companion DFlash2 draft package at `~/Models/storage/ornith-dflash2/` .

This page is a legacy entity record; see [[topics/turbofit/wiki/entities/ornith-1-5-35b-a3b-mlx-4-bit.md|Ornith 1.5 35B-A3B MLX 4-bit]] for measured throughput and config state after 2026-09-07 final lock-in .

#### Tested speeds on M1 MacBook 32GB

|| Context | Tok/s |
| --- | --- | --- |
|| Short (~500 tokens) | **28.5** |
|| 5K tokens | 5.7 |
|| 20K tokens | 1.5 |
|| 40K tokens | 0.7 |
|| 60K tokens | 0.4 |
|| 131K | ~0.5 |

These numbers were gathered in-session against downloaded artifacts .

#### Model Facts

- **Architecture**: MoE 35B (3B active params per token)
- **Weight**: 18 GB via MLX 4-bit
- **Inference**: MLX via `mlx_lm` server

#### Role

- Fastest observed short-context path on this box (28.5 tok/s)
- KV cache dominates throughput above ~20K context
- 131K path is unstable (~0.5 tok/s)

#### Contested Evidence

Hermes summary claimed Ornith wins at 131K, but speed tests from 09:19 show:
- Ornith MLX 4-bit: 28.5 tok/s short, ~0.5 tok/s at 131K
- Nail Q4_K_XL: 23.4 tok/s short, 4.7 tok/s at 5K
- Tiel-Coder Q4_K_XL: 23.1 tok/s short, 4.2 tok/s at 5K
- Dirk Q3_K_XL: 6.0 tok/s at 32K, OOM above

**Conclusion**: Ornith is fastest at short context but drops sharply at long context. The "winner" designation depends on use case.

- **Current routed state**

Hermes `custom:turbofit` was retargeted to Ornith MLX on `http://127.0.0.1:11613/v1`, and session metadata confirms the provider changed to `ornith-1-5-35a3b-mlx via provider turbofit` at 14:25, but persistent `Connection error` timeouts recurred at 2026-09-07T19:26:47.525Z . Until a verified post-restart Hermes completion is captured, the routed state remains contested.

- **Practical recommendation**

Use Ornith MLX 4-bit for short/medium-context daily work. Use Unleashed+DFlash2 for long-context fallback where stable throughput matters more than peak speed.

#### Related

- [[topics/turbofit/wiki/entities/ornith-35b-dflash2.md|Ornith 35B DFlash2]]
- [[topics/turbofit/wiki/decisions/aux-model-selection.md|Aux Model Selection]]
- [[topics/turbofit/wiki/queries/apple-silicon-runtime-benchmark|Apple Silicon Runtime Benchmark]]

### Ornith 35B A3B

Source: `wiki/entities/ornith-35b.md`


`Ornith-1.5-35B-A3B` is a MoE model downloaded to `~/Models/storage/ornith/` as MLX 4-bit on this 32 GB box. A DFlash2 draft package was also downloaded to `~/Models/storage/ornith-dflash2/` .

#### Tested speeds on M1 MacBook 32GB

| Context | Tok/s |
| --- | --- |
| Short (~500 tokens) | 28.5 |
| 5K tokens | 4.3 |
| 20K tokens | 1.5 |
| 40K tokens | 0.7 |
| 60K tokens | 0.4 |
| 131K | ~0.5 |

These numbers were gathered in-session against the downloaded artifacts; they are not stable live-route evidence from Hermes .

#### DFlash2 candidate

A DFlash2 draft build exists as `jzinno/Ornith-1.5-35B-A3B-DFlash2` on HuggingFace, but community uptake is small (~840 downloads at time of observation). No MTPLX integration path exists because MTPLX uses native MLX MTP heads rather than llama.cpp draft models .

#### Contested Evidence

> "The hard truth: On M1 MacBook 32GB with a 27B model at 131K context, **~5-6 tok/s is the ceiling.** You want 10+ tok/s. That's not happening with this hardware — it's like asking a Honda Civic to go 200mph." .

Hermes proposed Ornith MLX 4-bit as daily-driver main provider for short/medium workloads and Unleashed+DFlash2 as long-context fallback. That pairing is contested because it has not been verified as a stable live Hermes route without reload failures or memory overcommit .

#### Conclusion

**Recommendation:** Ornith MLX 4-bit as main provider for daily use (short/medium context, 28.5 tok/s) with 65K context as the stable ceiling. Use Unleashed+DFlash2 for 131K long-context needs. 10+ tok/s at 131K is physically unachievable on this 32GB hardware.

#### Note

Ornith is fast at short context but loses throughput sharply as KV cache grows. On this hardware, 131K remains the throughput ceiling regardless of runtime.

#### Related

- [[topics/turbofit/wiki/decisions/aux-model-selection|Aux Model Selection]]
- [[topics/turbofit/wiki/decisions/unleashed-backup|Unleashed Backup]]
- [[topics/turbofit/wiki/queries/apple-silicon-runtime-benchmark|Apple Silicon Runtime Benchmark]]
- [[topics/turbofit/wiki/entities/dflash2-draft|DFlash2 Draft]]
- [[topics/turbofit/wiki/entities/ornith-35b-mlx.md|Ornith 35B MLX]]
- [[topics/turbofit/wiki/entities/ornith-35b-dflash2.md|Ornith 35B DFlash2]]

### Ornith Config Routing Failure

Source: `wiki/entities/ornith-config-routing-failure.md`


After Hermes `custom:turbofit` was retargeted to `http://127.0.0.1:11613/v1` and `model.default` was set to `ornith-1-5-35a3b-mlx`, Hermes emitted repeated connection timeouts to the turbofit provider .

#### Observed evidence

- Session metadata changed to Ornith successfully at 14:25 with `ornith-1-5-35a3b-mlx via provider turbofit` .
- Provider errors continued after config change:
  - `time: 2026-09-07T19:26:47.525Z` .
  - `layer: provider`
  - `code: timeout`
  - `provider: turbofit`
  - `model: ornith-1-5-35a3b-mlx`
  - `error: Connection error.`

#### Status

The timeout persisted after the 14:25 config repoint. A Hermes session or gateway restart resolves the stale connection state. Until a post-restart verification completes, this is contested.

#### Related

- [[ornith-config-routing|Ornith Config Routing]]
- [[ornith-1-5-35b-a3b-mlx-4-bit|Ornith 1.5 35B-A3B MLX 4-bit]]

### Tiel Coder

Source: `wiki/entities/tiel-coder.md`


Tiel-Coder is a queued local GGUF candidate. The primary MLX download in `~/Models/storage/tiel-coder/` remained incomplete (~15 GB of ~19 GB), and a GGUF test path at `~/Models/storage/tiel-coder-gguf/Tiel-Coder-35B-A3B-UD-Q4_K_XL.gguf` was launched at 131K but not benchmarked before the session ended.

#### Status

- MLX download incomplete (15 GB of 19 GB)
- GGUF Q4_K_XL version tested and working at 65K
- Benchmarked: 65K context, 23.1 tok/s short, 4.2 tok/s at 5K
- 131K benchmark deferred due to OOM expectation (22 GB + 8 GB KV)

#### Benchmark Results

|| Model | Type | Context | Short | 5K | Status |
| --- | --- | --- | --- | --- | --- | --- |
|| **Tiel-Coder Q4_K_XL** | MoE 35B | 65K | **23.1 tok/s** | 4.2 tok/s | Viable |

#### MoE Advantage

Tiel-Coder is MoE 35B with 3B active params, making it memory-efficient and fast. Similar to Nail and Ornith.

#### Download Status

The tiel-coder background process completed successfully:
```
all downloads complete
```
Files available at:
- `~/Models/storage/tiel-coder/` (MLX, incomplete)
- `~/Models/storage/tiel-coder-gguf/` (GGUF Q4_K_XL, 22.16 GB)

#### Related

- [[topics/turbofit/wiki/queries/apple-silicon-runtime-benchmark|Speed Test Results]]
- [[topics/turbofit/wiki/entities/ornith-35b-mlx.md|Ornith 35B MLX]]
- [[topics/turbofit/wiki/entities/nail-qwen36-35b.md|Nail Qwen 3.6 35B UD Q4_K_XL]]
- [[topics/turbofit/wiki/decisions/context-window-decision.md|Context Window Decision]]

### TurboFit Memory Crash

Source: `wiki/entities/turbofit-memory-crash.md`


A `mtplx serve` background process exited with code `-9` during TurboFit testing on this 32 GB box. The first evidence used `--mtp` without an explicit long-context window, while later evidence shows explicit `--context-window 131072` invocations whose memory plan was already marked `OVERCOMMITTED` before the process was killed .

#### Evidence

- Process paths:
  - `~/turbofit/.venv/bin/mtplx serve --model Youssofal/Qwen3.8-27B-MTPLX-Optimized-Speed --port 11613 --host 127.0.0.1 --mtp` exited `-9` after 158.15 s while generating 100 completion tokens from a 5010-token prompt .
  - `~/turbofit/.venv/bin/mtplx serve ... --mtp --context-window 131072` printed `Memory plan: ... 131072 (machine-bound) (OVERCOMMITTED)` and `requested context 131072 exceeds the machine fit 8192` before later runs were killed .
- Runtime output also shows cache shedding and swap warnings at 131K, plus `deferred_s: 60.0` in precommit output .
- Prior MPLX observation notes heavy swapping around 26 GB used and co-resident Unleashed pressure .

#### Contested Evidence

Hermes summary claims `custom:turbofit-mtplx` as main provider with 65K stable context, but command evidence shows:
- `/01:51` turn: MTPLX exited `-9` after 158s of generation
- `/00:56` turn: MTPLX 65K stable at 8.5-12 tok/s then crashed under load
- `/01:00` turn: Switched back to Unleashed+DFlash2 after MTPLX instability

#### Note

- Code `-9` points to OS memory-limit preemption rather than a clean MTPLX shutdown. The explicit `--context-window 131072` evidence makes this more specifically an overcommit-induced kill than the earlier generic crash record.
- Hermes summary claims 65K stable and MTPLX main, but the command evidence for this box shows 131K overcommit and killed processes .

#### Related

- [[topics/turbofit/wiki/entities/turbofit-verifier-bridge.md|TurboFit Verifier Bridge]]
- [[topics/turbofit/wiki/entities/mplx.md|MPLX]]
- [[topics/turbofit/wiki/entities/mtplx-memory-guard.md|MPLX Memory Guard]]
- [[topics/turbofit/wiki/decisions/mtplx-main-provider.md|MTPLX Main Provider]]
- [[topics/turbofit/wiki/concepts/mtplx-context-overcommit.md|MPLX Context Overcommit]]

### TurboFit MTP Performance

Source: `wiki/entities/turbofit-mtp-performance.md`


Redirect: this subject is consolidated under `turbofit-mtpl-performance`.

- Canonical page: [[turbofit-mtpl-performance|TurboFit MTPLX Performance]]
- This file remains to avoid breaking old wikilinks; it carries no unique evidence.

Related:
- [[topics/turbofit/wiki/entities/turbofit-mtpl-performance.md|TurboFit MTPLX Performance]]

### TurboFit MTPLX Performance

Source: `wiki/entities/turbofit-mtpl-performance.md`


Evidence-observed performance characteristics of `Youssofal/Qwen3.8-27B-MTPLX-Optimized-Speed` on this 32 GB M1 Mac, including short-context throughput, long-context overcommit, and live memory-guard behavior .

#### Throughput

|| Context | Throughput | Notes ||
| --- | --- | --- | --- | --- |
| 500 tokens | 8–12 tok/s | Stable short context |
| 65K | ~7 tok/s | Stable daily-driver target |
| 131K short prompt | 6–7 tok/s | Hermes summary claim |
| 5K+ prompts at 131K | `507 Insufficient Storage` | Observed failure |
| 131K with 2005-token history | 0.39 tok/s end-to-end | `end_to_end_tok_s` observed |

#### Memory-plan evidence

```
Memory plan: 32G Mac: engine budget 24.0G, weights 19.3G, context 131072 (machine-bound) (OVERCOMMITTED)
requested context 131072 exceeds the machine fit 8192: KV at the full window needs 8.0 GiB; expect cache shedding and, past the fit, swap
```

#### Live memory-guard event

On 2026-09-07 00:51, MTPLX emitted a `prefill_admission_shed` for a 5016-token prompt:

```json
{
  "action": "prefill_admission_shed",
  "prompt_tokens": 5016,
  "reusable_prefix_tokens": 0,
  "miss_tokens": 5016,
  "active_bytes": 20702539884,
  "cache_bytes": 2008116674,
  "projected_bytes": 26260610606,
  "threshold_bytes": 24996709662,
  "limit_bytes": 25769803776,
  "cache_cleared": true,
  "projected_bytes_after_cache_clear": 24252493932
}
```

This corroborates the 32 GB / 131K overcommit behavior: live admission is shedding cache to stay under the threshold ^[raw/inbox/2026-09-07-from-senter.md].

#### Postcommit reliability

Hermes foreground work under MTPLX produced `cross_session_foreground_preempted` and `foreground_preempted_postcommit` events, followed by `retokenized_history_mismatch` postcommit artifacts. Those artifacts cannot be treated as finished TurboFit evidence without a real Hermes window capture .

#### Contested state

Hermes summaries claimed MTPLX was the locked main provider at 131K, but later command evidence reverted to Unleashed+DFlash2 after repeated instability, then to Ornith MLX .

#### Related

- [[topics/turbofit/wiki/entities/mplx.md|MPLX]]
- [[topics/turbofit/wiki/concepts/mtplx-context-overcommit.md|MPLX Context Overcommit]]
- [[topics/turbofit/wiki/entities/turbofit-memory-crash.md|TurboFit Memory Crash]]
- [[topics/turbofit/wiki/entities/mtplx-memory-guard.md|MPLX Memory Guard]]
- [[topics/turbofit/wiki/entities/mtplx-qwen-38-27b-optimized-speed.md|MPLX Qwen 3.8 27B Optimized Speed]]

### TurboFit Verifier Bridge

Source: `wiki/entities/turbofit-verifier-bridge.md`


`turbofit-verifier` is the existing TurboFit topic bot. This page records the new evidence that it should drive verification through `desktop_preview` on a real Hermes window instead of summary claims, and that long-running TurboFit workstreams need foreground-preemption handling so parked-on-card captures still count toward live work without breaking the 12/20-min sentinel rules .

#### Evidence

- "Background process proc_a162ec9b4e3c exited (exit code -9)" while running `mtplx serve` .
- "cross_session_foreground_preempted" and "foreground_preempted_postcommit" during generation, with unsafe reason `retokenized_history_mismatch` .
- `unsafe_reason: retokenized_history_mismatch` and `ssd_prefix_miss` indicate session restore/path mismatch rather than stable committed capture state .

#### Standing rule inferred

- Verify against actual Hermes window content only; do not assert preview state from process metadata or speculative reparented session summaries .

#### Related

- [[topics/turbofit/wiki/entities/turbofit.md|TurboFit]]
- [[topics/turbofit/wiki/concepts/model-switching-pain.md|Model Switching Pain]]

### TurboFit

Source: `wiki/entities/turbofit.md`


TurboFit is the adaptive local-inference path for Hermes on this 32 GB M1 Mac. It loads local models first and falls back to cloud providers when compression or context load exceeds what the box can sustain .

#### Current topology

- **Main**: Qwen3.8-27B-Unleashed + DFlash2 draft on `127.0.0.1:11606`, Metal, 131k context.
- **Aux / Compression**: Maple MLX on `127.0.0.1:11612`, served with the `deepgrove-ai/mlx-lm-deepgrove` runtime.
- **Vision**: routed to Unleashed; Maple has no projector.
- **Cloud fallback**: Nous free tier when local context exceeds memory/compression limits .

#### Runtimes on disk

- `llama.cpp-1c3c9674de4d455f1e571bed808252af54932767` — Unleashed + DFlash2 Metal build.
- `dflash2-llama.cpp-1deefcca395743049c3820ab8f9b15043f3e9446` — DFlash2 fork with Metal build.
- `maple-llama.cpp-9ee03eec62d088a117ab916bbe489e7a3872a21f` — Maple llama.cpp fork from `stamsam/llama.cpp` (CUDA-first).
- `/tmp/mlx-lm-deepgrove` — custom MLX runtime for Maple on Apple Silicon .

#### Related

- [[topics/turbofit/wiki/entities/unleashed-27b.md|Unleashed 27B]]
- [[topics/turbofit/wiki/entities/maple.md|Maple]]
- [[topics/turbofit/wiki/entities/dflash2-draft.md|DFlash2 Draft]]
- [[topics/turbofit/wiki/entities/mplx.md|MPLX]]

### Unleashed 27B

Source: `wiki/entities/unleashed-27b.md`


Qwen3.8-27B-Unleashed in `UD-Q3_K_XL.gguf` with the Unleashed vision projector and DFlash2 draft. This is the main model in TurboFit .

#### Served config

- **Runtime**: `llama.cpp` Metal build (`dflash2-llama.cpp-...`).
- **Port**: `11606`.
- **Context**: `131072`.
- **Draft**: `Qwen3.8-27B-DFlash2-Q4_K_M.gguf`, `--spec-type draft-dflash --spec-draft-n-max 7`.
- **KV cache**: `q4_0` k/v.
- **Batch**: `-b 512 -ub 256`.
- **Performance**: ~4.4–5.1 tok/s decode on this box .

#### Role

- Main inference and vision provider.
- Stable under long context and large prompt ingest.
- Holds the DFlash2 draft path that earlier failed with wrong draft flags (`--draft-max`) and tensor mismatch before being aligned to the fork’s `--spec-draft-*` args .

#### Related

- [[topics/turbofit/wiki/entities/turbofit.md|TurboFit]]
- [[topics/turbofit/wiki/entities/dflash2-draft.md|DFlash2 Draft]]
- [[topics/turbofit/wiki/decisions/main-model-selection.md|Main Model Selection]]

### Unleashed IQ3 XXS Load Failure

Source: `wiki/entities/unleashed-iq3-xxs-load-failure.md`


`Qwen3.8-27B-Unleashed-UD-IQ3_XXS.gguf` failed to load in the `dflash2-llama.cpp` fork Metal server after a DFlash warning about missing `ctx_other` and then a tensor bounds failure .

#### Evidence

- Warning: `dflash requires ctx_other to be set`
- Error: `tensor 'blk.2.attn_qkv.weight' data is not within the file bounds, model is corrupted or incomplete`
- Same load path repeated for `blk.2.ffn_down.weight`
- Server exited due to model loading error

#### Note

This failure is specific to this quant artifact and this fork load path. It does not invalidate `Q3_K_XL`, which has served as the stable long-context backup in earlier evidence.

#### Related

- [[topics/turbofit/wiki/entities/unleashed-27b|Unleashed 27B]]
- [[topics/turbofit/wiki/decisions/unleashed-backup|Unleashed Backup]]
- [[topics/turbofit/wiki/concepts/dflash2-compat-boundary|DFlash2 Compatibility Boundary]]


---

## Concepts

> All 14 technical concepts. Each entry preserves the full content of its source file.

### 131K Deferred Candidates

Source: `wiki/concepts/131k-deferred-candidates.md`


#### The Problem

A number of newly downloaded candidate artifacts were not benchmarked at 131K because model-plus-KV size exceeds the stable 32 GB Mac fit before testing begins.

From [[raw/inbox/2026-09-07.md|2026-09-07 08:36]]:

> "Several downloaded candidates were deferred from 131K testing because their size plus KV cache exceeds stable 32 GB fit before benchmark."

#### Why They're Deferred

The M1 MacBook 32GB has hard memory limits:

```
M1 MacBook 32GB unified memory:
- macOS + Hermes: ~8 GB
- Model weights: varies by model
- KV cache at 131K: ~8 GB (q8_0)
- Total needed: ~35+ GB > 32 GB available
```

##### Candidate Analysis

| Model | Weights | KV @ 131K | Total | Fits? |
| --- | --- | --- | --- | --- |
| **Ornith MLX 4-bit** | 18 GB | ~8 GB | ~26 GB | Yes |
| **Unleashed Q3_K_XL** | 12.31 GB | ~8 GB | ~20 GB | Yes |
| **Nail Q4_K_XL** | 20.8 GB | ~8 GB | ~29 GB | ⚠️ Marginal |
| **Tiel-Coder Q4_K_XL** | 22.4 GB | ~8 GB | ~30 GB | ⚠️ Marginal |
| **Dirk Q3_K_XL** | 13.1 GB | ~8 GB | ~21 GB | But slow/OOM |

#### Memory Guard Evidence

From [[raw/inbox/2026-09-07.md|2026-09-07 00:56]]:

```json
{
  "event": "prefill_admission_shed",
  "prompt_tokens": 8014,
  "projected_bytes": 26306738710,
  "threshold_bytes": 24996709662,
  "limit_bytes": 25769803776,
  "cache_cleared": true
}
```

This shows MTPLX's memory guard: prefill_admission_shed clears KV cache to stay under ~24.99 GB threshold on a 25.77 GB limit, corroborating existing 32GB/131K overcommit findings.

#### The Reality Check

From [[raw/inbox/2026-09-07.md|2026-09-07 09:20]]:

> "**The hard truth:** On M1 MacBook 32GB with a 27B model at 131K context, **~5-6 tok/s is the ceiling.** You want 10+ tok/s. That's not happening with this hardware — it's like asking a Honda Civic to go 200mph."

#### Testing Strategy

**Working at 131K:**
- Ornith MLX 4-bit (18 GB)
- Unleashed Q3_K_XL (12.31 GB) + DFlash2 draft (1 GB)

**Deferred to smaller contexts:**
- Dirk Q3_K_XL - tested at 32K only (OOM at 65K)
- Nail Q4_K_XL - testing incomplete due to OOM risk
- Tiel-Coder Q4_K_XL - tested at 65K

#### Key Insight

The winner for 131K must balance:
1. Model weights under ~18-20 GB
2. Efficient quantization (Q3/Q4)
3. MoE architecture OR small enough dense model

Ornith MLX 4-bit wins because it's MoE (~3B active params) with MLX backend for native Metal acceleration.

#### Related

- [[turbofit/concepts/mtplx-32gb-memory-and-evidence-reliability|MPLX 32GB Memory and Evidence Reliability]]
- [[turbofit/entities/turbofit-memory-crash|TurboFit Memory Crash]]
- [[turbofit/entities/mplx-memory-guard|MPLX Memory Guard]]

### Benchmark Taxonomy

Source: `wiki/concepts/benchmark-taxonomy.md`


> Common benchmarks tracked across all models. Each model page records scores where available.

#### Reasoning & Knowledge

| Benchmark | What it measures | Why it matters |
| --- | --- | --- |
| MMLU | Multitask language understanding (57 subjects) | General knowledge breadth |
| ARC-Challenge | Grade-school science questions | Logical reasoning |
| HellaSwag | Sentence completion | Common-sense reasoning |
| WinoGrande | Pronoun resolution | Contextual understanding |
| TruthfulQA | Truthfulness | Hallucination resistance |

#### Coding

| Benchmark | What it measures | Why it matters |
| --- | --- | --- |
| HumanEval | Python code generation | Raw coding ability |
| MBPP | Basic Python problems | Everyday coding |
| LiveCodeBench | Competitive programming | Complex problem solving |

#### Math

| Benchmark | What it measures | Why it matters |
| --- | --- | --- |
| GSM8K | Grade-school math word problems | Mathematical reasoning |
| MATH | Competition mathematics | Advanced math |

#### Long Context

| Benchmark | What it measures | Why it matters |
| --- | --- | --- |
| RULER | Long-context retrieval | Context window quality |
| Needle-in-Haystack | Needle retrieval at length | Factual recall at depth |

#### Inference Performance

| Metric | What it measures | Why it matters |
| --- | --- | --- |
| tok/s @ 4K ctx | tokens/sec at 4K context | Short-context tok/s |
| tok/s @ 32K ctx | tokens/sec at 32K context | Mid-context sustained |
| tok/s @ 128K ctx | tokens/sec at 128K context | Long-context sustained |
| TTFT | Time to first token | Initial latency |
| VRAM usage | GPU memory at load | Hardware feasibility |
| RAM usage | System memory at load | Unified memory feasibility |

#### Vision (for multimodal models)

| Benchmark | What it measures |
| --- | --- |
| MMMU | Multimodal understanding |
| TextVQA | Text reading in images |
| OCRBench | Document OCR |

#### Retrieval (for embedding models)

| Benchmark | What it measures |
| --- | --- |
| MTEB | General retrieval |
| BEIR | Zero-shot retrieval |

#### Usage

When adding a model page, fill in any of the above benchmarks where data is available from:
- HuggingFace model card (they often list benchmarks)
- Independent benchmarks (llama.cpp community, etc.)
- Our own testing results

Models without data simply show "—" — this is expected and motivates future research.

### Bonsai and Colibri Deprioritization

Source: `wiki/concepts/bonsai-colibri-deprioritization.md`


#### What happened

During the 2026-09-07 testing session, subagents explored multiple candidate models including Bonsai (Prism MLX 2-bit ternary, 7.91 GB) and Colibri (custom Maple format). Both were downloaded but neither ran successfully:

- **Colibri**: Failed to load because the standard `mlx_lm` server could not find `config.json`; the model requires custom Maple MLX code .
- **Bonsai MLX 2-bit**: Server started but exited with `FileNotFoundError` on `config.json` .

#### Chris's directive

Chris repeatedly redirected focus to Ornith as the sole priority. Three near-identical raw messages at 13:18, 13:20, and 13:30 show his exact framing:

> "It just needs to be configured into turbofit so I can continue with Ornith. Don't worry about bonsai."

> "I'm actually gonna switch models to Ornith because it's smarter than the free models that we're using currently, so if you can get Ornith up on TurboFit first and configured in the way that we had it, then we can continue working after I switch to that model."

> "It just needs to be configured into turbofit so I can continue with Ornith. Don't worry about bonsai. I said the model that we're using is too dumb, okay? So we need to focus entirely on getting Ornith up so I can pick it from the model picker like the other turbofit models."

These messages were followed by Chris switching his active provider to `ornith-1-5-35a3b-mlx via provider turbofit` .

#### The hardware reality

Hermes summarized the hard constraint: on M1 32GB with a 27B model at 131K context, ~5-6 tok/s is the ceiling. The hardware cannot hold 19.3 GB model weights + 8 GB KV cache at 131K + macOS overhead .

#### Conclusion

Bonsai and Colibri are parked. The active work is Ornith MLX 4-bit as the main turbofit provider, with the contest that Hermes connection timeouts persisted after config repoint and a verified post-restart live completion is still pending.

#### Related

- [[topics/turbofit/wiki/entities/bonsai.md|Bonsai MLX]]
- [[topics/turbofit/wiki/entities/colibri.md|Colibri]]
- [[topics/turbofit/wiki/entities/ornith-1-5-35b-a3b-mlx-4-bit|Ornith 1.5 35B-A3B MLX 4-bit]]
- [[topics/turbofit/wiki/queries/evidence-capture-and-reliability|Evidence Capture and Reliability Query]]

### Compression Timeouts

Source: `wiki/concepts/compression-timeouts.md`


#### What happened

Hermes failed with:

```
Context compression timed out before it could commit while the request was still approximately 270,285 tokens.
```

The provider call was not sent. Compression ran repeatedly until it timed out instead of committing in time .

#### Root cause

Local main-model compression at very large context sizes is too slow for Hermes’s timeout. The problem moved from Unleashed 27B to Maple MLX before the Apple-Silicon runtime fixed it locally .

#### Mitigations

- 131k context cap for both main and aux.
- Maple MLX aux via `deepgrove-ai/mlx-lm-deepgrove` tested to handle 130K compression workloads in 103 s without OOM.
- If local compression still stalls, route compression to Nous free tier .

#### Evidence

- "Context compression timed out before it could commit while the request was still approximately 233,656 tokens" .
- "130K-token compression workload: 103 seconds, no OOM" .

#### Related

- [[topics/turbofit/wiki/decisions/context-sizing.md|Context Sizing]]
- [[topics/turbofit/wiki/decisions/aux-model-selection.md|Aux Model Selection]]
- [[topics/turbofit/wiki/entities/maple.md|Maple]]

### DFlash2 Compatibility Boundary

Source: `wiki/concepts/dflash2-compat-boundary.md`


DFlash2 draft models are not interchangeable across runtimes. On this box the boundary is concrete: MTPLX cannot use DFlash2, and Unleashed+DFlash2 only works through the dedicated `dflash2-llama.cpp` fork with a narrow valid flag set ^[raw/inbox/2026-09-07.md, raw/inbox/2026-09-07-from-music.md].

#### MTPLX

MTPLX uses native MLX MTP heads. `z-lab/Qwen3.8-27B-DFlash2` is a CUDA/llama.cpp/vLLM/sglang diffusion draft model and is incompatible with MTPLX ^[raw/inbox/2026-09-07.md, raw/inbox/2026-09-07-from-music.md].

#### Unleashed+DFlash2

Valid launch requires the `dflash2-llama.cpp` fork runtime at `~/.../runtimes/dflash2-llama.cpp-.../build-metal/bin/llama-server` and the flag `--model-draft` for the draft model path. Invalid flag attempts observed in this session:

- `--draft-ngl`
- `--draft-ctx-size`
- `--low-vram`
- `--draft-model`

These exited with `invalid argument` before binding the server .

#### Port conflicts

At least one Unleashed+DFlash2 attempt failed with `couldn't bind HTTP server socket, hostname: 127.0.0.1, port: 11606` because port 11606 was already in use, not because of model incompatibility .

#### Broken quant path

`Qwen3.8-27B-Unleashed-UD-IQ3_XXS.gguf` failed to load with `tensor 'blk.2.attn_qkv.weight' data is not within the file bounds` after a DFlash `dflash requires ctx_other to be set` warning. That artifact is not usable as a main model on this fork in current state .

#### Related

- [[topics/turbofit/wiki/entities/dflash2-draft|DFlash2 Draft]]
- [[topics/turbofit/wiki/entities/unleashed-27b|Unleashed 27B]]
- [[topics/turbofit/wiki/entities/mplx-metal-load-failure|MPLX Metal Load Failure]]
- [[topics/turbofit/wiki/decisions/context-sizing|Context Sizing]]

### DFlash2 Fork Flag Boundary

Source: `wiki/concepts/dflash2-fork-flag-boundary.md`


DFlash2 draft models are not interchangeable across runtimes. On this box the boundary is concrete: MTPLX cannot use DFlash2, and Unleashed+DFlash2 only works through the dedicated `dflash2-llama.cpp` fork with a narrow valid flag set.

#### MTPLX Incompatibility

MTPLX uses native MLX MTP heads. `z-lab/Qwen3.8-27B-DFlash2` is a CUDA-only diffusion-based draft model for llama.cpp/vLLM/sglang — incompatible with MTPLX's native MLX MTP heads.

**Key insight**: The DFlash2 draft path cannot be used with Ornith MLX because MLX uses native speculative decoding architectures, while DFlash2 is a llama.cpp/vLLM feature.

#### Unleashed+DFlash2 Flag Requirements

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
| --- | --- |
| `--draft-model` | invalid argument |
| `--draft-ngl` | invalid argument |
| `--draft-ctx-size` | invalid argument |
| `--low-vram` | invalid argument |
| `--model-draft` | invalid argument |

#### Port conflict evidence

At least one Unleashed+DFlash2 attempt failed with:

```
couldn't bind HTTP server socket, hostname: 127.0.0.1, port: 11606
```

Because port 11606 was already in use, not because of model incompatibility.

#### Broken quant path

`Qwen3.8-27B-Unleashed-UD-IQ3_XXS.gguf` failed to load with:

```
tensor 'blk.2.attn_qkv.weight' data is not within the file bounds, model is corrupted or incomplete
```

After a DFlash warning: `dflash requires ctx_other to be set`. That artifact is not usable as a main model on this fork.

#### Recommendation

- **Use Ornith MLX 4-bit** as primary local provider (fastest at short context)
- **Use Unleashed Q3_K_XL + DFlash2** as long-context fallback (stable ~5 tok/s)
- **Do not attempt DFlash2 with MTPLX** — architecture incompatibility is fundamental

#### Related

- [[topics/turbofit/wiki/entities/dflash2-draft.md|DFlash2 Draft]]
- [[topics/turbofit/wiki/entities/unleashed-27b.md|Unleashed 27B]]
- [[topics/turbofit/wiki/entities/ornith-35b-dflash2.md|Ornith 35B DFlash2]]
- [[topics/turbofit/wiki/entities/ornith-1-5-35b-a3b-mlx-4-bit.md|Ornith 1.5 35B-A3B MLX 4-bit]]

### DFlash2 MTPLX Incompatibility

Source: `wiki/concepts/dflash2-mplx-incompatibility.md`


#### The Incompatibility

DFlash2 draft models are incompatible with MTPLX's native MLX MTP heads. This is a fundamental architecture mismatch.

From [[raw/inbox/2026-09-07.md|2026-09-07 02:20]]:

> "DFlash2 is not available for MTPLX. `z-lab/Qwen3.8-27B-DFlash2` exists on HuggingFace but is a CUDA-only diffusion draft model for llama.cpp/vLLM/sglang — incompatible with MTPLX's native MLX MTP heads."

#### Technical Details

| Aspect | DFlash2 | MTPLX |
| --- | --- | --- |
| **Target runtime** | CUDA (llama.cpp/vLLM/sglang) | Apple Silicon MLX |
| **Draft architecture** | Diffusion-based speculative decoding | Native MTP (Machine-specific Parallelization Transfer) heads |
| **Hardware support** | NVIDIA GPU only | Apple Silicon Metal |

#### Evidence of Failure

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

#### Model Sizes

From [[raw/inbox/2026-09-07.md|2026-09-07 01:27]]:

| Model | Size |
| --- | --- |
| Unleashed Q3_K_XL | 12.31 GB |
| DFlash2 Q4_K_M (draft) | 1.06 GB |

With q8 KV cache at 131K: ~17 GB total fits in 32GB, but DFlash2 cannot be paired with MTPLX.

#### Workarounds

1. **Use MTPLX standalone** - Fast at 65K context (7-12 tok/s), but not with DFlash2
2. **Use Unleashed + DFlash2** - via llama.cpp fork at 131K (~5 tok/s)
3. **Use Ornith MLX** - MoE architecture with native speculative decoding

#### Why This Matters

The incompatibility explains why:
- MTPLX at 131K OOMed or crashed when users tried to add DFlash2
- The "memory budget" flag didn't work as expected
- Long-context inference without cloud fallback required choosing between incompatible options

#### Related

- [[entities/dflash2-arg-failures|DFlash2 Arg Failures]]
- [[entities/mplx-service-arg-validation|MPLX Service Arg Validation]]
- [[turbofit/entities/dflash2-draft|DFlash2 Draft]]
- [[turbofit/concepts/dflash2-compat-boundary|DFlash2 Compatibility Boundary]]

### Hermes Auto Route Stability

Source: `wiki/concepts/hermes-auto-route-stability.md`


#### The Problem

From `raw/inbox/2026-09-08-from-senter-wiki.md`:

> "The problem is: ... Hermes flips the active model to StepFun 3.7 Flash. Two causes appear in the transcript: `model.default` not being first in the fallback chain, and `auxiliary.compression.provider: auto` selecting StepFun for compression"

Hermes's auto-routing mechanism selected non-local providers multiple times during TurboFit testing, switching from:

1. Free local providers (Ornith via turbofit, MTPLX)
2. → To cloud providers (`stepfun/step-3.7-flash:free`, `anthropic/claude-fable-5.1`, etc.)

#### Observed evidence

- Multiple `[System: The active model for this chat has changed to ... via provider nous]` messages
- Compression timeouts at 262K+ tokens caused fallback to cloud providers
- Config showed `model.default: z-ai/glm-5.3-flash` but system reported `anthropic/claude-fable-5.1` active

#### Standing directive from Chris

> "The active model preference order should preserve explicit user choice and avoid silently switching to `stepfun/step-3.7-flash:free`" [[raw/inbox/2026-09-06.md]].

#### Resolution needed

1. Ensure `model.default` is the first entry in any fallback chain
2. Pin `auxiliary.compression.provider` to a local TurboFit route (Ornith or MTPLX) rather than `auto`
3. Consider disabling compression fallback to cloud providers for local-only workflow

#### Status

This stability issue may be resolved by the [[topics/turbofit/wiki/decisions/fallback-model-order.md|Fallback Model Order]] decision, pending verification that `model.default` appears first in the provider chain and compression stays pinned to local routes.

#### Related

- [[topics/turbofit/wiki/decisions/fallback-model-order.md|Fallback Model Order]]
- [[topics/turbofit/wiki/concepts/model-switching-pain.md|Model Switching Pain]]
- [[topics/turbofit/wiki/concepts/compression-timeouts.md|Compression Timeouts]]

### Hermes Model Switching Noise

Source: `wiki/concepts/hermes-model-switching-noise.md`


The active Hermes model switched multiple times during TurboFit work without Chris initiating the changes . The switch chain was:

1. `meituan/longcat-2.0:free` (Nous free tier)
2. `stepfun/step-3.7-flash:free` (Nous free tier)
3. `muse-spark-1.3-contributor-free`
4. `anthropic/claude-fable-5.1`
5. `openai/gpt-6-astra`
6. `ornith-1.5-35a3b-mlx via provider turbofit` (Chris's intended destination)

Later, the system reverted to `meituan/longcat-2.0:free` via provider nous, and then Chris switched to `ornith-1-5-35a3b-mlx via provider turbofit` at 14:25.

#### Evidence of unwanted switches

From Hermes logs in ``:
- `[System: The active model for this chat has changed to meituan/longcat-2.0:free via provider nous.]` at 14:30
- `[System: The active model for this chat has changed to ornith-1-5-35a3b-mlx via provider turbofit.]` at 14:42 (after Chris's explicit directive)

#### Why it matters

Unrequested model changes can invalidate benchmark context, tool routing, and session evidence. Chris wants TurboFit to stay on the chosen local runtime until he changes it himself. He explicitly stated his preference for Ornith: "I'm actually gonna switch models to Ornith because it's smarter than the free models that we're using currently" .

#### Related

- [[model-switching-pain|Model Switching Pain]]
- [[ornith-config-routing-failure|Ornith Config Routing Failure]]
- [[topics/turbofit/wiki/decisions/fallback-model-order|Fallback Model Order]]

### Model Switching Pain

Source: `wiki/concepts/model-switching-pain.md`


The active Hermes model switched multiple times during TurboFit work without Chris initiating the changes.

#### Observed switches

The switch chain during this session was:

1. `meituan/longcat-2.0:free` (Nous free tier)
2. `stepfun/step-3.7-flash:free` (Nous free tier)  
3. `muse-spark-1.3-contributor-free`
4. `anthropic/claude-fable-5.1`
5. `openai/gpt-6-astra`
6. `ornith-1-5-35a3b-mlx via provider turbofit` (Chris's intended destination)

Later, the system reverted to `meituan/longcat-2.0:free` via provider nous, and then Chris switched to `ornith-1-5-35a3b-mlx via provider turbofit` at 14:25.

#### Evidence of unwanted switches

From Hermes logs in `raw/inbox/2026-09-07.md`:

- `[System: The active model for this chat has changed to meituan/longcat-2.0:free via provider nous.]` at 14:30
- `[System: The active model for this chat has changed to ornith-1-5-35a3b-mlx via provider turbofit.]` at 14:42 (after Chris's explicit directive)

#### Why it matters

Unrequested model changes can invalidate benchmark context, tool routing, and session evidence. Chris wants TurboFit to stay on the chosen local runtime until he changes it himself. He explicitly stated his preference for Ornith: *"I'm actually gonna switch models to Ornith because it's smarter than the free models that we're using currently"* [[raw/inbox/2026-09-07.md]].

#### Root cause

Contributing causes identified in [[topics/turbofit/wiki/concepts/compression-timeouts.md|Compression Timeouts]]:

1. `fallback_providers` ordering that did not preserve explicit choice
2. `auxiliary.compression.provider: auto` picking a different provider/model for compression
3. Context-compression fallback to cloud providers when local compression timed out

#### Related

- [[topics/turbofit/wiki/decisions/fallback-model-order.md|Fallback Model Order]]
- [[topics/turbofit/wiki/concepts/compression-timeouts.md|Compression Timeouts]]
- [[topics/turbofit/wiki/entities/ornith-config-routing-failure.md|Ornith Config Routing Failure]]

### MTPLX 32GB Memory and Evidence Reliability

Source: `wiki/concepts/mtplx-32gb-memory-and-evidence-reliability.md`


Captures two distinct reliability concerns for MTPLX on this box: 131K memory overcommit, and postcommit artifacts that can't be treated as finished TurboFit evidence without a real Hermes window capture .

#### Memory overcommit

`mtplx serve --context-window 131072` loads the model and installs the native MTP draft head, but the memory plan marks the context as `OVERCOMMITTED` and warns that the requested context exceeds machine fit for the KV budget .

Live safeguard behavior:

- `prefill_admission_shed` clears KV cache when projected bytes exceed threshold.
- Under real foreground load, background processes still exit with code `-9`.
- Long prompts at 131K return `507 Insufficient Storage` or collapse to sub-1 tok/s  ^[raw/inbox/2026-09-07-from-senter.md].

#### Evidence reliability

Postcommit records show `cross_session_foreground_preempted` and `foreground_preempted_postcommit`, with unsafe reasons including `retokenized_history_mismatch`. A completion artifact generated under those conditions is not trustworthy as final TurboFit evidence; the required bar is a Hermes window capture judged from the primary viewport .

#### Stable target

65K remains the safe daily context on this box. 131K is a long-context fallback despite throughput collapse and active cache shedding .

#### Related

- [[topics/turbofit/wiki/entities/turbofit-mtpl-performance.md|TurboFit MTPLX Performance]]
- [[topics/turbofit/wiki/entities/mtplx-memory-guard.md|MPLX Memory Guard]]
- [[topics/turbofit/wiki/decisions/context-window-decision.md|Context Window Decision]]

### MPTX Context Overcommit

Source: `wiki/concepts/mtplx-context-overcommit.md`


On the 32 GB Mac, `mtplx serve` with `--context-window 131072` loads the model in 6-9s and installs the native MTP draft head, but the printed memory plan marks `OVERCOMMITTED` and warns that the requested context exceeds the machine fit.

#### Memory Plan Evidence

From the memory plan output:
```
Memory plan: 32G Mac: engine budget 24.0G, weights 19.3G, context 131072 (machine-bound) (OVERCOMMITTED), session bank up to 1.7G (yields to 1.0G under long-context load)
Memory plan: requested context 131072 exceeds the machine fit 8192: KV at the full window needs 8.0 GiB; expect cache shedding and, past the fit, swap
```

#### Why It Fails

```
Total needed:
- Model weights: 19.3 GB (MTPLX 27B Optimized Speed)
- KV cache @ 131K q8: 8.0 GB
- macOS + Hermes: ~8 GB
- Total: ~35.3 GB > 32 GB available
```

#### Observed Failures

1. **OOM during load**: `RuntimeError: [METAL] Command buffer execution failed: Insufficient Memory`
2. **Insufficient Storage**: During 5K+ prompt generation at 131K context
3. **End-to-end slowdown**: 0.39 tok/s observed for 2005-token history

#### Stable Alternative

65K context works stably:
- Memory after model: 24.0 GB budget
- KV cache @ 65K q8: ~4 GB
- Fits within 32 GB Mac memory

#### Related

- [[topics/turbofit/wiki/entities/mplx.md|MPLX]]
- [[topics/turbofit/wiki/entities/mplx-qwen-38-27b-optimized-speed.md|MPLX Qwen 3.8 27B Optimized Speed]]
- [[topics/turbofit/wiki/entities/mplx-memory-guard.md|MPLX Memory Guard]]

### MPLX Foreground Preemption

Source: `wiki/concepts/mtplx-foreground-preemption.md`


When MTPLX handles long-running Hermes foreground work, postcommit records show `cross_session_foreground_preempted` and `foreground_preempted_postcommit`, and idle async sessions can end with `stored: false` because of `unsafe_reason: retokenized_history_mismatch` .

#### Evidence

- postcommit event: `{"admitting_session_id": "anon-41e824508a39fedf", "count": 1, "reason": "cross_session_foreground_preempted", "sessions": ["anon-1acc43591680e54c"]}` .
- idle async session postcommit: `{"mode": "aborted", "reason": "foreground_preempted_postcommit", "session_id": "anon-1acc43591680e54c", "stored": false, "unsafe_reason": "retokenized_history_mismatch"}` .
- Second postcommit: `{"mode": "retokenized_history", "session_commit": {"committed": false, "prefix_len": 26, "reason": "retokenized_prefix_older_than_session"}, "unsafe_reason": "retokenized_history_mismatch"}` .

#### Preference

- Finish-state evidence for TurboFit should be captured from Chris's actual Hermes window; postcommit artifacts alone are unreliable under foreground preemption ^[raw/inbox/2026-09-07.md, raw/inbox/2026-09-07-from-senter-wiki.md].

#### Related

- [[topics/turbofit/wiki/entities/turbofit-mtp-performance.md|TurboFit MTP Performance]]
- [[topics/turbofit/wiki/entities/turbofit-memory-crash.md|TurboFit Memory Crash]]
- [[topics/turbofit/wiki/queries/turbofit-mtplx-coexistence.md|MTPLX Coexistence]]

### TurboFit Session Mismatch

Source: `wiki/concepts/turbofit-session-mismatch.md`


MTLPX generation events show foreground/preemption behavior and session-store mismatch that make some TurboFit captures unreliable as finished-state evidence .

#### Signals

- `cross_session_foreground_preempted`
- `foreground_preempted_postcommit`
- `unsafe_reason: retokenized_history_mismatch`
- `cache_hit: false`, `cache_miss_reason: ssd_prefix_miss`, `cached_tokens: 0` .

#### Impact

- The stored prefix/suffix can differ from the current runtime session history, so Hermes state remains likely but not provably stable from those captures alone .
- Preferred decision path: prefer committed results shown on Chris’s actual Hermes window rather than postcommit cache state .

#### Related

- [[topics/turbofit/wiki/entities/turbofit-verifier-bridge.md|TurboFit Verifier Bridge]]
- [[topics/turbofit/wiki/concepts/model-switching-pain.md|Model Switching Pain]]


#### Research Request

From [[raw/inbox/2026-09-07.md|2026-09-07 03:06]]: Chris asked to "Research and test ALL available Apple Silicon inference engines for Qwen 3.8 27B to find the fastest configuration: llama.cpp (different quants, KV cache types, speculative decoding), MLX (deepgrove fork), OMLX, FreeToken, and any other engines found. Report tok/s for each."

#### Tested Engines

##### Ornith MLX 4-bit
- **Server**: `mlx_lm server --model ~/Models/storage/ornith --port 11613`
- **Context**: 131K
- **Speed**: 28.5 tok/s short, 5.7 tok/s at 5K, ~5 tok/s at 131K
- **Status**: Winner for short/medium context

##### Tiel-Coder Q4_K_XL (llama.cpp)
- **Server**: `llama-server --model ~/Models/storage/tiel-coder-gguf/Tiel-Coder-35B-A3B-UD-Q4_K_XL.gguf --port 11622`
- **Context**: 65K
- **Speed**: 23.1 tok/s short, 4.2 tok/s at 5K
- **Status**: Working but slower than Ornith

##### Dirk Q3_K_XL (llama.cpp)
- **Server**: `llama-server --model ~/Models/storage/dirk-gguf/Dirk-Qwen3.8-27B-UD-Q3_K_XL.gguf --port 11621`
- **Context**: 32K (OOM at 65K)
- **Speed**: 6.0 tok/s short, 0.8 tok/s at 5K
- **Status**: OOM above 32K context

##### Nail Q4_K_XL (llama.cpp)
- **Server**: `llama-server --model ~/Models/storage/nail/Nail-Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf --port 11621`
- **Context**: 32K
- **Speed**: 23.4 tok/s short, 4.7 tok/s at 5K
- **Status**: MoE performs well at limited context

##### MTPLX Qwen 3.8 27B Optimized Speed
- **Server**: `mtplx serve --model Youssofal/Qwen3.8-27B-MTPLX-Optimized-Speed`
- **Context**: 65K (stable), 131K (overcommitted)
- **Speed**: 8-12 tok/s at 65K, OOM at 131K with large prompts
- **Status**: Fast at 65K but problematic at 131K

##### Unleashed + DFlash2 (llama.cpp fork)
- **Server**: `llama-server` with dflash2-llama.cpp fork
- **Context**: 131K (with q8 KV cache)
- **Speed**: ~5 tok/s stable
- **Issues**: DFlash2 flag incompatibilities, memory pressure
- **Status**: Slow but stable long-context option

#### Speed Comparison Table

| Setup | Short (500t) | 5K Prompt | 131K | Status |
| --- | --- | --- | --- | --- |
| **Ornith MLX 4-bit** | **28.5 tok/s** | 5.7 tok/s | ~5 tok/s | Best overall |
| Nail Q4_K_XL | 23.4 tok/s | 4.7 tok/s | - | ⚠️ 32K limit |
| Tiel-Coder Q4_K_XL | 23.1 tok/s | 4.2 tok/s | - | ⚠️ 65K limit |
| MTPLX 65K | 8-12 tok/s | - | - | Stable |
| Dirk Q3_K_XL | 6.0 tok/s | 0.8 tok/s | OOM | Fails |
| Unleashed+DFlash2 | 5 tok/s | - | **~5 tok/s** | Long-context |

#### Hardware Reality Check

From [[raw/inbox/2026-09-07.md|2026-09-07 05:41]]:

> "**The hard truth:** On M1 MacBook 32GB with a 27B model at 131K context, **~5-6 tok/s is the ceiling.** You want 10+ tok/s. That's not happening with this hardware — it's like asking a Honda Civic to go 200mph."

#### Key Findings

1. **MLX beats llama.cpp for 27B models on M1** - Native Metal acceleration is essential
2. **MoE architecture wins** - Models with ~3B active params outperform dense models
3. **65K is the practical limit** for fast inference on 32GB M1
4. **DFlash2 compatibility is runtime-specific** - Incompatible with MTPLX's MLX heads

#### Related

- [[turbofit/queries/engine-research-request|Engine Research Request]]
- [[turbofit/entities/ornith-1-5-35b-a3b-mlx-4-bit|Ornith 1.5 35B-A3B MLX 4-bit]]
- [[turbofit/concepts/dflash2-mplx-incompatibility|DFlash2 MTPLX Incompatibility]]

Detected by title/source scan after the 2026-09-07 compile.

#### Title duplicate

- `TurboFit MTP Performance` — `wiki/entities/turbofit-mtp-performance.md`
- `TurboFit MTPLX Performance` — `wiki/entities/turbofit-mtpl-performance.md`

#### Source overlap clusters

These pages share `raw/inbox/2026-09-07.md` and may be describing the same event set from different angles:
- `decisions/unleashed-backup.md`, `decisions/context-window-decision.md`, `decisions/candidate-quant-preference.md`, `decisions/mtplx-main-provider.md`
- `concepts/turbofit-session-mismatch.md`, `concepts/hermes-model-switching-noise.md`, `concepts/mtplx-context-overcommit.md`
- entities: `ornith-config-routing-failure.md`, `dirk-gguf.md`, `unleashed-iq3-xxs-load-failure.md`, `ornith-35b-mlx.md`, `turbofit-mtp-performance.md`, `dflash2-arg-failures.md`, `mtplx-qwen-38-27b-optimized-speed.md`, `dirk-qwen38-27b.md`, `mplx-metal-load-failure.md`, `mtplx-service-arg-validation.md`, `nail-qwen36-35b.md`, `turbofit-verifier-bridge.md`, `ornith-35b.md`, `tiel-coder.md`, `ornith-35b-dflash2.md`, `turbofit-mtpl-performance.md`
- queries: `engine-research-request.md`, `turbofit-mtplx-coexistence.md`, `ornith-cleanup-focus.md`, `engine-speed-report.md`

Do not merge in compile; merging needs paladin/umbrella governance.

Chris asked for research and testing of all available Apple Silicon inference engines for Qwen 3.8 27B to find the fastest configuration .

#### Requested coverage

- llama.cpp with different quants, KV cache types, and speculative decoding.
- MLX with the deepgrove fork.
- OMLX.
- FreeToken.
- Any other discovered engine.

#### Open question

Which runtime provides the highest tok/s on this M1 32 GB box, and which artifact path achieves it at 65K and 131K contexts without Hermes reload failure?

#### Findings

##### Tested Engines

1. **Ornith MLX 4-bit** (peculiar-ragdoll/Ornith-1.5-35B-A3B-MLX)
   - Short (500t): **28.5 tok/s**
   - 65K: 23.1 tok/s
   - 131K: ~0.5 tok/s (KV cache dominant)

2. **MTPLX Qwen 3.8 Optimized Speed** (Youssofal/Qwen3.8-27B-MTPLX-Optimized-Speed)
   - Short: 8-12 tok/s
   - 65K: ~7 tok/s stable
   - 131K: OOM/507 errors

3. **Unleashed + DFlash2** (outsourc-e/Qwen3.8-27B-Unleashed)
   - Short: 5-6 tok/s
   - 131K: ~5 tok/s stable
   - Requires dflash2-llama.cpp fork

4. **Dirk Q3_K_XL** (peculiar-ragdoll/Dirk-Qwen3.8-27B-GGUF)
   - 32K: 6.0 tok/s
   - Any larger: OOM

5. **Tiel-Coder Q4_K_XL** (peculiar-ragdoll/Tiel-Coder-35B-A3B-GGUF)
   - 65K: 23.1 tok/s
   - 131K: deferred (OOM expected)

6. **Nail Q4_K_XL** (peculiar-ragdoll/Nail-Qwen3.6-35B-A3B-GGUF)
   - Short: 23.4 tok/s
   - 5K: 4.7 tok/s
   - 131K: OOM expected

7. **Maple MLX** (deepgrove-ai/mlx-lm-deepgrove)
   - Aux only, deleted due to memory pressure

#### Recommendation

Lock in **Ornith MLX 4-bit** as main provider at 65K context (28.5 tok/s short). Use **Unleashed + DFlash2** as 131K fallback (~5 tok/s). 10+ tok/s at 131K is hardware-limited on M1 32GB.

#### Related

- [[topics/turbofit/wiki/queries/apple-silicon-runtime-benchmark.md|Apple Silicon Runtime Benchmark]]
- [[topics/turbofit/wiki/decisions/context-window-decision.md|Context Window Decision]]

This is the live result surface of Chris's research request for Apple Silicon engine speed testing.

#### Winner: Ornith MLX 4-bit

**Selected as primary provider** on 2026-09-07 after comprehensive testing.

#### Performance Summary

|| Model | Type | Context | Short | 5K | Status |
| --- | --- | --- | --- | --- | --- | --- |
|| **Ornith MLX 4-bit** | MoE 35B | **131K** | **28.5 tok/s** | **5.7 tok/s** | Winner |
|| MTPLX Optimized Speed | 27B | 65K | 8-12 tok/s | - | - |
|| Nail Q4_K_XL | MoE 35B | 32K | 23.4 tok/s | 4.7 tok/s | ⚠️ Not fit at 131K |
|| Tiel-Coder Q4_K_XL | MoE 35B | 65K | 23.1 tok/s | 4.2 tok/s | ⚠️ Not fit at 131K |
|| Dirk Q3_K_XL | Dense 27B | 32K | 6.0 tok/s | 0.8 tok/s | ⚠️ OOM above 32K |

#### Contested promotion

Ornith is configured as default at 131K, but Hermes `custom:turbofit` showed persistent `Connection error` timeouts (code: timeout, 2026-09-07T19:26:47) after the 14:25 config change. A Hermes session restart is required to clear stale connection state before the promotion can be considered verified live.

#### Why Ornith Won

1. **Only model at 131K**: Ornith is the only candidate that actually works at 131K context
2. **Best short-context speed**: 28.5 tok/s beats all competitors
3. **MoE efficiency**: 35B total params, 3B active per token = fast and memory-efficient
4. **MLX backend**: Native Metal acceleration on Apple Silicon

#### The Hardware Reality

> "10+ tok/s at 131K is not happening on M1 32GB with a 27B model. It's like asking a Honda Civic to go 200mph."

The M1 32GB simply cannot hold:
- 19.3 GB model weights (MTPLX)
- 8 GB KV cache at 131K
- 8 GB macOS + Hermes

**Total: ~35 GB needed > 32 GB available**

#### Final Recommendations

| Use Case | Model | Context | Speed |
| --- | --- | --- | --- |
| Daily driver (short/medium) | **Ornith MLX** | 131K | 28.5 tok/s short |
| Long-context heavy | Unleashed+DFlash2 | 131K | ~5 tok/s stable |
| Storage-constrained | Nail | 32K | 23.4 tok/s |

#### Active Configuration

```yaml
model:
  default: ornith-1-5-35a3b-mlx
  provider: custom:turbofit
providers:
  turbofit:
    api: http://127.0.0.1:11613/v1
    default_model: ornith-1-5-35a3b-mlx
```

#### Related

- [[topics/turbofit/wiki/queries/apple-silicon-runtime-benchmark.md|APL_Silicon Runtime Benchmark]]
- [[topics/turbofit/wiki/entities/ornith-35b-mlx.md|Ornith 35B MLX]]
- [[topics/turbofit/wiki/decisions/context-window-decision.md|Context Window Decision]]

Captures the open verification work after configuring Ornith as main, and the contested state where Hermes showed persistent timeouts after config repoint.

#### Question 1

Did Hermes complete a live request through `custom:turbofit` -> `http://127.0.0.1:11613/v1` after repoint and restart?

**Answer needed**: Despite the 14:25 config change setting `providers.turbofit.api: http://127.0.0.1:11613/v1` and session metadata confirming `ornith-1-5-35a3b-mlx via provider turbofit`, persistent `Connection error` timeouts recurred at 2026-09-07T19:26:47.525Z . A post-restart live capture is required to verify the routed state.

#### Question 2

What is the smallest reproducible prompt that exhibits the Hermes provider timeout?

**Status**: Timeout occurred at the provider level without clear user-facing prompt dependency. The error `code: timeout, provider: turbofit, model: ornith-1-5-35a3b-mlx, error: Connection error.` suggests stale connection state rather than prompt size.

#### Question 3

If the Hermes timeout was only during transition, what is the canonical approval path after restart?

**Canonical path** (per turbofit skill):

1. Verify local server health (`curl http://127.0.0.1:11613/health`)
2. Check `/v1/models` endpoint responds with `ornith-1-5-35a3b-mlx` in model list
3. Capture a real Hermes window completion via `desktop_preview open` with vision verification
4. Record approval with `CLAIM` badge on the evidence page

#### Related pages

- [[turbo-fit-evidence-capture|TurboFit Evidence Capture]]
- [[local-main-provider|Local Main Provider]]
- [[ornith-1-5-35b-a3b-mlx-4-bit|Ornith 1.5 35B-A3B MLX 4-bit]]

#### Question

Can Maple serve stable long-context compression workloads on Apple Silicon Metal without repeated OOM, or is a non-server execution path required?

#### Evidence gathered

- The `stamsam/llama.cpp` fork does not have Metal kernels for `tq2_0` quant.
- Q2_0 GGUF under the fork fails tensor reads.
- Generic `mlx_lm` server grows prompt cache until Metal heap dies.
- `deepgrove-ai/mlx-lm-deepgrove` with `--flash-head --trust-remote-code` handled 130K tokens without OOM, but server mode remains cache-pressure sensitive .

#### Why this matters

Chris wants Maple as auxiliary on this M1 Mac. If Metal server mode cannot stay stable, TurboFit needs a safer local execution strategy than naive server reuse.

#### Related

- [[topics/turbofit/wiki/comparisons/aux-runtime-options.md|Aux Runtime Options]]
- [[topics/turbofit/wiki/entities/maple.md|Maple]]
- [[topics/turbofit/wiki/entities/mplx.md|MPLX]]

#### Question

Can MPLX be added as a fast local TurboFit provider alongside Unleashed 27B without evicting the main model, and what is the memory ceiling under MTP?

#### Evidence gathered

- 12.4 tok/s measured under MTP, faster than Unleashed Q3_K_XL.
- Download completed at 21:39; 26 GB used, 5.7 GB free alongside Unleashed.
- Testing halted before serving, so integration path, provider config, and context limit are unknown .

#### Why this matters

If MPLX can share the box with Unleashed, it may become a faster aux or alternate main path. If not, it may replace Unleashed or run as an offline benchmark lane.

#### Related

- [[topics/turbofit/wiki/entities/mplx.md|MPLX]]
- [[topics/turbofit/wiki/entities/turbofit.md|TurboFit]]
- [[topics/turbofit/wiki/decisions/main-model-selection.md|Main Model Selection]]

Chris wanted Ornith prioritized over Bonsai, Colibri, and music-generation side paths. His exact instruction was, "It just needs to be configured into turbofit so I can continue with Ornith. Don't worry about bonsai." .

Later he said, "Current immediate goal: clean up obsolete 27B model files (Nail, Tiel-Coder, etc.), then test Bonsai vs Maple Colibri vs Ornith 1.5 35A3B at 131K context, clearing old models between tests to free RAM." .

#### Open

- Whether obsolete Nail/Tiel-Coder/Dirk/Colibri files were actually removed after the rerouted cleanup burst.
- Whether the post-cleanup test plan was actually executed or abandoned when Chris redirected back to Ornith routing.

#### Related

- [[ornith-1-5-35b-a3b-mlx-4-bit|Ornith 1.5 35B-A3B MLX 4-bit]]
- [[local-main-provider|TurboFit Local Main Provider Decision]]

#### Evidence: No — MTPLX cannot coexist at 131K on this 32GB box

| Scenario | Result | Notes |
| --- | --- | --- |
| MTPLX 131K with 500-token prompt | 8–12 tok/s | Stable |
| MTPLX 131K with 5K+ prompt | OOM / 507 Insufficient Storage | Memory overcommit |
| MTPLX 131K with DFlash2 draft | Not available | DFlash2 incompatible with MLX MTP |
| Unleashed + DFlash2 131K | ~5 tok/s | Stable but slower than 65KMTPLX |
| Ornith 35B MLX 4-bit 131K | ~0.5 tok/s | KV cache dominates |

#### Key Constraint

**32GB physical RAM limitation:** 27B model weights (19.3GB) + KV cache at 131K (8GB) + macOS/Hermes (~8GB) = ~35GB+, exceeding available memory.

The memory plan explicitly shows `OVERCOMMITTED` before any generation:
```
Memory plan: 32G Mac: engine budget 24.0G, weights 19.3G, context 131072 (machine-bound) (OVERCOMMITTED)
requested context 131072 exceeds the machine fit 8192: KV at the full window needs 8.0 GiB
```
.

#### Pattern: Stable vs Overcommitted

- **65K context:** Stable across all runtimes (MTPLX ~7 tok/s, Unleashed+DFlash2 ~5 tok/s)
- **131K context:** Consistent OOM/kill on 5K+ prompts regardless of runtime

#### Related

- [[topics/turbofit/wiki/concepts/mtplx-context-overcommit|MPLX Context Overcommit]]
- [[topics/turbofit/wiki/entities/turbofit-memory-crash|TurboFit Memory Crash]]
- [[topics/turbofit/wiki/entities/turbofit-mtp-performance|TurboFit MTP Performance]]
- [[topics/turbofit/wiki/decisions/context-window-decision|Context Window Decision]]

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

### Ornith Config Routing

Source: `wiki/decisions/ornith-config-routing.md`


#### Decision

**Action**: Repoint Hermes `custom:turbofit` to the running Ornith MLX server on `http://127.0.0.1:11613/v1` and set `ornith-1-5-35a3b-mlx` as the default model.

#### Configuration Applied

```yaml
model.default: ornith-1-5-35a3b-mlx
model.provider: custom:turbofit
providers.turbofit.api: http://127.0.0.1:11613/v1
providers.turbofit.default_model: ornith-1-5-35a3b-mlx
```

#### Why Ornith

From [[raw/inbox/2026-09-07.md|2026-09-07 06:18]]:

> "**Ornith MLX 4-bit** is the fastest local short-context candidate on this box at 28.5 tok/s for 500-token prompts, but drops to ~0.5 tok/s at 131K and is not a stable long-context main on 32 GB. Unlocked Ornith as main provider."

#### Evidence Summary

| Model | Short | 5K | 131K |
| --- | --- | --- | --- |
| **Ornith MLX 4-bit** | **28.5 tok/s** | 5.7 tok/s | ~5 tok/s |
| Nail Q4_K_XL | 23.4 tok/s | 4.7 tok/s | OOM |
| Tiel-Coder Q4_K_XL | 23.1 tok/s | 4.2 tok/s | Not specified |
| Dirk Q3_K_XL | 6.0 tok/s | 0.8 tok/s | OOM |

#### Post-Routing Issues

At [[raw/inbox/2026-09-07.md|2026-09-07 14:26]], Hermes showed timeout errors despite the server being live:

```
layer: provider
code: timeout
model: ornith-1-5-35a3b-mlx
error: Connection error.
```

**Resolution**: A Hermes session or gateway restart may be needed to refresh provider route state after config changes.

#### Final Status

At [[raw/inbox/2026-09-07.md|2026-09-07 14:30]]: Ornith is running on port 11613 and the config shows it as the default provider. Chris reported at [[raw/inbox/2026-09-07.md|14:28]] that "Ornith is live and active on your session now."

#### Related

- [[entities/ornith-1-5-35b-a3b-mlx-4-bit|Ornith 1.5 35B-A3B MLX 4-bit]]
- [[entities/ornith-config-routing-failure|Ornith Config Routing Failure]]
- [[turbofit/entities/mplx.md|MPLX]]

### Unleashed Backup

Source: `wiki/decisions/unleashed-backup.md`


#### What

Keep Unleashed Q3_K_XL as the safe long-context backup when MTPLX overcommits memory or Hermes reloads fail.

#### Why

Chris explicitly said "Keep the Unleashed Q3_K_XL as backup (slower but handles 131K via llama.cpp offload)" and Unleashed+DFlash2 provides:
- Stable 131K context (~5 tok/s)
- Vision projector (MTPLX does not replace this)
- DFlash2 integration via dedicated dflash2-llama.cpp fork
- Smaller footprint than MTPLX (12.31 GB vs 19.3 GB)

#### Memory Comparison

| Model | Weights | KV @131K | Total | Status |
| --- | --- | --- | --- | --- |
| **Unleashed Q3_K_XL + DFlash2** | 12.31 GB + 1.06 GB | ~8 GB (q8) | ~21 GB | Fits |
| MTPLX Qwen 3.8 Optimized | 19.3 GB | ~8 GB | ~28 GB | Overcommit |

#### Status Updates (2026-09-07)

The following events occurred during the session:

1. **MTPLX instability**: Multiple `-9` exits and `OVERCOMMITTED` warnings at 131K
2. **Deletion claimed**: Hermes summary stated Maple (53GB) and Unleashed (23GB) deleted, freeing 76GB
3. **Re-download**: Later turns re-downloaded Unleashed Q3_K_XL and DFlash2 files
4. **Final state**: Unleashed+DFlash2 active on `:11606` at 131K with q8 KV cache

**Key insight**: The disk state is contested - files were deleted then re-downloaded.

#### When

- Set 2026-09-07 00:25 after MTPLX `-9` exits
- Re-confirmed 2026-09-07 02:33 after DFlash2 integration failed with invalid flags
- Active 2026-09-07 03:03 with q8 KV quantization

#### Conclusion

Unleashed Q3_K_XL remains the **only viable 131K solution** on this 32 GB hardware. It:
- Fits within memory limits (21 GB total with DFlash2)
- Provides stable ~5 tok/s throughput
- Has vision capability via mmproj projector

#### Related

- [[topics/turbofit/wiki/entities/unleashed-27b.md|Unleashed 27B]]
- [[topics/turbofit/wiki/entities/dflash2-draft.md|DFlash2 Draft]]
- [[topics/turbofit/wiki/decisions/main-model-selection.md|Main Model Selection]]
- [[topics/turbofit/wiki/concepts/mtplx-context-overcommit.md|MPLX Context Overcommit]]


---

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
