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
- [[topics/turbofit/wiki/index|Wiki Index]]
