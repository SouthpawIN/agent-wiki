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

## See Also

- [[concepts/benchmark-taxonomy|Benchmark Taxonomy]]
- [[topics/turbofit/wiki/index|Wiki Index]]
