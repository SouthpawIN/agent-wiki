---
title: Turbohaul Manager
created: 2026-10-28
updated: 2026-10-28
type: entity
tags: [repo, turbofit, ecosystem]
sources: [raw/sources/2026-10-28-github-consolidation.md]
confidence: high
---

# Turbohaul Manager

> Ollama-shape inference manager on Tom's TurboQuant llama.cpp fork — the manager line TurboFit's runtime work descends from.

| | |
| --- | --- |
| **Repo** | [turbohaul-manager](https://github.com/SouthpawIN/turbohaul-manager) |
| **Status** | legacy line — separate repo, not shipped in the TurboFit package |

## What it does

- Accepts OpenAI / Ollama-shape `/v1/chat/completions` requests.
- Single-slot serial sidecar (one `llama-server` child holds the model).
- FIFO queue + grace window + **IDLE_HOT** 5-minute warm-hold; model swap tears down and respawns.
- **ACTIVE_MATCH cascade** for same-thread follow-ups (warm-process reuse).
- Safety guardrails: refuses to spawn when VRAM / RAM / CPU / IO-wait would put the host at risk.
- NVIDIA RTX incl. Blackwell; Docker + bare-metal launch paths.

## Why it matters here

The TurboQuant flag doctrine (`turbo2/3/4` KV quant), hot-hold/swap semantics, and the launch-string generator ([turbohaul-llmfit](turbohaul-llmfit.md)) all originate in this line. Read it when reasoning about TurboFit's own engine/flags matrix ([runtime-backends](../../references/runtime-backends.md), [scaling-ladder](../../references/scaling-ladder.md)).

## Related
- [[turbofit]] · [[ecosystem]] · [[fit-ladder]]
