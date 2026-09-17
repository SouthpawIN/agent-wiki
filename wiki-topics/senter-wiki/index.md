---
title: Senter Wiki
created: 2026-07-07
updated: 2026-09-17
type: wiki
links:
  github: https://github.com/SouthpawIN/Senter
  vault: ~/Documents/Projects/Projects
sources:
  - index.md
  - BRIEF.md
  - README.md
  - wiki/
---

# Senter Wiki

> Cursor for markdown. A live-acting second brain.

This vault is the **coordination layer** between Chris and the Hermes fleet. Every idea, decision, and artifact lives here as markdown. Edit any file — that's the steering wheel.

---

## INTEGRATIONS

This wiki is fed by:

- **GitHub:** [SouthpawIN/Senter](https://github.com/SouthpawIN/Senter) — repo, issues, PRs
- **Hermes state.db:** every chat message cut into `wiki-topics/<t>/raw/inbox/`
- **Sessions:** `wiki-topics/senter-wiki/.system/sessions/` — full conversation transcripts
- **Fleet daemons:** watcher, topic-agent, umbrella, bridge, scanwatch

---

## README

| Topic | What |
|-------|------|
| [Turbofit](wiki-topics/turbofit/index.md) | Model research, pipelines, hardware tiers — evidence-backed local inference runtime. |
| [Hermes Agent](wiki-topics/hermes-agent/index.md) | Runtime configuration, provider setup, model routing. |
| [Klerik](wiki-topics/klerik/index.md) | Profile factory, bot reviews, surgical corrections. |
| [Anser](wiki-topics/anser/index.md) | Native Hermes answers, trust per-row citations only. |
| [Looker](wiki-topics/looker/index.md) | UI-QA service bot: screenshots, vision, verification. |
| [Teknium](wiki-topics/teknium/index.md) | Hermes-Agent builder, core fixes, upstream PRs. |
| [Paladin](wiki-topics/paladin/index.md) | Vault structure warden, repo hygiene, merges. |
| [Weaver](wiki-topics/weaver/index.md) | Senter Wiki UI builder: vault-live.html, CSS, layout. |
| [Dogeman](wiki-topics/dogeman/index.md) | YouTube/content studio: rants, scripts, visuals. |
| [Turbosovth](wiki-topics/turbosovth/index.md) | TurboFit support agent — model research, never merges. |
| [Music](wiki-topics/music/index.md) | Music generation and AI composition. |
| [Dispatched M2S](wiki-topics/dispatched-m2s/index.md) | Dispatch pipeline for multi-agent workflows. |
| [Burner Phone](wiki-topics/burner-phone/index.md) | Mobile device management. |
| [Case MacBook](wiki-topics/case-macbook/index.md) | MacBook accessories and cases. |
| [Nous Community](wiki-topics/nous-community/index.md) | Nous Research community engagement. |
| [Kashik](wiki-topics/kashik/index.md) | Kashik project. |
| 40+ Archived | Absorbed topics preserved in `wiki-topics/_archive/`. |

---

## SKILLS

### Fleet Coordination

- **senter-fleet-coordination** — Operating playbook: route fleet ideas, bots, vault logs
- **progressive-disclosure** — How to read the vault: index → file → section
- **wiki-ui-knobs** — Live wiki UI rules and verification loops
- **remote-absorption-ssh** — Multi-machine consolidation over SSH

### Build & Verify

- **candidate-quant-comparison** — Evaluate new local model candidates
- **dflash2-fork-flag-boundary** — DFlash2 flag set that succeeds/fails
- **turbo-artifact-download-spec** — Reproducible download records with verification
- **turbo-fit-evidence-capture** — Capture performance from live Hermes window
- **turbo-model-store-cleanup** — Free storage, delete wiki-marked artifacts only
- **maple-mlx-server-runtime** — Run Maple MLX on Apple Silicon
- **mtplx-32gb-macos-tuning** — Tune MTPLX on 32GB macOS

### Review & Reflection

- **sdlc-review** — Review Kanban handoffs and route verified outcomes
- **simplify-code** — Parallel cleanup of recent code changes
- **requesting-code-review** — Pre-commit review: security, quality gates, auto-fix

---

## BOTS

| Bot | Role | Use |
|-----|------|-----|
| **senter** | Sidebar | Chris talks here. Routes, never builds. |
| **klerik** | Profile factory | Reviews and corrects other bots |
| **looker** | UI-QA | Screenshots, vision, verification |
| **teknium** | Core builder | Hermes-Agent fixes, upstream PRs |
| **paladin** | Warden | Vault structure, repo hygiene |
| **weaver** | UI builder | vault-live.html, CSS, layout |
| **dogeman** | Content studio | YouTube, scripts, visuals |
| **turbosovth** | TurboFit support | Model research, never merges |
| **anser** | Native answers | Citations only, no hallucination |
| **hermes-agent** | Runtime | Provider config, model routing |
| **turbofit** | Inference | Model zoo, pipelines, hardware |

---

## LOOPS

| Loop | Cadence | What |
|------|---------|------|
| **senter-umbrella** | 30m | Governance: merge, dedupe, catalogs |
| **senter-watcher** | continuous | Cut messages into per-topic inbox |
| **senter-scanwatch** | continuous | Snapshot `.system-live.json` |
| **turbofit-health-check** | 2h | All runtime processes healthy? |
| **turbofit-memory-monitor** | 15m | Memory usage across devices |
| **turbofit-candidate-discovery** | 6h | New models on HuggingFace |
| **hermes-model-change-detector** | 5m | Alert if model switches |
| **compression-timeout-watch** | 10m | Hermes compression failures |
