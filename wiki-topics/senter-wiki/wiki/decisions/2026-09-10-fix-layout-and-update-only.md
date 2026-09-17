---
title: "Fix the layout and fix the update — only those two"
created: 2026-09-10
updated: 2026-09-10
type: decision
tags: [decision, preference, ui, chris, plan]
sources: [raw/inbox/2026-09-10.md]
confidence: high
---

## What Chris said

> "Hey, I need you to fix the layout and fix the update. Don't do anything else just do those two because I've been asking you to keep getting stuck"  
> — chris · 2026-09-10 09:51 · ^[raw/inbox/2026-09-10.md]

Chris narrows the [[wiki-topics/senter-wiki/wiki/concepts/proactive-completion-directive|proactive-completion directive]] to exactly two objectives for this pass: the **layout** and the **update**. He has been circling these two and getting stuck, and he wants them both finished end to end without further confirmation or scope creep.

## Scope (exactly two)

1. Fix the layout — [[wiki-topics/senter-wiki/wiki/entities/vault-live-html|vault-live.html]] layout issues, row geometry, dot placement, hero orbs, HUD cluster, side chat alignment, and any positioning regressions from the recent restoration work.
2. Fix the update — the live update flow: how vault-live.html and the wiki pages propagate into the Hermes preview pane, the [[wiki-topics/senter-wiki/wiki/entities/senter-bridge|/file]] route and `.system-live.json` serving, and the [[wiki-topics/senter-wiki/wiki/entities/context-card-live-diff|live diff]] rendering.

## Out of scope

Everything else. No music player, no star map, no headphone EQ, no new bots-profiles/triggers-loops/skills unless they directly service layout or update. This is the "close, not quite it" round made surgical.

## Reasoning

Chris's 09:10 directive extends the 2026-09-09 proactive completion order with a specificity constraint: "I've been asking you to keep getting stuck." The root cause is scope creep in the restoration — layout and update fixes were being interleaved with broader feature work. Narrowing to two objectives removes the friction of partial passes and lets the agent land both ends cleanly before any further polish.

## Links

- [[wiki-topics/senter-wiki/wiki/concepts/proactive-completion-directive|Proactive completion directive]]
- [[wiki-topics/senter-wiki/wiki/entities/vault-live-html|vault-live.html]]
- [[wiki-topics/senter-wiki/wiki/concepts/hand-placement-mode|Hand-placement mode]]
- [[wiki-topics/senter-wiki/wiki/concepts/row-geometry-and-dot-column|Row geometry and dot column]]
- [[wiki-topics/senter-wiki/wiki/entities/context-card-live-diff|Context card live diff]]
- [[wiki-topics/senter-wiki/wiki/entities/senter-bridge|senter-bridge]]
