---
title: Hollow = selected/rest, solid = hover/active — one ring knob
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [ui, preference]
sources:
  - raw/sources/knowledge/skill-agent-wiki-vault.md
  - raw/inbox/2026-09-05-legacy-inbox.md
confidence: high
---

# Hollow = selected/rest, solid = hover/active

Chris's inverse recipe for any circle that mirrors the row dots (active [[topics/senter-wiki/wiki/entities/hero-orbs|hero orb]], the [[topics/senter-wiki/wiki/entities/hud-cluster|gear]], the mute dot, PROPOSED rows): ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

```
background:transparent; box-shadow:0 0 0 var(--ringW) #fff inset; color:#fff   /* rest / selected: hollow, white glyph */
hover → solid #fff + black glyph
```
`--ringW` (1px — "thinner") lives on `:root` so every hollow circle changes together; he compares them side by side. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## Where it shows up
- Active orb = the section under the hero, drawn inverse. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- Gear disc = `.orb` recipe. ^[raw/sources/knowledge/ref-vault-live-hud-place-2026-09-03.md]
- Proposed rows: "a hollow ring + PROPOSED tag in SKILLS/BOTS/LOOPS" ([[topics/senter-wiki/wiki/concepts/approval-policy|approval policy]]). ^[raw/inbox/2026-09-05-legacy-inbox.md]
- Muted = hollow ring on the [[topics/senter-wiki/wiki/entities/volume-rocker|mute dot]]. ^[raw/inbox/2026-09-05-legacy-inbox.md]

Colour comes from [[topics/senter-wiki/wiki/concepts/paper-palette|paper palette]]; the inverse is state-by-presence, never opacity.
