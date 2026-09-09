# Injections

## [READ]

== absorbed from senter idea-wiki (2026-08-28) ==
---
title: turbohaul-manager
created: 2026-07-12
updated: 2026-07-12
type: entity
tags: [entity, idea-capture, provenance]
sources: ["raw/github/turbohaul-manager-aab2afdd20.md"]
confidence: medium
---

# turbohaul-manager

## Current context

Ollama-shape inference manager using Tom's TurboQuant llama.cpp. FIFO queue + grace + IDLE_HOT hot-hold + model swap on Blackwell. # Turbohaul-Manager Ollama-shape inference manager using [Tom's TurboQuant](https://github.com/TheTom/llama-cpp-turboquant) fork of llama.cpp. FIFO queue + grace + IDLE_HOT hot-hold + model swap on Nvidia RTX GPU's including Blackwell. ## What it does - Accepts OpenAI / Ollama-shape `/v1/chat/completions` requests - Single-slot serial sidecar (one llama-server child holds the model) - ACTIVE_MATCH cascade for same-thread follow-ups within a grace window (warm-process reuse) - IDLE_HOT 5-minute warm-hold after grace expires: same-model follow-ups inherit the warm process; different-model swap tears down + spawns new - Safety guardrails: refuses spawn when VRAM / RAM / CPU / IO-wait would put the host at risk ## Quick start ## API Compatible with Ollama-shape clients: - `GET /api/tags` -- list models - `GET /api/show?name=<tag>` -- model detail - `POST /v1/chat/completions` -- OpenAI-shape inference - `POST /api/chat` -- Ollama-shape inference - `PUT /api/manifests/{tag}` -- register a new model (requires GGUF blob in store) - `POST /api/pull-hf` -- pull a GGUF from HuggingFace - `POST /api/pull-url` -- pull a GGUF from arbitrary HTTPS URL (SSRF-guarded) - `POST /api/import` -- import a local GGUF file - `GET /status` -- live queue + active + idle_hot snapshot ## Setting up AI Agents Pointing an AI agent (Hermes, langchain, llama-index, LiteLLM, raw OpenAI SDK, Ollama clients, etc.) at Turbohaul is two lines: Turbohaul ships with sane defaults for multi-tool-call agent loops — `idle_hot_load_seconds=600`, `grace_seconds=30`, streaming SSE pass-through, tool-call field forwarding, and ACTIVE_MATCH warm-slot reuse for same-`thread_id` follow-ups (sub-second after the first turn). **Full guide:** [docs/AI_AGENT_SETUP.md](docs/AI_AGENT_SETUP.md) — per-agent config recipes (Hermes / OpenAI SDK / langchain / llama-index / LiteLLM / Ollama / curl), multi-tool-call workflow notes, production setup, validation smoke tests, and a troubleshooting table. ## License MIT (see LICENSE). All third-party deps audited MIT-compatible (see THIRD_PARTY_NOTICES.md). ## Contributors See [CONTRIBUTORS.md](CONTRIBUTORS.md). MrTrench (founder) shipped v0.2.1.

## Version policy

The latest available update marker is canonical: `https://github.com/SouthpawIN/turbohaul-manager` (`2026-07-08T20:37:24Z`). Earlier captures remain linked in the raw source inventory.

## Related concepts

- [[concepts/agent-fleet|Agent Fleet]]
- [[concepts/local-inference|Local Inference]]
- [[concepts/model-merging-training|Model Merging Training]]
- [[concepts/product-experiments|Product Experiments]]
