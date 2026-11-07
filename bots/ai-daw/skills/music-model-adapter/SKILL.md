---
name: music-model-adapter
description: Add or evaluate a music generation engine behind one interface.
version: 1.0.0
author: Riff
license: MIT
metadata:
  hermes:
    tags: [music, models, adapter, evaluation]
---

# Music model adapter

ACE-Step 1.5 is the baseline. Everything else is judged against it on the same
prompt set.

## Interface (every adapter implements)

```python
class MusicEngine(Protocol):
    name: str
    def capabilities(self) -> dict:   # duration_s, vocals, stems, bpm_key_cond, streaming, local, license
    def generate(self, req: GenerationRequest) -> GenerationResult
    def health(self) -> bool
```

`GenerationRequest`: `{prompt, lyrics, duration_s, bpm, key, seed, stems_wanted,
reference_audio, section_map}`. `GenerationResult`: `{audio_paths, stems,
seed_used, model, cost, elapsed_s}`.

## Candidates and what they are good at

| Engine | Strength | Watch |
|---|---|---|
| ACE-Step 1.5 (local) | fast, layer/LEGO conditioning, Apache-style open weights | quality ceiling; check the model card |
| MusicGen / AudioCraft (local) | melody conditioning, short clips | 30 s ceiling, no stems |
| Stable Audio Open (local) | texture and loops | short, no vocals |
| YuE (local) | full songs with vocals | slow, heavy VRAM |
| DiffRhythm (local) | full-length song from lyrics | less controllable structure |
| Hosted APIs | quality, no GPU | per-generation cost, licensing of output |

## Procedure

1. Read the model card: license, weights availability, sample rate, max duration,
   whether stems are native or must be separated (Demucs) post-hoc.
2. Write `adapters/<engine>.py` implementing the interface. Wrap the real API —
   do not reimplement inference.
3. **Health check** before every batch: a 5 s silent render must succeed, or the
   adapter is marked down and the plugin falls back to the next engine in order.
4. **Fixed eval set** — 6 prompts that stress different things: bpm-locked house,
   key-locked ballad, vocal hook, instrumental loop, 2-minute structure, a
   re-generate with same seed. Score 1–5 on prompt adherence, musical coherence,
   and editability (stems + MIDI extractability).
5. **Adopt only on evidence**: beats baseline on the eval AND is not slower than
   2× the baseline for interactive use.
6. Record the verdict in `bots/ai-daw/engines.md` with date, versions, and the
   eval scores. Recommendations rot; scores decay gracefully.

## Refusals

- Voice cloning of a named artist, or "in the style of <living artist>" prompts.
- Models whose license forbids commercial output, if the project is commercial.
