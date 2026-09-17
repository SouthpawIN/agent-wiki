---
title: DFlash2 Arg Failures
created: 2026-09-07
updated: 2026-09-07
type: entity
tags: [pain, tool, model]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---

# DFlash2 Arg Failures

All attempted llama.cpp DFlash2 integration commands failed with invalid/unrecognized argument errors. The `dflash2-llama.cpp` fork has a different flag set than stock llama.cpp.

## Failed Commands and Errors

|| Command | Error |
||---------|-------|
| `llama-server -m ... --draft-model <path> --draft-ngl 999 --draft-ctx-size 131072 --low-vram 0` | `error: invalid argument: --draft-model` |
| `llama-server -m ... --draft-ngl 999 --low-vram 0` | `error: invalid argument: --draft-ngl` |
| `llama-server -m ... --draft-ctx-size 131072 --low-vram 0` | `error: invalid argument: --draft-ctx-size` |
| `llama-server -m ... --low-vram 0` | `error: invalid argument: --low-vram` |
| `mtplx serve --model ... --memory-budget 32GB` | `error: unrecognized arguments: --memory-budget 32GB` |

## Root Cause

The `dflash2-llama.cpp` fork uses different argument names than stock llama.cpp:
- `--draft-model` → not supported; use `--spec-draft-model`
- `--draft-ngl` → not supported; use `--spec-draft-ngl`
- `--draft-ctx-size` → not supported
- `--low-vram` → not supported

MTPLX's `--memory-budget` flag is also rejected; use `MTPLX_MEMORY_BUDGET` environment variable instead.

## Workarounds

For stock llama.cpp with DFlash2:
```bash
llama-server -m <main-model> --model-draft <draft-model> --spec-draft-ngl 999
```

For the dflash2-llama.cpp fork:
```bash
llama-server -m <main-model> --spec-draft-model <draft-model> --spec-draft-ngl 999 --spec-draft-n-max 7
```

## Related

- [[topics-wiki/turbofit/wiki/entities/dflash2-draft.md|DFlash2 Draft]]
- [[topics-wiki/turbofit/wiki/entities/mplx-service-arg-validation.md|MPLX Service Arg Validation]]
- [[topics-wiki/turbofit/wiki/concepts/dflash2-compat-boundary.md|DFlash2 Compatibility Boundary]]