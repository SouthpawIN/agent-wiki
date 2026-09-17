---
title: Tailscale network
created: 2026-09-15
updated: 2026-09-15
type: concept
tags: [infra, tool, timeline]
sources: ["raw/inbox/2026-09-13.md", "raw/inbox/2026-09-14.md"]
confidence: high
---

# Tailscale network

Chris's devices are joined on one Tailscale tailnet, reachable by their 100.x addresses. Tailscale is the connective tissue for both Steam streaming and cross-device model access.^[raw/inbox/2026-09-13.md]

## Device inventory (as of 2026-09-13 14:56)
| Device | Tailscale name | IP | Status |
|--------|---------------|-----|--------|
| MacBook | christophers-macbook-pro | 100.81.37.77 | online |
| Surface Duo 2 | surface-duo-2 | 100.79.15.54 | online |
| HP workstation | omarchy | 100.68.42.68 | online |
| (other) | chriss-s10 | 100.93.96.90 | offline 165d |

^[raw/inbox/2026-09-13.md]

## Notes
- Omarchy re-probed live 2026-09-14 20:13 at 100.68.42.68.^[raw/inbox/2026-09-14.md]
- Steam Link auto-discovery (mDNS/broadcast) does **not** cross Tailscale subnets, so hosts must be added by Tailscale IP. See [[topics-wiki/tailscale-steam/wiki/queries/steam-link-discovery|Steam Link discovery query]].
- Tailscale SSH needs a one-time auth check in the browser (login.tailscale.com). See [[topics-wiki/tailscale-steam/wiki/concepts/tailscale-remote-access|Tailscale remote access]].

Related: [[topics-wiki/tailscale-steam/wiki/entities/omarchy|Omarchy]], [[topics-wiki/tailscale-steam/wiki/entities/macbook|MacBook]].
