---
title: MPLX Metal Load Failure
created: 2026-09-07
updated: 2026-09-07
type: entity
tags: [pain, infra, tool]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
---

# MPLX Metal Load Failure

A `mtplx serve --download` background process exited with code `1` after 42.2 s because model loading failed with `RuntimeError: [METAL] Command buffer execution failed: Insufficient Memory (00000008:***)` during MTP injection ^[raw/inbox/2026-09-07.md].

## Evidence

- Command path: `~/turbofit/.venv/bin/mtplx serve --model Youssofal/Qwen3.8-27B-MTPLX-Optimized-Speed --download --port 11613 --host 127.0.0.1` ^[raw/inbox/2026-09-07.md].
- Failure site: `mtplx/runtime.py:762 load()` → `inject_mtp_support(...)` → `mx.eval(mtp.parameters())` ^[raw/inbox/2026-09-07.md].
- Sidecar note in MTPLX output: `"[mtp norms] sidecar gains are delta-encoded; restoring the +1.0 convention"` ^[raw/inbox/2026-09-07.md].

## Note

- The same model earlier caused an exit code `-9`, which points to OS memory-limit preemption under MTPLX serving and Metal allocation pressure. This load failure is a separate stop at the runtime/Metal boundary.

## Related

- [[topics/turbofit/wiki/entities/turbofit-memory-crash.md|TurboFit Memory Crash]]
- [[topics/turbofit/wiki/entities/turbofit-mtp-performance.md|TurboFit MTP Performance]]
