---
title: Layer stack (z-index contract) of vault-live.html
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [ui]
sources:
  - raw/sources/knowledge/skill-agent-wiki-vault.md
  - raw/inbox/2026-09-05-legacy-inbox.md
  - raw/sources/knowledge/ref-vault-live-editor-card-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-settings-card-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-hud-2026-09-03.md
confidence: high
---

# Layer stack (z-index contract)

Ordered bottom → top, with dates where it changed. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

| z | Element | Notes |
|---|---|---|
| 1 | `#mindmap` star canvas | lifted to 6 + `pointer-events:auto` in SPACE ([[wiki-topics/senter-wiki/wiki/entities/space-star-map|SPACE]]) |
| 5 | (`#view-senter`, retired) | empty view that once ate SPACE clicks |
| 30 | row icon stacks | hover cards over neighbours |
| 40 | sticky `.hero` | must out-rank every row-level z (was 8 → icons scrolled over it) |
| 50 / 55 | chat / search overlay (older fixed overlays) | |
| 70 | [[wiki-topics/senter-wiki/wiki/entities/editor-card|editor card]] | |
| 80 → 110 (130 open) | [[wiki-topics/senter-wiki/wiki/entities/corner-feed|feed]] expanded | 2026-09-05: side chat z110, z130 when open ^[raw/inbox/2026-09-05-legacy-inbox.md] |
| 90 | [[wiki-topics/senter-wiki/wiki/entities/settings-card|settings card]] shell | |
| 58 → 120 | [[wiki-topics/senter-wiki/wiki/entities/hud-cluster|HUD]] (player, rocker, gear) | 2026-09-05: "HUD is now z120 … above cards (70) and settings (90)"; play button confirmed top hit at its centre ^[raw/inbox/2026-09-05-legacy-inbox.md] |
| 2001–9999 | temp debug/demo buttons, hand-placement layer | strip before shipping |

## Rules
- Feed open hides `#hudCluster` (`body:has(#chat.open) #hudCluster { display:none }`) — Chris: "the media player is still visually in the way"; SPACE hides chat, `#intRail`, HUD. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- Containers for fixed children carry NO transform (HUD trap). ^[raw/sources/knowledge/ref-vault-live-hud-2026-09-03.md]
- Cards (editor, settings) share the click-off swallow contract: closing press eaten once, next press untouched. ^[raw/sources/knowledge/ref-vault-live-editor-card-2026-09-03.md] ^[raw/sources/knowledge/ref-vault-live-settings-card-2026-09-03.md]
- Dead zone excludes `.hero, #hudCluster, #warnMask, #view-editor` — chrome and cards are never dead space. ^[raw/sources/knowledge/ref-vault-live-settings-card-2026-09-03.md]

Conflicting history is a supersession, not a contradiction: 58 → 120 and 80 → 110/130 are dated moves.
