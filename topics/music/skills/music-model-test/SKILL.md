---
name: music-model-test
description: Use when setting up or validating a local generative music model on Chris's Mac. Check memory budget, verify runner support, install missing runtime deps, run one generation test, report exact blockers.
version: 0.1.0
distilled: 2026-09-07 05:08
topic: music
---
# music-model-test
1. Inspect current MTPLX/memory state; abort if no headroom.
2. Confirm model file exists and size matches expectation.
3. Verify mlx_audio or chosen runner supports the model type.
4. Install missing runtime deps (e.g., soundfile) only when needed.
5. Run a single generation test; capture loader/runtime errors verbatim.
6. Report success with output path, or root-cause blocker.

## Evidence
> MTPLX is eating ~20GB of your 32GB. Music models need 13-15GB. We can't run both at once without OOM.
> ACE-Step couldn't load (model type not supported in mlx_audio), and then soundfile was missing.
> Beats folder is empty — the script failed before generating anything.
