---
title: "The Duo (Android/ADB) vs the Omarchy box (x86/control-plane) — two device-access stories"
created: 2026-09-16
updated: 2026-09-16
type: comparison
tags: [tool, infra, decision, pain]
sources: [raw/inbox/2026-09-13.md, raw/inbox/2026-09-14.md, raw/inbox/2026-09-15.md]
confidence: high
---

# The Duo (Android/ADB) vs the Omarchy box (x86/control-plane)

Two different "only devices" in Chris's setup, and they have opposite access stories: one is onboarding cleanly, the other is currently unreachable.

| | The Duo (Android) | Omarchy box (x86) |
|---|---|---|
| What | Android device running Termux + Hermes | x86 / HP-style machine |
| Tailscale | reachable | reachable (`pong from omarchy in 6ms`) |
| Normal channel | ADB wireless pairing (Path B) / Termux SSH (Path A) | SSH (port 22) |
| SSH status | being paired up (2026-09-13) | **refused** — server not running |
| Other open port | — | **443** — OS control plane, open but TLS/HTTP unresponsive |
| Access verdict | onboarding in progress | **no remote access path** (2026-09-15) |

## Why they differ
The Duo is Android, so Hermes's standing choice is **wireless ADB** — "lets me control the screen, install apps, run commands, everything" — with Termux SSH as the fast fallback. ^[raw/2026-09-13.md] The Omarchy box is x86, where SSH is the normal channel — and on 2026-09-14 → 09-15 that channel was **refused** (server down) while the only open port, **443**, is the OS control plane that answers TCP but not TLS/HTTP. ^[raw/2026-09-14.md] ^[raw/2026-09-15.md]

## What it means
- The Duo is the device Hermes is actively bringing online; the Omarchy box is the one currently locked out.
- Getting Hermes onto the Omarchy box needs either SSH (port 22) to come up — Chris said he started it locally on 2026-09-15 09:24 ("I successfully sent those two commands on my Omarchy") — or the 443 control plane to start responding. ^[raw/2026-09-15.md]
- Both share the same Mac-side tooling gap: no shell `timeout`, so probes hang instead of failing fast. ^[raw/2026-09-14.md]

See also: [[topics/only-device/wiki/entities/duo|The Duo]] · [[topics/only-device/wiki/decisions/hermes-duo-access-path|Duo access-path decision]] · [[topics/only-device/wiki/decisions/omarchy-no-shell-access-path|Omarchy box access blocked]] · [[topics/only-device/wiki/concepts/omarchy-os-control-plane|Omarchy OS control plane]] · [[topics/only-device/wiki/concepts/adb-wireless-debugging|ADB wireless debugging]]
