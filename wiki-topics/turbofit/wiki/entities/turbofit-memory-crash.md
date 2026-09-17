---
title: TurboFit Memory Crash
created: 2026-09-07
updated: 2026-09-07
type: entity
tags: [pain, infra, tool]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
contested: true
---

# TurboFit Memory Crash

A `mtplx serve` background process exited with code `-9` during TurboFit testing on this 32 GB box. The first evidence used `--mtp` without an explicit long-context window, while later evidence shows explicit `--context-window 131072` invocations whose memory plan was already marked `OVERCOMMITTED` before the process was killed ^[raw/inbox/2026-09-07.md].

## Evidence

- Process paths:
  - `~/turbofit/.venv/bin/mtplx serve --model Youssofal/Qwen3.8-27B-MTPLX-Optimized-Speed --port 11613 --host 127.0.0.1 --mtp` exited `-9` after 158.15 s while generating 100 completion tokens from a 5010-token prompt ^[raw/inbox/2026-09-07.md].
  - `~/turbofit/.venv/bin/mtplx serve ... --mtp --context-window 131072` printed `Memory plan: ... 131072 (machine-bound) (OVERCOMMITTED)` and `requested context 131072 exceeds the machine fit 8192` before later runs were killed ^[raw/inbox/2026-09-07.md].
- Runtime output also shows cache shedding and swap warnings at 131K, plus `deferred_s: 60.0` in precommit output ^[raw/inbox/2026-09-07.md].
- Prior MPLX observation notes heavy swapping around 26 GB used and co-resident Unleashed pressure ^[raw/inbox/2026-09-06.md].

## Contested Evidence

Hermes summary claims `custom:turbofit-mtplx` as main provider with 65K stable context, but command evidence shows:
- `/01:51` turn: MTPLX exited `-9` after 158s of generation
- `/00:56` turn: MTPLX 65K stable at 8.5-12 tok/s then crashed under load
- `/01:00` turn: Switched back to Unleashed+DFlash2 after MTPLX instability

## Note

- Code `-9` points to OS memory-limit preemption rather than a clean MTPLX shutdown. The explicit `--context-window 131072` evidence makes this more specifically an overcommit-induced kill than the earlier generic crash record.
- Hermes summary claims 65K stable and MTPLX main, but the command evidence for this box shows 131K overcommit and killed processes ^[raw/inbox/2026-09-07.md].

## Related

- [[wiki-topics/turbofit/wiki/entities/turbofit-verifier-bridge.md|TurboFit Verifier Bridge]]
- [[wiki-topics/turbofit/wiki/entities/mplx.md|MPLX]]
- [[wiki-topics/turbofit/wiki/entities/mtplx-memory-guard.md|MPLX Memory Guard]]
- [[wiki-topics/turbofit/wiki/decisions/mtplx-main-provider.md|MTPLX Main Provider]]
- [[wiki-topics/turbofit/wiki/concepts/mtplx-context-overcommit.md|MPLX Context Overcommit]]