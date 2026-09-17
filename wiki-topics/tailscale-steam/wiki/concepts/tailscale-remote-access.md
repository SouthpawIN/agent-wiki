---
title: Tailscale remote access (SSH + model discovery)
created: 2026-09-15
updated: 2026-09-15
type: concept
tags: [infra, plan, tool, timeline]
sources: ["raw/inbox/2026-09-13.md", "raw/inbox/2026-09-15.md"]
confidence: high
---

# Tailscale remote access (SSH + model discovery)

Two related goals ride on Tailscale here: remote shell access to Chris's machines, and accessing his Hermes *models* from any device.

## SSH remote access
- Hermes needs shell access to the HP (Omarchy) to install Steam and configure Remote Play. SSH wasn't running; Chris was asked to enable it.^[raw/inbox/2026-09-13.md]
- SSH is running on Omarchy as of 2026-09-15 09:25 but needs a Tailscale auth check: https://login.tailscale.com/a/l1d036c193b56d6.^[raw/inbox/2026-09-15.md]
- **sudo access is non-negotiable** for the work.^[raw/inbox/2026-09-13.md] See [[wiki-topics/tailscale-steam/wiki/decisions/sudo-access-decision|sudo access decision]].

## Model discovery vision
- Chris's aim: search and access his Hermes instances and models across his HP, workstation, phone, and MacBook — e.g. "Quinn next flash" and "Quinn 27" available on his phone and the MacBook.^[raw/inbox/2026-09-13.md]
- As of 2026-09-15 15:38, setting up Tailscale model discovery after a restart.^[raw/inbox/2026-09-15.md]

Related: [[wiki-topics/tailscale-steam/wiki/entities/surface-duo-2|Surface Duo 2]], [[wiki-topics/tailscale-steam/wiki/entities/macbook|MacBook]], [[wiki-topics/tailscale-steam/wiki/concepts/tailscale-network|Tailscale network]].
