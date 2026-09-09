# Injections

## [READ]

== absorbed from senter idea-wiki (2026-08-28) ==
---
title: omnistep-fusion
created: 2026-07-12
updated: 2026-07-12
type: entity
tags: [entity, idea-capture, provenance]
sources: ["raw/github/omnistep-fusion-fc3e89c8f0.md"]
confidence: medium
---

# omnistep-fusion

## Current context

Fuse Cosmos3-Nano + AceStep into one omni-modal model: see, hear, generate video, generate music, think. # OmniStep Fusion **One model. All modalities. See, hear, generate video, generate music, think.** Fuses [Cosmos3-Nano](https://huggingface.co/nvidia/Cosmos3-Nano) (vision + video + text) with [AceStep](https://huggingface.co/ACE-Step/acestep-5Hz-lm-4B) (music + audio) into a single unified model. ## What Is This? OmniStep Fusion creates a truly omni-modal model by: 1. **Merging the backbones** — Both are Qwen3-family with identical transformer internals (GQA 32Q/8KV, head_dim=128, 36 layers). Darwin merge blends the weights. 2. **Bridging dimensions** — Cosmos uses hidden=4096, AceStep uses 2560. Projection layers map between them. 3. **Unifying vocabulary** — 151K Cosmos tokens + 65K music tokens = 217K merged vocabulary. 4. **Attaching all encoders/decoders** — Vision (Cosmos ViT), Audio (AceStep encoder), Video (Cosmos diffusion), Music (AceStep DiT). ## Architecture ## Status - [x] Architecture design - [x] Projection layer code - [x] Vocabulary merger code - [x] Backbone fusion engine - [x] Unified model class - [x] Training recipe - [ ] Train projection layers (needs parallel embeddings data) - [ ] Fuse actual model weights (needs Cosmos + AceStep models) - [ ] Multimodal fine-tuning - [ ] Benchmarking - [ ] GGUF quantization ## Quick Start ## File Structure ## Related Projects - [Evolutionary Training](https://github.com/SouthpawIN/evolutionary-training) — Darwin merge engine - [OmniStep 12A3B](https://huggingface.co/sovthpaw/omnistep-12a3b) — Current non-fused version - [Southpaw's Turbohaul](https://github.com/SouthpawIN/southpaw-turbohaul) — Model server ## License Apache 2.0 (following parent model licenses) --- ## Related: the OmniSenter architecture OmniStep-Fusion is one of the pieces of the broader OmniSenter system. The full picture: - **OmniSenter** (main project): [evolutionary-training](https://github.com/SouthpawIN/evolutionary-training) - **Design post**: [OmniSenter: The Self-Evolving Multimodal Auxiliary for Hermes](https://github.com/SouthpawIN/evolutionary-training/blob/master/blog/omnisenter-self-evolving.md) - **Architecture wiki**: `~/wiki/concepts/omnisenter-architecture.md` - **Cosmos × ACE-Step × Nemotron ASR** master plan: `~/wiki/concepts/omnimodal-fusion-architecture.md` - **Sparse upcycle** (Stage 3 of the pipeline):…

## Version policy

The latest available update marker is canonical: `https://github.com/SouthpawIN/omnistep-fusion` (`2026-07-09T00:02:20Z`). Earlier captures remain linked in the raw source inventory.

## Related concepts

- [[concepts/creative-music|Creative Music]]
- [[concepts/model-merging-training|Model Merging Training]]
- [[concepts/multimodal-voice|Multimodal Voice]]
- [[concepts/personal-vision|Personal Vision]]
