---
title: TurboFit Local Main Provider Decision
created: 2026-09-07
updated: 2026-09-07
type: decision
tags:
  - turbofit
  - decision
  - main
  - runtime
  - evidence
sources:
  - raw/inbox/2026-09-07.md
  - raw/inbox/2026-09-07-from-senter-wiki.md
confidence: medium
contested: true
---

# TurboFit Local Main Provider Decision

What Chris wanted: the smartest feasible local runtime as Hermes main, with verified evidence, not just Hermes internal logs.

^[raw/inbox/2026-09-07.md]

## The candidate field
| Candidate | Notes |
|---|---|
| Ornith MLX 4-bit | Short-context fastest; deepest long-context compatibility tested on this box |
| MTPLX Qwen 3.8 27B | Stable 65K fallback; explicit 131K overcommit warnings on 32GB |
| Unleashed Q3_K_XL + DFlash2 | Safe long-context backup; flag mismatches caused repeated failures |
| Nail Q4_K_XL | Faster at 32K than 27B dense, but not usable at 131K |
| Tiel-Coder Q4_K_XL | Works at 65K, not confirmed stable at 131K |
| Dirk Q3_K_XL | Dense 27B; OOMs above 32K |
| Bonsai | Incomplete for MLX; GGUF needs llama.cpp; custom formats blocked |
| Colibri | Custom Maple format, incompatible with standard MLX server |
| Maple | Stable at 65K; OOM at 131K under load |
| FreeToken | Optional CUDA-13 MoE candidate, no in-session promotion |

^[raw/inbox/2026-09-07.md]
^[raw/inbox/2026-09-07-from-senter-wiki.md]

## Chris's last intent
Repeated messages on 2026-09-07 say Ornith should be configured into turbofit and set as main so he can continue with a smarter local model instead of weaker free ones. He accepted hardware limits: "10+ tok/s at 131K is not happening on M1 32GB."

^[raw/inbox/2026-09-07.md]

## Verified state
Ornith is configured as default in Hermes via `custom:turbofit`, but Hermes connection timeouts were still observed after repoint. A full Hermes restart remains needed to confirm the live route. Until that restart and a successful completion are observed, final promotion is contested.

^[raw/inbox/2026-09-07.md]

## Evidence standard
Final TurboFit evidence requires a real Hermes window capture plus the primary viewport/approval path, not only server logs or Hermes postcommit artifacts.

^[raw/inbox/2026-09-07.md]

## Related pages
- [[ornith-1-5-35b-a3b-mlx-4-bit|Ornith 1.5 35B-A3B MLX 4-bit]]
- [[turbo-fit-evidence-capture|TurboFit Evidence Capture]]
