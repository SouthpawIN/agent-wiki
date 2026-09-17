---
title: hermes install broken on Omarchy
created: 2026-09-15
updated: 2026-09-15
type: query
tags: [question, pain, infra]
sources: [raw/inbox/2026-09-15.md]
confidence: high
---
Something broke Chris's **hermes install on the Omarchy**: "the 'hermes' command does not work and installation seems to be broken with both the CLI and the desktop."^[raw/inbox/2026-09-15.md] He wants Hermes to fix it **and "take note of things that work for next time."**^[raw/inbox/2026-09-15.md]

This overlaps with the remote-desktop work: the Omarchy runs a desktop OS reached over **Tailscale** (control plane on 443, SSH/22 refused as of 2026-09-14).^[raw/inbox/2026-09-14.md]

Outstanding: get the hermes CLI + desktop working on the Omarchy, and document the working steps (a candidate for a skill).

Related: [[wiki/entities/omarchy|Omarchy]], [[wiki/decisions/remote-desktop-vnc-to-omarchy|remote desktop/VNC to Omarchy]], [[wiki/entities/tailscale|Tailscale]]
