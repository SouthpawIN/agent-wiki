# vault-live.html — editor as hover card (2026-09-03, late)

Chris: "I don't want a different editor page. I still want that editor though … when something is
selected, underneath the line there is the overview. Hover over that and a window appears — like
the hover cards we used for tags/integrations and the feed messages now — as an overlay; that's
the HTML editor. If the user clicks then it stays in place so they can edit; click outside the
window to close and save."

## What changed (presentation only — logic untouched)

CSS (`#view-editor` rule, ~line 217):
```css
#view-editor { position:fixed; z-index:70; left:var(--edX,26px); top:var(--edY,200px);
  width:min(1100px, calc(100vw - var(--edX,26px) - 40px));
  max-height:calc(100vh - var(--edY,200px) - 24px); overflow-y:auto; padding:0 22px 26px;
  background:#000; border:1px solid #fff; box-sizing:border-box; display:none; }
#view-editor.on { display:block; }
#view-editor.peek { opacity:.96; }            /* MUST stay hoverable — see trap */
#view-editor.peek #edHero .edtools, #view-editor.peek #edBack { visibility:hidden; }
#view-editor.pinned { opacity:1; }
```

`showView('editor')`: early branch — keep `#view-wiki.on`, add `.on` to the editor, call
`placeEditorCard()` (reads `#heroOverview.getBoundingClientRect()` → `--edX` = left,
`--edY` = vertical centre of the overview so the card's top edge sits mid-overview).
Every other `showView(v)` removes `.on/.peek/.pinned` from the editor.
`closeEditor` no longer calls `showView(home)` when the wiki is already on — just drops `.on`.

## State machine (IIFE after `let edFrom`)

- `heroRow()` = the `#view-wiki .topic` whose `.tname` equals `#heroTitle` text.
- overview `pointerenter` → 160ms → `openEditor(row)` + `.peek`.
- Close only when pointer is outside BOTH: flags `overOv/overEd` set on enter/leave of overview
  and card; `maybeHide()` = ONE `requestAnimationFrame` (was 260ms — Chris: "disappear instantly
  if I don't have it locked"; one frame is all the overview→card hand-off needs).
- `pin()` = overview click or card `pointerdown` while peeking → `.pinned`, toolbar visible.
- `document.pointerdown` (capture) outside card+overview while pinned → `closeEditor(true)` (save)
  AND swallow that press: `preventDefault(); stopImmediatePropagation()`, then one-shot capture
  listeners eat the matching `pointerup`/`mouseup`/`click` (`{capture:true, once:true}`, click guard
  auto-removed after 400ms). Chris: "clicking off must not trigger the area underneath — but don't
  block it normally"; the NEXT press is untouched.
- Feed expanded (`#chat.open`) is z80 so it overlays even a pinned card (card z70).
- Arrow-key nav and Enter-to-open skip when `#view-editor.on`.

## Trap

First cut had `.peek { pointer-events:none }` so the preview "wouldn't steal the mouse" — the
card then disappeared the moment the pointer left the overview (leave fired, nothing could hold
it). Vision reported "empty white-bordered box" because the capture landed mid-close. The DOM
readout (`document.title='ED cls=… rect=… edBody.children=1 inner=CONTEXT …'` via
`drive_preview elements max=1`) proved content was present and pinned — trust that over vision.

## Verification recipe

1. `drive_preview reload` → `click selector=#heroOverview` (pins).
2. `elements max=1` → title readout shows `cls=view on pinned rect=26,121,1086,478 edBody.children=1`.
3. Strip the TEMP title hook; re-check `node --check` + brace balance (`scripts/vault-live-check.py`).
