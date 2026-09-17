---
title: Qwen 3.8 27B Base
created: 2026-09-16
updated: 2026-09-16
type: model
tags: [model, omarchy, macbook]
sources: []
confidence: medium
---

# Qwen 3.8 27B (Base)

> Base Qwen 3.8 27B — foundation for derivatives. Dense, multilingual, strong coding.

## Research
- Dense 27B parameter model from Alibaba/Qwen team
- Strong performance on MMLU, HumanEval, GSM8K
- Multilingual: 29+ languages supported natively
- Base for many community fine-tunes (Unleashed, abliterated)

## Runtimes

### NVIDIA GPU (CUDA) — Omarchy RTX 3090×2
llama.cpp CUDA, -ngl 99

### AMD GPU (ROCm)
llama.cpp with ROCm (if supported)

### Apple Silicon (Metal) — MacBook M1 Pro
MLX native, llama.cpp fallback

### CPU
llama.cpp AMX

## Systems
- omarchy
- macbook

## Notes
Size: 20G total
Cross-references: [[topics-wiki/turbofit/index|wiki index]]
