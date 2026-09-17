---
title: evolutionary-model-merging
updated: 2026-08-27
type: topic
repo: https://github.com/SouthpawIN/evolutionary-model-merging
status: dormant
tags: [repo]
---

# evolutionary-model-merging

> Training-free weight-space recombination of LLMs using evolutionary algorithms. Implements the Darwin Family paper (arXiv:2605.14386) methodology.

**[Open on GitHub](https://github.com/SouthpawIN/evolutionary-model-merging)** · DORMANT (since 2026-07-08) · last push 2026-07-08

## Facts
- **Language:** Python
- **Stars / forks:** 19 / 3
- **License:** MIT
- **Fork of:** original work
- **Created:** 2026-06-02 · **Last push:** 2026-07-08
- **Open issues:** 0
- **Status:** DORMANT (since 2026-07-08)

## From the README

# Evolutionary Model Merging (Darwin Family)

**Training-free weight-space recombination of LLMs using evolutionary
algorithms.** Faithful implementation of the
[Darwin Family paper](https://arxiv.org/abs/2605.14386) (Kim et al., 2026) —
MRI-Trust Fusion, Architecture Mapper, and CMA-ES genome search.

The paper's flagship result: **Darwin-27B-Opus at 86.9% on GPQA Diamond**,
ranking #6 out of 1,252 evaluated models, beating its fully-trained
foundation model with **zero gradient updates**.

## What is this?

When you have two (or more) pretrained LLMs, can you recombine their
weights — *without any training* — to get a new model that's **better
than either parent**? The Darwin Family paper says yes, and shows a
27B child hitting top-10 globally by recombining frozen parents.

The mechanism is a **genetic algorithm over a 14-dimensional merge
genome**, with CMA-ES as the optimizer and MRI-Trust Fusion as the
per-tensor mixing rule.

## The paper in one screen

### The 14-dimensional genome
```
g = (γ, α_attn, α_ffn, α_emb, ρA, ρB, r0, r1, r2, r3, r4, r5, τ, λ)
```
- **Core (6)**: global ratio + 3 per-component ratios + 2 parent densities
- **Block (6)**: r0..r5 — 6 independent layer-block merge ratios
- **Hyper (2)**: τ (MRI-Trust), λ (regularization)

Different genome values → different child. The genome is what evolves.

### MRI-Trust Fusion (per-tensor)
```
r_final(T) = τ · r_MRI(T) + (1 - τ) · r_genome(T)
```
where
```
r_MRI(T) = MRI_B(T) / (MRI_A(T) + MRI_B(T))
MRI(T)   = α · Static(T) + (1 - α) · Probe(T),  α = 0.5
```
- **Static**: normalized entropy + variance + capped ℓ2-norm (no
  calibration data needed)
- **Probe**: cosine distance between reasoning-conditioned and generic
  activations (requires small calibration set)
- **τ**: trust parameter, paper converges to 0.35-0.55 empirically

### The merge kernel
```
θM(T) = (1 - r_final(T)) · θA(T) + r_final(T) · θB(T)
```
A pure convex combination. No extra scaling, no random projection.

### Architecture Mapper (cross-architecture)
```
Comp(i, j) = 0.5 · Type(i,j) + 0.3 · Dim(i,j) + 0.2 · Param(i,j)
```
Tensors below the compatibility threshold are **skipped** (parent A
kept). The paper demonstrated Transformer + Mamba cross-architecture
merges.

### CMA-ES evolution loop
1. Sample N candidate genomes from multivariate Gaussian
2. Build N children (one full merge per candidate)
3. Score each on a real benchmark → fitness
4. Update the Gaussian toward higher-fitness candidates
5. Repeat 20-50 generations

Population: 20-50. After evolution, keep the best-genome child.


*…truncated — full README at repo link*


## Archived
Archived 2026-09-02 — absorbed into [[topics-wiki/evolutionary/README|evolutionary]] by merge-topics.py v1.1.0. Nothing here was deleted or rewritten.
