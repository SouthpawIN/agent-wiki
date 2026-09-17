---
title: "UI layout regression after diff view change"
created: 2026-09-06
updated: 2026-09-08
type: entity
tags:
  - ui
  - pain
  - preference
sources:
  - raw/inbox/2026-09-06.md
  - raw/inbox/2026-09-08.md
confidence: high
---

# UI layout regression after diff view change

## What happened
Chris asked for a small change — show diffs — and instead elements shifted to the right and then worsened to a black screen. He explicitly stated the UI ended up further from where it was, not closer.

> "I only asked for the diffs to be shown and then everything got pushed to the right. I need them back where it was." ^[raw/inbox/2026-09-06.md]
> "No, now it's even more broken. Now I just see a black screen. Come on, we're getting further away. I asked for a small change. This was almost done." ^[raw/inbox/2026-09-06.md]
> "They're not lined up like right now. And the navigation at the top and almost everything is gone." ^[raw/inbox/2026-09-06.md]

## Escalation
The regression worsened to a black screen. Top navigation and most elements disappeared, leaving Chris unable to confirm progress.

> "No, now it's even more broken. Now I just see a black screen. Come on, we're getting further away. I asked for a small change. This was almost done." ^[raw/inbox/2026-09-06.md]
> "They're not lined up like right now. And the navigation at the top and almost everything is gone." ^[raw/inbox/2026-09-06.md]

He used a test prompt afterward to probe whether the surface was actually restored.

^[raw/inbox/2026-09-06-from-klerik.md]

## Restoration verification
A later session turn reported UI restoration as complete, with verification intent centered on checking the restored state.

> "The UI restoration is complete. Let me verify the final state by checking a few key elements:" ^[raw/inbox/2026-09-08.md]

The raw item does not add a new regression, but it confirms Chris kept the UI-restoration surface under verification rather than accepting completion from internal work alone.

## Related
- [[topics-wiki/back-where/wiki/entities/model-picker-persistence|Model picker persistence until fallback]]
- [[topics-wiki/back-where/wiki/queries/restoration-and-billing|Restoration and billing]]
