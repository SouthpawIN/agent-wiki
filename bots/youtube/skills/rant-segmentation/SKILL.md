---
name: rant-segmentation
description: Group a long rambling recording into topic-coherent video candidates.
version: 1.0.0
author: Cutroom
license: MIT
metadata:
  hermes:
    tags: [transcript, segmentation, youtube, whisper]
---

# Rant segmentation

Input: `transcript.json` (word-level timestamps). Output: `segments.json`.
This is the skill that decides what the video is *about*; everything downstream
inherits its mistakes.

## Procedure

1. **Load words**, not lines. Lines are an artifact of whisper's chunking and
   will cut mid-sentence at topic jumps.
2. **Find hard boundaries** — gaps ≥ 2.5 s with no words, or a laugh/applause
   burst. Record `gap` seconds at each boundary.
3. **Score window topics.** For each 60-word window compute top TF-IDF terms
   after removing filler (`like, right, kinda, you know, dude, chat`).
4. **Merge** adjacent windows with ≥ 2 shared terms into a chunk. A chunk under
   45 s is absorbed into its neighbor; over 25 min is split at its weakest gap.
5. **Name each chunk** with a 3–6 word title from its distinctive terms, plus
   one `hook_line`: the single sentence in the first 20 s that best states the
   claim (longest declarative sentence containing a top term).
6. **Score**
   - `hook`: 1.0 if a claim lands in the first 8 s, decaying to 0 at 40 s.
   - `density`: words/min ÷ 180, capped at 1.5.
   - `reaction`: 1.0 if laughter/applause within the chunk.
   - `visual`: 1.0 if the chunk references something on screen ("look at this",
     "watch", a game title, a clip).
   - `rank = 0.4*hook + 0.25*density + 0.15*reaction + 0.2*visual`
7. **Write `segments.json`** — array sorted by `rank` desc, each with
   `{id, start, end, title, hook_line, rank, terms, boundaries}`. Keep an
   `unranked` copy sorted by time for the "full session" cut.
8. **Report** the top 5 with one line each and the total hours available.

## Calibration rule

Thresholds above are defaults. After the first real session, re-fit `density`
and gap length against Chris's own picks and record the delta in
`.system/continuity.md`. Never tune on a synthetic clip.
