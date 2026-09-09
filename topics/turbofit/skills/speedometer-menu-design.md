---
title: speedometer-menu-design
updated: 2026-08-27
type: skill
tags: [turbofit, desktop-plugin, design, theming]
---

# Skill: TurboFit speedometer plugin menu (design record)

Decisions captured 2026-08-27, from live conversation. Redesign target: `desktop/plugin.js`
(781 lines, single TurbofitPage, registered at /turbofit via @hermes/plugin-sdk).

## Concept
The plugin's main surface is a **speedometer**: the gauge needle shows where the machine
sits on the Fit List ladder — memory pressure and tier position at a glance.

## Gauge inputs (all available from existing pieces)
- Hardware fingerprint (total usable memory) — static arc segmentation = Fit List tiers
  (8 / 16 / 24+ GB bands; Maple | Ornith | Unleashed zones)
- Pressure probe (live usable memory) — needle position
- Current rung/model — digital readout under the needle
- Contraction/expansion events — needle animation between zones

## Theming
- Themable via CSS custom properties; theme packs set tokens (needle, arc zones, glow,
  warning/redline). No hardcoded colors in component code — token indirection only.
- Existing palette in the code uses var(--ui-*) tokens; extend with turbofit-scoped tokens
  (e.g. --tf-needle, --tf-zone-quiet, --tf-zone-pressure) so Hermes themes cascade and
  TurboFit packs override.

## Plugin menu structure (to finalize)
- Main route /turbofit: the speedometer + current model/aux/context readouts
- Palette commands: open, shift up, shift down, shift intelligence|balanced|speed,
  theme picker, update. Expansion policy toggle (conservative one-rung recovery = default
  vs jump-to-fit) lives in the menu as an option.
- Menu contract open question: whether settings (theme, expansion policy) are palette
  commands, a settings drawer under the gauge, or a separate route.

## Implementation notes
- Single-file plugin.js, jsx-runtime (no build step, matches existing code)
- Gauge = inline SVG; arc segments from Fit List tier boundaries; needle = rotation transform
- Live data: poll turbofit-runtime status / gateway /v1/models (same polling the page does now)
