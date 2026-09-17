---
title: Settings card (gear → card, not a modal page)
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [ui, pain]
sources:
  - raw/sources/knowledge/ref-vault-live-settings-card-2026-09-03.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
  - raw/sources/knowledge/ref-vault-live-hud-place-2026-09-03.md
confidence: high
---

# Settings card (gear → card, not a modal page)

## Chris's words
"When I back out of settings, I'm in nowhere — the back room, a blank space." After the card conversion: "when I open the settings page I still see the list and everything else disappear." And the rule: "settings should not make everything else go black … overlay everything instead of making everything else hide." ^[raw/sources/knowledge/ref-vault-live-settings-card-2026-09-03.md]

## Root cause of "nowhere" (one DOM readout)
`document.title='SET body='+…` read via `drive_preview elements max=1` → `body=deadzone views= wikiRows=19 wikiRect=0,0,0,0 viewWikiDisp=none`. The gear sits in the right-hand dead-zone band; its click reached the settings handler AND the dead-zone click handler → `showView('senter')` → `#view-senter` had been retired → every `.view` lost `.on`. The old 72 %-black `#warnMask` dimmer made it look like a modal page. ^[raw/sources/knowledge/ref-vault-live-settings-card-2026-09-03.md]

## Fixes (all root-cause)
1. Dead zone excludes chrome + cards: `closest('.hero, #hudCluster, #warnMask, #view-editor')`; click ignore list gained `#hudCluster, #view-editor`.
2. `showView()` never ends with zero views on — missing target → `view-wiki`.
3. Settings `close()` lands on the wiki explicitly (if `body.space` or wiki not on). ^[raw/sources/knowledge/ref-vault-live-settings-card-2026-09-03.md]

## Card presentation
`#warnMask.settings` is a transparent, `pointer-events:none`, z90 layout shell; the `.warn` inside is `pointer-events:auto; background:#000` (1px white border), anchored under the gear (`--setY = gear.bottom+12`, `--setR = innerWidth − gear.right`) and stretched left to the hero underline (`--setL = #heroLine.left`) plus `--setNudge`. Chris's sizing sequence: "a lot wider — to where the other cards start" → "too far left — to the edge of the title and the line" → "shift it about 10 pixels" → "and about 30 more" (→ 40px). "Keep the nudge a named knob; he tunes by feel." ^[raw/sources/knowledge/ref-vault-live-settings-card-2026-09-03.md]

## Click-off
Same swallow contract as the [[wiki-topics/senter-wiki/wiki/entities/editor-card|editor card]]: a `document` capture `pointerdown` installed on the next tick ignores `.warn`/`#navSettings`, closes, and eats the matching pointerup/click once; the NEXT press is untouched. Gear toggles the card (open → click again closes); no CLOSE button. ^[raw/sources/knowledge/ref-vault-live-settings-card-2026-09-03.md] ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

Other overlays sharing `#warnMask` (askBox, discard-warn, wallpaper `pick()`) keep the dimmer — intentional for true modals. ^[raw/sources/knowledge/ref-vault-live-settings-card-2026-09-03.md]

Gear itself: [[wiki-topics/senter-wiki/wiki/entities/hud-cluster|HUD cluster]]. Layer order: [[wiki-topics/senter-wiki/wiki/concepts/layer-stack|layer stack]].
