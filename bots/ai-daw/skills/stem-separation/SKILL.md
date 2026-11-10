---
name: stem-separation
description: Recover stems from engines that cannot emit them, with Demucs, without lying about quality.
version: 1.0.0
author: Riff
license: MIT
metadata:
  hermes:
    tags: [music, stems, demucs, fallback, mixing]
---

# Stem separation

Not every engine gives you stems. MusicGen, Stable Audio Open, and most hosted
APIs hand back one mixed file. This skill turns that file into stems — and
records, in the project, the fact that they are *separated*, never *native*.

**Native always wins.** Separation is a downgrade: it invents information that
was never in the mix, and the artifacts are audible under a compressor. Run this
only when `capabilities()["stems"]` is `false`, and never re-run it over an
engine that already returned stems.

## When it loads

- An adapter returned `audio_paths` with no `stems`.
- The user asks for stems from a project mixed by such an engine.
- A render is requested and the project marked the track `stems_quality: separated`.

## Procedure

1. **Decide the mode before running anything.** Cheapest mode that answers the
   user's question:

   | Need | Model | Flags |
   |---|---|---|
   | vocals / instrumental split only | `htdemucs` | `--two-stems=vocals` |
   | four stems (vocals, drums, bass, other) | `htdemucs_ft` | — |
   | six stems (+ guitar, piano) | `htdemucs_6s` | — , slower, weaker guitar/piano |

   `htdemucs_ft` is 4× slower than `htdemucs` and clearly better on drums and
   vocals; use it for keepers, `htdemucs` for audition loops.

2. **Probe the source first.** Sample rate, channels, duration. Mono input is
   upmixed to stereo — allowed, but log it, because the separation model was
   trained on stereo and will hallucinate a phantom center. Do not resample the
   source to 48 k before separating; separate at the source rate, resample the
   output to the project rate afterwards.

3. **Run with explicit, recorded flags.** Determinism matters more than the last
   half dB:

   ```bash
   demucs --name htdemucs_ft --shifts 5 --overlap 0.25 --device cuda \
          --out "<project>/stems/<track>/sep" "<source>.wav"
   ```

   - `--shifts 5` for keepers (5 random offsets averaged), `--shifts 1` for
     auditions. Never leave it at the default and call it reproducible.
   - `--segment 7` when VRAM is tight; it costs speed, not much quality.
   - Write to `stems/<track>/sep/<model>/`, then rename into `stems/<track>/sep/`
     atomically. Never write over an existing separated set.

4. **Record provenance in `project.json`.** Under the track:

   ```json
   {"stems": ["vocals","drums","bass","other"],
    "stems_quality": "separated",
    "separated_from": "stems/<track>/v1.wav",
    "separation": {"tool": "demucs", "model": "htdemucs_ft", "shifts": 5, "version": "<demucs --version>"}}
   ```

   `stems_quality` is the honest field: `native` or `separated`. The renderer and
   the UI both read it, so a separated stem is never presented as isolated.

5. **Gate on reconstruction.** Sum the stems back and null against the source:

   ```bash
   ffmpeg -i vocals.wav -i drums.wav -i bass.wav -i other.wav \
          -filter_complex "[0][1][2][3]amix=inputs=4:normalize=0[m];[m]volume=1[s]"
   ```

   then mix `[s]` inverted with the source and measure RMS. A correct run nulls
   to roughly −60 dBFS on a 10 s window; anything above −40 dBFS means a
   misaligned or truncated stem — delete the set, keep the source as a single
   stem, and report the failure instead of shipping it.

6. **Use separated stems for mixing, not for conditioning.** Generating the next
   layer on top of a separated mix compounds bleed: vocals leak into "other",
   "other" conditions the next generation, and the leak doubles. Condition on the
   original mixed render unless the user explicitly asks otherwise.

## Budgets

- `htdemucs_ft` on a 3090: ~0.1× realtime. On this container's CPU: ~1.5×
  realtime, so a 4-minute track is ~6 minutes. Say the number before you start.
- No GPU and a track over 10 minutes: run `--two-stems=vocals` only, or refuse
  and offer the mixed file. Do not silently start an hour-long CPU job.

## Failure modes

| Symptom | Cause | Fix |
|---|---|---|
| CUDA OOM | segment too long for VRAM | `--device cpu --segment 7`, warn about time |
| Output length ≠ source | tail truncation | re-run with `--overlap 0.5`; verify with step 5 |
| Vocals bleed in "other" | normal, model limitation | label it; do not EQ the bleed away and claim isolation |
| Metallic cymbals | `htdemucs` (non-ft) on dense drums | re-run `htdemucs_ft` if it is a keeper |

## Refusals

- Separating a commercial track to redistribute the parts, or to publish a
  karaoke/instrumental version of someone else's recording.
- Presenting separated stems as studio multitracks, in the manifest, the UI, or
  a filename. The field `stems_quality: separated` stays.
