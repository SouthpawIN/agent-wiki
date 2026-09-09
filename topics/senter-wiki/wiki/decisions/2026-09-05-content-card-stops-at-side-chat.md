---
title: "Decision 2026-09-05 19:06: the expanded content card fills up to the side chat and never overlaps it"
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, ui, pain, preference]
sources:
  - raw/inbox/2026-09-05.md
confidence: high
---

# Decision 2026-09-05 19:06: content card stops where the side chat starts

## Symptom (Chris)
> "Okay, so the full context when it opens up, I still don't like it even with the media player and the side chat over it. How about instead of expanding to fill the whole screen? How about it just fills up to where the side chat starts so that it never overlaps it. But then I can still look through that wiki as it goes. So I do not like the layout of it." (19:06) ^[raw/inbox/2026-09-05.md]

## What
The opened CONTEXT card no longer expands to the whole pane. Its right edge stops **14 px short of the side chat** — measured 684 vs the chat's left at 698 — so it *"never overlaps the feed or the player; you read the wiki while both stay live."* (19:12, DOM-proven) ^[raw/inbox/2026-09-05.md]

## Why
The [[topics/senter-wiki/wiki/entities/corner-feed|corner feed]], the [[topics/senter-wiki/wiki/entities/music-player|media player]] and the sidebar chat are how Chris watches the fleet and talks to it; a card that covers them takes the room away from the very things he reads while the wiki changes. Same instinct as the [[topics/senter-wiki/wiki/concepts/layer-stack|layer stack]] rule that the player and feed are never swallowed by a card.

## Knob
Card right edge = side-chat left − 14 px (derived from the chat's measured position, not a fixed width — see the "measured, not guessed" rule in [[topics/senter-wiki/wiki/concepts/row-geometry-and-dot-column|row geometry / derived anchors]]). Recorded in [[topics/senter-wiki/wiki/queries/ui-knob-registry|the knob registry]].

## Paired change
Same message, same fix pass: [[topics/senter-wiki/wiki/decisions/2026-09-05-context-is-the-wiki-with-live-diffs|CONTEXT is the wiki itself with live diffs]].
