---
title: Editor card (hover-peek / click-pin markdown editor)
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [ui, decision]
sources:
  - raw/sources/knowledge/ref-vault-live-editor-card-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
confidence: high
---

# Editor card (hover-peek / click-pin markdown editor)

## Chris's ask
2026-09-03 (queued first as "consolidate the editor page so that when you mouse over the preview it will expand it. If you click on it, then it will lock it … a quick markdown editor for each one of these items"), then late that day: "I don't want a different editor page. I still want that editor though … when something is selected, underneath the line there is the overview. Hover over that and a window appears — like the hover cards … as an overlay; that's the HTML editor. If the user clicks then it stays in place so they can edit; click outside the window to close and save." → [[topics/senter-wiki/wiki/decisions/2026-09-03-editor-is-a-card-not-a-page|decision]]. ^[raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md] ^[raw/sources/knowledge/ref-vault-live-editor-card-2026-09-03.md]

## Implementation (presentation only — logic untouched)
Same `#view-editor` DOM + `openEditor/closeEditor/edSave`. `position:fixed; z-index:70; left:var(--edX); top:var(--edY); background:#000; border:1px solid #fff` (feed-card style), anchored under `#heroOverview` by `placeEditorCard()`; `showView('editor')` leaves the wiki view ON. ^[raw/sources/knowledge/ref-vault-live-editor-card-2026-09-03.md]

## State machine
- overview `pointerenter` → 160 ms → `openEditor(row)` + `.peek` (toolbar hidden).
- Close only when pointer is outside BOTH overview and card (`overOv/overEd` flags); `maybeHide()` = ONE `requestAnimationFrame` — Chris rejected a 260 ms grace: "disappear instantly if I don't have it locked" / "delays half a second".
- `pin()` = overview click or card pointerdown → `.pinned`, toolbar visible.
- `document.pointerdown` (capture) outside while pinned → `closeEditor(true)` (save) AND swallow that press with one-shot capture eaters — "clicking off must not trigger the area underneath — but don't block it normally". ^[raw/sources/knowledge/ref-vault-live-editor-card-2026-09-03.md]
- **Every open path must set the same state the click-off guard keys on**: row click / Enter / star / deep link opened un-pinned and click-off fell through to the dead zone → SPACE opened behind the card. Canonical state now set inside `openEditor()` (locked by default; peek downgrades). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## Trap
`.peek { pointer-events:none }` made the card vanish the instant the pointer left the overview; vision said "empty white-bordered box" because the capture landed mid-close — the `document.title` readout (`ED cls=… edBody.children=1`) proved content was present. Trust the DOM readout over vision ([[topics/senter-wiki/wiki/concepts/pane-driving-and-verification|verification]]). ^[raw/sources/knowledge/ref-vault-live-editor-card-2026-09-03.md]

## Bottom bar `#edBar`
SHARE → part toggles (context/skills/bots/loops) + COPY (markdown bundle) + SEND TO HERMES (`hermes.send`). Hidden while peeking. Queued buttons: LOCK (bridge `/write`), HISTORY (log.md), ASK, OPEN IN OBSIDIAN; verify COPY with `pbpaste`. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## Legacy quirks
Reload restored `#bots/<name>`, browser back didn't close the old editor page, Enter didn't search while open — all reasons the card replaced the page. Scoped close from the driver: `drive_preview press key=Escape selector=#edBody` (never global Escape). ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md]

Layering: card z70 < settings 90 < feed open 80→ see [[topics/senter-wiki/wiki/concepts/layer-stack|layer stack]]. Related: [[topics/senter-wiki/wiki/entities/settings-card|settings card]] (same click-off contract).
