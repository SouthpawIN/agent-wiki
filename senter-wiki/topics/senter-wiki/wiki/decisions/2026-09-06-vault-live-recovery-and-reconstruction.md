---
title: "Decision 2026-09-06: vault-live.html damage recovery and feature reconstruction"
created: 2026-09-06
updated: 2026-09-06
type: decision
tags: [decision, ui, pain, infra]
sources:
  - raw/inbox/2026-09-06.md
confidence: medium
contested: true
---

# Decision 2026-09-06: vault-live.html damage recovery and feature reconstruction

## Incident
During the diff-badge experiment on 2026-09-06, `vault-live.html` was damaged: 271 KB with no `</style>`. The page rendered black and the music player, settings, wallpaper, and nav routing all failed to initialize. ^[raw/inbox/2026-09-06.md]

## Failed restores
Restoring `/tmp/vault-live.before.html` (318 KB, Sept 3) and `/tmp/vc139.js` initially looked like fixes, but both lacked the recent good-state additions from the 2026-09-05 session: `window.mdRender`, `--orbShift`, and the BRIEF layer. Chris noted: *"You need to, um, so like this is like the backup one. We just had a good one where all the dots were in the middle. We just made a bunch of recent changes."* (01:36) ^[raw/inbox/2026-09-06.md]

## Reconstructed pieces (verified)
After stopping blind retries, Hermes rebuilt the missing pieces on top of a clean backup:

- **Hover anchor** — `pointerover` sets `data-anchored` on `.orbs`; CSS `.orbs[data-anchored] { transform:translateX(var(--orbShift,0px)) }` shifts the container so the hovered orb stays under the cursor while siblings grow around it. `pointerout` clears the attribute. ^[raw/inbox/2026-09-06.md]
- **Diff badges + usage** — `mkTopic` accepts `diffbadge` and `usage` params; `refreshWikiOrbs` reads `.system-live.json`, computes day-over-day delta, inserts `.usage` then `.diffbadge` before `.tname`. ^[raw/inbox/2026-09-06.md]
- **Chat gutter** — `#chat { right:4px }` (was `14px`), closing the gap between side chat and expanded content. ^[raw/inbox/2026-09-06.md]
- **Boot crash fix** — the editor module ended with `return {..., md, ...}` but `md` no longer existed under that name after it became `window.mdRender`. Pointing at `window.mdRender` explicitly stopped the load-time throw that killed initialization of everything below the editor. ^[raw/inbox/2026-09-06.md]
- **Dot centering** — the orb cluster now uses equal auto margins so every row's dots line up in the middle instead of trailing the title. ^[raw/inbox/2026-09-06.md]

## Status
File is structurally valid, JS parses clean, and the known-good behaviors are reconstructed. The exact pre-diff pixel state cannot be guaranteed without a backup of the exact good file; verified by DOM readouts and local vision on a free aux model. ^[raw/inbox/2026-09-06.md]

## Root cause chain
1. Row-geometry experiment added `.rdiff` and changed selectors.
2. A rollback deleted large sections of the page.
3. Restore picked an older backup that lacked 2026-09-05 additions.
4. Subsequent patches re-introduced `md` binding that no longer existed.

## Related
[[topics/senter-wiki/wiki/entities/vault-live-html|vault-live.html]], [[topics/senter-wiki/wiki/decisions/2026-09-05-markdown-titles-render-in-context-card|markdown render fix]], [[topics/senter-wiki/wiki/queries/first-compile-results-2026-09-05|first compile results]]
