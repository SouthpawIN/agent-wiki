---
title: hermes-android
updated: 2026-08-27
type: topic
repo: https://github.com/SouthpawIN/hermes-android
status: dormant
tags: [repo]
---

# hermes-android

> Hermes Agent Android builds

**[Open on GitHub](https://github.com/SouthpawIN/hermes-android)** · DORMANT (since 2026-07-14) · last push 2026-07-14

## Facts
- **Language:** Shell
- **Stars / forks:** 3 / 0
- **License:** MIT
- **Fork of:** original work
- **Created:** 2026-06-24 · **Last push:** 2026-07-14
- **Open issues:** 0
- **Status:** DORMANT (since 2026-07-14)

## From the README

# Hermes Android — Senter surface

This repository contains the existing Hermes Android APK/Termux distribution.
The Senter mobile contract is declarative and approval-gated; it does not grant
host access or turn the APK into a second agent.

## Contract artifacts

- `ANDROID_SURFACE.json` — compact/expanded UI, gestures, blocks, permissions.
- `ANDROID_BRIDGE.json` — one-operation, user-approved ADB allowlist.
- `../goop/ANDROID.md` — human-readable product contract.
- `../goop/STS_CONFIG.json` — auxiliary speech boundary.

The bridge is disabled by default. The client may request one bounded operation
only after explicit user approval. Host credentials, Hermes session databases,
unrestricted shell, install/push/pull, forwarding, and raw ADB are forbidden.

## Existing distribution

- APK: `hermes-0.17.0-android-debug.apk` (pre-existing artifact; verify checksum
  before distribution).
- Termux setup: `setup-termux.sh`.

The Android client communicates with a controlled Senter endpoint. Device
permissions remain enforced by Android; the host never receives unrestricted
phone control.

## Verification

From the Agent Wiki root:

```bash
python3 sandbox/goop/validate_android_surface.py sandbox/hermes-android/ANDROID_SURFACE.json
python3 sandbox/goop/validate_android_bridge.py sandbox/hermes-android/ANDROID_BRIDGE.json
sha256sum sandbox/hermes-android/hermes-0.17.0-android-debug.apk
```

A native APK rebuild is not claimed: this checkout contains the prebuilt APK and
no Gradle source tree. For the source-backed Senter interaction prototype, use
`../android-surface/` from the Agent Wiki sandbox.

## Safety

Never pipe an unreviewed remote installer into a live environment. Use a
throwaway Android emulator/device and an isolated Hermes profile for testing.


## Archived
Archived 2026-09-02 — absorbed into [[wiki-topics/hermes-agent/README|hermes-agent]] by merge-topics.py v1.1.0. Nothing here was deleted or rewritten.
