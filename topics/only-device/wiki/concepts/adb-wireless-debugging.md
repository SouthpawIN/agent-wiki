---
title: "ADB wireless debugging"
created: 2026-09-13
updated: 2026-09-13
type: concept
tags: [tool, plan]
sources: [raw/inbox/2026-09-13.md]
confidence: high
---

# ADB wireless debugging

Wireless **ADB** is the intended full-control channel for getting Hermes onto **the Duo** (Android). It trades a quick SSH hop for complete device access — screen, app installs, arbitrary commands.

## The pairing flow (Path B)
The steps Hermes gave Chris on 2026-09-13:

1. Enable **Developer Options** on the Duo — tap **Build Number 7 times**. ^[raw/2026-09-13.md]
2. Enable **"Wireless debugging"** inside Developer Options. ^[raw/2026-09-13.md]
3. Tap **"Pair device with pairing code"** — it displays an **IP:port** and a **6-digit pairing code**. ^[raw/2026-09-13.md]
4. Give Hermes the **IP:port** and **code**; it pairs and "takes over completely — no more asking, no more options." ^[raw/2026-09-13.md]

## Why Path B over Path A
Path A (**Termux SSH over `tailscale ssh`**) is faster to start but gives a shell only. Path B "lets me control the screen, install apps, run commands, everything" — so Hermes steered Chris toward pairing for the fuller control. This is the [[topics/only-device/wiki/decisions/hermes-duo-access-path|access-path decision]].

## Caveat
Pairing codes are short-lived; Chris was asked to re-read them ("Tap **'Pair device with pairing code'**, read me the **new** IP:port and 6-digit code") — if the session drifts, re-pair rather than reuse an old code. ^[raw/2026-09-13.md]

See also: [[topics/only-device/wiki/entities/duo|The Duo]] · [[topics/only-device/wiki/decisions/hermes-duo-access-path|Hermes access path decision]]
