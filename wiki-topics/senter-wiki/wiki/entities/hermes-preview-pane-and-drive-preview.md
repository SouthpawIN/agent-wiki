---
title: Hermes desktop preview pane + drive_preview
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [tool, infra, ui]
sources:
  - raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
  - raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md
confidence: high
---

# The preview pane IS the UI

[[wiki-topics/senter-wiki/wiki/entities/vault-live-html|vault-live.html]] renders inside the Hermes desktop app's preview pane, beside the chat sidebar — the "Cursor setup". Chris
(2026-09-03): *"no try again … you need to practice your computer use, not work around."* Driving the pane by selector is driving the real thing he is looking at. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## The trap
The wiki lives inside the Hermes app the agent runs in. `computer_use` / `cua-driver` keys to pid Hermes land in the chat composer; **Escape = Stop agent** —
the assistant cancelled its own run four times (exit 130). Background `cua-driver call click x,y` routes via AX and never fires page handlers. Window `4956` is the real
Hermes body (1512×949); `4988` is a 32-pt strip. Retina crop coordinates from vision must be halved for pt. ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md]

## Selector map (passed end-to-end 2026-09-03)
| Intent | Call |
|---|---|
| start header search | `drive_preview click selector=#heroGap` |
| type + Enter | `drive_preview type selector=#senterHiddenInput text=discord submit=true` |
| re-cut by kind | `drive_preview click selector='#heroOrbs .orb[data-k="skills"]'` (`ctx`/`agents`/`loops`) |
| open a ranked item | `… selector='#wiki-list .topic[data-bot="anser"] .thead .tname'` |
| clear | `drive_preview click selector=#rankOff` |
| close editor (scoped) | `drive_preview press key=Escape selector=#edBody` |
| prove state | `desktop_preview read` (≈24k cap) / `drive_preview elements max=1` (echoes `document.title`) |
Page changes that made it possible: `#heroGap` as a real span; `#senterHiddenInput` moved to `<body>` (1 px, on-screen); blank-space handler excludes `.heroOrbs, #rankBar`. ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md]

## What the pane strips
URL hash `#q=…&k=…` is rewritten during boot (arrives unranked) and `?eqdemo` flags are stripped — demo/debug triggers must be visible fixed `<button id=…>`
elements clicked via `drive_preview`. `desktop_preview open` STACKS tabs: reload = close all, open one. ^[raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md] ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## Readers
`desktop_preview read` = visible text only (24k cap — prepend readouts to `#view-wiki .hero`); `drive_preview elements` = buttons/links/labelled divs; every
`drive_preview` result echoes `document.title` in full — the cleanest readout ([[wiki-topics/senter-wiki/wiki/concepts/verification-and-proof-methods|proof methods]]). A black
`screencapture` = display asleep. See [[wiki-topics/senter-wiki/wiki/comparisons/pane-driving-methods|pane-driving methods]]. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
