# Injections

## [READ]

== absorbed from senter idea-wiki (2026-08-28) ==
---
title: herm-sovth
created: 2026-07-12
updated: 2026-07-12
type: entity
tags: [entity, idea-capture, provenance]
sources: ["raw/github/herm-sovth-9f0bd0e160.md"]
confidence: medium
---

# herm-sovth

## Current context

The Hermes TUI built with OpenTUI # Herm - Dashboard TUI for Hermes <img width="1711" height="927" alt="image" src="https://github.com/user-attachments/assets/d3b855a0-b1b2-4ea1-8eab-84f9716c8de9" /> > **herm** /hɜːm/ _noun_ : a sculptured head of Hermes on a square stone pillar, used in ancient Greece as a boundary marker at crossroads. Herm is a tabbed, mouse-aware TUI built with [OpenTUI](https://github.com/anomalyco/opentui) (React renderer) and [Bun](https://bun.sh/). It talks to the same gateway `hermes` cli uses. ## What it does - **Chat** with streaming, markdown, inline images (chafa), LaTeX→unicode, diff chips, tool-call expansion, and an animated ASCII avatar - **Tabs** for sessions, context, agents, analytics, skills, cron, toolsets, config, env, memory, kanban - **Profile switching** — hop between Hermes profiles without leaving the TUI - **Command palette** (`Ctrl+K`), **slash popover**, **@-refs** for file/diff context - **Fully rebindable keys** (`/keys`, opencode-compatible) and theme picker ## Install Herm needs a working [Hermes Agent](https://github.com/NousResearch/hermes-agent) install and [Bun](https://bun.sh). Or from source: Herm looks for `~/.hermes`. If yours lives elsewhere, set `HERMES_HOME`. See [`.env.example`](./.env.example) for rarely-needed overrides. ## Development ## Motivation Before Hermes, OpenCode was my daily driver. I built Herm because I wanted Hermes capabilities with an OpenCode style interface. Herm uses the same TUI framework OpenCode is built with, OpenTUI, and also exposes dashboard style tabs that centralizes everything I need to do in Hermes in my interface of choice--the terminal. ## Acknowledgments - [Hermes Agent](https://github.com/NousResearch/hermes-agent) — the brain - [OpenTUI](https://github.com/anomalyco/opentui) — the TUI framework - [OpenCode](https://github.com/anomalyco/opencode) — the inspiration ## License MIT — see [LICENSE](./LICENSE).

## Version policy

The latest available update marker is canonical: `https://github.com/SouthpawIN/herm-sovth` (`2026-07-08T20:37:24Z`). Earlier captures remain linked in the raw source inventory.

## Related concepts

- [[concepts/agent-fleet|Agent Fleet]]
- [[concepts/memory-wiki|Memory Wiki]]
