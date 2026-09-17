---
title: Wallpaper tint approaches compared (why only the mask worked)
created: 2026-09-05
updated: 2026-09-05
type: comparison
tags: [ui, pain]
sources:
  - raw/sources/knowledge/ref-vault-live-palette.md
confidence: high
---

# Tinting the wallpaper girl to `--paper`

| Attempt | Result / why it read wrong |
|---|---|
| `brightness(1.67)` on the image | 153→255 pure white; later the UI went blue-white → she read **warm** |
| `sepia()` / `hue-rotate` filters | approximate tints never match a hex — *"still cream"* |
| element `background:var(--paper)` + picture `mix-blend-mode:multiply` | `filter` on the element runs after pseudo-children blend (washed the tint back); multiply(paper × 60 % grey) is darker → measured (176,176,176) neutral grey, reads WARM beside blue-white; bare paper background leaked below the `contain` picture = the *"gray bar along the bottom"* three fade fixes couldn't remove |
| **picture as luminance MASK over flat paper, stacked twice** | ink pixels are exactly `--paper`; black stays black; nothing paints outside the picture — pixel-verified |
^[raw/sources/knowledge/ref-vault-live-palette.md]

Lesson: tint = colour variables; fade = mask; never `filter` a container (dims stars, breaks fixed children). See
[[wiki-topics/senter-wiki/wiki/entities/wallpaper-girl|paper palette]], [[wiki-topics/senter-wiki/wiki/decisions/2026-09-03-paper-palette-blue-white|decision]].
