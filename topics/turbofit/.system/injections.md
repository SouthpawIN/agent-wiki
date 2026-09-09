# Injections

## [READ]

== absorbed from senter idea-wiki (2026-08-28) ==
---
title: turbofit
created: 2026-07-12
updated: 2026-07-12
type: entity
tags: [entity, idea-capture, provenance]
sources: ["raw/github/turbofit-3b80602d62.md"]
confidence: medium
---

# turbofit

## Current context

Hardware-fit checker + multi-launcher installer (llama.cpp / Ollama / vllm / SGlang) for Hermes-Agent. Uses llmfit to verify model fit, generates accurate backend-specific launch strings, launches detached, wires into Hermes as main or auxiliary. Bundles 5-model curated NVIDIA NIM free-tier API list. Enforces 64K context floor. v1.0.0. # turbofit — opinionated unified LLM backend for Hermes Agent Turbofit manages the entire lifecycle of LLMs with Hermes Agent: detecting your GPU, picking the best model, launching local servers, wiring API providers, managing daemons (systemd on Linux, PID files on Windows), scaling under VRAM pressure, tracking real-time pricing, integrating Mixture of Agents, and auto-updating a model database every day. **End-user UX:** `serve auto main` → done. Works on Linux and Windows. ## What's New (v1.5) - **🔌 First-class Hermes Agent provider** — no more `custom:llama-main` hacks. Turbofit is now a native provider: `hermes config set model.provider custom:turbofit`. The gateway at :8091 routes to Darwin, Carnice, or API fallback automatically. - **🌐 Remote access via Tailscale** — use turbofit from your phone or any device. `https://senter.tail6ff78b.ts.net/main/v1` serves the same models wirelessly. - **🖥️ Dynamic gateway routing** — `/main/v1` for chat, `/aux/v1` for vision/compression, `/status` for live model info. No manual model switching. - **📊 Live benchmark leaderboard** — `serve recommend` now pulls real lm-eval benchmarks (MMLU, GSM8K, GPQA, HumanEval) from GitHub. Rankings are never hardcoded. - **🔧 Scaling watcher v2** — gradual 5-level contraction based on absolute per-GPU free VRAM, +4GB expansion hysteresis, multi-profile management. Handles OOM from turbofit's own daemons, not just external apps. Previously (v1.0–v1.1): native Windows support, MoA integration with 5 presets, model database auto-updates, NVIDIA NIM free tier, daemon management. --- ## Install After install, `source ~/.bashrc` (or open a new shell) to get the `serve` and `name` commands. --- ## Use as a Hermes Agent Provider Turbofit is a **native Hermes Agent provider** — no separate API key needed. The gateway serves OpenAI-compatible endpoints at `http://127.0.0.1:8091/main/v1`: The gateway dynamically routes to whatever model the scaling watcher has active — Darwin (local), Carnice (local aux), or API fallback (Nous Portal, OpenAI, DeepSeek). No…

## Version policy

The latest available update marker is canonical: `https://github.com/SouthpawIN/turbofit` (`2026-07-12T21:25:51Z`). Earlier captures remain linked in the raw source inventory.

## Related concepts

- [[concepts/agent-fleet|Agent Fleet]]
- [[concepts/local-inference|Local Inference]]
- [[concepts/model-merging-training|Model Merging Training]]
- [[concepts/personal-vision|Personal Vision]]
