---
title: "Hermes access path for the Duo — prefer ADB wireless"
created: 2026-09-13
updated: 2026-09-13
type: decision
tags: [decision, tool, plan]
sources: [raw/inbox/2026-09-13.md]
confidence: high
contested: false
---

# Hermes access path for the Duo — prefer ADB wireless (Path B)

## What
Choose how Hermes gets onto and controls **the Duo**: **Path A = Termux SSH** over `tailscale ssh`, versus **Path B = wireless ADB** pairing. Hermes recommends **Path B**.

## Why
Path A is "fastest" but only gives a shell. Path B "lets me control the screen, install apps, run commands, everything" — so it's the better **long-term** setup even though pairing takes a couple of steps. ^[raw/2026-09-13.md]

## When
Decided implicitly on **2026-09-13**, while re-establishing Hermes after Chris reinstalled Termux. The immediate next action is Chris reading off the ADB **IP:port + 6-digit pairing code**. ^[raw/2026-09-13.md]

## Trade-off
Path A wins on speed-to-first-command; Path B wins on control surface. Chris gets shell now via Path A if needed and pairs for Path B as the standing channel.

See also: [[wiki-topics/only-device/wiki/entities/duo|The Duo]] · [[wiki-topics/only-device/wiki/concepts/adb-wireless-debugging|ADB wireless debugging]]
