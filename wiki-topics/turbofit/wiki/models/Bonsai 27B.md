---
title: Bonsai 27B
created: 2026-09-16
updated: 2026-09-16
type: model
tags: [model, ternary]
sources: []
---

# Bonsai 27B

> Ternary 1-bit quantization, ~64GB for 27B params.

## Specifications

- **HuggingFace:** [prism-ml/Bonsai-27B-gguf](https://huggingface.co/prism-ml/Bonsai-27B-gguf)
- **Type:** LLM (Ternary)
- **Architecture:** Dense (quantized)
- **Parameters:** 27B
- **Active params per token:** 27B
- **Context window:** Unknown
- **Quantization:** Ternary 1-bit / 2-bit
- **Size on disk:** 64G
- **Format:** GGUF

## System Availability

| System | Available | Path |
|--------|-----------|------|
| Omarchy | Yes | `/home/sovthpaw/Models/storage/gguf/prism-ml_Bonsai-27B-gguf/` |
| MacBook | No | `—` |

## Inference Performance

| Runtime | Platform | tok/s | Notes |
|---------|----------|-------|-------|
| llama.cpp CUDA | Omarchy RTX 3090×2 | — |  |
| llama.cpp Metal | MacBook M1 Pro | — |  |
| MLX | MacBook M1 Pro | — |  |

## Benchmarks

> Filled in as research completes. Use [[benchmark-taxonomy|Benchmark Taxonomy]] for the canonical list.

### Reasoning & Knowledge

| Benchmark | Score |
|-----------|-------|
| MMLU | — |
| ARC-C | — |
| HellaSwag | — |
| WinoGrande | — |
| TruthfulQA | — |

### Coding

| Benchmark | Score |
|-----------|-------|
| HumanEval | — |
| MBPP | — |
| LiveCodeBench | — |

### Math

| Benchmark | Score |
|-----------|-------|
| GSM8K | — |
| MATH | — |

### Long Context

| Benchmark | Score |
|-----------|-------|
| RULER | — |
| Needle-in-Haystack | — |

## Research Notes
> Notes from focused sub-agent research.

### Bonsai MLX

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

- [[ornith-1-5-35b-a3b-mlx-4-bit|Ornith 1.5 35B-A3B MLX 4-bit]]
- [[engine-research-request|Engine Research Request]]
- [[local-main-provider|TurboFit Local Main Provider Decision]]


### Colibri

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

- [[maple|Maple]]
- [[ornith-1-5-35b-a3b-mlx-4-bit|Ornith 1.5 35B-A3B MLX 4-bit]]
- [[local-main-provider|TurboFit Local Main Provider Decision]]


### Bonsai and Colibri Deprioritization

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

- [[bonsai|Bonsai MLX]]
- [[colibri|Colibri]]
- [[ornith-1-5-35b-a3b-mlx-4-bit|Ornith 1.5 35B-A3B MLX 4-bit]]
- [[evidence-capture-and-reliability|Evidence Capture and Reliability Query]]


## See Also

- [[benchmark-taxonomy|Benchmark Taxonomy]]
- [[index|Wiki Index]]

### From entity: bonsai

## What this is

Bonsai refers to models from `prism-ml`: `Bonsai-27B-mlx-1bit` (1-bit binary, 1.4M downloads) and `Ternary-Bonsai-27B-mlx-2bit` (2-bit ternary, 1.4M downloads). The Ternary 2-bit variant at 7.91 GB was downloaded to `~/Models/storage/bonsai-mlx/` for testing on the M1 32GB box ^[raw/inbox/2026-09-07.md].

A separate GGUF variant also exists but requires llama.cpp, not MLX.

## Status

- **Ternary Bonsai MLX 2-bit** — downloaded (7.91 GB), files intact, but server failed to start because `/bonsai-mlx/config.json` was missing ^[raw/inbox/2026-09-07.md]. The process exited with `FileNotFoundError` on `config.json`.
- **Bonsai MLX 1-bit** — downloaded from prism-ml but was "not the right variant" per Hermes assessment ^[raw/inbox/2026-09-07.md].
- **Bonsai GGUF** — requires llama.cpp runtime, incompatible with the active MLX turbofit engine.

## Chris's directive

Chris explicitly said "Don't worry about bonsai" — his priority was getting Ornith up as the main provider so he could continue working. Bonsai was deprioritized twice: at 2026-09-07 13:18 and again at 13:30, both times stating "It just needs to be configured into turbofit so I can continue with Ornith" ^[raw/inbox/2026-09-07.md].

## Memory fit

At 7.91 GB, Ternary Bonsai would fit within the 32 GB memory budget, but no verified speed tests were completed before Chris redirected focus to Ornith ^[raw/inbox/2026-09-07.md].

## Related

- [[ornith-1-5-35b-a3b-mlx-4-bit|Ornith 1.5 35B-A3B MLX 4-bit]]
- [[engine-research-request|Engine Research Request]]
- [[local-main-provider|TurboFit Local Main Provider Decision]]
