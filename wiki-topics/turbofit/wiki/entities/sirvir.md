---
title: Sirvir
created: 2026-10-28
updated: 2026-10-28
type: entity
tags: [repo, turbofit, ecosystem]
sources: [raw/sources/2026-10-28-github-consolidation.md]
confidence: high
---

# Sirvir

> Turbofit customer service — installs, configures, troubleshoots, and turns support findings into tested upstream PRs.

| | |
| --- | --- |
| **Repo** | [sirvir](https://github.com/SouthpawIN/sirvir) |
| **Status** | active support surface (Turbofit package installs the TurboSouth profile) |

## What it is

Sirvir supports one product — [`SouthpawIN/turbofit`](https://github.com/SouthpawIN/turbofit) — and one execution boundary: local models served by Turbofit, loopback by default, optional private Tailnet routes. It **fails closed** when no local route is viable.

It does **not** select, configure, benchmark, budget, or fall back to hosted model APIs, and it does not bundle a second copy of Turbofit — the Turbofit plugin remains the sole implementation and source of truth.

Sirvir ships as a Hermes profile (`hermes profile install ...`), carrying its own `SOUL.md`, `AGENTS.md`, `config.yaml`, `distribution.yaml` and a `sirvir` skill.

## Where it lives in this vault

- Bot SOUL contract absorbed as [turbosovth-soul](../../references/turbosovth-soul.md) and [skill-contract](../../references/skill-contract.md) in `references/`.
- TurboSouth install path is documented in [install-paths](../../references/install-paths.md) and the hub [README](../../README.md).

## Related
- [[turbofit]] · [[ecosystem]] · [[fit-ladder]]
