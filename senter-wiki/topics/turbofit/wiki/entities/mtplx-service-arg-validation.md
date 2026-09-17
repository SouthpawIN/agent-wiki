---
title: MT_PlX Service Arg Validation
created: 2026-09-07
updated: 2026-09-07
type: entity
tags: [pain, tool]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---

# MT_PlX Service Arg Validation

`mtplx serve` with `--memory-budget 32GB` exits with an error:

```
usage: mtplx [-h] [--no-color] [--version] {help,advanced,...}
mtplx: error: unrecognized arguments: --memory-budget 32GB
```

## Accepted Arguments

MTPLX's CLI does not accept `--memory-budget` as a flag. According to the model family documentation, memory management should be handled via:

1. **Environment variables**: `MTPLX_MEMORY_BUDGET` for memory budget control
2. **Native runtime config**: Per-model memory planning is automatic

## Working Command Pattern

```bash
# Correct: Environment variable for memory budget
MTPLX_MEMORY_BUDGET=34359738368 mtplx serve --model <model-id> --port 11613

# Or let MTPLX auto-calculate based on available memory
mtplx serve --model <model-id> --port 11613
```

## Related

- [[topics/turbofit/wiki/entities/mplx-qwen-38-27b-optimized-speed.md|MPLX Qwen 3.8 27B Optimized Speed]]
- [[topics/turbofit/wiki/entities/mplx.md|MPLX]]
- [[topics/turbofit/wiki/concepts/mtplx-32gb-memory-and-evidence-reliability.md|MPLX 32GB Memory and Evidence Reliability]]