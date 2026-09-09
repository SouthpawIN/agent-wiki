---
name: wiki-hit-zone-layering
description: Use when adding or changing an invisible click/hover zone in the Senter wiki. Lift real controls above the zone, scope openers to one element, and probe-click every neighbour before claiming done.
version: 0.1.0-proposed
proposed: 2026-09-05 17:06
topic: senter-wiki
---
# wiki-hit-zone-layering
# Wiki hit-zone layering

Invisible interaction zones (media area, dead zone, feed hover) keep stealing clicks from real controls. Every zone change follows this loop.

## Steps
1. Measure the zone from the DOM (`getBoundingClientRect`) — write its edges as derived CSS vars (e.g. `--eqLeft`), never literal px.
2. Give the zone the LOWEST stacking level and explicitly raise every real control inside its rect (`position:relative; z-index` above it). A `position:fixed; z-index:0` zone still paints over `z-index:auto` buttons — that is the bug Chris hit.
3. Scope 'open' handlers to one element (`#mNow` for the player), not the whole widget; swallow other clicks so nothing opens by accident.
4. Enumerate which behaviours must coexist inside the rect (transport buttons work, title opens player, zone click toggles mute, wheel moves level) and probe-click EACH with `elementFromPoint` / synthetic click; report the hit target per probe.
5. Verify in Chris's real window (wiki-look-verify) before the done line.

## Rules
- Zone edges come from the layout (EQ placer, feed top, pane edge) so they survive resize.
- Anchor end caps and indicators to the stable container (track), not the value-driven element (fill) that collapses to 0.
- Never fix an overlap by shrinking the zone — fix stacking order (root cause).

## Pitfalls
- Fixed zones with `z-index:0` beat unpositioned siblings.
- Any-click-on-widget openers (old line ~2421) trip the zone; restrict them.
- Chris reports overlap as 'buttons mute and unmute' — that is a stacking bug, not a handler bug.

## Evidence
> Okay, so a little issue is right now if I click the player buttons they mute and unmute So it's like that's overlapping that I still want the player buttons to work And I still want clicking on the artist or the title right below the player buttons to open up the media player
> Confirmed: the fixed zone (`z-index:0`) paints *over* the buttons and title, which have `z-index:auto` — so every click lands on the zone. Lift the real controls above it
> Line 2421: any click on the widget that isn't a button opens the player. Restrict to `#mNow` (title/artist)
> Zone spans x 936 (EQ left) → 1152 (edge), y 0 → 416, and a probe click inside lands on the zone.
