---
name: dflash2-fork-flag-boundary
description: Use when testing DFlash2 speculative decoding with the dflash2-llama.cpp fork. Record the exact flag set that succeeds/fails to avoid retrying invalid combinations.
version: 0.1.0
distilled: 2026-09-07 20:13
topic: turbofit
---
# dflash2-fork-flag-boundary
## dflash2-fork-flag-boundary

This fork's flag set differs from stock llama.cpp and from standard MTPLX paths.

### Confirmed invalid in dflash2-llama.cpp
- `--draft-ngl`
- `--draft-ctx-size`
- `--low-vram`
- `--draft-model`

### Confirmed valid replacement
- `--model-draft` instead of `--draft-model`
- `--spec-draft-ngl` instead of `--draft-ngl`
- `--ctx-size` governs both main and draft context; omit separate draft context flags

### Runtime boundary
- MTPLX cannot use DFlash2 because it uses native MLX MTP heads.
- Unleashed + DFlash2 only works through the dflash2-llama.cpp fork, not stock llama.cpp or MTPLX.

### Pitfall
Every invalid flag combination fails before bind, wasting benchmark time. Record the exact accepted flag set in the wiki the first time a model launches successfully.

## Evidence
> error: invalid argument: --draft-model
> error: invalid argument: --draft-ngl
> error: invalid argument: --draft-ctx-size
> error: invalid argument: --low-vram
> auto-detected speculative type 'draft-dflash' from the draft model metadata
