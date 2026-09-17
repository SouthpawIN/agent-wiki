---
title: Steam streaming setup
created: 2026-09-15
updated: 2026-09-15
type: concept
tags: [plan, tool, pain, timeline]
sources: ["raw/inbox/2026-09-13.md"]
confidence: high
---

# Steam streaming setup

Chris wants to stream games from his HP workstation (Omarchy, the steam machine) to his MacBook screen via **Steam Link**.^[raw/inbox/2026-09-13.md]

## Steps taken
1. Wipe old Steam + games (~30GB) and Whisky/Wine from the MacBook; install fresh clean Steam.app.^[raw/inbox/2026-09-13.md]
2. Steam running on the HP (confirmed 2026-09-13 15:42).^[raw/inbox/2026-09-13.md]
3. Install **Steam Link** on the MacBook (free).^[raw/inbox/2026-09-13.md]
4. Connect Steam Link to the HP **manually by Tailscale IP** (100.68.42.68), because mDNS auto-discovery doesn't cross Tailscale subnets.^[raw/inbox/2026-09-13.md]

## Pain
- Chris struggled to get Steam Link to "find" the HP; auto-discovery fails across the tailnet, requiring manual IP entry and a PIN. See [[wiki-topics/tailscale-steam/wiki/queries/steam-link-discovery|Steam Link discovery query]].

## Naming
- Chris first said "Steam Play," then corrected to **Steam Link**. See [[wiki-topics/tailscale-steam/wiki/decisions/steam-terminology-decision|Steam terminology decision]] and [[wiki-topics/tailscale-steam/wiki/comparisons/steam-remote-play-terms|Steam Play vs Steam Link vs Remote Play]].

Related: [[wiki-topics/tailscale-steam/wiki/entities/omarchy|Omarchy]], [[wiki-topics/tailscale-steam/wiki/entities/steam-link-app|Steam Link app]].
