---
title: "Omarchy host address (100.68.42.68)"
created: 2026-09-15
updated: 2026-09-15
type: query
tags: [tool, infra, plan]
sources: [raw/inbox/2026-09-15.md]
confidence: medium
---

# Omarchy host address (100.68.42.68)

A single-line observation from 2026-09-15 about where the Omarchy machine actually lives.

^[raw/inbox/2026-09-15.md] At 02:17 Hermes reported: **"Found that `omarchy` is the Linux box (100.68.42.68). Let me try that, plus read the musician's guide and constants in parallel."**

The `100.68.42.68` address sits in the 100.64.0.0/10 CGNAT range — the signature of a WireGuard/Tailscale exit node, not a LAN address. So the Omarchy box that Chris was building a bootable USB for (see [[topics-wiki/object-important/wiki/concepts/omarchy-iso-bootable-usb|Omarchy 4.0.3 bootable-USB write]]) is reached over the tailnet, and Hermes was about to connect to it at that address.

The follow-up ("let me try that, plus read the musician's guide and constants") is truncated in the raw — it is unclear whether the connection succeeded or what the musician's guide is for.

Related:
- [[topics-wiki/object-important/wiki/concepts/omarchy-iso-bootable-usb|Omarchy 4.0.3 bootable-USB write]] — the ISO written to `/dev/rdisk4` on 2026-09-12.
- [[topics-wiki/object-important/wiki/concepts/ornith-routing-config|Ornith 1.5 routing config (8091)]] — Hermes's own local model endpoint, the other host Chris was reconfiguring that week.
