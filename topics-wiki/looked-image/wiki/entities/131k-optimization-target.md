---
title: 131K optimization target
created: 2026-09-07
updated: 2026-09-07
type: entity
tags: [decision, preference, infra, plan]
sources:
  - raw/inbox/2026-09-07.md
confidence: 0.92
---

# 131K optimization target

An explicit size/resource constraint introduced by Chris for an unnamed artifact.^[raw/inbox/2026-09-07.md]

## Evidence
- Chris: "ok so it needs to be 131K".^[raw/inbox/2026-09-07.md]
- Chris believes additional optimizations are available: "and I think there'd more optimizations you can do if you research better".^[raw/inbox/2026-09-07.md]
- A hermes side-channel surfaced `--paged-kv-quantization q8`, claiming ~50% KV cache memory reduction.^[raw/inbox/2026-09-07.md]
- Chris later said: "I want to compare that versus the 131 KUF here at Stafford-Douglasal Science Department", shifting the target from generic to site-specific.^[raw/inbox/2026-09-07.md]

## Context
- This target sits beside the topic's visual revert workflow; both express the same corrective pattern: when state diverges from target, change the artifact rather than only describing the gap.
- The optimization suggestion is recorded as a candidate only. Whether it satisfies the target or applies to the actual artifact is unverified.

## Conflicts
- `2026-09-07`: the target is first stated generically as "it needs to be 131K", then reframed as a site-specific comparison against "131 KUF here at Stafford-Douglasal Science Department".^[raw/inbox/2026-09-07.md] `contested: true`

## Related
- [[topics-wiki/looked-image/wiki/decisions/research-optimization-before-rebuild|Research optimization before rebuild]]
- [[topics-wiki/looked-image/wiki/comparisons/131k-abstract-vs-stafford-douglasal|131K abstract vs Stafford-Douglasal]]
