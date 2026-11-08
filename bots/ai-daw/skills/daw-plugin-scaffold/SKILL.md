---
name: daw-plugin-scaffold
description: Scaffold a Hermes plugin that controls a DAW through tools.
version: 1.0.0
author: Riff
license: MIT
metadata:
  hermes:
    tags: [hermes, plugin, daw, tools, python]
---

# DAW plugin scaffold

## The implementation

`bots/ai-daw/plugin/` is this scaffold, built and tested:

```
plugin.yaml            six daw_* tools, python_runtime: external (stdlib + ffmpeg)
plugin_tools.py        thin wrappers: resolve project id -> daw.core -> small dict
daw/core.py            Project: manifest, generate_layer, reference_mix, render_stems, render_mix
daw/adapters/base.py   MusicEngine protocol + get_engine()
daw/adapters/dryrun.py ffmpeg lavfi voices per instrument - real audio, no GPU
daw/adapters/acestep.py HTTP client for a local ACE-Step server
```

Run it: `PYTHONPATH=bots/ai-daw/plugin python -m pytest bots/ai-daw/tests -q`.

## Procedure

1. **Create the plugin directory** next to the other Hermes plugins:
   ```
   ~/.hermes/plugins/ai-daw/
   ├── plugin.yaml          # name, version, description, tools list
   ├── plugin_tools.py      # tool implementations, one function per tool
   ├── adapters/base.py     # MusicEngine interface
   ├── adapters/acestep.py  # local engine
   └── projects/            # user projects (plain files)
   ```
2. **Declare tools, verbs first.** Minimum viable surface:
   `daw_project_create`, `daw_layer_generate`, `daw_layer_regenerate`,
   `daw_track_set`, `daw_render_stems`, `daw_render_mix`, `daw_project_status`.
   Each tool takes a `project` id, never an absolute path from the model.
3. **Keep tool returns small.** Return ids and file paths, not audio bytes or
   long JSON. The agent loops on ids; a 4 MB base64 payload poisons the context.
4. **Idempotency**: `daw_layer_generate` with the same `project/track/seed/prompt`
   must return the existing stem rather than regenerate. Cheap and prevents
   accidental spend on hosted engines.
5. **Manifest is the API**: `project.json` holds `{bpm, key, sections[], tracks[]}`
   where each track is `{id, instrument, engine, model, seed, prompt, files[],
   gain_db, muted, version}`. The UI and the agent both read it.
6. **Failure surface**: every tool returns `{ok, error, hint}`. A missing model
   returns the adapter's install hint, not a traceback.
7. **Verify** by running one full cycle headless: create → generate drums →
   generate bass conditioned on drums → render stems → render mix → `ffprobe`
   durations are equal. Only then expose the tools.
8. **Document** each tool in `plugin.yaml` with a one-line description and an
   example call, because that description is what the model sees.

## Rules

- Never shell out with an unquoted prompt. Write a request file and pass the path.
- Bound every render with a timeout and a max duration; a 12-minute generation
  that hangs must die, not block the session.
- No absolute paths in prompts or manifests — projects are relative to `projects/`.
