# Injections

## [READ]

== absorbed from senter idea-wiki (2026-08-28) ==
---
title: sidecar
created: 2026-07-12
updated: 2026-07-12
type: entity
tags: [entity, idea-capture, provenance]
sources: ["raw/github/sidecar-0f7a3d480d.md"]
confidence: medium
---

# sidecar

## Current context

Use sidecar next to CLI agents for diffs, file trees, conversation history, and task management with td # Sidecar You might never open your editor again. **Status: Ready for daily use.** Please [report any issues](https://github.com/marcus/sidecar/issues) you encounter. [Documentation](https://marcus.github.io/sidecar/) · [Getting Started](https://marcus.github.io/sidecar/docs/intro) ## Overview Sidecar puts your entire development workflow in one shell: plan tasks with [td](https://github.com/marcus/td), chat with AI agents, review diffs, stage commits, review past conversations, and manage workspaces—all without leaving Sidecar. ## Quick Install ### macOS (recommended) This builds from source and avoids macOS Gatekeeper warnings. ### Linux / Other **More options:** [Binary downloads](https://github.com/marcus/sidecar/releases) · [Manual install](docs/getting-started.md) ## Requirements - macOS, Linux, or WSL - Go 1.21+ (only if building from source) ## Quick Start After installation, run from any project directory: ## Suggested Use Split your terminal horizontally: run your coding agent (Claude Code, Cursor, etc.) on the left and sidecar on the right. **Tip:** You can run two sidecar instances side-by-side to create a dashboard view. For example, keep one on the [Tasks] plugin and the other on [Git] or [Workspaces] to monitor everything at once. As the agent works, you can: - Watch tasks move through the workflow in TD Monitor - See files change in real-time in the Git plugin - Browse and edit code yourself in the File Browser - View and resume conversations across all supported agent adapters - Switch between built-in and community themes with live previews This setup gives you visibility into what the agent is doing without interrupting your workflow. The entire dev loop—planning, monitoring, reviewing, committing—happens in the terminal while agents write the code. ## Usage ## Updates Sidecar checks for updates on startup. When a new version is available, a toast notification appears. Press `!` to open the diagnostics modal and see the update command. ## Plugins ### Git Status View staged, modified, and untracked files with a split-pane interface. The sidebar shows files and recent commits; the main pane shows syntax-highlighted diffs. [Full documentation →](https://marcus.github.io/sidecar/docs/git-plugin) **Features:** - Stage/unstage files with…

## Version policy

The latest available update marker is canonical: `https://github.com/SouthpawIN/sidecar` (`2026-07-08T20:37:30Z`). Earlier captures remain linked in the raw source inventory.

## Related concepts

- [[concepts/agent-fleet|Agent Fleet]]
- [[concepts/community-ideas|Community Ideas]]
