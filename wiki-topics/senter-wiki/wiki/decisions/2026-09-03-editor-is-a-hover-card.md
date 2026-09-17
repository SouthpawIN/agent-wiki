---
title: Decision: the editor is a hover card over the wiki, not a page
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, ui]
sources:
  - raw/sources/knowledge/ref-vault-live-editor-card-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md
confidence: high
---

# Editor is a hover card (2026-09-03, late)

**What.** Replaces the separate editor page. Hover the hero overview → card peeks; click → pinned/editable; click outside → close + save (bridge `POST /write`).
Same `#view-editor` DOM and `openEditor/closeEditor/edSave` logic — *"presentation only."* ^[raw/sources/knowledge/ref-vault-live-editor-card-2026-09-03.md]

**Chris's ask, twice.** First (afternoon, queued): *"consolidate the editor page so that when you mouse over the preview it will expand it. If you click on it, then it will lock
it so the user can edit the item as it's up there … a quick markdown editor for each one of these items."* Then (late): *"I don't want a different editor page. I still want that
editor though … as an overlay; that's the HTML editor."* ^[raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md]

**Why.** Pages broke flow (browser back left the editor open; reload restored a sticky `#bots-profiles/<name>` hash). **Constraints he added.** Instant disappear when not locked;
click-off must not hit the page underneath but the next press must work. See [[wiki-topics/senter-wiki/wiki/concepts/hover-card-contract|hover-card contract]] and [[wiki-topics/senter-wiki/wiki/entities/vault-live-html|vault-live.html]].
