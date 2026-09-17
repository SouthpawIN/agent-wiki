---
title: Decision 2026-09-03: the editor is a hover card over the wiki, not a page
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, ui]
sources:
  - raw/sources/knowledge/ref-vault-live-editor-card-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md
confidence: high
---

# Decision 2026-09-03: the editor is a hover card, not a page

## What
Chris: "I don't want a different editor page. I still want that editor though … Hover over [the overview] and a window appears — like the hover cards … as an overlay; that's the HTML editor. If the user clicks then it stays in place so they can edit; click outside the window to close and save." ^[raw/sources/knowledge/ref-vault-live-editor-card-2026-09-03.md]

## Why
The editor page broke navigation: reload restored `#bots/<name>` and overrode `#wiki`, browser back didn't close it, Enter didn't search while it was open. Chris's model is Cursor-like inline editing of the item under the cursor. ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md] ^[raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md]

## Result
[[topics/senter-wiki/wiki/entities/editor-card|Editor card]]: peek after 160 ms, pin on click, close+save on click-off with a one-shot swallow, one-frame hide (no grace). Same contract reused for the [[topics/senter-wiki/wiki/entities/settings-card|settings card]].
