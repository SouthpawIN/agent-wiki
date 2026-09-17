# only-device — wiki index
> One line per page. The wiki row's CONTEXT section renders this file.
> Last updated: 2026-09-16 | Total pages: 8

## Entities
- [[topics/only-device/wiki/entities/duo|The Duo]] — Chris's **Android device**, nicknamed **the Duo**, that he runs as a personal server via **Termux** and **Hermes**.

## Concepts
- [[topics/only-device/wiki/concepts/adb-wireless-debugging|ADB wireless debugging]] — Wireless **ADB** is the intended full-control channel for getting Hermes onto **the Duo** (Android). It trades a quick SSH hop for complete device access — scre
- [[topics/only-device/wiki/concepts/boot-from-file|UEFI boot-from-file — the only-device boot menu]] — A **boot troubleshooting** thread from 2026-09-12 around an **x86 / HP-style machine** (EFI boot paths, not the Android Duo). Chris was trying to get a machine 
- [[topics/only-device/wiki/concepts/mac-no-timeout-command|Mac probe tooling lacks `timeout` — cascading SSH/TLS failures]] — While probing the **Omarchy** box (Tailscale `100.68.42.68`) on **2026-09-14 → 09-15**, Hermes hit the same wall twice: the host **Mac has no `timeout` command*
- [[topics/only-device/wiki/concepts/omarchy-os-control-plane|Omarchy OS control plane (port 443)]] — The **Omarchy OS control plane** is the service that answers on **port 443** on the machine Chris is setting up. Observed on **2026-09-14 20:14** while Hermes w

## Decisions
- [[topics/only-device/wiki/decisions/hermes-duo-access-path|Hermes access path for the Duo — prefer ADB wireless]] — Choose how Hermes gets onto and controls **the Duo**: **Path A = Termux SSH** over `tailscale ssh`, versus **Path B = wireless ADB** pairing. Hermes recommends 
- [[topics/only-device/wiki/decisions/omarchy-no-shell-access-path|Omarchy box access is blocked — no shell, control plane unresponsive]] — On **2026-09-15 09:21** Hermes diagnosed the **Omarchy** machine (Tailscale `100.68.42.68`) and concluded: **"No remote access path exists right now. The SSH se

## Comparisons
- [[topics/only-device/wiki/comparisons/duo-android-vs-omarchy-x86-access|The Duo (Android/ADB) vs the Omarchy box (x86/control-plane) — two device-access stories]] — Two different "only devices" in Chris's setup, and they have opposite access stories: one is onboarding cleanly, the other is currently unreachable.

## Queries


