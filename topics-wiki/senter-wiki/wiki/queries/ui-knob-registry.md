---
title: UI knob registry — every tuned value and the rule that owns it
created: 2026-09-05
updated: 2026-09-05
type: query
tags: [ui, preference]
sources:
  - raw/sources/knowledge/skill-agent-wiki-vault.md
  - raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-eq-feed-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-hud-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-hud-place-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-palette.md
  - raw/sources/knowledge/ref-vault-live-settings-card-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-editor-card-2026-09-03.md
  - raw/inbox/2026-09-05-legacy-inbox.md
confidence: high
---

# UI knob registry — every tuned value and the rule that owns it

Compiled counterpart of the `wiki-ui-knobs` skill ([[topics-wiki/senter-wiki/wiki/entities/senter-wiki-skills|topic skills]]). Values are Chris's locked numbers as of 2026-09-05; change = his say-so.

## Layout / rows
| Knob | Value | Owner |
|---|---|---|
| `--rowcap` / `--orbcol` / `--dotsc` | measured by `orbColumn()`; `--dotsc` = centre of row dots | [[topics-wiki/senter-wiki/wiki/entities/hero-orbs|hero orbs]] ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md] |
| `--heroNudge` | 0 (retired) | ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md] |
| `--heroOrbsTop` | 16px (was 26) | ^[raw/sources/knowledge/ref-vault-live-eq-feed-2026-09-03.md] |
| row dots rest / hover | 4px / 32px (gap 12); dots cell 164px reserved | [[topics-wiki/senter-wiki/wiki/concepts/standard-row-anatomy|row]] ^[raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md] |
| hero orbs | 40px / 1.8em gap 14 (half-group 101px) — earlier 48px/2.2em | ^[raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md] ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md] |
| hero title | 2.4em; font drop accepted 3.3→3.0em earlier | ^[raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md] ^[raw/sources/knowledge/skill-agent-wiki-vault.md] |
| `--hfs` | hover title cap 1.5em | ^[raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md] |
| `--bandInset` | 20px (trim from top) | ^[raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md] |
| `--usageW` / `WEEKS` / dot | 140px / 10 / 3px | [[topics-wiki/senter-wiki/wiki/entities/usage-strip|usage strip]] ^[raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md] |
| `--ringW` | 1px | [[topics-wiki/senter-wiki/wiki/concepts/hollow-vs-solid-rings|rings]] ^[raw/sources/knowledge/skill-agent-wiki-vault.md] |
| hero z / HUD z / card z / settings z / feed z | 40 / 120 / 70 / 90 / 110 (130 open) | [[topics-wiki/senter-wiki/wiki/concepts/layer-stack|layers]] ^[raw/inbox/2026-09-05-legacy-inbox.md] |

## Tone
| Knob | Value | Owner |
|---|---|---|
| `--paper` | `color-mix(#dfe8f5 96%, #000)` via `--paperPct` | [[topics-wiki/senter-wiki/wiki/concepts/paper-palette|palette]] ^[raw/sources/knowledge/ref-vault-live-palette.md] |
| `--wallInk` | 1 (two stacked masked layers) | ^[raw/sources/knowledge/ref-vault-live-palette.md] |
| `--spaceGlow` | .46 | ^[raw/sources/knowledge/ref-vault-live-palette.md] |
| attention | `#FFE45A` | ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md] |
| feed mask | `--fadeNear 12%`, `--fadeFar 82%`, mid .5 @42% | [[topics-wiki/senter-wiki/wiki/entities/corner-feed|feed]] ^[raw/sources/knowledge/ref-vault-live-hud-2026-09-03.md] |

## Wallpaper-anchored
| Knob | Value | Owner |
|---|---|---|
| `WALL_AR` | 1.54 | [[topics-wiki/senter-wiki/wiki/entities/wallpaper-girl|wallpaper]] ^[raw/sources/knowledge/ref-vault-live-eq-feed-2026-09-03.md] |
| `--eqCX/--eqCY` | 0.8282 / 0.3937 | [[topics-wiki/senter-wiki/wiki/entities/headphone-eq|EQ]] ^[raw/sources/knowledge/ref-vault-live-eq-feed-2026-09-03.md] |
| `--eqW/--eqH`, `COLS×ROWS` | 3.2 / 4.6 %, 7×6; dots 4.5px `#000`, unlit `scale(.44)` | ^[raw/sources/knowledge/ref-vault-live-eq-feed-2026-09-03.md] |
| `HEAD_BACK` | 0.905 | [[topics-wiki/senter-wiki/wiki/entities/hud-cluster|HUD]] ^[raw/sources/knowledge/ref-vault-live-hud-2026-09-03.md] |
| `__figFrac` | .62 fallback (fingertips) | ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md] |

## HUD / player / rocker
| Knob | Value | Owner |
|---|---|---|
| bake | media `W − 222` from right, top 105, w180; gear 40px top 23, cx = play ring | ^[raw/sources/knowledge/ref-vault-live-hud-place-2026-09-03.md] |
| `--gearSize`, `--gearNudgeX/Y` | 30px, optical | ^[raw/sources/knowledge/ref-vault-live-hud-place-2026-09-03.md] |
| rocker centre | 1140 (derived: (1128+1152)/2) | [[topics-wiki/senter-wiki/wiki/entities/volume-rocker|rocker]] ^[raw/inbox/2026-09-05-legacy-inbox.md] |
| `--volLen` | 495px | ^[raw/sources/knowledge/skill-agent-wiki-vault.md] |
| wheel step | `clamp(deltaY*0.0006, ±.022)`, inverted | ^[raw/sources/knowledge/skill-agent-wiki-vault.md] |
| `--volDot` / `--volGap` / `--volMuteGap` / `--volMuteHit` | 5px / 10px / 14px / 26px | ^[raw/inbox/2026-09-05-legacy-inbox.md] |
| `--eqLeft` | 936 (media-zone left edge) | ^[raw/inbox/2026-09-05-legacy-inbox.md] |

## Cards
| Knob | Value | Owner |
|---|---|---|
| `--edX/--edY` | from `#heroOverview` rect; card width `min(1100px, …)` | [[topics-wiki/senter-wiki/wiki/entities/editor-card|editor]] ^[raw/sources/knowledge/ref-vault-live-editor-card-2026-09-03.md] |
| peek delay / hide | 160 ms / 1 frame | ^[raw/sources/knowledge/ref-vault-live-editor-card-2026-09-03.md] |
| `--setY/--setR/--setL` | gear.bottom+12 / innerWidth−gear.right / `#heroLine.left` | [[topics-wiki/senter-wiki/wiki/entities/settings-card|settings]] ^[raw/sources/knowledge/ref-vault-live-settings-card-2026-09-03.md] |
| `--setNudge` | 40px (10 → 40 by feel) | ^[raw/sources/knowledge/ref-vault-live-settings-card-2026-09-03.md] |
| `SPY_LOCK` release | 160 ms after last scroll, 700 ms fallback | ^[raw/sources/knowledge/skill-agent-wiki-vault.md] |
| CONTEXT card right edge | side-chat left − 14px (measured 684 vs chat 698); never overlaps feed/player | [[topics-wiki/senter-wiki/wiki/decisions/2026-09-05-content-card-stops-at-side-chat|decision]] ^[raw/inbox/2026-09-05.md] |
| diff settle / peek | 6 s to plain text; closed card peeks 9 s unless one is pinned | [[topics-wiki/senter-wiki/wiki/entities/context-card-live-diff|live diff]] ^[raw/inbox/2026-09-05.md] |
| CONTEXT counts | none — *"I don't want any numbers indicating what's in the wiki"* (orb number contested) | ^[raw/inbox/2026-09-05.md] |
| row-dot hover origin | the hovered dot stays under the cursor; right overhang allowed (asked 19:18, pending) | [[topics-wiki/senter-wiki/wiki/decisions/2026-09-05-row-dots-expand-from-hovered-dot|decision]] ^[raw/inbox/2026-09-05.md] |

## Similarity
auto ≥0.50, propose ≥0.35, `name_contains` floor 0.65 — [[topics-wiki/senter-wiki/wiki/concepts/similarity-ranking|ranking]] ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md]
