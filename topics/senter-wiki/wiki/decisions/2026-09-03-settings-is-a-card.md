---
title: Decision: settings is a card; the 'nowhere' bug root-caused
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, ui, pain]
sources:
  - raw/sources/knowledge/ref-vault-live-settings-card-2026-09-03.md
confidence: high
---

# Settings is a card (2026-09-03, late)

**Symptom.** Chris: *"When I back out of settings, I'm in nowhere — the back room, a blank space."* Then: *"when I open the settings page I still see the list and everything
else disappear."* ^[raw/sources/knowledge/ref-vault-live-settings-card-2026-09-03.md]

**Root cause (one DOM readout).** `body=deadzone views= viewWikiDisp=none` — the gear sits in the dead-zone band; its click also reached the dead-zone handler →
`showView('senter')` → `#view-senter` retired → every view lost `.on`. The 72 %-black `#warnMask` made it look like a modal page. ^[raw/sources/knowledge/ref-vault-live-settings-card-2026-09-03.md]

**Decision.** (1) Dead zone excludes chrome + cards; (2) `showView()` never ends with zero views on (falls back to wiki); (3) settings becomes a transparent-shell CARD with the
same click-off swallow contract as the editor — *"settings should not make everything else go black … overlay everything instead of making everything else hide."*
See [[topics/senter-wiki/wiki/concepts/hover-card-contract|hover-card contract]], [[topics/senter-wiki/wiki/entities/hud-cluster|HUD cluster]].
