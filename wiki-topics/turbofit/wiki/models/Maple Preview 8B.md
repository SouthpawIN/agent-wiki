---
title: Maple Preview 8B
created: 2026-09-16
updated: 2026-09-16
type: model
tags: [model, aux]
sources: []
---

# Maple Preview

> 8B model for aux/compression tasks, used in Hermes.

## Specifications

- **HuggingFace:** [deepgrove/maple-preview-GGUF](https://huggingface.co/deepgrove/maple-preview-GGUF)
- **Type:** Aux LLM
- **Architecture:** Custom (Maple)
- **Parameters:** 8B
- **Active params per token:** 8B
- **Context window:** Up to 131K
- **Quantization:** Q4_K_M
- **Size on disk:** 22G
- **Format:** GGUF

## System Availability

| System | Available | Path |
|--------|-----------|------|
| Omarchy | Yes | `/home/sovthpaw/Models/storage/gguf/deepgrove_maple-preview-GGUF/` |
| MacBook | No | `—` |

## Inference Performance

| Runtime | Platform | tok/s | Notes |
|---------|----------|-------|-------|
| llama.cpp CUDA | Omarchy RTX 3090×2 | 12.4 | MLX runtime on Mac (was replaced) |
| llama.cpp Metal | MacBook M1 Pro | — |  |
| MLX | MacBook M1 Pro | 12.4 | MLX runtime |

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

## See Also

- [[concepts/benchmark-taxonomy|Benchmark Taxonomy]]
- [[wiki-topics/turbofit/wiki/index|Wiki Index]]
