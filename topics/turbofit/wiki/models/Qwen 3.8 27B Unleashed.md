---
title: Qwen 3.8 27B Unleashed
created: 2026-09-16
updated: 2026-09-16
type: model
tags: [model, general]
sources: []
---

# Qwen 3.8 27B Unleashed

> Best general-purpose Qwen variant. Fine-tuned to remove alignment, improve coding and creativity.

## Specifications

- **HuggingFace:** [outsourc-e/Qwen3.8-27B-Unleashed-GGUF](https://huggingface.co/outsourc-e/Qwen3.8-27B-Unleashed-GGUF)
- **Type:** General LLM
- **Architecture:** Dense
- **Parameters:** 27B
- **Active params per token:** 27B
- **Context window:** Up to 262K
- **Quantization:** Q3_K_XL
- **Size on disk:** 39G
- **Format:** GGUF

## System Availability

| System | Available | Path |
|--------|-----------|------|
| Omarchy | Yes | `/home/sovthpaw/Models/storage/gguf/Qwen3.8-27B-Unleashed/` |
| MacBook | Yes | `~/Models/storage/gguf/Qwen3.8-27B-Unleashed/` |

## Inference Performance

| Runtime | Platform | tok/s | Notes |
|---------|----------|-------|-------|
| llama.cpp CUDA | Omarchy RTX 3090×2 | 85 | MTP default, reasoning ON, 262K ctx |
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

### MTPLX Qwen 3.8 27B Optimized Speed

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


### Unleashed 27B

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


### Dirk GGUF Q3_K_XL

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


### Unleashed Backup

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


## See Also

- [[concepts/benchmark-taxonomy|Benchmark Taxonomy]]
- [[topics/turbofit/wiki/index|Wiki Index]]

### From entity: dirk-gguf

`Dirk-Qwen3.8-27B-UD-Q3_K_XL.gguf` (12.24 GB) is the requested Q3 Dirk artifact at `~/Models/storage/dirk-gguf/`, selected because Chris prefers Q3 when it is described as near base-model quality and because 13 GB fits the short-context candidate path better than heavier quants on this 32 GB box ^[raw/inbox/2026-09-07.md].

## Status

- Downloaded and verified on disk (12.24 GB, GGUF magic number confirmed)
- No benchmark evidence yet; 131K testing deferred because Dirk is a dense 27B model
- Chris explicitly wanted GGUF vs MLX compared, with preference for Q3 when near base quality

## Memory Impact

Dirk is a **dense 27B model** (not MoE), so:
- Model weights: 12.24 GB (Q3_K_XL)
- KV cache at 131K (q8): ~8 GB
- Total: ~20 GB + macOS/Hermes (~8 GB) = ~28 GB at 32K context

**Result**: OOM expected above 32K context window.

## Repo Correction

- Requested: `peculiar-ragdoll/Dirk-Qwen3.8-27B-GGUF-MTP` (returned 404)
- Actual: `peculiar-ragdoll/Dirk-Qwen3.8-27B-GGUF` (MTP is a model capability, not repo name)

## Runtimes Tested

| Runtime | Status | Notes |
|---------|--------|-------|
| llama.cpp stock | ❌ Incompatible | `unknown model architecture: 'maple'` (Maple only) |
| llama.cpp Qwen branch | ✅ | Works with Q3_K_XL |
| MLX | 🔄 Pending | Would need 131K streaming verification |

## Related

- [[topics/turbofit/wiki/entities/dirk-qwen38-27b.md|Dirk Qwen 3.8 27B GGUF]]
- [[topics/turbofit/wiki/decisions/candidate-quant-preference.md|Candidate Quant Preference]]
- [[topics/turbofit/wiki/queries/apple-silicon-runtime-benchmark|Apple Silicon Runtime Benchmark]]
- [[topics/turbofit/wiki/entities/unleashed-27b.md|Unleashed 27B]]

### From entity: dirk-qwen38-27b

Chris requested Dirk GGUF downloads for local comparison. The actual repo is `peculiar-ragdoll/Dirk-Qwen3.8-27B-GGUF` because MTP is a model capability, not a repo suffix ^[raw/inbox/2026-09-07.md].

## Requested artifacts

- `Dirk-Qwen3.8-27B-UD-Q3_K_XL.gguf` (~12.24 GB) downloaded to `~/Models/storage/dirk-gguf/` and verified on disk ^[raw/inbox/2026-09-07.md].
- `Dirk-Qwen3.8-27B-GGUF-MTP` repo lookup returned 404 before the correction ^[raw/inbox/2026-09-07.md].

## Status

- Q3_K_XL downloaded; no speed evidence yet. 131K benchmark was deferred because larger candidates OOM on this box before Dirk was exercised.
- Chris wants GGUF vs MLX compared for each candidate, with a preference for Q3 when near base quality ^[raw/inbox/2026-09-07.md].

## Related

- [[topics/turbofit/wiki/entities/dirk-gguf.md|Dirk GGUF Q3_K_XL]]
- [[topics/turbofit/wiki/decisions/candidate-quant-preference.md|Candidate Quant Preference]]
- [[topics/turbofit/wiki/queries/apple-silicon-runtime-benchmark|Apple Silicon Runtime Benchmark]]
- [[topics/turbofit/wiki/entities/unleashed-27b.md|Unleashed 27B]]

### From entity: unleashed-27b

Qwen3.8-27B-Unleashed in `UD-Q3_K_XL.gguf` with the Unleashed vision projector and DFlash2 draft. This is the main model in TurboFit ^[raw/inbox/2026-09-06.md].

## Served config

- **Runtime**: `llama.cpp` Metal build (`dflash2-llama.cpp-...`).
- **Port**: `11606`.
- **Context**: `131072`.
- **Draft**: `Qwen3.8-27B-DFlash2-Q4_K_M.gguf`, `--spec-type draft-dflash --spec-draft-n-max 7`.
- **KV cache**: `q4_0` k/v.
- **Batch**: `-b 512 -ub 256`.
- **Performance**: ~4.4–5.1 tok/s decode on this box ^[raw/inbox/2026-09-06.md].

## Role

- Main inference and vision provider.
- Stable under long context and large prompt ingest.
- Holds the DFlash2 draft path that earlier failed with wrong draft flags (`--draft-max`) and tensor mismatch before being aligned to the fork’s `--spec-draft-*` args ^[raw/inbox/2026-09-06.md].

## Related

- [[topics/turbofit/wiki/entities/turbofit.md|TurboFit]]
- [[topics/turbofit/wiki/entities/dflash2-draft.md|DFlash2 Draft]]
- [[topics/turbofit/wiki/decisions/main-model-selection.md|Main Model Selection]]

### From entity: unleashed-iq3-xxs-load-failure

`Qwen3.8-27B-Unleashed-UD-IQ3_XXS.gguf` failed to load in the `dflash2-llama.cpp` fork Metal server after a DFlash warning about missing `ctx_other` and then a tensor bounds failure ^[raw/inbox/2026-09-07.md].

## Evidence

- Warning: `dflash requires ctx_other to be set`
- Error: `tensor 'blk.2.attn_qkv.weight' data is not within the file bounds, model is corrupted or incomplete`
- Same load path repeated for `blk.2.ffn_down.weight`
- Server exited due to model loading error

## Note

This failure is specific to this quant artifact and this fork load path. It does not invalidate `Q3_K_XL`, which has served as the stable long-context backup in earlier evidence.

## Related

- [[topics/turbofit/wiki/entities/unleashed-27b|Unleashed 27B]]
- [[topics/turbofit/wiki/decisions/unleashed-backup|Unleashed Backup]]
- [[topics/turbofit/wiki/concepts/dflash2-compat-boundary|DFlash2 Compatibility Boundary]]
