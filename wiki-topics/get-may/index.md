---
title: get-may
created: 2026-09-17
updated: 2026-09-17
type: wiki
sources:
  - index.md
  - wiki/
  - raw/inbox/
  - .system/
---

# get-may

Last updated: 2026-09-16 | Total pages: 15

---

## INTEGRATIONS

This wiki is fed by:

- **Raw inbox:** `raw/inbox/` — daily cuts from Hermes sessions
- **Sessions:** `.system/sessions/` — full conversation transcripts
- **Wiki pages:** `wiki/` — structured knowledge base

---

## README

### Entities

- [Armored Core 6](wiki/armored-core-6.md) — **Armored Core 6** is a game Chris is playing on his **Omarchy** and the reason he wants to stream.^[raw/inbox/2026-09-14.md] He wants to play on the Omarchy bu
- [Balena Etcher](wiki/balena-etcher.md) — Chris referred to Balena Etcher as "Bellina etcher" and later "blina etcher" in transcript dictation.^[raw/inbox/2026-09-12.md] He used it to write the Omarchy
- [macOS sudo password](wiki/macbook-sudo-password.md) — Chris's new MacBook has a forgotten sudo/login password that was set once during initial setup and never written down.^[raw/inbox/2026-09-12.md] He called it th
- [OBS Studio](wiki/obs-studio.md) — **OBS** (OBS Studio) is the streaming software Chris wants **installed on his MacBook**.^[raw/inbox/2026-09-14.md] He wants the MacBook — not the Omarchy — to r
- [Omarchy](wiki/omarchy.md) — **Omarchy** is Chris's custom arch-based Linux device (dictated variously as "Omarchy", "Omar"/"Omar key", and "obarcus").^[raw/inbox/2026-09-13.md]^[raw/inbox/
- [Tailscale](wiki/tailscale.md) — **Tailscale** is the private overlay network Chris uses to reach his fleet of devices from his MacBook — the **Omarchy**, the **HP** (flashed with the Omarchy i

### Concepts

- [Apple sudo recovery](wiki/apple-sudo-recovery.md) — The established recovery path for Chris's forgotten sudo password is Apple Silicon Recovery Mode: shut down, hold the power button until "Loading startup option
- [Centralized storage reorganization](wiki/centralized-storage.md) — Chris plans to use the **Omarchy's 16 TB** as a **central storage hub** to "free up my phone and my Google drives and my other devices as well."^[raw/inbox/2026
- [Streaming setup (MacBook-managed)](wiki/streaming-setup.md) — The streaming setup Chris wants is to **run the game on the Omarchy but manage the broadcast from his MacBook**.^[raw/inbox/2026-09-14.md] His rationale: the Ma

### Decisions

- [Install OBS on the MacBook](wiki/install-obs-on-macbook.md) — What: Install **OBS** on Chris's **MacBook** so it captures and manages the stream.
- [Remote desktop / VNC into Omarchy](wiki/remote-desktop-vnc-to-omarchy.md) — What: Establish a **remote desktop** into the **Omarchy** from the MacBook, using **VNC or similar**, over **Tailscale**.
- [Use Balena Etcher instead of sudo dd](wiki/use-balena-etcher-over-sudo-dd.md) — What: Flash the Omarchy 4.0.3 ISO with Balena Etcher rather than `sudo dd` from terminal.

### Queries

- [hermes install broken on Omarchy (09-15)](wiki/hermes-install-broken-on-omarchy-2026-09-15.md) — On 2026-09-15 Chris escalated the hermes-on-Omarchy problem: "Something broke with my hermes install on my omarchy, the 'hermes' command doers not work and inst
- [hermes install broken on Omarchy](wiki/hermes-install-broken-on-omarchy.md) — Something broke Chris's **hermes install on the Omarchy**: "the 'hermes' command does not work and installation seems to be broken with both the CLI and the des
- [Tailscale HP and Duo access](wiki/tailscale-hp-duo-access.md) — Chris asked Hermes to verify whether the HP device flashed with Omarchy was visible over Tailscale: "Let me know if you see it."^[raw/inbox/2026-09-13.md] He al

---

## SKILLS

No topic skills yet.

---

## BOTS

Proposed bots:

- **[storage-organizer](agents/storage-organizer.md.proposed) — **I see you're about to do that big reorganization onto your Omarchy's 16 TB — want a bot that catalogs what's on your phone, Google drives and other 
- **[streaming-pilot](agents/streaming-pilot.md.proposed) — **I see you're building the Omarchy→MacBook streaming setup for Armored Core 6 — want a bot that keeps the VNC/OBS troubleshooting notes as Hermes wor


---

## LOOPS

No loops yet.