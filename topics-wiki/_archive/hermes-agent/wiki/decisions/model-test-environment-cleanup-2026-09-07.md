---
title: "Model Test Environment Cleanup — 2026-09-07"
created: 2026-09-07
updated: 2026-09-07
type: decision
tags: [person, tool, decision, preference, pain]
sources: ["raw/inbox/2026-09-07.md"]
confidence: high
---

# Model Test Environment Cleanup — 2026-09-07

On `2026-09-07`, Chris required that model evaluation for `Qwen 3.8 27B` run only after removing Maple and deleting any remaining uncensored model variant, so the test environment would not confuse results.^[raw/inbox/2026-09-07.md]

## What
- Remove `Maple` before testing.
- Delete any remaining uncensored model variant if present.
- Do not stop Hermes Agent itself, since the evaluation is happening inside the running Hermes session.

## Why
- Chris wants the `27B` test to measure only the active model and configuration, not residual artifacts from prior setups.
- He said this repeatedly in a short window (00:08, 01:02, 01:03), confirming it as a standing precondition, not a one-time cleanup request.

## Repetition Signal
- `2026-09-07 00:08` — first statement.^[raw/inbox/2026-09-07.md]
- `2026-09-07 01:02` — verbatim repeat.^[raw/inbox/2026-09-07.md]
- `2026-09-07 01:03` — verbatim repeat again.^[raw/inbox/2026-09-07.md]
- The third repetition at `01:03` confirms this is a standing rule, not an incidental request.

## Implementation
This is a standing precondition that should be documented in any model evaluation protocol. The cleanup must happen before any `27B` variant evaluation begins.

## Evidence
- `2026-09-07 00:08` — Chris: "I would really rather you be testing this 27B with as clean of a hard drive as you can... take off maple... delete that if it's still here."^[raw/inbox/2026-09-07.md]
- `2026-09-07 01:02` — same cleanup request repeated verbatim.^[raw/inbox/2026-09-07.md]
- `2026-09-07 01:03` — same cleanup request repeated verbatim again.^[raw/inbox/2026-09-07.md]
- `2026-09-07 03:06` — Chris: "Must be Qwen 3.8 27B variant. Target: 10+ tok/s at 131K context." (implies clean state for evaluation)^[raw/inbox/2026-09-07.md]

## Related
- [[topics-wiki/hermes-agent/wiki/decisions/compression-test-2026-09-06|Compression Test — 2026-09-06]]
- [[topics-wiki/hermes-agent/wiki/entities/model-check-20260903|Model Check — 20260903_001447_7bc70a]]
- [[topics-wiki/hermes-agent/wiki/entities/session-20260907-030601|Session Check — 20260907_030601]]
- [[topics-wiki/hermes-agent/wiki/decisions/main-provider-lock-2026-09-07|Main Provider Lock — 2026-09-07]]
- [[topics-wiki/hermes-agent/wiki/decisions/targeted-27b-131k-2026-09-07|Targeted 27B at 131K — 2026-09-07]]