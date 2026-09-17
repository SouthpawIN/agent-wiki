---
title: "TurboFit options missing after restarting the desktop app"
created: 2026-09-15
updated: 2026-09-15
type: entity
tags:
  - ui
  - pain
  - infra
  - tool
sources:
  - raw/inbox/2026-09-15.md
confidence: high
---

# TurboFit options missing after restarting the desktop app

## The observation

On 2026-09-15 Chris restarted the Hermes desktop app on the MacBook and found the **TurboFit** options gone — they did not come back after the restart. ^[raw/inbox/2026-09-15.md]

> "Okay, so I just restarted this desktop app on the MacBook and I don't see those turbo-fit options" ^[raw/inbox/2026-09-15.md]

This is a UI regression on his own hardware: the TurboFit controls that were present before the restart are absent after it. It lands squarely in back-where's scope — Chris's runtime/UI issue on local M1 hardware — rather than generic wiki-UI work (weaver) or upstream Hermes code (teknium PR ledger). ^[raw/inbox/2026-09-15.md]

## Context: an interrupted turn

The restart observation came right after a system note that Chris's previous turn had been interrupted mid-run — the app or its backend stopped before the turn finished, and he was told to check current state before redoing anything. ^[raw/inbox/2026-09-15.md] A second interruption note followed at 18:12, this time flagging that a background process (`proc_53905ab10dea`) matched the watch pattern "mesh". ^[raw/inbox/2026-09-15.md] So the missing TurboFit options appeared inside a session that was itself being interrupted, not in a clean fresh start.

## Relation to the double-GPU model work

The TurboFit concern sits in the same session as the [[topics/back-where/wiki/entities/q3k-xl-double-gpu-gaming-choice|Q3K XL / Unleashed double-GPU choice]] — the desktop app Chris restarted is the one carrying his TurboFit-tuned models. The prior session's 13:21 report ("Both models verified working through Hermes") did not survive into this post-restart turn, where the TurboFit surface itself was already missing. ^[raw/inbox/2026-09-15.md]

## Status

Open as of 2026-09-15 18:12. The TurboFit options had not returned after the desktop-app restart, and the turn was still interrupted (background process matching "mesh" still active). No recovery action recorded. ^[raw/inbox/2026-09-15.md]

## Related

- [[topics/back-where/wiki/entities/q3k-xl-double-gpu-gaming-choice|Q3K XL / Unleashed double-GPU choice]]
- [[topics/back-where/wiki/concepts/ui-layout-regression|UI layout regression after diff view change]]
- [[topics/back-where/wiki/concepts/end-to-end-verification|End-to-end verification before declaring done]]
