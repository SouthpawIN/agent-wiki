---
title: Bots
created: 2026-09-17
updated: 2026-09-17
type: bots
---

# Bots

> Every Hermes profile in the fleet.

Bots are Hermes profiles in `~/.hermes/profiles/<name>/`. Each can have its own topic with SKILLS, BOTS (sub-agents), and LOOPS.

## Active Bots

| Bot | Role | Status |
|-----|------|--------|
| **senter** | Sidebar (primary chat) | ACTIVE |
| **klerik** | Profile factory, bot reviews | ACTIVE |
| **looker** | UI-QA (screenshots, vision) | ACTIVE |
| **teknium** | Hermes-Agent builder, core fixes | ACTIVE |
| **paladin** | Vault structure warden | ACTIVE |
| **weaver** | Senter Wiki UI builder | ACTIVE |
| **dogeman** | YouTube/content studio | ACTIVE |
| **turbosovth** | TurboFit support (never merges) | ACTIVE |
| **anser** | Native answers, citations only | ACTIVE |
| **hermes-agent** | Runtime, provider config | ACTIVE |
| **turbofit** | Inference, model zoo | ACTIVE |

## Bot-Proposed Agents

Each topic's `agents/` directory contains proposed bots awaiting approval:
- `topics/*/agents/*.md.proposed` → awaiting review
- Approved via card click → bot profile created

---

## Add a New Bot

1. Create `topics/<topic>/agents/<name>.md.proposed`
2. Review and approve via card
3. Bot profile created in `~/.hermes/profiles/<name>/`
