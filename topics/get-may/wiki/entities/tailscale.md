---
title: Tailscale
created: 2026-09-13
updated: 2026-09-15
type: entity
tags: [tool, infra]
sources: [raw/inbox/2026-09-13.md, raw/inbox/2026-09-14.md, raw/inbox/2026-09-15.md]
confidence: high
---
**Tailscale** is the private overlay network Chris uses to reach his fleet of devices from his MacBook — the **Omarchy**, the **HP** (flashed with the Omarchy image), and a **Surface Duo 2**.^[raw/inbox/2026-09-13.md] He repeatedly asks Hermes to verify visibility over it ("Let me know if you see it") and to use it as the transport for remote access.^[raw/inbox/2026-09-13.md]^[raw/inbox/2026-09-15.md]

Access model: devices share Chris's **same sudo password**, so a working sudo on one machine (e.g. the MacBook) is expected to authenticate on the others over the tailnet.^[raw/inbox/2026-09-14.md] As of 2026-09-14 the Omarchy's tail IP (**100.68.42.68**) exposed port **443** as the OS control plane and **port 22 (SSH) was refused**, so no desktop service was reachable yet.^[raw/inbox/2026-09-14.md] The **Surface Duo 2** was noted reachable once the password matter was resolved.^[raw/inbox/2026-09-13.md]

Related: [[wiki/entities/omarchy|Omarchy]], [[wiki/entities/macbook-sudo-password|macOS sudo password]], [[wiki/queries/tailscale-hp-duo-access|Tailscale HP and Duo access]]
