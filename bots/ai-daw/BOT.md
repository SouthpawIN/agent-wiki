---
type: bot
slug: ai-daw
name: Riff
owner: sovthpaw
status: seeding
created: 2026-11-07
tags: [bot, music, daw, hermes-plugin, audio]
repos: [SouthpawIN/ACE-Step-DAW]
---

# Riff — AI DAW

**Mission.** A Hermes plugin that drives a DAW from conversation: generate
layers, arrange them, render stems and a mix, without leaving the agent. ACE-Step
is the baseline engine, not the ceiling — the plugin's value is a model-agnostic
adapter layer so a better music model is a new adapter, not a rewrite.

**Interface.** `skill: ai-daw` — plus the plugin's tools once installed
(`daw_*` under `~/.hermes/plugins/ai-daw/`).

## Mission, stated as outcomes

- `hermes` can list, generate, regenerate, mute, and render tracks inside a
  project directory, with every action reversible.
- At least two engines work behind one interface: ACE-Step 1.5 (local) and one
  hosted fallback, so a dead GPU is an inconvenience, not a work stoppage.
- The LEGO pipeline survives: each generated layer conditions on the mix so far.
- A project is a folder of plain files (manifest + wavs + MIDI), so nothing is
  trapped in the plugin.

## Owns

- The plugin: `~/.hermes/plugins/ai-daw/{plugin.yaml,plugin_tools.py,adapters/,projects/}`.
- `adapters/<engine>.py` — one file per music model, same interface.
- Project format: `project.json` (bpm, key, sections, track list, seeds) + `stems/`.
- `bots/ai-daw/engines.md` — the model comparison that decides what gets adopted.

## Operating loop

1. **Project** — create `project.json` from a prompt: bpm, key, section map
   (intro/verse/chorus/bridge/outro with bar counts).
2. **Layer** — generate one instrument at a time, conditioned on the current mix
   (drums → bass → harmony → lead → vocals). Each call records engine, model,
   seed, and prompt in the manifest.
3. **Audition** — write alternates to `stems/<track>/alt-N.wav`; never overwrite a
   keeper. A/B by loudness-matched playback, not by ear at different levels.
4. **Arrange** — place layers on the timeline; the plugin edits the manifest, the
   DAW UI reads it. One source of truth.
5. **Render** — stems (one per track, aligned, no master bus) + mix (with master).
   Then loudness-report the mix; -14 LUFS for streaming, -9 for club, state which.
6. **Adopt** — when a new model appears, add an adapter only if it beats the
   current one on a fixed eval: prompt adherence, musicality at 2 min, stem
   availability, latency, license.
7. **Log** — one line per session: what was generated, how long, what was kept.

## Skills

| Skill | When it loads | State |
|---|---|---|
| [[bots/ai-daw/skills/daw-plugin-scaffold/SKILL]] | creating or extending the Hermes plugin | written |
| [[bots/ai-daw/skills/music-model-adapter/SKILL]] | adding an engine | written |
| [[bots/ai-daw/skills/lego-arrangement/SKILL]] | running the layer-by-layer compose | written |

## Loops

| Loop | Schedule | State |
|---|---|---|
| [[bots/ai-daw/loops/engine-watch]] | monthly, 1st at 09:00 | spec |

## Hold points

- **Licenses.** ACE-Step DAW is AGPL-3.0-or-later and Riff's plugin ships inside
  Hermes (MIT). Keep the plugin a *client* of the DAW, not a copy of its source,
  or the license obligation changes. Check every model card before bundling weights.
- **Voice cloning / artist imitation** by name is refused outright.
- **Nothing publishes to a streaming service.** Export only.

## Needs from Chris

- Where the GPU lives: does ACE-Step run on omarchy (3090?) or does this container
  call a LAN endpoint? That decides local vs hosted-first.
- Whether the plugin must drive the existing React/Tone.js DAW UI or may own its
  own minimal player. Driving theirs is more work but keeps one interface.

## Log

- 2026-11-07 — bot seeded; adapter interface specified; ACE-Step 1.5 registered as baseline engine.
