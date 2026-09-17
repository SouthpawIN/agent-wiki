---
title: Hover cards: editor, settings, click-off swallow contract
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [ui, spec, decision]
sources:
  - raw/sources/knowledge/ref-vault-live-editor-card-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-settings-card-2026-09-03.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
  - raw/sources/knowledge/ref-vault-live-eq-feed-2026-09-03.md
confidence: high
---

# Hover-card contract

Chris (2026-09-03): *"I don't want a different editor page. I still want that editor though … when something is selected, underneath the line there is the overview.
Hover over that and a window appears — like the hover cards we used for tags/integrations and the feed messages now — as an overlay; that's the HTML editor. If the user
clicks then it stays in place so they can edit; click outside the window to close and save."* ([[wiki-topics/senter-wiki/wiki/decisions/2026-09-03-editor-is-a-hover-card|decision]]) ^[raw/sources/knowledge/ref-vault-live-editor-card-2026-09-03.md]

## Card look
Black, 1px paper border (feed-card style: `#chat .mini .msg` / `#stream .msg` — NOT `.post`), `position:fixed`. Retired: the per-row `.hcard` hover cards
(`wireHoverCards()` returns first line); their look moved to the feed. ^[raw/sources/knowledge/ref-vault-live-eq-feed-2026-09-03.md]

## Editor card (`#view-editor`, z70)
- Anchored under `#heroOverview` via `--edX/--edY`; `showView('editor')` leaves the wiki ON.
- States: overview `pointerenter` → 160ms → **peek** (toolbar hidden); click overview / card pointerdown → **pinned** (editable); pointerdown outside → close + SAVE.
- Close only when the pointer is outside BOTH overview and card; `maybeHide()` = one `requestAnimationFrame` — Chris: *"disappear instantly if I don't have it locked"*,
  rejected a 260ms grace (*"delays half a second"*).
- Trap: `.peek { pointer-events:none }` made the card vanish the instant the pointer left the overview. Vision reported an "empty white-bordered box" (capture mid-close);
  the `document.title` DOM readout proved content present — *"trust that over vision."*
- Every open path (row click / Enter / star / deep link) must set the same canonical state inside `openEditor()`; the guard fires on "card is open", not one sub-state —
  otherwise click-off fell through to the dead zone and opened SPACE behind the card.
- Bottom bar `#edBar`: SHARE part toggles + COPY (markdown bundle) + SEND TO HERMES; hidden while peeking. Queued buttons: LOCK, HISTORY, ASK, OPEN IN OBSIDIAN. ^[raw/sources/knowledge/ref-vault-live-editor-card-2026-09-03.md] ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## Settings card (`#warnMask.settings`, z90)
Chris: *"settings should not make everything else go black … overlay everything instead of making everything else hide."* Shell transparent + `pointer-events:none`;
`.warn` black, anchored under the gear (`--setY = gear.bottom+12`, `--setR`), stretched left to `#heroLine.left` + `--setNudge`. His sizing sequence: *"a lot wider — to
where the other cards start"* → *"too far left — to the edge of the title and the line"* → *"shift it about 10 pixels"* → *"and about 30 more"* (nudge 40px, kept as a knob).
Gear click toggles; no CLOSE button. ([[wiki-topics/senter-wiki/wiki/decisions/2026-09-03-settings-is-a-card|decision]]) ^[raw/sources/knowledge/ref-vault-live-settings-card-2026-09-03.md]

## The swallow contract (shared)
Chris: *"clicking off must not trigger the area underneath — but don't block it normally."* Document-capture `pointerdown` outside the card → close (+save), `preventDefault();
stopImmediatePropagation()`, then one-shot capture eaters for the matching `pointerup`/`mouseup`/`click` (click guard auto-removed after 400ms). The NEXT press is untouched.
Installed on the next tick so the opening click isn't eaten. ^[raw/sources/knowledge/ref-vault-live-settings-card-2026-09-03.md]

## Layer rules
Feed expanded (`#chat.open`) out-ranks even a pinned card and hides the HUD; the dead zone never includes chrome or cards (`.hero, #hudCluster, #warnMask, #view-editor`);
`showView()` never ends with zero views on. Other `#warnMask` users (askBox, discard-warn, wallpaper pick) keep the 72 % dimmer on purpose. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
