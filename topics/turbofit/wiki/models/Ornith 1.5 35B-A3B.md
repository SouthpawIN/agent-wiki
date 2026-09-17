---
title: Ornith 1.5 35B-A3B
created: 2026-09-16
updated: 2026-09-16
type: model
tags: [model, code]
sources: []
---

# Ornith 1.5 35B-A3B

> Predecessor to Cyber Tiel Coder, legacy MacBook model.

## Specifications

- **HuggingFace:** [none](#)
- **Type:** Code LLM
- **Architecture:** MoE
- **Parameters:** 35B
- **Active params per token:** 3B
- **Context window:** 131K
- **Quantization:** MLX 4-bit
- **Size on disk:** 21G
- **Format:** GGUF

## System Availability

| System | Available | Path |
|--------|-----------|------|
| Omarchy | No | `—` |
| MacBook | Yes | `~/Models/storage/gguf/Ornith-1.5-35B-A3B/` |

## Inference Performance

| Runtime | Platform | tok/s | Notes |
|---------|----------|-------|-------|
| llama.cpp CUDA | Omarchy RTX 3090×2 | — |  |
| llama.cpp Metal | MacBook M1 Pro | — |  |
| MLX | MacBook M1 Pro | — |  |

## Benchmarks

> Filled in as research completes. Use [[concepts/benchmark-taxonomy|Benchmark Taxonomy]] for the canonical list.

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

### Ornith 35B A3B

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


### Ornith 1.5 MLX 4-bit

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


### Ornith Config Routing Failure

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


### Nail Qwen 3.6 35B UD Q4_K_XL

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


### Ornith Config Routing

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


## See Also

- [[concepts/benchmark-taxonomy|Benchmark Taxonomy]]
- [[topics/turbofit/wiki/index|Wiki Index]]

### From entity: ornith-1-5-35b-a3b-mlx-4-bit

Local candidate for TurboFit main on the M1 32GB box, owned by MLX, tested from `~/Models/storage/ornith/`.

## What this is

Ornith is a Mixture of Experts (MoE) model with 35B total parameters and roughly 3B active parameters per token. The tested artifact here is the MLX 4-bit build served by `mlx_lm server` on `http://127.0.0.1:11613/v1`. This is the variant Chris repeatedly wanted running on TurboFit so he could switch Hermes off weaker free models.

^[raw/inbox/2026-09-07.md]

## Provenance

Ornith is owned by TurboFit routing, not the wiki itself. See `[[turbofit-runtime-providers|TurboFit Runtime Providers]]` and `[[turbo-fit-evidence-capture|TurboFit Evidence Capture]]` for how service health should be checked when Hermes can't reach it.

^[raw/inbox/2026-09-07-from-senter-wiki.md]

## Status

- **Local server:** MLX deepgrove fork via `mlx_lm server --model ~/Models/storage/ornith --port 11613 --host 127.0.0.1` ^[raw/inbox/2026-09-07.md]
- **Config:** Hermes provider `custom:turbofit`; `providers.turbofit.api: http://127.0.0.1:11613/v1`; `model.default: ornith-1-5-35a3b-mlx` ^[raw/inbox/2026-09-07.md]
- **Context supported:** 131K claimed from server logs; throughput at that window drops sharply under prompt load ^[raw/inbox/2026-09-07.md]
- **Q3 preference note:** Chris wants GGUF vs MLX compared for new candidates and prefers the Q3 quant when page notes place it near base model quality; this page records the MLX run only ^[raw/inbox/2026-09-06.md].
- **Final configuration locked:** 2026-09-07 — Ornith MLX 4-bit configured as main provider at 131K context ^[raw/inbox/2026-09-07.md].

## Measured throughput

|| Test | Measured value |
||---|---|
|| Warmup | ~68s first run; much faster on restarts |
|| Short prompt | 15.6 tok/s at ~517 tokens in / 100 out |
|| 5K prompt | 5.7 tok/s at ~3519 tokens in / 100 out |
|| 131K-loaded server | short-context benchmark also reported at ~28-29 tok/s under lighter conditions |
|| After restart verification | 29 tok/s short prompt, 226 tok/s 5K prompt |

## Benchmark Results (vs competitors)

|| Benchmark | Ornith 1.5 | Ornith 1.0 | Qwen3.6 35B | Gemma 4 31B | Muse Glimmer 30B | Qwen3.5 397B |
||-----------|------------|------------|-------------|-------------|------------------|--------------|
|| **Terminal-Bench (Terminus-2)** | **67.8** | 64.2 | 52.5 | 42.1 | 51.7 | 53.5 |
|| **Terminal-Bench (Claude Code)** | **68.5** | 62.8 | 49.2 | - | - | 48.6 |
|| **SWE-bench Verified** | **79.0** | 75.6 | 73.4 | 52.0 | - | 76.4 |
|| **SWE-bench Pro** | **59.6** | 50.4 | 49.5 | 35.7 | 51.2 | 51.6 |
|| **SWE-bench Multilingual** | **71.4** | 69.3 | 67.2 | 51.7 | - | 69.3 |

## Why It Feels Smarter Than Free Models

1. **Agentic coding**: Outperforms 35B+ models on coding tasks by wide margins
2. **Continuous self-improvement**: Uses reinforcement learning to optimize task generation and solution rollouts
3. **Efficient MoE**: Gets 35B-level reasoning with 3B active parameters = faster, smarter than dense models

## Behavioral notes

Chris repeatedly asked to ignore Bonsai, Maple Colibri, and music generation noise and focus on getting Ornith up as the main provider. Three near-duplicate raw messages on 2026-09-07 at 13:18/13:20/13:30 show his exact framing: "It just needs to be configured into turbofit so I can continue with Ornith. Don't worry about bonsai."

^[raw/inbox/2026-09-07.md]

## Decision trail

Hermes-side `custom:turbofit` was retargeted to `http://127.0.0.1:11613/v1`, but Hermes timeouts occurred until restart. Chris switched his active provider to `ornith-1-5-35a3b-mlx via provider turbofit` at 14:25, and session metadata confirms the provider change; however, provider `timeout` errors (`code: timeout`, `provider: turbofit`, `model: ornith-1-5-35a3b-mlx`, `error: Connection error.`) recurred at 2026-09-07T19:26:47.525Z ^[raw/inbox/2026-09-07.md]. A full Hermes restart remains needed to confirm the live route. Until that restart and a successful completion are observed, final promotion is contested ^[raw/inbox/2026-09-07.md].

Chris's final directive at 14:25: "It just needs to be configured into turbofit so I can continue with Ornith" ^[raw/inbox/2026-09-07.md].

^[raw/inbox/2026-09-07.md]

## Related pages

- [[turbo-fit-evidence-capture|TurboFit Evidence Capture]]
- [[mtplx-main-provider|MPLX Main Provider]]
- [[unleashed-backup|Unleashed Backup]]

### From entity: ornith-35b-dflash2

`jzinno/Ornith-1.5-35B-A3B-DFlash2` was inspected on HuggingFace and downloaded as a local draft artifact for speculative-decode experiments ^[raw/inbox/2026-09-07.md].

## Status

- Community uptake is small (~840 downloads at observation time)
- No usable MTPLX integration path: MTPLX uses native MLX MTP heads rather than llama.cpp draft models
- DFlash2 is a CUDA-only diffusion-based draft model for llama.cpp/vLLM/sglang, incompatible with MLX MTP

## Benchmark Evidence

The DFlash2 draft model is **not viable for this hardware configuration**. From the speed tests:

| Setup | Short | 131K |
|-------|-------|------|
| **Ornith MLX 4-bit** | **28.5 tok/s** | ~0.5 tok/s |
| Ornith + DFlash2 | N/A | Cannot test |

The DFlash2 draft path cannot be used with Ornith MLX because:
1. MTPLX cannot use DFlash2 (native MLX MTP heads vs CUDA diffusion draft)
2. llama.cpp DFlash2 integration failed with invalid argument errors (`--draft-ngl`, `--draft-ctx-size`, `--low-vram` not supported)

## Contested Recommendation

Hermes recommended pairing Ornith MLX 4-bit with Unleashed+DFlash2 for 131K coverage; that pairing is contested because:
- DFlash2 cannot be integrated with Ornith MLX (different runtimes)
- Ornith MLX alone drops to ~0.5 tok/s at 131K due to KV cache dominance

## Final Recommendation

**Ornith MLX 4-bit solely as main provider** for short/medium context (28.5 tok/s at 500 tokens). For long context, use **Unleashed + DFlash2** at 131K (~5 tok/s) or **Nail Q4_K_XL** at 32K (23.4 tok/s).

## Related

- [[topics/turbofit/wiki/entities/ornith-35b-mlx.md|Ornith 35B MLX]]
- [[topics/turbofit/wiki/concepts/dflash2-mplx-incompatibility|MPLX DFlash2 Incompatibility]]
- [[topics/turbofit/wiki/entities/dflash2-draft.md|DFlash2 Draft]]
- [[topics/turbofit/wiki/queries/apple-silicon-runtime-benchmark|Apple Silicon Runtime Benchmark]]

### From entity: ornith-35b-mlx

`Ornith-1.5-35B-A3B` MLX 4-bit is a MoE local candidate downloaded to `~/Models/storage/ornith/` with a companion DFlash2 draft package at `~/Models/storage/ornith-dflash2/` ^[raw/inbox/2026-09-07.md].

This page is a legacy entity record; see [[topics/turbofit/wiki/entities/ornith-1-5-35b-a3b-mlx-4-bit.md|Ornith 1.5 35B-A3B MLX 4-bit]] for measured throughput and config state after 2026-09-07 final lock-in ^[raw/inbox/2026-09-07.md].

## Tested speeds on M1 MacBook 32GB

|| Context | Tok/s |
||---------|-------|
|| Short (~500 tokens) | **28.5** |
|| 5K tokens | 5.7 |
|| 20K tokens | 1.5 |
|| 40K tokens | 0.7 |
|| 60K tokens | 0.4 |
|| 131K | ~0.5 |

These numbers were gathered in-session against downloaded artifacts ^[raw/inbox/2026-09-07.md].

## Model Facts

- **Architecture**: MoE 35B (3B active params per token)
- **Weight**: 18 GB via MLX 4-bit
- **Inference**: MLX via `mlx_lm` server

## Role

- Fastest observed short-context path on this box (28.5 tok/s)
- KV cache dominates throughput above ~20K context
- 131K path is unstable (~0.5 tok/s)

## Contested Evidence

Hermes summary claimed Ornith wins at 131K, but speed tests from 09:19 show:
- Ornith MLX 4-bit: 28.5 tok/s short, ~0.5 tok/s at 131K
- Nail Q4_K_XL: 23.4 tok/s short, 4.7 tok/s at 5K
- Tiel-Coder Q4_K_XL: 23.1 tok/s short, 4.2 tok/s at 5K
- Dirk Q3_K_XL: 6.0 tok/s at 32K, OOM above

**Conclusion**: Ornith is fastest at short context but drops sharply at long context. The "winner" designation depends on use case.

- **Current routed state**

Hermes `custom:turbofit` was retargeted to Ornith MLX on `http://127.0.0.1:11613/v1`, and session metadata confirms the provider changed to `ornith-1-5-35a3b-mlx via provider turbofit` at 14:25, but persistent `Connection error` timeouts recurred at 2026-09-07T19:26:47.525Z ^[raw/inbox/2026-09-07.md]. Until a verified post-restart Hermes completion is captured, the routed state remains contested.

- **Practical recommendation**

Use Ornith MLX 4-bit for short/medium-context daily work. Use Unleashed+DFlash2 for long-context fallback where stable throughput matters more than peak speed.

## Related

- [[topics/turbofit/wiki/entities/ornith-35b-dflash2.md|Ornith 35B DFlash2]]
- [[topics/turbofit/wiki/decisions/aux-model-selection.md|Aux Model Selection]]
- [[topics/turbofit/wiki/queries/apple-silicon-runtime-benchmark|Apple Silicon Runtime Benchmark]]

### From entity: ornith-35b

`Ornith-1.5-35B-A3B` is a MoE model downloaded to `~/Models/storage/ornith/` as MLX 4-bit on this 32 GB box. A DFlash2 draft package was also downloaded to `~/Models/storage/ornith-dflash2/` ^[raw/inbox/2026-09-07.md].

## Tested speeds on M1 MacBook 32GB

| Context | Tok/s |
|---------|-------|
| Short (~500 tokens) | 28.5 |
| 5K tokens | 4.3 |
| 20K tokens | 1.5 |
| 40K tokens | 0.7 |
| 60K tokens | 0.4 |
| 131K | ~0.5 |

These numbers were gathered in-session against the downloaded artifacts; they are not stable live-route evidence from Hermes ^[raw/inbox/2026-09-07.md].

## DFlash2 candidate

A DFlash2 draft build exists as `jzinno/Ornith-1.5-35B-A3B-DFlash2` on HuggingFace, but community uptake is small (~840 downloads at time of observation). No MTPLX integration path exists because MTPLX uses native MLX MTP heads rather than llama.cpp draft models ^[raw/inbox/2026-09-07.md].

## Contested Evidence

> "The hard truth: On M1 MacBook 32GB with a 27B model at 131K context, **~5-6 tok/s is the ceiling.** You want 10+ tok/s. That's not happening with this hardware — it's like asking a Honda Civic to go 200mph." ^[raw/inbox/2026-09-07.md].

Hermes proposed Ornith MLX 4-bit as daily-driver main provider for short/medium workloads and Unleashed+DFlash2 as long-context fallback. That pairing is contested because it has not been verified as a stable live Hermes route without reload failures or memory overcommit ^[raw/inbox/2026-09-07.md].

## Conclusion

**Recommendation:** Ornith MLX 4-bit as main provider for daily use (short/medium context, 28.5 tok/s) with 65K context as the stable ceiling. Use Unleashed+DFlash2 for 131K long-context needs. 10+ tok/s at 131K is physically unachievable on this 32GB hardware.

## Note

Ornith is fast at short context but loses throughput sharply as KV cache grows. On this hardware, 131K remains the throughput ceiling regardless of runtime.

## Related

- [[topics/turbofit/wiki/decisions/aux-model-selection|Aux Model Selection]]
- [[topics/turbofit/wiki/decisions/unleashed-backup|Unleashed Backup]]
- [[topics/turbofit/wiki/queries/apple-silicon-runtime-benchmark|Apple Silicon Runtime Benchmark]]
- [[topics/turbofit/wiki/entities/dflash2-draft|DFlash2 Draft]]
- [[topics/turbofit/wiki/entities/ornith-35b-mlx.md|Ornith 35B MLX]]
- [[topics/turbofit/wiki/entities/ornith-35b-dflash2.md|Ornith 35B DFlash2]]

### From entity: ornith-config-routing-failure

After Hermes `custom:turbofit` was retargeted to `http://127.0.0.1:11613/v1` and `model.default` was set to `ornith-1-5-35a3b-mlx`, Hermes emitted repeated connection timeouts to the turbofit provider ^[raw/inbox/2026-09-07.md].

## Observed evidence

- Session metadata changed to Ornith successfully at 14:25 with `ornith-1-5-35a3b-mlx via provider turbofit` ^[raw/inbox/2026-09-07.md].
- Provider errors continued after config change:
  - `time: 2026-09-07T19:26:47.525Z` ^[raw/inbox/2026-09-07.md].
  - `layer: provider`
  - `code: timeout`
  - `provider: turbofit`
  - `model: ornith-1-5-35a3b-mlx`
  - `error: Connection error.`

## Status

The timeout persisted after the 14:25 config repoint. A Hermes session or gateway restart resolves the stale connection state. Until a post-restart verification completes, this is contested.

## Related

- [[ornith-config-routing|Ornith Config Routing]]
- [[ornith-1-5-35b-a3b-mlx-4-bit|Ornith 1.5 35B-A3B MLX 4-bit]]
