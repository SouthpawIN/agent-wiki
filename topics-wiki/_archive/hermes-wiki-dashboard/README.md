---
title: hermes-wiki-dashboard
updated: 2026-08-27
type: topic
repo: https://github.com/SouthpawIN/hermes-wiki-dashboard
status: dormant
tags: [repo]
---

# hermes-wiki-dashboard

> Hermes dashboard tab: browse ~/.hermes/wiki markdown and queue agent-wiki factory tasks

**[Open on GitHub](https://github.com/SouthpawIN/hermes-wiki-dashboard)** · DORMANT (since 2026-07-15) · last push 2026-07-15

## Facts
- **Language:** Python
- **Stars / forks:** 1 / 0
- **License:** MIT
- **Fork of:** original work
- **Created:** 2026-07-15 · **Last push:** 2026-07-15
- **Open issues:** 0
- **Status:** DORMANT (since 2026-07-15)

## From the README

# Hermes Idea Wiki — Dashboard Plugin (fork of clankerbot99/hermes-wiki-dashboard)

> Browse the captured **Idea Wiki** (`~/idea-wiki/`) markdown and queue factory
> tasks from the Hermes web dashboard. Adapted from the upstream Agent-Wiki
> plugin so the surface renders the **live operating view** — each topic carries a
> colored state rail (active / proposed / blocked / idea / stale) driven by
> `~/idea-wiki/.system/wiki-state.json`.

## What it does

| Feature | Description |
|---------|-------------|
| **Wiki browser** | Sidebar of all `.md` under `~/idea-wiki/` (optional `.system/` paths) |
| **Live state rails** | Each topic shows a colored dot + badges (active agents / loops / proposed) from `wiki-state.json` — colors shift as the wiki operates |
| **Favorites** | Pin frequently used pages at the top of the sidebar (stored in `~/.hermes/wiki-dashboard-favorites.json`) |
| **Reader** | Rendered or raw markdown view |
| **Queue tasks** | Append `[SKILLS]` / `[AGENTS]` / `[LOOPS]` items to `topics-wiki//.system/queue.md` |

## What it does

| Feature | Description |
|---------|-------------|
| **Wiki browser** | Sidebar of all `.md` under `~/.hermes/wiki/` (optional `.system/` paths) |
| **Favorites** | Pin frequently used pages at the top of the sidebar (stored in `~/.hermes/wiki-dashboard-favorites.json`) |
| **Reader** | Rendered or raw markdown view |
| **Queue tasks** | Append `[SKILLS]` / `[AGENTS]` / `[LOOPS]` items to `topics-wiki//.system/queue.md` |

Scheduled factories (`skills-factory`, `agents-factory`, `loops-factory`) read those queue files on their cron ticks — same format as manual edits in the wiki spec.

## Prerequisites

1. **Hermes Agent** with `hermes dashboard`
2. **Agent Wiki** clone:

   ```bash
   git clone https://github.com/SouthpawIN/agent-wiki.git ~/.hermes/wiki
   ```

3. Factory crons configured (see agent-wiki `spec.md`)

## Install

```bash
git clone https://github.com/clankerbot99/hermes-wiki-dashboard.git ~/.hermes/plugins/wiki-dashboard
```

Enable the plugin in `~/.hermes/config.yaml`:

```yaml
plugins:
  enabled:
    - wiki-dashboard
```

**Restart the dashboard** (Python API routes mount at startup):

```bash
systemctl --user restart hermes-dashboard
# or: stop/start your hermes dashboard process
```

Log in to the dashboard → you should see a **Wiki** tab (positioned after Kanban).

If the tab does not appear, use **Plugins** → rescan or:

```bash
curl -b cookies.txt -c cookies.txt ... /api/dashboard/plugins/rescan
```

## Usage


*…truncated — full README at repo link*


## Archived
Archived 2026-09-02 — absorbed into [[topics-wiki/senter-wiki/README|senter-wiki]] by merge-topics.py v1.1.0. Nothing here was deleted or rewritten.
