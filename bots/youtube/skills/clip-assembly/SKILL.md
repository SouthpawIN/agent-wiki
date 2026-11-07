---
name: clip-assembly
description: Render ranked segments into a finished 1080p60 video with clean audio.
version: 1.0.0
author: Cutroom
license: MIT
metadata:
  hermes:
    tags: [ffmpeg, render, edl, youtube]
---

# Clip assembly

Input: `segments.json` + source media. Output: `render.mp4` + `edl.json`.

## Procedure

1. **Build the EDL first**, as JSON, before touching ffmpeg:
   ```json
   {"segments":[{"src":"session.mp4","in":128.4,"out":402.9,
                 "transition_in":"fade","lower_third":"sovthpaw"}],
    "audio":{"target_lufs":-14,"true_peak":-1.5,"lra":11}}
   ```
2. **Pad cuts.** Start 0.6 s before the hook line, end 0.8 s after the last word.
   Trimming to the exact word is the single most common amateur tell.
3. **Cut accurately** — put `-ss` *before* `-i` for speed, but on long sources
   cut on the nearest keyframe then trim with `-ss` after `-i`:
   ```bash
   ffmpeg -ss "$IN" -to "$OUT" -i src.mp4 -c:v libx264 -preset slow -crf 18 \
          -r 60 -pix_fmt yuv420p -c:a aac -b:a 192k part.mp4
   ```
4. **Normalize audio once, at the end** — never per part, or levels pump between
   segments:
   ```bash
   ffmpeg -i concat.mp4 -af loudnorm=I=-14:TP=-1.5:LRA=11 -c:v copy out.mp4
   ```
5. **Concat** with the concat demuxer on identical-encoded parts, not the filter.
6. **Dress** — title card 3 s, lower third on name first-appearance only,
   chapter card at each segment start if the segments are presented as chapters.
7. **Verify before declaring done**: `ffprobe` duration ±1 s of EDL total, no
   black frames over 0.5 s, audio peak ≤ -1.0 dBTP, moov atom present.
8. **Emit** `edl.json`, `render.mp4`, and a one-line render report (duration,
   bitrate, loudness, dropped segments and why).

## Rules

- Never re-encode twice. One cut pass, one loudnorm pass.
- If a segment's source is variable-frame-rate (OBS default), force CFR 60 first.
- 1080p60 unless the source is lower; never upscale to fake 4K.
