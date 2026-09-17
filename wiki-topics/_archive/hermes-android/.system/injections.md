# Injections

## [READ]

== absorbed from senter idea-wiki (2026-08-28) ==
---
title: hermes-android
created: 2026-07-12
updated: 2026-07-12
type: entity
tags: [entity, idea-capture, provenance]
sources: ["raw/github/hermes-android-3e66c8ac66.md"]
confidence: medium
---

# hermes-android

## Current context

Hermes Agent Android builds # Hermes Android Hermes Agent on Android — APK builds + Termux setup scripts. ## Quick Install ### Option 1: APK (recommended) Download and install the latest APK: **[⬇️ Download hermes-0.17.0-android-debug.apk](https://github.com/SouthpawIN/hermes-android/raw/main/hermes-0.17.0-android-debug.apk)** You'll need to enable "Install from unknown sources" in your phone's settings. ### Option 2: Termux (full agent control) 1. Install [Termux](https://f-droid.org/en/packages/com.termux/) from F-Droid 2. Run: This gives you: SSH access, ADB daemon, Hermes CLI, and the gateway running on your phone. ## What you get | Method | Chat | Gateway | Agent Tools | SSH | |--------|------|---------|-------------|-----| | **APK** | ✅ React UI | Connects to remote | Via gateway | ❌ | | **Termux** | ✅ CLI | ✅ Full | ✅ Full | ✅ | ## Architecture The APK is the Hermes Desktop React renderer (Vite + React + Tailwind) wrapped in Capacitor for Android. It connects to a Hermes gateway via WebSocket — either on your local machine, or running in Termux on the same phone. ## Connecting to your gateway On first launch, the app needs to know where your Hermes gateway is running: - **Same WiFi**: `http://192.168.x.x:8642` - **Tailscale**: `http://100.x.x.x:8642` - **Termux on same phone**: `http://localhost:8642` ## Building from source APK output: `android/app/build/outputs/apk/debug/app-debug.apk` ## TOWARDS SELF-IMPROVEMENT

## Version policy

The latest available update marker is canonical: `https://github.com/SouthpawIN/hermes-android` (`2026-07-08T20:37:16Z`). Earlier captures remain linked in the raw source inventory.

## Related concepts

- [[concepts/agent-fleet|Agent Fleet]]
- [[concepts/local-inference|Local Inference]]
