---
title: Remote desktop / VNC into Omarchy
created: 2026-09-15
updated: 2026-09-15
type: decision
tags: [decision, plan]
sources: [raw/inbox/2026-09-14.md, raw/inbox/2026-09-15.md]
confidence: high
---
What: Establish a **remote desktop** into the **Omarchy** from the MacBook, using **VNC or similar**, over **Tailscale**.

Why: So Chris can play games (e.g. Armored Core 6) on the Omarchy while controlling/monitoring the stream from the MacBook.^[raw/inbox/2026-09-14.md] He said he "likes any kind of remote computer options, like a VNC or something like that into [the] Omarchy from my MacBook."^[raw/inbox/2026-09-15.md]

When: 2026-09-14–15. Hermes was testing reachability; as of 2026-09-14 the Omarchy tail IP (100.68.42.68) exposed only the OS control plane on 443 and refused SSH/22, so no desktop service was reachable yet.^[raw/inbox/2026-09-14.md] As of 2026-09-15 Hermes had installed **wayvnc** on the Omarchy and was setting it up as a **systemd user service** to provide the desktop/VNC endpoint.^[raw/inbox/2026-09-15.md] On 2026-09-15 at 18:16 Hermes reported the service was **not starting the wayvnc model/server**, so he was fixing the systemd user service so the model actually starts.^[raw/inbox/2026-09-15.md] He said he "likes any kind of remote computer options, like a VNC or something like that into [the] Omarchy from my MacBook."^[raw/inbox/2026-09-15.md]

Related: [[wiki/entities/tailscale|Tailscale]], [[wiki/decisions/install-obs-on-macbook|install OBS on MacBook]], [[wiki/queries/hermes-install-broken-on-omarchy|hermes install broken on Omarchy]]
