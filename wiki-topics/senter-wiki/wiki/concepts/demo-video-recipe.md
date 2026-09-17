---
title: Demo video recipe (full screen, sidebar included)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [skill, ui, plan]
sources:
  - raw/sources/knowledge/ref-vault-live-demo-video.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
confidence: high
---

# Demo video recipe (validated 2026-09-03)

Chris: *"take a demo video … show off all the animations … music playing so the visualizer goes … lots of bot activity, permissions arriving and getting accepted, scrolling
through topics, stars lighting up … very lively, highly agentic."* Then: *"it needs to show the Hermes sidebar too — the whole thing operates together like a cursor setup."*
Then: *"drag the mouse through a couple of tiles at medium speed (cascade), and show the editor opening."* ^[raw/sources/knowledge/ref-vault-live-demo-video.md]

## Principle
Drive the REAL pipeline ([[wiki-topics/senter-wiki/wiki/concepts/ui-performs-the-fleet|UI performs the fleet]]): expose `window.__senterHandle=(e)=>handle(e)` inside the events IIFE and feed
scripted events (msg every 2 ticks, tool every 3, skill every 4, approval every 7 with decided 2–5 s later; tick 650 ms), `hpEq.demo(sec)`, a drawn SVG cursor sweep adding
`.demoHover` (must replicate the hover CSS — `:hover` can't be forced), `scrollTour`, `openEditor/closeEditor`, SPACE round-trip. Trigger = fixed `<button id="demoGo">`
(URL flags stripped by the pane). ^[raw/sources/knowledge/ref-vault-live-demo-video.md]

## Recording
`screencapture -v -V 52 -x ~/Desktop/senter-demo.mov &` → `drive_preview click #demoGo` → stay silent so the sidebar shows steady state → `mdls -name kMDItemDurationSeconds`.
Full-screen = sidebar left + pane right. No ffmpeg on this Mac; the .mov (3024×1964, ~200 MB/50 s) is the deliverable. Record AFTER the visual state is approved (a demo before
the usage-chart fix had to be redone). Everything tagged `TEMP-DEMO` and stripped; at the MVP checkpoint the demo buttons and hook were removed (re-addable). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

Related: [[wiki-topics/senter-wiki/wiki/entities/headphone-eq|EQ]].
