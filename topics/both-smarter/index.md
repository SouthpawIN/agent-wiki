---
title: both-smarter
created: 2026-09-17
updated: 2026-09-17
type: wiki
sources:
  - index.md
  - wiki/
  - raw/inbox/
  - .system/
---

# both-smarter

Last updated: 2026-09-17 | Total pages: 14

---

## INTEGRATIONS

This wiki is fed by:

- **Raw inbox:** `raw/inbox/` — daily cuts from Hermes sessions
- **Sessions:** `.system/sessions/` — full conversation transcripts
- **Wiki pages:** `wiki/` — structured knowledge base

---

## README

### Entities

- [Model Candidates on Hugging Face](wiki/model-candidates.md) — While hunting for a model to run on his unified-memory hardware, Chris gave voice-transcribed clues for a model on Hugging Face. The names are almost certainly
- [Ornith](wiki/ornith.md) — The model or runtime handle referenced in session-state output. In this raw item, Hermes broadcast: "Ornith is live and active on your session now." and claimed

### Concepts

- [Benchmark Maintenance Plan](wiki/benchmark-maintenance-plan.md) — Chris wants model research to go beyond a one-time lookup: a maintained, comparable set of **benchmarks** for each model in the widget, refreshed over time. ^[r
- [both-smarter](wiki/both-smarter.md) — Chris wants the model to be **both smarter and faster** than free models, not merely one or the other. This is a standing preference for his model selection and
- [Browser Tab Bar with +](wiki/browser-tab-bar.md) — Chris wants a browser tab bar in the Senter Wiki preview, with a small **+** symbol to open additional tabs so he can load Discord, Hugging Face, or any other s
- [Device-Specific Model Lanes](wiki/device-specific-model-lanes.md) — Chris wants models selected **per device type** — distinct "lanes" rather than one model for everything — because his hardware (a MacBook / laptop with integrat
- [Model Zoo Table with Hugging Face Repo Links](wiki/model-zoo-table-with-hf-links.md) — On 2026-09-16 Chris decided to **replace the Hugging Face models table with a "model zoo" table** that instead links each model to its Hugging Face repository.
- [Wiki Portal — Clickable Model Pages](wiki/wiki-portal-model-pages.md) — Chris wants the model table/widget to be a **portal**: instead of a blurb sitting as an item on the table, each model should be *clickable* and open its *own pa

### Decisions

- [Cyber-Tiel-Coder Confirmed Running through Hermes (2026-09-15)](wiki/cyber-tiel-coder-confirmed-2026-09-15.md) — On 2026-09-15 Hermes confirmed two models actually running through Hermes on Chris's machine, resolving the earlier model-search query. ^[raw/inbox/2026-09-15.m
- [Quantization Lane Rules for Unified Memory (2026-09-16)](wiki/quantization-lane-rules-2026-09-16.md) — On 2026-09-16 Chris laid out quantization guidance for the per-device model lanes — the unified-memory/CPU lane and the GPU (VRAM) lane. The CPU guidance is sta
- [Research Source Policy](wiki/research-source-policy.md) — **What:** Source model research directly from the model's Hugging Face page or official authoritative source. Do not regurgitate session-known info.
- [TurboFit Rule Tracking (2026-09-16)](wiki/turbo-fit-rule-tracking-2026-09-16.md) — On 2026-09-16 Chris said to start **keeping a running track of the rules he gives for TurboFit** (transcribed "turbo fitness") as he goes, and to implement them

### Queries

- [Benchmark Research Request](wiki/benchmark-research-request-2026-09-07.md) — Chris asked for research on the active model, including benchmarks and a gauge of intelligence.
- [Model Search — Unified Memory (2026-09-15)](wiki/model-search-unified-memory-2026-09-15.md) — On 2026-09-15 Chris asked for help finding a specific model on Hugging Face that runs well on Apple unified-memory devices (MacBook / laptop without dedicated G

---

## SKILLS

Topic skills stored in this wiki:

- **[device-model-lane-selection](skills/device-model-lane-selection/SKILL.md) — See wiki/skills/device-model-lane-selection.md
- **[turbo-fit-lane-rules](skills/turbo-fit-lane-rules/SKILL.md) — See wiki/skills/turbo-fit-lane-rules.md

---

## BOTS

Proposed bots:

- **[common-benchmark-audit](agents/common-benchmark-audit.md.proposed) — **Want me to look into what the most common benchmarks are for comparing these models, and gather the best concrete benchmarks for each?**
- **[killier-ragdoll-lookup](agents/killier-ragdoll-lookup.md.proposed) — **I see the 'Killier Ragdoll' from your Hugging Face clue was never verified against a real model card — want a bot that resolves it into a concrete m
- **[maple-lookup](agents/maple-lookup.md.proposed) — **I see you've dropped another near-indecipherable alias — "maple" for the lowest model tier — want a lookup bot like Killier Ragdoll's to resolve it 
- **[model-benchmark-refresh](agents/model-benchmark-refresh.md.proposed) — **I see you want those benchmarks kept fresh without you nudging — want a daily job that searches the web for each model's latest published benchmarks
- **[model-benchmarks](agents/model-benchmarks.md.proposed) — **I see you're after concrete benchmarks for each model — want a bot that defines the common cross-model benchmark set and researches the best publish
- **[model-lane-server](agents/model-lane-server.md.proposed) — **I see you're running models on your MacBook's unified memory and want one that actually fits and stays fast — want a bot that picks and serves the r


---

## LOOPS

Proposed loops:

- **[benchmark-refresh-watch](loops/benchmark-refresh-watch.md.proposed) — owner: looker · cadence: every 2 days · status: SUGGESTED
- **[model-lane-health](loops/model-lane-health.md.proposed) — owner: looker · cadence: every 6 hours · status: SUGGESTED
- **[unified-memory-model-watch](loops/unified-memory-model-watch.md.proposed) — owner: looker · cadence: daily at 9am · status: SUGGESTED
