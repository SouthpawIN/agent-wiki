---
title: Driving the preview pane and proving it — the verification contract
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [skill, ui, preference]
sources:
  - raw/sources/knowledge/skill-agent-wiki-vault.md
  - raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-editor-card-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-hud-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-hud-place-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-demo-video.md
confidence: high
---

# Driving the preview pane and proving it

## Chris's demand
"no try again … you need to practice your computer use, not work around." The preview pane IS the UI he watches; driving it by selector is driving the real thing. A claim about what he sees without a capture of his window = lying to him (memory). ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md]

## Pre-flight (every reload)
`python3 scripts/vault-live-check.py` — extracts every `<script>` → `node --check` (`~/.hermes/node/bin/node`) AND brace-balances the CSS (a replace that ended a rule with `*/` and no `}` swallowed every later rule: rows rendered stuck open, "you broke some stuff"). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## Drive by selector (`drive_preview`)
| Intent | Call |
|---|---|
| start header search | `click selector=#heroGap` |
| type + Enter | `type selector=#senterHiddenInput text=discord submit=true` |
| re-cut by kind | `click selector='#heroOrbs .orb[data-k="skills"]'` |
| open item | `click selector='#wiki-list .topic[data-bot="anser"] .thead .tname'` |
| hover a row | `hover selector='#wiki-list .topic[data-topic="x"] .thead'` (acted string dumps row text) |
| close editor | `press key=Escape selector=#edBody` (never global Escape) |
| prove | `desktop_preview read` (≈24k cap) / `elements max=1` | ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md] ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
Made possible by: `#heroGap` a real span sized by the alignment pass; `#senterHiddenInput` moved to `<body>` (1×1px, on-screen). ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md]

## What NOT to do
The wiki lives inside the Hermes app the agent runs in: `computer_use`/`cua-driver` foreground clicks land in the chat composer and **Escape = Stop agent** (self-cancelled four times, exit 130). Background AX clicks "succeed" and never fire page handlers. Window `4956` is the real Hermes body; `4988` a 32-pt strip. Retina crop coords ÷2 for pt. ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md]

## Cleanest proof = `document.title`
Every `drive_preview` result echoes the page title in full while `acted` truncates (~80) and `read` caps at 24k. Set `document.title='X rect='+[...]` from a temp hook, call `elements max=1`, strip the hook (`assert 'TEMP-' not in s`). One round, no screenshot. Found: `--orbcol` clamp, settings "nowhere" (`body=deadzone views= viewWikiDisp=none`), HUD "not present" (`gear[1077,28 40x40] media[1007,100]`), editor content while vision saw an empty box. ^[raw/sources/knowledge/skill-agent-wiki-vault.md] ^[raw/sources/knowledge/ref-vault-live-settings-card-2026-09-03.md] ^[raw/sources/knowledge/ref-vault-live-hud-2026-09-03.md] ^[raw/sources/knowledge/ref-vault-live-editor-card-2026-09-03.md]

## Screenshots and vision — when and how
- `screencapture -x` IMMEDIATELY after hover (2.5 s idle timer reverts hover visuals). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- Vision "element not present" is a crop error until proven otherwise (pane narrower than the screen; HUD at x≈1100, crops at x>1700). Never trust vision for the last few px — MEASURE rects, self-correct over 2 rAF passes, write final Δ to `data-*`. Prove alignment with `scripts/pixel-span-diff.py` (byte-identical spans). ^[raw/sources/knowledge/skill-agent-wiki-vault.md] ^[raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md]
- Tone: histogram pixels ([[topics/senter-wiki/wiki/concepts/paper-palette|paper palette]]). A black capture = display asleep. ^[raw/sources/knowledge/ref-vault-live-palette.md]

## Self-checks must be shown to run
A typo (`querivalector`) made a loop return early for a round while reported as working; keep invocation counters (`window.__xRuns++`) and read them back. When replacing a line with a python patch, assert the neighbour line still exists (`placeHud` scheduling lost twice). ^[raw/sources/knowledge/skill-agent-wiki-vault.md] ^[raw/sources/knowledge/ref-vault-live-hud-place-2026-09-03.md]

## Terminal traps
Grep/sed with several quoted alternations and `$(grep …)` trip the hardline parser block — use `search_files`/`read_file` and `python3 - <<'EOF'` for multi-line edits. Exit 130 with no error → your own input hit your host app; run detached with `nohup`. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

Feeds the [[topics/senter-wiki/wiki/concepts/chris-ui-working-rules|working rules]]; demo recording in [[topics/senter-wiki/wiki/concepts/demo-video-recipe|demo recipe]].
