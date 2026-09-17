---
title: only-device
created: 2026-09-17
updated: 2026-09-17
type: wiki
sources:
  - index.md
  - wiki/
  - raw/inbox/
  - .system/
---

# only-device

Last updated: 2026-09-16 | Total pages: 8

---

## INTEGRATIONS

This wiki is fed by:

- **Raw inbox:** `raw/inbox/` — daily cuts from Hermes sessions
- **Sessions:** `.system/sessions/` — full conversation transcripts
- **Wiki pages:** `wiki/` — structured knowledge base

---

## README

### Entities

- [The Duo](wiki/duo.md) — Chris's **Android device**, nicknamed **the Duo**, that he runs as a personal server via **Termux** and **Hermes**.

### Concepts

- [ADB wireless debugging](wiki/adb-wireless-debugging.md) — Wireless **ADB** is the intended full-control channel for getting Hermes onto **the Duo** (Android). It trades a quick SSH hop for complete device access — scre
- [UEFI boot-from-file — the only-device boot menu](wiki/boot-from-file.md) — A **boot troubleshooting** thread from 2026-09-12 around an **x86 / HP-style machine** (EFI boot paths, not the Android Duo). Chris was trying to get a machine
- [Mac probe tooling lacks `timeout` — cascading SSH/TLS failures](wiki/mac-no-timeout-command.md) — While probing the **Omarchy** box (Tailscale `100.68.42.68`) on **2026-09-14 → 09-15**, Hermes hit the same wall twice: the host **Mac has no `timeout` command*
- [Omarchy OS control plane (port 443)](wiki/omarchy-os-control-plane.md) — The **Omarchy OS control plane** is the service that answers on **port 443** on the machine Chris is setting up. Observed on **2026-09-14 20:14** while Hermes w

### Decisions

- [Hermes access path for the Duo — prefer ADB wireless](wiki/hermes-duo-access-path.md) — Choose how Hermes gets onto and controls **the Duo**: **Path A = Termux SSH** over `tailscale ssh`, versus **Path B = wireless ADB** pairing. Hermes recommends
- [Omarchy box access is blocked — no shell, control plane unresponsive](wiki/omarchy-no-shell-access-path.md) — On **2026-09-15 09:21** Hermes diagnosed the **Omarchy** machine (Tailscale `100.68.42.68`) and concluded: **"No remote access path exists right now. The SSH se

### Comparisons

- [The Duo (Android/ADB) vs the Omarchy box (x86/control-plane) — two device-access stories](wiki/duo-android-vs-omarchy-x86-access.md) — Two different "only devices" in Chris's setup, and they have opposite access stories: one is onboarding cleanly, the other is currently unreachable.

---

## SKILLS

No topic skills yet.

---

## BOTS

Proposed bots:

- **[omarchy-control-plane-dig](agents/omarchy-control-plane-dig.md.proposed) — **Want me to look into what Omarchy's OS control plane on port 443 actually exposes (boot/flash/telemetry API) so there's a second way in if SSH never
- **[omarchy-watch](agents/omarchy-watch.md.proposed) — **I see you're still locked out of the Omarchy box — want a bot that watches port 22 (and 443) and pings you the instant SSH comes back so I can drive


---

## LOOPS

No loops yet.