---
title: turbohaul-llmfit
created: 2026-10-28
updated: 2026-10-28
type: entity
tags: [repo, turbofit, ecosystem]
sources: [raw/sources/2026-10-28-github-consolidation.md]
confidence: high
---

# turbohaul-llmfit

> Hermes skill that generates optimized llama-server launch strings and turbohaul manifests from llmfit hardware detection + TurboQuant flag doctrine.

| | |
| --- | --- |
| **Repo** | [turbohaul-llmfit](https://github.com/SouthpawIN/turbohaul-llmfit) |
| **Status** | skill repo (installable via `hermes skills install`) |

## What it is

A single-SKILL repo. Given a machine and a model, it emits a launch string + manifest using llmfit's hardware detection and the TurboQuant flag doctrine, instead of hand-tuning `--n-gpu-layers` / `--ctx-size` / KV quant flags.

## Why it matters here

This is the same problem TurboFit solves automatically: hardware → profile → flags. Keep it as the reference for *what a correct launch string looks like* per GPU class when validating TurboFit's generated commands ([runtime-backends](../../references/runtime-backends.md)).

## Related
- [[turbofit]] · [[ecosystem]] · [[fit-ladder]]
