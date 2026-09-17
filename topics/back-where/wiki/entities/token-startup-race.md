---
title: "Token startup race condition"
created: 2026-09-08
updated: 2026-09-08
type: entity
tags:
  - tool
  - infra
  - pain
  - question
sources:
  - raw/inbox/2026-09-08.md
confidence: medium
related_notes:
  - raw/inbox/2026-09-08.md (compaction handoff lines 12, 24, 41 — Hermes internal working prose, not Chris utterance)
---

# Token startup race condition

## What Hermes reported
During UI restoration, a token was being read but the server was still rejecting it. Hermes traced the likely cause to a startup race: the server had not fully started yet.

> "The token is being read but the server is still rejecting it. This might be a startup race condition — the server may not have fully started yet. Let me check if the server is actually listening and ready:" ^[raw/inbox/2026-09-08.md]

This quote appears twice in the raw (09:41 and again at 09:41, the final Hermes working line), confirming the same server-readiness check was re-asserted on the 2026-09-08 session pass ^[raw/inbox/2026-09-08.md].

## Why it matters
If the same pattern repeats, retries without waiting for server readiness will keep failing. This aligns with Chris's broader pattern of unstable runtime paths during repair and verification after UI/backend changes.

## Related
- [[topics/back-where/wiki/entities/ui-layout-regression|UI layout regression after diff view change]]
- [[topics/back-where/wiki/concepts/recovery-repair-plan|Recovery repair plan]]
- [[topics/back-where/wiki/concepts/end-to-end-verification|End-to-end verification before declaring done]]
