---
title: Streaming setup (MacBook-managed)
created: 2026-09-15
updated: 2026-09-15
type: concept
tags: [plan, idea]
sources: [raw/inbox/2026-09-14.md, raw/inbox/2026-09-15.md]
confidence: high
---
The streaming setup Chris wants is to **run the game on the Omarchy but manage the broadcast from his MacBook**.^[raw/inbox/2026-09-14.md] His rationale: the MacBook has "a better mic" and lets him "keep the screen open" while he plays Armored Core 6 on the Omarchy.^[raw/inbox/2026-09-14.md]

The shape of it:
- **OBS** runs on the MacBook, not the Omarchy.^[raw/inbox/2026-09-15.md]
- A **remote desktop / VNC** session reaches into the Omarchy over **Tailscale** so Chris can see and control the game from the MacBook.^[raw/inbox/2026-09-14.md]^[raw/inbox/2026-09-15.md]
- The MacBook **handles OBS and media edits**.^[raw/inbox/2026-09-15.md]

Outstanding: the Omarchy's desktop service over Tailscale was not reachable as of 2026-09-14 (port 443 is the OS control plane, SSH/22 refused). As of 2026-09-15 Hermes was standing up **wayvnc** as a systemd user service on the Omarchy to fill this gap.^[raw/inbox/2026-09-14.md]^[raw/inbox/2026-09-15.md]

Related: [[wiki/entities/armored-core-6|Armored Core 6]], [[wiki/entities/obs-studio|OBS Studio]], [[wiki/entities/tailscale|Tailscale]]
