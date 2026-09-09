# Injections

## [READ]

== absorbed from senter idea-wiki (2026-08-28) ==
---
title: multimodal-expansion
created: 2026-07-12
updated: 2026-07-12
type: entity
tags: [entity, idea-capture, provenance]
sources: ["raw/github/multimodal-expansion-75c500c39d.md"]
confidence: medium
---

# multimodal-expansion

## Current context

Add audio, speech, or vision modalities to an existing LLM. Three approaches — LLaVA-style adapter, REAP + expert replacement, EvoMoE-style specialization — with training pipelines and GPU feasibility. # Multimodal Expansion > **Add audio, speech, or vision to an LLM that doesn't have them.** Three concrete approaches, training pipelines, GPU feasibility, and the architectural pitfalls that derail cross-family merges. This is the practical playbook for **adding a new modality to an existing language model** — whether you're bolting Whisper onto Qwen, replacing MoE experts via REAP, or letting an existing MoE organically specialize. The hard truth up front: **most cross-family merges don't work.** Qwen3 with DeltaNet can't weight-merge with Qwen2.5 transformers. ACE-Step's UMT5 + DiT can't be folded into a Qwen LLM. Knowing *what you can't merge* is half the value of this skill. --- ## Quick decision tree --- ## The three approaches | Approach | Effort | Compute | Native? | When to use | |---|---|---|---|---| | **A. LLaVA-style adapter** | Days | Dual 3090 OK with LoRA | Bolt-on | First-time modality add, limited GPU | | **B. REAP + expert replacement** | Weeks | Cloud (A100/H100) | Native (MoE) | Have an MoE LLM, want zero-shot modality integration | | **C. EvoMoE-style specialization** | Weeks | Dual 3090+ | Native (organic) | Have an MoE LLM, want it to learn modalities naturally | ### 🅰️ Approach A: Adapter-Based (LLaVA Pattern) — MOST FEASIBLE Add modality-specific encoders + projectors. The LLM stays mostly frozen. **Architecture:** **Training pipeline (3 stages):** 1. **Encoder Alignment** — Freeze LLM. Train encoder + projector on paired data (e.g. ASR: speech→text). ~10K hours. 2. **Multimodal Fine-Tune** — LoRA on LLM. Diverse audio tasks: ASR, captioning, QA, music, sound events. ~1M examples. 3. **Speech Output** (optional) — Train Talker on Thinker hidden states, OR use external TTS (ElevenLabs, Edge TTS). **Audio encoder options:** | Encoder | Strengths | License | Notes | |---|---|---|---| | Whisper-large-v3 | Easy, well-supported, 99 langs | MIT | Default choice | | Qwen-Audio encoder | Better Chinese/multilingual | Apache 2.0 | Pair with Qwen LLMs | | AuT (Qwen3-Omni) | Best in class | Apache 2.0 (model) | 20M hr training data NOT public | | Wav2Vec2-BERT | SSL pretraining | Apache 2.0 | Good for fine-tuning | **Tools:** -…

## Version policy

The latest available update marker is canonical: `https://github.com/SouthpawIN/multimodal-expansion` (`2026-07-08T20:37:39Z`). Earlier captures remain linked in the raw source inventory.

## Related concepts

- [[concepts/automation-event-systems|Automation Event Systems]]
- [[concepts/creative-music|Creative Music]]
- [[concepts/model-merging-training|Model Merging Training]]
- [[concepts/multimodal-voice|Multimodal Voice]]
