---
title: "The Duo"
created: 2026-09-13
updated: 2026-09-13
type: entity
tags: [tool, plan]
sources: [raw/inbox/2026-09-13.md]
confidence: high
---

# The Duo

Chris's **Android device**, nicknamed **the Duo**, that he runs as a personal server via **Termux** and **Hermes**.

## What it is
The Duo is an Android device that Chris is setting up to run Hermes. As of 2026-09-13 he had "**just reinstalled Termux and are reinstalling Hermes**" on it, so the device was sitting idle waiting for Hermes to be brought back up — and Chris had to re-establish the connection from scratch. [[wiki-topics/only-device/wiki/concepts/adb-wireless-debugging|ADB wireless debugging]] is the long-term control channel; [[wiki-topics/only-device/wiki/decisions/hermes-duo-access-path|the access-path decision]] locks in which path.

## Why it matters
Chris wants full control of the box — screen, apps, shell. Hermes framed the two ways in and called the wireless path the better long-term investment.

## Status
Hermes was mid-onboarding on 2026-09-13, waiting for Chris to read off a **pairing IP:port + 6-digit code** so it can pair via ADB and "take over completely." ^[raw/2026-09-13.md]

See also: [[wiki-topics/only-device/wiki/concepts/adb-wireless-debugging|ADB wireless debugging]] · [[wiki-topics/only-device/wiki/decisions/hermes-duo-access-path|Hermes access path decision]]
