---
title: Steam Link can't find the HP over Tailscale
created: 2026-09-15
updated: 2026-09-15
type: query
tags: [question, pain, tool]
sources: ["raw/inbox/2026-09-13.md"]
confidence: high
---

# Steam Link can't find the HP over Tailscale

## Question
Why won't Steam Link auto-discover the HP workstation, and how should Chris connect?

## Evidence
- 2026-09-13 15:42 Chris: "Okay, steam is running on my HP. I'm trying to get steam play to find it's having a hard time. See what's up."^[raw/inbox/2026-09-13.md]
- 2026-09-13 15:42 hermes: "the issue is likely auto-discovery — Steam Link uses mDNS/broadcast which doesn't cross Tailscale subnets. We need to connect manually via the Tailscale IP."^[raw/inbox/2026-09-13.md]

## Workaround (applied)
In Steam Link on the MacBook: click **"Other Computer"** → enter the HP's Tailscale IP **100.68.42.68** → pair → enter PIN.^[raw/inbox/2026-09-13.md]

See [[topics-wiki/tailscale-steam/wiki/concepts/steam-streaming-setup|Steam streaming setup]], [[topics-wiki/tailscale-steam/wiki/comparisons/steam-remote-play-terms|Steam Play vs Steam Link vs Remote Play]].
