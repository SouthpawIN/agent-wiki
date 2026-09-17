---
title: Omarchy (HP Workstation)
created: 2026-09-15
updated: 2026-09-15
type: entity
tags: [tool, infra, timeline]
sources: ["raw/inbox/2026-09-13.md", "raw/inbox/2026-09-14.md", "raw/inbox/2026-09-15.md"]
confidence: high
---

# Omarchy (HP Workstation)

Omarchy is Chris's HP desktop workstation — the "steam machine" that hosts his games and is the streaming source for Steam Link on the MacBook.^[raw/inbox/2026-09-13.md] It is the machine games are streamed *from* to the MacBook.

## Tailscale
- Tailscale name: **omarchy**
- Tailscale IP: **100.68.42.68**
- Status: online (seen online 2026-09-13 14:56)^[raw/inbox/2026-09-13.md]
- Re-probed live on Tailscale 2026-09-14 20:13 ("Omarchy is live on Tailscale at 100.68.42.68").^[raw/inbox/2026-09-14.md]

## Steam / streaming
- Steam is running on it (confirmed 2026-09-13 15:42).^[raw/inbox/2026-09-13.md]
- Steam Remote Play (port 27036) open on it.^[raw/inbox/2026-09-13.md]
- Steam Link on the MacBook connects to it via its Tailscale IP (100.68.42.68) because mDNS auto-discovery doesn't cross Tailscale subnets.^[raw/inbox/2026-09-13.md]

## Remote access (SSH)
- SSH was not running initially; Chris was asked to enable it.^[raw/inbox/2026-09-13.md]
- SSH is now running on Omarchy as of 2026-09-15 09:25, but Tailscale SSH required a one-time auth check at https://login.tailscale.com/a/l1d036c193b56d6.^[raw/inbox/2026-09-15.md]

Related: [[topics-wiki/tailscale-steam/wiki/concepts/steam-streaming-setup|Steam streaming setup]], [[topics-wiki/tailscale-steam/wiki/concepts/tailscale-remote-access|Tailscale remote access]].
