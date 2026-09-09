---
name: wiki-overlay-z-order
description: Use when any wiki UI change touches layering. Keep chat + music HUD topmost and hit-test-prove it.
version: 0.1.0
distilled: 2026-09-05 17:35
topic: senter
---
# wiki-overlay-z-order
# Wiki overlay z-order

Locked layers (vault-live.html): music HUD z=120, side chat z=110–130, cards z=70. Everything else (topic panes, feed, mind-map, backdrop) sits below 70.

## Steps for every UI change
1. Before editing, grep the changed component for `z-index`; if it is ≥ 70 and is not chat/HUD/card, lower it.
2. After editing, hit-test in the DOM: `document.elementFromPoint(cx, cy)` at the centre of the Play button and at the chat input must return those elements (or a descendant), never a card/pane.
3. Also hit-test while a topic is open and a card is showing — layering bugs only appear under concurrency.
4. Record the proof (element returned per point) in the done line; a described fix without the elementFromPoint result is not done.

## Rules
- Chat and music are never covered, dimmed, or pointer-blocked by wiki activity; Chris must be able to control music while workers edit the wiki.
- Do not raise a new element above 70 to 'win' a bug — fix the offending element instead (root-cause rule).
- Mute zone / transport buttons: z-index proven over the backdrop, per the earlier DOM-proven fix.

## Pitfalls
- `pointer-events: none` on an overlay wrapper silently kills the Play hit; hit-test after every wrapper change.
- Stacking contexts (transform/opacity on a parent) reset z-index — check the parent chain, not just the value.

## Evidence
> I want to make sure that the side chat and the music player are always overlaid over everything and are not interrupted by anything. So I can control the music as you're playing around with the wiki
> Play button is the top hit at its own centre, HUD 120 / chat 110–130 / cards 70. Clean up and record:
