# Injections

## [READ]

== absorbed from senter idea-wiki (2026-08-28) ==
---
title: evolutionary-model-merging
created: 2026-07-12
updated: 2026-07-12
type: entity
tags: [entity, idea-capture, provenance]
sources: ["raw/github/evolutionary-model-merging-36cb227206.md"]
confidence: medium
---

# evolutionary-model-merging

## Current context

Training-free weight-space recombination of LLMs using evolutionary algorithms. Implements the Darwin Family paper (arXiv:2605.14386) methodology. # Evolutionary Model Merging (Darwin Family) **Training-free weight-space recombination of LLMs using evolutionary algorithms.** Faithful implementation of the [Darwin Family paper](https://arxiv.org/abs/2605.14386) (Kim et al., 2026) — MRI-Trust Fusion, Architecture Mapper, and CMA-ES genome search. The paper's flagship result: **Darwin-27B-Opus at 86.9% on GPQA Diamond**, ranking #6 out of 1,252 evaluated models, beating its fully-trained foundation model with **zero gradient updates**. --- ## What is this? When you have two (or more) pretrained LLMs, can you recombine their weights — *without any training* — to get a new model that's **better than either parent**? The Darwin Family paper says yes, and shows a 27B child hitting top-10 globally by recombining frozen parents. The mechanism is a **genetic algorithm over a 14-dimensional merge genome**, with CMA-ES as the optimizer and MRI-Trust Fusion as the per-tensor mixing rule. --- ## The paper in one screen ### The 14-dimensional genome - **Core (6)**: global ratio + 3 per-component ratios + 2 parent densities - **Block (6)**: r0..r5 — 6 independent layer-block merge ratios - **Hyper (2)**: τ (MRI-Trust), λ (regularization) Different genome values → different child. The genome is what evolves. ### MRI-Trust Fusion (per-tensor) where - **Static**: normalized entropy + variance + capped ℓ2-norm (no calibration data needed) - **Probe**: cosine distance between reasoning-conditioned and generic activations (requires small calibration set) - **τ**: trust parameter, paper converges to 0.35-0.55 empirically ### The merge kernel A pure convex combination. No extra scaling, no random projection. ### Architecture Mapper (cross-architecture) Tensors below the compatibility threshold are **skipped** (parent A kept). The paper demonstrated Transformer + Mamba cross-architecture merges. ### CMA-ES evolution loop 1. Sample N candidate genomes from multivariate Gaussian 2. Build N children (one full merge per candidate) 3. Score each on a real benchmark → fitness 4. Update the Gaussian toward higher-fitness candidates 5. Repeat 20-50 generations Population: 20-50. After evolution, keep the best-genome child. ### Recursive "Family" evolution Take the best child, merge it with…

## Version policy

The latest available update marker is canonical: `https://github.com/SouthpawIN/evolutionary-model-merging` (`2026-07-08T20:37:24Z`). Earlier captures remain linked in the raw source inventory.

## Related concepts

- [[concepts/model-merging-training|Model Merging Training]]
