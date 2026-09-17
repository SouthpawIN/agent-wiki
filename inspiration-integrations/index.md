---
title: Integrations
created: 2026-09-17
updated: 2026-09-17
type: integrations
---

# Integrations

> Everything that feeds data into the Senter Wiki.

Integrations are data sources: GitHub repos, HuggingFace models, raw inbox cuts from Hermes sessions, and fleet daemons.

## Active Integrations

| Integration | Feeds Into | What |
|-------------|------------|------|
| GitHub | All topics | Code, issues, PRs via `gh` CLI |
| HuggingFace | Turbofit | Model repos, downloads, benchmarks |
| Hermes state.db | All topics | Chat messages cut into per-topic inbox |
| Sessions | All topics | Full conversation transcripts |
| Fleet Daemons | senter-wiki | watcher, topic-agent, umbrella, bridge, scanwatch |

## By Topic

Each topic defines its own INTEGRATIONS section. See:
- [Turbofit](topics/turbofit/index.md) — GitHub, HF, Omarchy, raw inbox
- [Music](topics/music/index.md) — YouTube, Suno, raw inbox
- [Senter](topics/senter/index.md) — Hermes state.db, sessions, fleet daemons

## Add a New Integration

1. Identify the data source (API, file, feed)
2. Add to the relevant topic's INTEGRATIONS section
3. If cross-topic, add this page and link from the topic
