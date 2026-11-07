---
name: track-kit
description: Build kart tracks from a spline kit instead of modelling each one.
version: 1.0.0
author: Apex
license: MIT
metadata:
  hermes:
    tags: [unity, tracks, splines, level-design]
---

# Track kit

Eight tracks from one kit: a spline defines the road, everything else derives
from it. Hand-modelled tracks cost a week each and drift out of tune.

## Procedure

1. **Center spline** — closed loop, 8–14 control points, min turn radius ≥ 18 m so
   karts at top speed can hold the line with a drift.
2. **Road mesh** — extrude 12 m wide, 4 segments across, UVs continuous along the
   spline so the texture does not swim.
3. **Walls** — offset ±7 m, extruded 2 m tall, with a soft collision material
   (bounce 0.1, friction 0.4) so hits scrub speed instead of stopping dead.
4. **Checkpoints** — every 15 % of spline length, in order, as trigger volumes;
   lap validation requires all checkpoints in sequence (anti-shortcut).
5. **Item boxes** — rows of 3–5 along the spline at 55–75 % width offset, respawn
   4 s after pickup.
6. **Respawn volumes** — a falling kart returns to the last checkpoint facing
   forward, 8 m above the road.
7. **Shortcuts** — exactly one per track, and it must cost time if missed. A
   shortcut that is never risky is just a wider road.
8. **Validate** — drive a full lap at max speed with no wall clip; confirm a
   deliberate wrong-way drive does not count a lap.

## Cup assembly

Four tracks per cup, difficulty ramps: wide/fast → technical → hazard-heavy →
finale with a signature set piece. Cup points 15/12/10/8/6/4/2/1.
