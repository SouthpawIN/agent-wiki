---
title: "Omarchy OS control plane (port 443)"
created: 2026-09-14
updated: 2026-09-14
type: concept
tags: [tool, pain, infra]
sources: [raw/inbox/2026-09-14.md, raw/inbox/2026-09-15.md]
confidence: high
---

# Omarchy OS control plane (port 443)

The **Omarchy OS control plane** is the service that answers on **port 443** on the machine Chris is setting up. Observed on **2026-09-14 20:14** while Hermes was probing the box.

## What it is
On 2026-09-14 the only open port the probe found was **443**, and Hermes identified it as the **Omarchy OS control plane — not SSH**. ^[raw/2026-09-14.md] So the machine speaks an out-of-band management plane over HTTPS rather than the SSH that Hermes normally reaches. This shapes how Hermes can drive the box: not the usual shell-in over SSH, but whatever the control plane exposes on 443. ^[raw/2026-09-14.md]

## What Hermes did next
Hermes said it would "**probe it**" — i.e. interrogate the control-plane API on 443 to learn how to talk to the OS. ^[raw/2026-09-14.md]
On **2026-09-15 09:21** the probe concluded the control plane is **open but not responding** — TCP connects but the TLS handshake fails and there is no HTTP response. Combined with SSH being refused, Hermes reported no usable access path at all. ^[raw/2026-09-15.md]

## Why it matters
- Changes the access story: the [[topics/only-device/wiki/entities/duo|Duo]] uses ADB/SSH, but this x86-style box may live behind a control-plane handshake instead. ^[raw/2026-09-14.md]
- Ties to the same boot/EFI troubleshooting thread — a machine that won't boot its USB normally ([[(topics/only-device/wiki/concepts/boot-from-file|UEFI boot-from-file)]]]) but still serves a control plane on 443.

## Open question
What the control plane actually offers (OS telemetry? flash/boot control?) is unknown; as of 2026-09-15 it answers TCP but not TLS/HTTP, so it offers nothing usable yet. ^[raw/2026-09-15.md]

See also: [[topics/only-device/wiki/concepts/boot-from-file|UEFI boot-from-file]] · [[topics/only-device/wiki/concepts/adb-wireless-debugging|ADB wireless debugging]] · [[topics/only-device/wiki/concepts/mac-no-timeout-command|Mac lacks `timeout`]]
