---
title: SALT Core
created: 2026-10-28
updated: 2026-10-28
type: entity
tags: [repo, turbofit, ecosystem]
sources: [raw/sources/2026-10-28-github-consolidation.md]
confidence: high
---

# SALT Core

> Portable C99 state-assured latent-transition engine: deterministic arithmetic, authenticated model packages, live KV/state ownership, exportable state, CPU/Metal/CUDA/HIP backends.

| | |
| --- | --- |
| **Repo** | [SALT-core](https://github.com/SouthpawIN/SALT-core) |
| **Status** | dry-run public export — not yet a release |

## What it is

SALT (State Assured Latent-Transition engine) — paper: [Zenodo preprint 23111764](https://zenodo.org/records/23111764). The public contract centres on:

- deterministic arithmetic,
- authenticated model packages,
- live state / KV ownership,
- portable state export / import,
- subordinate CPU, Metal, CUDA and HIP physical backends.

> Preserved KV/state is more than a saved prompt: it carries the accumulated effects of an agent's automated activity and can support continued or branched execution. Retention permission is not unrestricted reuse permission.

## Relation to TurboFit

TurboFit carries a SALT integration surface — see [salt-core-integration](../../references/salt-core-integration.md) and the `salt-core-gate-report.json` artifact in the product repo.

## Related
- [[turbofit]] · [[ecosystem]] · [[fit-ladder]]
