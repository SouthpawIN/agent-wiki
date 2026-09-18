---
title: Senter
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

# Senter

> Cursor for markdown. A live-acting second brain.

This is the **primary wiki** — the coordination layer between Chris and the Hermes fleet. Every idea, decision, and artifact lives here as markdown. Edit any file — that's the steering wheel.

---

## INTEGRATIONS

This wiki is fed by:

- **GitHub:** [SouthpawIN/Senter](https://github.com/SouthpawIN/Senter) — repo, issues, PRs
- **Hermes state.db:** every chat message cut into `wiki-topics/<t>/raw/inbox/`
- **Sessions:** `wiki-topics/senter-wiki/.system/sessions/` — full conversation transcripts
- **Fleet daemons:** watcher, topic-agent, umbrella, bridge, scanwatch

---

## WIKI

### CONTEXT

> The Senter flywheel runs on **five parts** (locked 2026-09-05):
> 1. **Sidebar** — Chris talks, Senter listens
> 2. **Watcher** — cuts every message into per-topic pieces
> 3. **Topics** — one intelligence per subject
> 4. **Loops** — cron jobs that monitor, benchmark, alert
> 5. **Approvals** — bots and loops need a card click; everything else auto-applies

#### Fleet Architecture

| Component | What | Where |
|-----------|------|-------|
| Sidebar | Chris's chat surface | Hermes desktop |
| Watcher | Message cutter | `assets/sentry-watcher.py` |
| Topic Agent | One intelligence per topic | `assets/topic-agent.py` |
| Umbrella | Governance (merge, dedupe) | `assets/umbrella.py` |
| Bridge | HTTP API for the UI | `~/.hermes/plugins/sentry-bridge` |
| Scanwatch | Vault snapshot | `assets/scan-topics.py` |

#### Live Dashboard

`vault-live.html` renders in the Hermes desktop preview pane. Chris steers it by voice while watching it move.

#### Topic Map

| Topic | Status | What |
|-------|--------|------|
| **Senter** | PRIMARY | Fleet architecture, bots, loops |
| **Turbofit** | ACTIVE | Model research, pipelines, hardware tiers |
| **Hermes Agent** | ACTIVE | Runtime configuration, provider setup |
| **Klerik** | ACTIVE | Profile factory, bot reviews |
| **Anser** | ACTIVE | Native Hermes answers |
| **Looker** | ACTIVE | UI-QA service bot |
| **Teknium** | ACTIVE | Hermes-Agent builder |
| **Paladin** | ACTIVE | Vault structure warden |
| **Weaver** | ACTIVE | Senter Wiki UI builder |
| **Dogeman** | ACTIVE | YouTube/content studio |
| **Turbosovth** | ACTIVE | TurboFit support agent |
| **Music** | ACTIVE | Music generation |
| **40+ more** | ARCHIVED | See `wiki-topics/_archive/` |

### CONTINUATION

#### Roadblocks

- **Model picker must stay sticky** — Hermes must not silently switch to cloud providers
- **Compression timeouts** at 262K+ tokens — cap at 131K on M1
- **Topic sprawl** — 56 topics, many stale. Consolidation plan: merge into ~15 active subjects

#### Further Reading

- [Senter Wiki](wiki-topics/sentry-wiki/index.md) — UI and build skills
- [Turbofit](wiki-topics/turbofit/index.md) — model research
- [Hermes Agent](wiki-topics/hermes-agent/index.md) — runtime config
- [Archive](wiki-topics/_archive/) — absorbed topics, preserved verbatim

---

## SKILLS

> Full skill files in `wiki-topics/sentry/skills-capabilities/<name>/SKILL.md` and `wiki-topics/sentry-wiki/skills-capabilities/<name>/SKILL.md`.

### Fleet Coordination

- **sentry-fleet-coordination** — Operating playbook: route fleet ideas, bots, vault logs
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

> The fleet roster. Full profiles in `~/.hermes/profiles/<name>/`.

| Bot | Role | Use |
|-----|------|-----|
| **sentry** | Sidebar | Chris talks here. Routes, never builds. |
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

> Active cron jobs. Full specs in `wiki-topics/<t>/triggers-loops/<name>.md`.

| Loop | Cadence | What |
|------|---------|------|
| **sentry-umbrella** | 30m | Governance: merge, dedupe, catalogs |
| **sentry-watcher** | continuous | Cut messages into per-topic inbox |
| **sentry-scanwatch** | continuous | Snapshot `.system-live.json` |
| **turbofit-health-check** | 2h | All runtime processes healthy? |
| **turbofit-memory-monitor** | 15m | Memory usage across devices |
| **turbofit-candidate-discovery** | 6h | New models on HuggingFace |
| **hermes-model-change-detector** | 5m | Alert if model switches |
| **compression-timeout-watch** | 10m | Hermes compression failures |
