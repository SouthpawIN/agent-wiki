---
title: sidecar
updated: 2026-08-27
type: topic
repo: https://github.com/SouthpawIN/sidecar
status: dormant
tags: [repo]
---

# sidecar

> Use sidecar next to CLI agents for diffs, file trees, conversation history, and task management with td

**[Open on GitHub](https://github.com/SouthpawIN/sidecar)** · DORMANT (since 2026-07-08) · last push 2026-07-08

## Facts
- **Language:** Go
- **Stars / forks:** 1 / 0
- **License:** MIT
- **Fork of:** original work
- **Created:** 2026-02-13 · **Last push:** 2026-07-08
- **Open issues:** 0
- **Status:** DORMANT (since 2026-07-08)

## From the README

# Sidecar

You might never open your editor again.

**Status: Ready for daily use.** Please [report any issues](https://github.com/marcus/sidecar/issues) you encounter.

[Documentation](https://marcus.github.io/sidecar/) · [Getting Started](https://marcus.github.io/sidecar/docs/intro)

## Overview

Sidecar puts your entire development workflow in one shell: plan tasks with [td](https://github.com/marcus/td), chat with AI agents, review diffs, stage commits, review past conversations, and manage workspaces—all without leaving Sidecar.

## Quick Install

### macOS (recommended)

```bash
brew install marcus/tap/sidecar
```

This builds from source and avoids macOS Gatekeeper warnings.

### Linux / Other

```bash
curl -fsSL https://raw.githubusercontent.com/marcus/sidecar/main/scripts/setup.sh | bash
```

**More options:** [Binary downloads](https://github.com/marcus/sidecar/releases) · [Manual install](docs/getting-started.md)

## Requirements

- macOS, Linux, or WSL
- Go 1.21+ (only if building from source)

## Quick Start

After installation, run from any project directory:

```bash
sidecar
```

## Suggested Use

Split your terminal horizontally: run your coding agent (Claude Code, Cursor, etc.) on the left and sidecar on the right.

```
┌─────────────────────────────┬─────────────────────┐
│                             │                     │
│   Claude Code / Cursor      │      Sidecar        │
│                             │                     │
│   $ claude                  │   [Git] [Files]     │
│   > fix the auth bug...     │   [Tasks] [Workspaces]│
│                             │                     │
└─────────────────────────────┴─────────────────────┘
```

**Tip:** You can run two sidecar instances side-by-side to create a dashboard view. For example, keep one on the [Tasks] plugin and the other on [Git] or [Workspaces] to monitor everything at once.

As the agent works, you can:

- Watch tasks move through the workflow in TD Monitor
- See files change in real-time in the Git plugin
- Browse and edit code yourself in the File Browser
- View and resume conversations across all supported agent adapters
- Switch between built-in and community themes with live previews

This setup gives you visibility into what the agent is doing without interrupting your workflow. The entire dev loop—planning, monitoring, reviewing, committing—happens in the terminal while agents write the code.

## Usage

```bash
# Run from any project directory
sidecar

# Specify project root
sidecar --project /path/to/project

# Enable debug logging
sidecar --debug


*…truncated — full README at repo link*


## Archived
Archived 2026-09-02 — absorbed into [[topics-wiki/dev-tooling/README|dev-tooling]] by merge-topics.py v1.1.0. Nothing here was deleted or rewritten.
