---
title: multimodal-expansion
updated: 2026-08-27
type: topic
repo: https://github.com/SouthpawIN/multimodal-expansion
status: dormant
tags: [repo]
---

# multimodal-expansion

> Add audio, speech, or vision modalities to an existing LLM. Three approaches — LLaVA-style adapter, REAP + expert replacement, EvoMoE-style specialization — with training pipelines and GPU feasibility.

**[Open on GitHub](https://github.com/SouthpawIN/multimodal-expansion)** · DORMANT (since 2026-07-08) · last push 2026-07-08

## Facts
- **Language:** Python
- **Stars / forks:** 4 / 0
- **License:** MIT
- **Fork of:** original work
- **Created:** 2026-06-03 · **Last push:** 2026-07-08
- **Open issues:** 0
- **Status:** DORMANT (since 2026-07-08)

## From the README

# Multimodal Expansion

> **Add audio, speech, or vision to an LLM that doesn't have them.** Three concrete approaches, training pipelines, GPU feasibility, and the architectural pitfalls that derail cross-family merges.

This is the practical playbook for **adding a new modality to an existing language model** — whether you're bolting Whisper onto Qwen, replacing MoE experts via REAP, or letting an existing MoE organically specialize.

The hard truth up front: **most cross-family merges don't work.** Qwen3 with DeltaNet can't weight-merge with Qwen2.5 transformers. ACE-Step's UMT5 + DiT can't be folded into a Qwen LLM. Knowing *what you can't merge* is half the value of this skill.

## Quick decision tree

```
Want to add audio/speech to an LLM?
├─ Text-only model, no vision? → Full LLaVA-style: add both vision + audio encoders
├─ Already has vision (like Qwen3.6 35B A3B)? → Just add audio encoder + projector
├─ Want speech OUTPUT too? → Add Talker module OR use external TTS (simpler)
├─ Want native MoE integration (not bolt-on)? → See approach B or C below
└─ Limited compute (dual 3090 class)? → Approach A with LoRA is the only viable path

Building a multi-modal hub with multiple specialist models?
├─ Same backbone family? → Merge shared transformer layers (Darwin MRI-Trust)
├─ Different architectures (T5 + DiT + Qwen)? → Keep specialists routed, merge only the common backbone
├─ "One base model for everything"? → Anchor on a dense 3B Omni (text + vision + audio native), route all generation to specialists
└─ Need self-evolving architecture? → Darwin (weight-space) + GEPA (parameter-space) optimization loop
```

## The three approaches

| Approach | Effort | Compute | Native? | When to use |
|---|---|---|---|---|
| **A. LLaVA-style adapter** | Days | Dual 3090 OK with LoRA | Bolt-on | First-time modality add, limited GPU |
| **B. REAP + expert replacement** | Weeks | Cloud (A100/H100) | Native (MoE) | Have an MoE LLM, want zero-shot modality integration |
| **C. EvoMoE-style specialization** | Weeks | Dual 3090+ | Native (organic) | Have an MoE LLM, want it to learn modalities naturally |

### 🅰️ Approach A: Adapter-Based (LLaVA Pattern) — MOST FEASIBLE

Add modality-specific encoders + projectors. The LLM stays mostly frozen.

**Architecture:**
```
[Audio] → [Audio Encoder] → [Projector/Adapter] → [LLM (frozen or LoRA)] → text
                                                                      → [Talker] → speech (optional)
```

**Training pipeline (3 stages):**


*…truncated — full README at repo link*


## Archived
Archived 2026-09-02 — absorbed into [[topics-wiki/omnisenter-models/README|omnisenter-models]] by merge-topics.py v1.1.0. Nothing here was deleted or rewritten.
