---
name: lego-arrangement
description: Compose a track layer by layer, each conditioned on the mix so far.
version: 1.0.0
author: Riff
license: MIT
metadata:
  hermes:
    tags: [composition, arrangement, stems, mixing]
---

# LEGO arrangement

The reason to use an AI DAW instead of a one-shot generator: every layer hears
what came before it.

## Procedure

1. **Skeleton first.** Set bpm, key, and a section map in bars. Everything
   downstream is conditioned on this; changing bpm later invalidates every stem.
2. **Order**: drums → bass → harmony (keys/guitar) → lead → vocals → ear candy.
   Conditioning target is the *cumulative* mix, rendered to a low-bitrate
   reference (mono, 32 kbps) so the adapter hears arrangement, not fidelity.
3. **One instrument per call.** Stop at a layer that works; do not batch five.
4. **Negative constraints are part of the prompt**: "no snare fills in the
   verses", "bass stays under 120 Hz", "no vocal ad-libs".
5. **Seeds**: keep the seed that produced a keeper. Regenerating with the same
   seed and a changed prompt is the fastest way to fix one bad layer.
6. **Loudness discipline**: generate at the engine's native level, then gain-stage
   each stem to -18 dBFS RMS before the mix bus. Never let a generated layer clip
   into the bus.
7. **Render**: stems aligned to bar 1, plus a reference mix. Report LUFS and true
   peak; if the mix is over -1 dBTP, fix the bus, not the stems.
8. **Version**: every keeper gets a `version` bump and a one-line note. "v3 —
   tighter kick, bass simplified in chorus".

## Stop conditions

- Three failed regenerations of the same layer → change the conditioning
  reference (it is almost always the skeleton, not the model).
- A layer that needs more than 3 alternates is usually a composition problem;
  say so instead of burning compute.
