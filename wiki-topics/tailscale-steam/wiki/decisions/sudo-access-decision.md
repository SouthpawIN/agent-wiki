---
title: sudo access required
created: 2026-09-15
updated: 2026-09-15
type: decision
tags: [decision, preference, infra]
sources: ["raw/inbox/2026-09-13.md"]
confidence: high
---

# sudo access required

## Decision
Chris requires **sudo access** on the machines being configured. He called it "non-negotiable."

## Why
- 2026-09-13 14:16 Chris: "We will absolutely need sudo access. That is non-negotiable."^[raw/inbox/2026-09-13.md]

## Context
- Needed to install/configure Steam, enable SSH, and fix Hermes on the Surface Duo (Termux).^[raw/inbox/2026-09-13.md]
- sudo was recovered/stored on the Mac 2026-09-13 14:24.^[raw/inbox/2026-09-13.md]

Related: [[wiki-topics/tailscale-steam/wiki/concepts/tailscale-remote-access|Tailscale remote access]].
