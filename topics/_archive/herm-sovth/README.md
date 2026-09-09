---
title: herm-sovth
updated: 2026-08-27
type: topic
repo: https://github.com/SouthpawIN/herm-sovth
status: dormant
tags: [repo]
---

# herm-sovth

> The Hermes TUI built with OpenTUI

**[Open on GitHub](https://github.com/SouthpawIN/herm-sovth)** · DORMANT (since 2026-07-14) · last push 2026-07-14

## Facts
- **Language:** TypeScript
- **Stars / forks:** 3 / 0
- **License:** MIT
- **Fork of:** original work
- **Created:** 2026-05-11 · **Last push:** 2026-07-14
- **Open issues:** 0
- **Status:** DORMANT (since 2026-07-14)

## From the README

# Herm - Dashboard TUI for Hermes

> **herm** /hɜːm/ _noun_ : a sculptured head of Hermes on a square stone pillar, used in ancient Greece as a boundary marker at crossroads.

Herm is a tabbed, mouse-aware TUI built with [OpenTUI](https://github.com/anomalyco/opentui) (React renderer) and [Bun](https://bun.sh/). It talks to the same gateway `hermes` cli uses.

## What it does

- **Chat** with streaming, markdown, inline images (chafa), LaTeX→unicode, diff chips, tool-call expansion, and an animated ASCII avatar
- **Tabs** for sessions, context, agents, analytics, skills, cron, toolsets, config, env, memory, kanban
- **Profile switching** — hop between Hermes profiles without leaving the TUI
- **Command palette** (`Ctrl+K`), **slash popover**, **@-refs** for file/diff context
- **Fully rebindable keys** (`/keys`, opencode-compatible) and theme picker

## Install

Herm needs a working [Hermes Agent](https://github.com/NousResearch/hermes-agent) install and [Bun](https://bun.sh).

```bash
bunx herm-tui              # try without installing
bun add -g herm-tui        # stable
npm i -g herm-tui          # also fine
bun add -g herm-tui@next   # bleeding edge (every dev push)
herm                       # fresh session
herm -c                    # resume last session
```

Or from source:

```bash
git clone https://github.com/liftaris/herm.git
cd herm && bun install
bun run src/index.tsx
```

Herm looks for `~/.hermes`. If yours lives elsewhere, set `HERMES_HOME`. See [`.env.example`](./.env.example) for rarely-needed overrides.

## Development

```bash
bun run dev            # watch mode
bun run typecheck
bun test
```

## Motivation
Before Hermes, OpenCode was my daily driver. I built Herm because I wanted Hermes capabilities with an OpenCode style interface. Herm uses the same TUI framework OpenCode is built with, OpenTUI, and also exposes dashboard style tabs that centralizes everything I need to do in Hermes in my interface of choice--the terminal.

## Acknowledgments

- [Hermes Agent](https://github.com/NousResearch/hermes-agent) — the brain
- [OpenTUI](https://github.com/anomalyco/opentui) — the TUI framework
- [OpenCode](https://github.com/anomalyco/opencode) — the inspiration

## License

MIT — see [LICENSE](./LICENSE).


## Archived
Archived 2026-09-02 — absorbed into [[topics/hermes-agent/README|hermes-agent]] by merge-topics.py v1.1.0. Nothing here was deleted or rewritten.
