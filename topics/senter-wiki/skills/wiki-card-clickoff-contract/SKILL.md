---
name: wiki-card-clickoff-contract
description: Use when adding any overlay/card to the Senter wiki. Peek→pin→click-off-saves; the closing press is swallowed once, the next press is live; chrome and cards are never dead zone.
version: 0.1.0
distilled: 2026-09-05
topic: senter-wiki
---
# wiki-card-clickoff-contract

Every card in vault-live.html (editor `#view-editor`, settings `#warnMask.settings`, future ASK/HISTORY cards) obeys ONE contract. Chris compares them side by side.

## Contract
1. **Look**: `position:fixed`, `background:#000`, 1px `var(--paper)` border (feed-card style). Shell/mask is transparent + `pointer-events:none`; only the card body takes events. Never dim the page behind ("settings should not make everything else go black … overlay everything instead of making everything else hide").
2. **States**: hover source → *peek* after ~160ms (toolbar hidden, STILL hoverable — never `pointer-events:none` on peek); click source or card → *pinned* (editable); pointerdown outside → close (+save).
3. **Close timing**: unpinned card closes when the pointer is outside BOTH source and card, on the next `requestAnimationFrame`. No grace delay — Chris: "disappear instantly if I don't have it locked"; 260ms was "delays half a second".
4. **Swallow**: the closing `pointerdown` is `preventDefault(); stopImmediatePropagation()`; one-shot capture eaters take the matching `pointerup`/`mouseup`/`click` (click guard removed after 400ms). The NEXT press is untouched ("clicking off must not trigger the area underneath — but don't block it normally"). Install the document listener on the next tick so the opening click is not eaten.
5. **Canonical state set inside the opener** (`openEditor()` etc.), not per entry path; the click-off guard fires on "card is open", not one sub-state — otherwise row/Enter/star/deep-link opens fall through to the dead zone and open SPACE behind the card.
6. **Dead zone excludes chrome + cards**: `mousemove`/click use `closest('.hero, #hudCluster, #warnMask, #view-editor')`. `showView()` must never end with zero views on (fallback `view-wiki`). Every close path lands on the wiki explicitly.
7. **Anchoring** is derived from a real rect (`#heroOverview` → `--edX/--edY`; gear rect + `#heroLine.left` → `--setY/--setR/--setL`) plus ONE named nudge knob (`--setNudge`) — Chris tunes by feel (10 → 40px).
8. **Layers**: feed expanded (`#chat.open`) out-ranks every card and hides the HUD; HUD 120 > chat 110/130 > settings 90 > editor 70 > hero 40.

## Verify
`document.title='ED cls='+el.className+' rect='+[...]` from a temp handler → `drive_preview elements max=1`. Vision reported an "empty white-bordered box" when the capture landed mid-close; the DOM readout proved content present. Strip `TEMP-` hooks after.

## Evidence
> "I don't want a different editor page. I still want that editor though … as an overlay; that's the HTML editor. If the user clicks then it stays in place so they can edit; click outside the window to close and save."
> "settings should not make everything else go black … overlay everything instead of making everything else hide."
> "When I back out of settings, I'm in nowhere — the back room, a blank space."
