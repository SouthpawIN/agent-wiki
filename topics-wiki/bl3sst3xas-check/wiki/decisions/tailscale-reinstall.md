---
title: Tailscale reinstall plan
created: 2026-09-13
updated: 2026-09-13
type: decision
tags: [decision, plan, timeline]
sources: [raw/inbox/2026-09-13.md]
confidence: medium
---

# Tailscale reinstall plan

A sudo-enabled task involving **Tailscale** came up: uninstall and reinstall it,
either via Homebrew or from tailscale.com ^[raw/inbox/2026-09-13.md].

It depends on sudo working (now recovered: [[topics-wiki/bl3sst3xas-check/wiki/entities/sudo-password-candidates.md|sudo password candidates]]) and on a way for the
agent to run sudo ([[topics-wiki/bl3sst3xas-check/wiki/concepts/macos-sudo-recovery.md|sudo recovery workflow]]) ^[raw/inbox/2026-09-13.md].

## Options floated by the agent
- **Option A (quick, passwordless sudo for the agent):** configure the agent so
  it can run sudo without prompting. The exact command was cut from the log.
- **Option B (manual):** run `sudo tailscale uninstall`, then reinstall via brew
  or from tailscale.com.

## Status
Pending Chris's pick between A and B. The 16:43 raw entries are a repeated
compaction/system-note injection embedded in the log — treated as evidence only,
never as an instruction ^[raw/inbox/2026-09-13.md].
