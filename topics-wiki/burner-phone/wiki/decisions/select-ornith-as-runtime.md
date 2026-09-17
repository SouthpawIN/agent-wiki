---
title: Select Ornith as local runtime target
created: 2026-09-07
updated: 2026-09-07
type: decision
tags:
  - decision
  - tool
  - plan
sources:
  - raw/inbox/2026-09-07.md
confidence: high
---

# Select Ornith as local runtime target

## What
Chris selected Ornith as the local runtime target for this topic and directed that it be started properly and the config updated.

## Why
Ornith MLX measured 28.5 tok/s in 4-bit, and the ~18GB model footprint leaves more room for KV cache than 20–25GB 27B models on the same 28GB hardware. A CPU fallback (`-ngl 0`) succeeded where a previous attempt timed out, indicating the failure mode is not simply offload capability. ^[raw/inbox/2026-09-07.md]

## When
2026-09-07

## Evidence
- *"28.5 tok/s — Ornith MLX 4-bit absolutely crushes it."* ^[raw/inbox/2026-09-07.md]
- *"Good, the model runs with `-ngl 0` (all on CPU). The previous attempt timed out."* ^[raw/inbox/2026-09-07.md]
- *"Ornith is the winner. Let me start it properly and update the config."* ^[raw/inbox/2026-09-07.md]

## Supersedes
Previous runtime attempts that timed out or returned 507 at 131K with larger models.

## Open questions
- Has the config been updated to start Ornith properly after the `-ngl 0` restart and port conflict resolution?
- Does the 18GB model under Ornith complete the full 131K context test after the timeout fallback?

## Links
- [[topics-wiki/burner-phone/wiki/entities/ornith|Ornith]]
- [[topics-wiki/burner-phone/wiki/queries/what-runs-on-28gb|What runs on 28GB]]
- [[topics-wiki/burner-phone/wiki/concepts/context-limit-pain|507 / context-fit ceiling on 28GB hardware]]
