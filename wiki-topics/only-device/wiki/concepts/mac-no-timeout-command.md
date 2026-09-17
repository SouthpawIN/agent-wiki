---
title: "Mac probe tooling lacks `timeout` — cascading SSH/TLS failures"
created: 2026-09-15
updated: 2026-09-15
type: concept
tags: [infra, pain]
sources: [raw/inbox/2026-09-14.md, raw/inbox/2026-09-15.md]
confidence: high
---

# Mac probe tooling lacks `timeout` — cascading SSH/TLS failures

While probing the **Omarchy** box (Tailscale `100.68.42.68`) on **2026-09-14 → 09-15**, Hermes hit the same wall twice: the host **Mac has no `timeout` command**, and that single gap cascaded into two separate access failures. ^[raw/2026-09-14.md]

## What happened
- **SSH probe (2026-09-14 20:38):** first attempt with `timeout` → `timeout: command not found`; retry *without* timeout → `ssh: connect to host 100.68.42.68 port 22: Connection refused`. ^[raw/2026-09-14.md]
- **TLS probe (2026-09-14 22:22):** port 443 reachable via TCP but "**the TLS handshake is hanging (Mac has no `timeout`, and earlier `s_client` produced no cert)**." ^[raw/2026-09-14.md]

## Why it matters
The box's SSH server was refused regardless (it wasn't running), but the **missing `timeout` made the 443 probe hang instead of failing fast**, wasting cycles and leaving the control plane unprobed. It's a tooling gap in Hermes's own shell environment, not a property of the target box. ^[raw/2026-09-14.md]

## Lesson for future passes
When probing a remote box from this Mac, **use Python socket connection timeouts instead of the shell `timeout` command** — `timeout` is not installed, so any probe that relies on it will hang or error. ^[raw/2026-09-14.md]

See also: [[wiki-topics/only-device/wiki/decisions/omarchy-no-shell-access-path|Omarchy box access is blocked]] · [[wiki-topics/only-device/wiki/concepts/omarchy-os-control-plane|Omarchy OS control plane]]
