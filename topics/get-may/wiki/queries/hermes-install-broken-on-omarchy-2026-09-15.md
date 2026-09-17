---
title: hermes install broken on Omarchy (09-15)
created: 2026-09-15
updated: 2026-09-15
type: query
tags: [question, pain, infra]
sources: [raw/inbox/2026-09-15.md]
confidence: high
---
On 2026-09-15 Chris escalated the hermes-on-Omarchy problem: "Something broke with my hermes install on my omarchy, the 'hermes' command doers not work and installation seems to be broken with both the CLI and the desktop."^[raw/inbox/2026-09-15.md] He asked Hermes to get in via **Tailscale** (same sudo password as the MacBook) and to **"take note of things that work for next time."**^[raw/inbox/2026-09-15.md]

This is the same broken install flagged on 2026-09-15 earlier (see [[wiki/queries/hermes-install-broken-on-omarchy|hermes install broken on Omarchy]]): it predates the current streaming setup and affects both the `hermes` CLI and the desktop. As of 2026-09-15 Hermes was already working on the Omarchy — installing **wayvnc** and setting it up as a systemd user service — so access was being established at the same time.

A likely root cause surfaced 2026-09-13: his "Turmix" (likely T Remix) OS "was messed up," so he reinstalled Turmix and was reinstalling Hermes.^[raw/inbox/2026-09-13.md]

Outstanding: restore the hermes CLI + desktop on the Omarchy, and document the working steps as a skill so it survives the next break.

Related: [[wiki/entities/omarchy|Omarchy]], [[wiki/entities/tailscale|Tailscale]], [[wiki/decisions/remote-desktop-vnc-to-omarchy|remote desktop/VNC to Omarchy]]
