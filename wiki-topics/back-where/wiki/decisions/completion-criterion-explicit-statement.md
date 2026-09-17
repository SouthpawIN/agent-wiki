---
title: "Explicit completion and block criterion"
created: 2026-09-10
updated: 2026-09-10
type: decision
tags:
  - decision
  - preference
  - plan
sources:
  - raw/inbox/2026-09-09.md
confidence: high
---

# Explicit completion and block criterion

## Decision

Chris defined an explicit criterion for how Hermes should signal the end of a task: completion must be stated explicitly and then stop, or blockage must be stated clearly and then stop. This prevents silent completion claims or silent continuation without user direction.

> "If you believe the goal is complete, state so explicitly and stop. If you are blocked and need input from the user, say so clearly and stop." ^[raw/inbox/2026-09-09.md]

## Context

This instruction appeared in the 2026-09-09 session, alongside the repeated context compaction handoff pattern. The session involved debugging scan-topics.py tooling and Python environment isolation issues before Chris issued this directive.

## Why it matters

The completion criterion reinforces Chris's standing preference for end-to-end verification before declaring done. Rather than continuing indefinitely or declaring completion silently, Hermes must explicitly state its status and stop, giving Chris a clear signal point. This pairs with the compaction handoff rule — after a context reset, Hermes should not resume old work unless explicitly directed.

## Related
- [[wiki-topics/back-where/wiki/concepts/end-to-end-verification|End-to-end verification before declaring done]]
- [[wiki-topics/back-where/wiki/concepts/recovery-repair-plan|Recovery repair plan]]
- [[wiki-topics/back-where/wiki/entities/compaction-handoff-repetition|Context compaction handoff repetition (2026-09-09)]]
- [[wiki-topics/back-where/wiki/entities/token-startup-race|Token startup race condition]]
