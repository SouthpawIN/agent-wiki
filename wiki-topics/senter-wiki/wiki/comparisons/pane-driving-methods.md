---
title: Ways to drive/verify the preview pane, compared
created: 2026-09-05
updated: 2026-09-05
type: comparison
tags: [tool, skill, ui]
sources:
  - raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
  - raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md
confidence: high
---

# Driving the pane — what works and what cost rounds

| Method | Fires page handlers? | Verdict |
|---|---|---|
| `computer_use` / `cua-driver` foreground keys to pid Hermes | no — focus is the chat composer; **Escape = Stop agent** (self-cancelled ×4) | never for page work |
| background `cua-driver call click x,y window_id=4956` | no — routes via AX, "succeeds" and does nothing | no |
| URL hash `#q=…&k=…` / `?eqdemo` | rewritten/stripped during boot → unranked | human deep link only, not a harness |
| **`drive_preview click/type/hover/press` by selector** | yes — the real pane Chris watches | THE method; needs real elements (`#heroGap`, on-screen `#senterHiddenInput`) |
| visible fixed `<button id=…>` + `drive_preview click` | yes | demo/debug triggers |
| node script over `.system-live.json` | n/a | supplement for pure ranking logic |
| `desktop_preview read` | read-only, 24k cap | order/caption proof |
| `drive_preview elements max=1` → `document.title` | read-only, full length | cleanest geometry/state proof |
| `screencapture` + `vision_analyze` | read-only | last resort; crop errors, misses 3px, needs immediate capture |
^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md] ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

Chris's requirement that ranks them: *"practice your computer use, not work around."* See [[wiki-topics/senter-wiki/wiki/entities/hermes-preview-pane-and-drive-preview|preview pane]],
[[wiki-topics/senter-wiki/wiki/concepts/verification-and-proof-methods|proof methods]].
