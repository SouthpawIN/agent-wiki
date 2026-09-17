---
name: wiki-ui-knobs
description: Use when Chris asks to move, resize, recolour or re-time anything in vault-live.html. Every knob, where it lives, and the rule that owns it.
version: 1.0.0
---
# wiki-ui-knobs
Root-cause rule: change the knob, never add a second writer. Positional truth for the HUD is `placeHud` (inline !important);
CSS positional rules for `#hudCluster .navgear` / `#media` were removed on purpose. Verify with a TEMP DOM readout
(`getBoundingClientRect` → `document.title`), remove it after. JS check:
`python3 -c "import re;s=open('vault-live.html').read();open('/tmp/vc.js','w').write('\n;\n'.join(re.findall(r'<script>([\s\S]*?)</script>',s)))" && node --check /tmp/vc.js`

## Named knobs (Chris-tuned values as of 2026-09-05)
| Knob | Value | Owns |
|---|---|---|
| `--paper` / `--paperDim` | #dfe8f5 / .96 | the ONE white; wallpaper multiplied onto it |
| `--wallGain` / `--wallContrast` | 1.67 / 1.35 | girl brightness/contrast |
| `--spaceGlow` | .46 | star map dimmer (the only one — inline opacity removed) |
| `--fadeNear` / `--fadeFar` | 30% / 82% | feed diagonal mask |
| `--volLen` / `--volShift` | 495px / 13px | rocker length / x (centre between feed edge and pane edge) |
| `--volDot` / `--volGap` | 5px / 16px | segmented rocker dots and the level gap |
| `--volMuteGap` / `--volMuteHit` | 14px / 26px | mute dot offset and hitbox (whole rocker region toggles mute) |
| `--eqLeft` | set by EQ placer | left edge of the media/mute zone (her headphones) |
| `--gearSize` / `--gearNudgeX/Y` | 30px | SVG cog inside the 40px hollow ring |
| `MEDIA_FROM_RIGHT / MEDIA_TOP / MEDIA_W` | 221 / 105 / 180 | player anchor (right edge); gear x = play-button centre |
| z-order | HUD 120 · chat 110 (open 130) · settings 90 · cards 70 | player+feed always on top; their clicks never cancel STAGE |
| peek / spy release / focus re-assert | 160ms / 160ms·700ms / 150ms | hover card, orb scroll-spy lock, hover=focus |

All `--*` custom properties present in the file (36): --a --accent --bandInset --bg --border --c --dim --eqCX --eqCY --eqH --eqW --err --fadeFar --fadeNear --fadeY --gearNudgeX --gearNudgeY --gearSize --heroNudge --muted --ok --paper --ringW --spaceGlow --surface --surface2 --text --tool --usageW --volDot --volGap --volLen --volPad --volShift --wallDim --warn
