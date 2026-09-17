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
  - wiki-topics/
  - skills-capabilities/
  - bots-profiles/
  - triggers-triggers-loops/
  - inspiration-inspiration-integrations/
---

# Senter Wiki

> Cursor for markdown. A live-acting second brain.

The Senter Wiki is the **master orchestration layer** for everything Chris cares about. It's a structured knowledge base that coordinates the entire Hermes fleet — turning haphazard conversations into organized, actionable work across dozens of topics simultaneously.

---

## README

### What This Is

The Sentry Wiki is a **bonsai tree of knowledge**: the same structure repeats at every scale. The vault root has INTEGRATIONS, README, SKILLS, BOTS, and LOOPS. Every topic inside it has the same. Every sub-topic within that has the same. This creates a self-similar, navigable hierarchy where any level can be understood the same way.

**The pattern:**
```
INTEGRATIONS — what data feeds this level
README       — what this is, table of contents for what's inside
SKILLS       — what Hermes knows how to do at this level
BOTS         — the autonomous agents working at this level
LOOPS        — scheduled automations running at this level
```

### How It Works

Chris talks freely about anything. Hermes (the sidebar agent) listens, extracts ideas, and sorts them into topics. Each topic gets its own focused wiki with evidence, decisions, and action items.

When a topic accumulates enough patterns — repeated issues, common tasks, monitorable conditions — Hermes proposes **skills** (reusable procedures), **bots** (autonomous agents), and **loops** (scheduled automations). Chris approves via card clicks. The work happens automatically.

This means Chris can talk about **everything at once** — Turbofit one minute, Music the next, then random macOS troubleshooting — and the wiki self-organizes. Each topic gets its own focused workstream without Chris having to context-switch.

### The Four Primitives

| Primitive | What | Example |
|-----------|------|---------|
| **Topics** | Subjects Chris cares about | Turbofit, Music, Dispatched M2S |
| **Skills** | Reusable procedures Hermes can run | candidate-quantification, turbo-artifact-download-spec |
| **Bots** | Autonomous Hermes profiles | senter, klerik, looker, turbosovth |
| **Loops** | Scheduled/cron automations | senter-umbrella (30m), turbofit-health-check (2h) |

### Current Topics

| Topic | What |
|-------|------|
| [Turbofit](wiki-topics/turbofit/index.md) | Model research, pipelines, hardware tiers |
| [Music](wiki-topics/music/index.md) | Music generation and AI composition |
| [Dispatched M2S](wiki-topics/dispatched-m2s/index.md) | Multi-agent dispatch pipeline |
| [Burner Phone](wiki-topics/burner-phone/index.md) | Mobile device management |
| [Case MacBook](wiki-topics/case-macbook/index.md) | MacBook accessories |
| [Nous Community](wiki-topics/nous-community/index.md) | Nous Research community |
| [Back Where](wiki-topics/back-where/index.md) | Context and memory management |
| [Both Smarter](wiki-topics/both-smarter/index.md) | Dual intelligence systems |
| [Beyond Pissed](wiki-topics/beyond-pissed/index.md) | Advanced troubleshooting |
| [Central Asked](wiki-topics/central-asked/index.md) | Central query hub |
| [Click Options](wiki-topics/click-options/index.md) | Click handling patterns |
| [Crow](wiki-topics/crow/index.md) | Crow project |
| [Dev Tooling](wiki-topics/dev-tooling/index.md) | Development tools |
| [Evolutionary](wiki-topics/evolutionary/index.md) | Evolutionary algorithms |
| [Faster Without](wiki-topics/faster-without/index.md) | Performance optimization |
| [Life Links](wiki-topics/life-links/index.md) | Personal knowledge management |
| [Object Important](wiki-topics/object-important/index.md) | Object importance tracking |
| [Only Device](wiki-topics/only-device/index.md) | Device-specific config |
| [Pocket Shop](wiki-topics/pocket-shop/index.md) | Pocket shop app |
| [Process Important](wiki-topics/process-important/index.md) | Process importance tracking |
| [Restore Hdiutil](wiki-topics/restore-hdiutil/index.md) | macOS disk utility |
| [Self File](wiki-topics/self-file/index.md) | Self-file management |
| [Tailscale Steam](wiki-topics/tailscale-steam/index.md) | Tailscale + Steam streaming |
| [Talked Architecture](wiki-topics/talked-architecture/index.md) | Architecture discussions |
| [Try Again](wiki-topics/try-again/index.md) | Retry logic |
| [User Message](wiki-topics/user-message/index.md) | User messaging |
| [Want Version](wiki-topics/want-version/index.md) | Version requests |
| [What Mean](wiki-topics/what-mean/index.md) | Meaning analysis |
| [Whoa There](wiki-topics/whoa-there/index.md) | Alerts and monitoring |
| [Wiki Want](wiki-topics/wiki-want/index.md) | Wiki feature requests |
| [YouTube](wiki-topics/youtube/index.md) | YouTube content |
| 20+ Archived | Absorbed topics in `wiki-topics/_archive/` |

### Progressive Disclosure

This wiki uses the same pattern Hermes uses for skill discovery:

1. **Scan** — README shows topic names + one-line descriptions (this page)
2. **Click** — Open any topic to see its own README with full detail
3. **Drill** — Each topic's SKILLS/BOTS/LOOPS link to their full definitions
4. **Act** — Edit any file, approve any card, spawn any bot

No need to read everything. Navigate by relevance.

### Active Fleet

**11 bots** in the fleet, each a Hermes profile:
- **senter** — Chris's sidebar (routes, never builds)
- **klerik** — Profile factory, reviews other bots
- **looker** — UI-QA (screenshots, vision, verification)
- **teknium** — Hermes-Agent builder, core fixes
- **paladin** — Vault structure warden
- **weaver** — Senter Wiki UI builder
- **dogeman** — YouTube/content studio
- **turbosovth** — TurboFit support (never merges)
- **anser** — Native answers, citations only
- **hermes-agent** — Runtime, provider config
- **turbofit** — Inference, model zoo

### Active Loops

**8 cron jobs** monitoring and maintaining the system:
- **senter-umbrella** (30m) — Governance: merge, dedupe, catalogs
- **senter-watcher** (continuous) — Cut messages into per-topic inbox
- **senter-scanwatch** (continuous) — Snapshot vault state
- **turbofit-health-check** (2h) — Runtime process health
- **turbofit-memory-monitor** (15m) — Memory usage across devices
- **turbofit-candidate-discovery** (6h) — New models on HuggingFace
- **hermes-model-change-detector** (5m) — Alert on model switches
- **compression-timeout-watch** (10m) — Hermes compression failures

### Principles

- **Local first** — Cloud fallback only when local capability exceeded
- **Evidence-driven** — Every claim needs a source
- **Evidence before winner** — No declaring winners without benchmarks
- **Reasoning ON** — All models think by default
- **Stop asking, start building** — Preempt decisions, complete gaps
- **Motion = progress** — The wiki should move while Chris talks

### How to Use This Wiki

1. **Talk naturally** — Chris discusses anything with the sidebar agent
2. **Watch it organize** — Hermes sorts ideas into topics automatically
3. **Review cards** — Approve/reject proposed skills, bots, and loops
4. **Click to dive** — Open any topic for full depth
5. **Edit anything** — Every file is the steering wheel

---

## SKILLS

See [Skills](skills-capabilities/index.md) for all Hermes skills.

## BOTS

See [Bots](bots-profiles/index.md) for all Hermes profiles.

## LOOPS

See [Loops](triggers-triggers-loops/index.md) for all cron jobs and automations.
