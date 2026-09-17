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

## See Also

- [[concepts/benchmark-taxonomy|Benchmark Taxonomy]]
- [[topics/turbofit/wiki/index|Wiki Index]]
