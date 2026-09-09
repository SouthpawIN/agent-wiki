---
title: Verification and proof methods for wiki UI work
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [skill, ui, tool]
sources:
  - raw/sources/knowledge/skill-agent-wiki-vault.md
  - raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-hud-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-palette.md
confidence: high
---

# Verification and proof methods

Chris's standard: a claim about what he sees without proof from his real window is lying to him; *"he distrusts vision verdicts and accepts pixel triples."*
The methods that earned trust, in order of cost: ^[raw/sources/knowledge/ref-vault-live-palette.md]

## 0. Pre-flight before every reload
`scripts/vault-live-check.py`: extract `<script>` blocks → `node --check`, AND brace-balance the CSS with comments stripped. A python replace that ended a rule with
`… */\n` and no `}` swallowed every rule after it — rows stuck open, no charts — and vision misread it (*"you broke some stuff"*). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## 1. `document.title` readout (cleanest, one round, no screenshot)
Set `document.title='X rect='+[...]` from a temp handler (element's own click or `setTimeout` after the pass), then `drive_preview elements max=1` — every drive_preview
result echoes the title in full (`acted` strings truncate ~80 chars; `desktop_preview read` caps 24k). Examples: `body=deadzone views= viewWikiDisp=none` explained the
"nowhere" bug where three screenshots had not; `ED cls=view on pinned rect=… edBody.children=1` refuted vision's "empty box". Strip with `assert 'TEMP-' not in s`. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## 2. Fixed `<button id="dbgOut">` readout
Only visible text / buttons surface to the readers — an `aria-label`, `data-*` or anything inside a hidden hero never shows. Dump computed geometry per cell
(`class{x w flexGrow/Shrink/Basis maxWidth marginLeft}`); read via `drive_preview click`'s `acted` string. Found the `--orbcol` clamp instantly. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## 3. Self-checks must prove they ran
Invocation counters (`window.__xRuns++`) in every layout pass; read back after each patch (`placeHud` `runs=0` twice; `querivalector` typo returned early a whole round while
reported as working). Record final Δ in a `data-*` attribute — *"prove 0.00 instead of arguing with a screenshot."* ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## 4. Pixel proof
`screencapture -x` immediately after a hover (a ~2.5 s idle timer reverts hover visuals) → `scripts/pixel-span-diff.py A.png B.png` for byte-identical spans;
histograms for tone. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## 5. Vision — last, and doubted
- *"Vision 'element not present' is a crop error until proven otherwise"* — pane is narrower than the screen (HUD at x≈1100, crops at x>1700 found nothing three times).
- Vision says "flush" when Chris sees 3px; when the measured Δ IS 0.00 and he still sees it off, he is aligning CENTRES, not edges.
- Retina crops → halve for pt. Crop from the pane's left edge (~x660) or use the whole frame with a pointed question. ^[raw/sources/knowledge/ref-vault-live-hud-2026-09-03.md] ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## 6. Headless logic tests
Pure ranking/sorting = plain functions over `.system-live.json` → 30-line node script (`/tmp/ranktest.js`) before touching the pane. Supplement only — Chris wants the real
pane driven ([[topics/senter-wiki/wiki/entities/hermes-preview-pane-and-drive-preview|preview pane]]). ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md]

## Terminal pitfalls
Grep/sed with several quoted alternations or `$(…)` inside `sed -n` trip the hardline payload block — use `search_files`/`read_file` and `python3 - <<'EOF'` for edits.
Exit 130 with no error = your own input hit your own host app; run detached (`nohup … &`) to separate. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

See [[topics/senter-wiki/wiki/concepts/chris-ui-working-rules|Chris's working style]] for why each of these exists.
