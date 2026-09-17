---
title: Senter Wiki
created: 2026-07-07
updated: 2026-09-17
type: wiki
links:
  github: https://github.com/SouthpawIN/Senter
  vault: ~/Documents/Projects/Projects
sources:
  - senter-wiki.md
  - BRIEF.md
  - topics/
---

# Senter Wiki

> Cursor for markdown. A live-acting second brain.

This vault is the **coordination layer** between Chris and the Hermes fleet. Every idea, decision, and artifact lives here as markdown. Edit any file — that's the steering wheel.

---

## INTEGRATIONS

This wiki is fed by:

- **GitHub:** [SouthpawIN/Senter](https://github.com/SouthpawIN/Senter) — repo, issues, PRs
- **Hermes state.db:** every chat message cut into `topics/<t>/raw/inbox/`
- **Sessions:** `topics/senter-wiki/.system/sessions/` — full conversation transcripts
- **Fleet daemons:** watcher, topic-agent, umbrella, bridge, scanwatch

---

## README

> Every topic Chris cares about. Click to open its wiki.

| Topic | What |
|-------|------|
| [Turbofit](topics/turbofit/index.md) | Model research, pipelines, hardware tiers — evidence-backed local inference runtime. |
| [Music](topics/music/index.md) | Music generation and AI composition. |
| [Dispatched M2S](topics/dispatched-m2s/index.md) | Dispatch pipeline for multi-agent workflows. |
| [Burner Phone](topics/burner-phone/index.md) | Mobile device management. |
| [Case MacBook](topics/case-macbook/index.md) | MacBook accessories and cases. |
| [Nous Community](topics/nous-community/index.md) | Nous Research community engagement. |
| [Kashik](topics/kashik/index.md) | Kashik project. |
| [Back Where](topics/back-where/index.md) | Context and memory management. |
| [Both Smarter](topics/both-smarter/index.md) | Dual intelligence systems. |
| [Beyond Pissed](topics/beyond-pissed/index.md) | Advanced troubleshooting. |
| [Central Asked](topics/central-asked/index.md) | Central query hub. |
| [Click Options](topics/click-options/index.md) | Click handling patterns. |
| [Crow](topics/crow/index.md) | Crow project. |
| [Dev Tooling](topics/dev-tooling/index.md) | Development tools. |
| [Evolutionary](topics/evolutionary/index.md) | Evolutionary algorithms. |
| [Faster Without](topics/faster-without/index.md) | Performance optimization. |
| [Life Links](topics/life-links/index.md) | Personal knowledge management. |
| [Object Important](topics/object-important/index.md) | Object importance tracking. |
| [Only Device](topics/only-device/index.md) | Device-specific config. |
| [Pocket Shop](topics/pocket-shop/index.md) | Pocket shop app. |
| [Process Important](topics/process-important/index.md) | Process importance tracking. |
| [Restore Hdiutil](topics/restore-hdiutil/index.md) | macOS disk utility. |
| [Self File](topics/self-file/index.md) | Self-file management. |
| [Tailscale Steam](topics/tailscale-steam/index.md) | Tailscale + Steam streaming. |
| [Talked Architecture](topics/talked-architecture/index.md) | Architecture discussions. |
| [Try Again](topics/try-again/index.md) | Retry logic. |
| [User Message](topics/user-message/index.md) | User messaging. |
| [Want Version](topics/want-version/index.md) | Version requests. |
| [What Mean](topics/what-mean/index.md) | Meaning analysis. |
| [Whoa There](topics/whoa-there/index.md) | Alerts and monitoring. |
| [Wiki Want](topics/wiki-want/index.md) | Wiki feature requests. |
| [YouTube](topics/youtube/index.md) | YouTube content. |
| 20+ More | Additional topics in `topics/`. |

---

## SKILLS

> What Hermes knows how to do. Each skill is a SKILL.md with frontmatter.

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

> The fleet. Each bot is a Hermes profile in `~/.hermes/profiles/<name>/`.

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

> Scheduled automations.

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
