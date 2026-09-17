# Injections

## [READ]

== absorbed from senter idea-wiki (2026-08-28) ==
---
title: southpaw-turbohaul
created: 2026-07-12
updated: 2026-07-12
type: entity
tags: [entity, idea-capture, provenance]
sources: ["raw/github/southpaw-turbohaul-ea25a47ca5.md"]
confidence: medium
---

# southpaw-turbohaul

## Current context

Curated model server for Nous Research community. Fork of turbohaul-manager with AtomicBot llama.cpp (TQ3/TQ4 + MTP + NextN) and Southpaw's hand-picked models. # Turbohaul-Manager Ollama-shape inference manager using [Tom's TurboQuant](https://github.com/TheTom/llama-cpp-turboquant) fork of llama.cpp. FIFO queue + grace + IDLE_HOT hot-hold + model swap on Nvidia RTX GPU's including Blackwell. ## What it does - Accepts OpenAI / Ollama-shape `/v1/chat/completions` requests - Single-slot serial sidecar (one llama-server child holds the model) - **MTP speculative decoding (draft-mtp) composes with TurboQuant turbo2/3/4 KV cache quantization** in a single llama.cpp binary — faster decode without sacrificing the quantized KV-cache memory footprint - ACTIVE_MATCH cascade for same-thread follow-ups within a grace window (warm-process reuse) - IDLE_HOT 5-minute warm-hold after grace expires: same-model follow-ups inherit the warm process; different-model swap tears down + spawns new - Multiplexed multi-agent serialization on one shared GPU (proven with three concurrent agents — see [docs/MULTI_AGENT_SHARING.md](docs/MULTI_AGENT_SHARING.md)) - Transparent tool-call recovery for jinja-templated GGUFs that emit calls as text JSON in `message.content` instead of the structured `tool_calls` field (notably Qwen3-family per upstream llama.cpp issues #20809 / #20837 / #20260) — see [docs/TOOL_CALL_HANDLING.md](docs/TOOL_CALL_HANDLING.md) - Safety guardrails: refuses spawn when VRAM / RAM / CPU / IO-wait would put the host at risk ## Quick start The `-v $(pwd)/state:/var/lib/turbohaul` mount is **required** for production deployment — without it, `state.sqlite`, `manifests/*.yaml`, and the `blobs/` store live inside the container layer and are destroyed by `docker rm` or container-layer corruption. See [docs/PERSISTENCE_CHECKLIST.md](docs/PERSISTENCE_CHECKLIST.md) for the full hardening checklist. ## API Compatible with Ollama-shape clients: - `GET /api/tags` -- list models - `GET /api/show?name=<tag>` -- model detail - `POST /v1/chat/completions` -- OpenAI-shape inference (supports `response_format` json_object + json_schema) - `POST /api/chat` -- Ollama-shape inference - `POST /v1/embeddings` -- llama-server embeddings passthrough - `GET /v1/logging` -- paginated audit events - `PUT /api/manifests/{tag}` -- register a new model (requires GGUF blob in store; ETag/If-Match…

## Version policy

The latest available update marker is canonical: `https://github.com/SouthpawIN/southpaw-turbohaul` (`2026-07-09T00:00:37Z`). Earlier captures remain linked in the raw source inventory.

## Related concepts

- [[concepts/agent-fleet|Agent Fleet]]
- [[concepts/automation-event-systems|Automation Event Systems]]
- [[concepts/community-ideas|Community Ideas]]
- [[concepts/local-inference|Local Inference]]
