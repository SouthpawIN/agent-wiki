---
title: "Omarchy box access is blocked — no shell, control plane unresponsive"
created: 2026-09-15
updated: 2026-09-16
type: decision
tags: [decision, pain, infra, timeline]
sources: [raw/inbox/2026-09-14.md, raw/inbox/2026-09-15.md]
confidence: high
contested: false
---

# Omarchy box access is blocked — no shell, control plane unresponsive

## What
On **2026-09-15 09:21** Hermes diagnosed the **Omarchy** machine (Tailscale `100.68.42.68`) and concluded: **"No remote access path exists right now. The SSH server is down and the web control plane is unresponsive."** ^[raw/2026-09-15.md] There is no working shell-in path to this box yet.

## Evidence (2026-09-14 → 09-15)
- 2026-09-14 20:38: SSH on `100.68.42.68:22` with `~/.ssh/id_ed25519` (root@) → **`timeout: command not found`**; retry without timeout → **`ssh: connect to host 100.68.42.68 port 22: Connection refused`**. Port scan (22, 222, 3389, 5900, 5901, 8080, 8000, 3000, 80, 443, 6080) → **only 443 OPEN**. ^[raw/2026-09-14.md]
- 2026-09-14 22:22: 443 reachable via TCP but **TLS handshake hangs** (Mac has no `timeout`; earlier `s_client` produced no cert). ^[raw/2026-09-14.md]
- 2026-09-15 09:19: "**Port 22 is closed on Omarchy — SSH isn't running.** Only 443 is open (Omarchy's web control plane). I can't get a shell from here." ^[raw/2026-09-15.md]
- 2026-09-15 09:21: full status — Tailscale ✅ (`pong from omarchy in 6ms`); SSH ❌ connection refused; 443 ❌ open but TLS/HTTP fails; all other ports closed. Bottom line: no remote access path. ^[raw/2026-09-15.md]

## What Chris did
- 2026-09-15 09:24: "**Okay, I successfully sent those two commands on my Omarchy**" — meaning Chris reached the box by some local/physical path and ran two commands (likely to start SSH), but Hermes still reported no shell afterward. ^[raw/2026-09-15.md]
- 2026-09-15 10:08: Hermes switched approach — run **as root directly through `tailscale ssh`** and use Python to manage the process, because shell quoting was creating orphans. ^[raw/2026-09-15.md]

## Why it matters
The x86-style Omarchy box has a different access story than the Android Duo: SSH is the normal channel and it is **refused**; the 443 control plane (see [[topics/only-device/wiki/concepts/omarchy-os-control-plane|Omarchy OS control plane]]) answers TCP but not TLS/HTTP. Until SSH is up (or the control plane responds), Hermes cannot drive the box. ^[raw/2026-09-15.md]

## Status
As of 2026-09-15 13:22 Hermes was "**Waiting for next steps**." ^[raw/2026-09-15.md] The decision is provisional: SSH must be started on the box (or the control plane made to respond) before any remote control is possible. As of that last line Hermes had not yet re-established a shell — the box remains unreachable remotely.

## Heartbeat (2026-09-16)
Re-compiled `raw/2026-09-14.md` + `raw/2026-09-15.md`; all content already captured here and in [[topics/only-device/wiki/concepts/mac-no-timeout-command|Mac lacks `timeout`]], [[topics/only-device/wiki/concepts/omarchy-os-control-plane|Omarchy OS control plane]], and [[topics/only-device/wiki/comparisons/duo-android-vs-omarchy-x86-access|Duo vs Omarchy access]]. Box still waiting for SSH (port 22) to come up — no new development since 09-15 13:22.

See also: [[topics/only-device/wiki/concepts/omarchy-os-control-plane|Omarchy OS control plane]] · [[topics/only-device/wiki/concepts/mac-no-timeout-command|Mac lacks `timeout`]] · [[topics/only-device/wiki/entities/duo|The Duo]] · [[topics/only-device/wiki/decisions/hermes-duo-access-path|Hermes access path decision]]
