---
title: MPLX
created: 2026-09-06
updated: 2026-09-07
type: entity
tags: [tool, model, plan, pain]
sources: [raw/inbox/2026-09-06.md, [raw/inbox/2026-09-07.md](../../raw/inbox/2026-09-07.md), raw/inbox/2026-09-07-from-senter-wiki.md]
confidence: medium
---

# MPLX

MPLX is an experimental additional local runtime discovered late in the session. It was downloaded and measured at 12.4 tok/s, roughly 2.5x faster than Unleashed Q3_K_XL on this hardware, but testing stopped before serving or integration ^[raw/inbox/2026-09-06.md].

## Observed behavior

- 26 GB used during download, 5.7 GB free, heavy swapping with Unleashed also resident.
- Tested by temporarily removing Unleashed to free RAM.
- Measured speeds:
  - 300 tokens in 61 s → ~5.1 tok/s
  - 350 tokens in 80 s → ~4.4 tok/s
  - MPLX MTP path: 12.4 tok/s reported ^[raw/inbox/2026-09-06.md].
- `--memory-budget 32GB` is not a valid `mtplx serve` argument; MTPLX exits with usage error when that flag is passed ^[raw/inbox/2026-09-07-from-senter-wiki.md].

## Open questions

- Can it coexist with Unleashed on 32 GB?
- What is its real memory ceiling with MTP enabled?
- Is there a first-class Hermes provider definition for it, or only manual path config?

## Related

- [[turbofit|TurboFit]]
- [[unleashed-27b|Unleashed 27B]]
- [[mplx-integration|MPLX Integration]]
