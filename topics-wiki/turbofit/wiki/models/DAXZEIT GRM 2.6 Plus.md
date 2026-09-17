---
title: DAXZEIT GRM 2.6 Plus
created: 2026-09-16
updated: 2026-09-16
type: model
tags: [model, omarchy]
sources: []
confidence: medium
---

# DAXZEIT GRM 2.6 Plus MTP

> General Reasoning Model with MTP — predicts N future tokens for 2x speed boost.

## Research
- MTP: N tokens per forward pass — up to 2x speed boost
- Reasoning variant fine-tuned on chain-of-thought datasets
- GRM-2.6-Plus base is Qwen3.8-27B with MTP head
- Supports draft-token speculative decoding in llama.cpp

## Runtimes

### NVIDIA GPU (CUDA) — Omarchy RTX 3090×2
llama.cpp with --spec-type draft-mtp, CUDA

### AMD GPU (ROCm)
llama.cpp with ROCm (if MTP supported)

### Apple Silicon (Metal) — MacBook M1 Pro
llama.cpp with Metal (if MTP supported), else standard

### CPU
llama.cpp with AMX, MTP may fall back to standard

## Systems
- omarchy

## Notes
Size: 123G total
Cross-references: [[topics-wiki/turbofit/index|wiki index]]
