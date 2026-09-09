---
name: wiki-drive-preview
description: Use when you must operate or prove the Senter wiki UI. Drive the real preview pane by selector with drive_preview; never computer_use into Hermes; prove state via document.title.
version: 0.1.0
distilled: 2026-09-05
topic: senter-wiki
---
# wiki-drive-preview

The preview pane IS the UI Chris watches. Driving it by selector is driving the real thing. Chris: "no try again … you need to practice your computer use, not work around."

## Pre-flight (every reload)
`python3 scripts/vault-live-check.py` — `node --check` on every `<script>` block AND CSS brace balance with comments stripped. One unbalanced rule swallowed every rule after it; vision misread the wreck as "expanded rows".

## Never
- `computer_use` / `cua-driver` foreground keys to pid Hermes: focus is the chat composer, **Escape = Stop agent** (self-cancelled ×4, exit 130 with no error).
- Background `cua-driver call click x,y` — routes via AX, never fires page handlers.
- Relying on `#q=…&k=…` or `?flag` URLs: the pane rewrites the hash and strips queries during boot.
- `desktop_preview open` repeatedly — it STACKS tabs; reload = close all, open one.

## Drive (selector map)
| Intent | Call |
|---|---|
| start header search | `drive_preview click selector=#heroGap` |
| type + Enter | `drive_preview type selector=#senterHiddenInput text=<term> submit=true` |
| section re-cut | `drive_preview click selector='#heroOrbs .orb[data-k="skills"]'` (`ctx|agents|loops`) |
| open item | `drive_preview click selector='#wiki-list .topic[data-bot="anser"] .thead .tname'` (`data-topic|data-skill|data-loop`) |
| hover a row | `drive_preview hover selector='#wiki-list .topic[data-topic="x"] .thead'` (its `acted` string dumps row text) |
| close editor | `drive_preview press key=Escape selector=#edBody` (scoped, never global) |
| clear | `drive_preview click selector=#rankOff`; EMPTY input + Enter = plain wiki |
| demo/debug trigger | visible fixed `<button id=…>` + `drive_preview click` |
Hit targets must be real on-screen elements (`#heroGap` span; `#senterHiddenInput` on `<body>`, 1px, not inside a clipped container). If a click lands but nothing happens, check what else the handler filters (`.heroOrbs, #rankBar` exclusion).

## Prove
1. **`document.title` readout** (best): temp handler sets `document.title='X rect='+[...]`; `drive_preview elements max=1` echoes it in full. `acted` truncates ~80 chars; `desktop_preview read` caps 24k (prepend readouts to `#view-wiki .hero`).
2. Fixed `<button id="dbgOut">` with computed cell geometry — only visible text/buttons surface; `aria-label`/`data-*` don't.
3. Self-checks must show they ran: `window.__xRuns` counters, final Δ in a `data-*` attribute.
4. `screencapture -x` IMMEDIATELY after hover (2.5s idle timer reverts visuals) → `scripts/pixel-span-diff.py` for byte-identical spans.
5. Vision last: "not present" is a crop error until a rect readout says otherwise (pane ≈ x660–1810 on a 2× screen; halve retina coords for pt).
Strip every `TEMP-` hook: `assert 'TEMP-' not in s`.

## Evidence
> "no try again … you need to practice your computer use, not work around."
> "you broke some stuff" (CSS brace imbalance shipped without the pre-flight)
> "I'm worried the positioning is based on the lettering" (caught by hovering rows — prove with pixel-span diffs, not screenshots)
