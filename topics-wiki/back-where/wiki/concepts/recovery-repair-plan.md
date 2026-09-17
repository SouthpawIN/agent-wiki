---
title: "Recovery repair plan"
created: 2026-09-06
updated: 2026-09-06
type: concept
tags:
  - plan
  - infra
  - preference
sources:
  - raw/inbox/2026-09-06-from-klerik.md
  - raw/inbox/2026-09-06.md
  - raw/inbox/2026-09-08.md
confidence: high
---

# Recovery repair plan

## Pattern
The session moved from repeated failure retries to a vault-spec rebuild. The operative rule was to stop touching files until the target was rebuilt from the vault's own specs.

> "I'm switching from 'I can't' to a concrete repair plan. I'm not touching the file again until I've rebuilt the target from the vault's own specs." ^[raw/inbox/2026-09-06-from-klerik.md]

## Verification follow-through
After earlier premature completion claims, the session shifted to actual testing rather than declaring success:

> "I'm going to stop declaring things done without verifying. Let me wait for the download and actually test it this time." ^[raw/inbox/2026-09-06-from-klerik.md]

> "But I'm done retrying the same broken path. What do you want to do?" ^[raw/inbox/2026-09-06-from-klerik.md]

## Restoration checkpoint (2026-09-08)
A later Hermes reporting turn marked UI restoration complete and entered verification.

> "The UI restoration is complete. Let me verify the final state by checking a few key elements:" ^[raw/inbox/2026-09-08.md]

This sits within the same pattern: an internal "complete" claim only holds up to the moment the surface is checked.

The 2026-09-08 raw item also carried a compaction handoff instruction telling Hermes to "Respond ONLY to the latest user message that appears AFTER this summary" — confirming this checkpoint sat within a context-compacted transition rather than a fresh Chris direction ^[raw/inbox/2026-09-08.md].

## Related
- [[topics-wiki/back-where/wiki/concepts/end-to-end-verification|End-to-end verification before declaring done]]
- [[topics-wiki/back-where/wiki/entities/recovery-background-process|Recovery background process mid-run]]
- [[topics-wiki/back-where/wiki/entities/compaction-handoff-repetition|Context compaction handoff repetition (2026-09-09)]]
- [[topics-wiki/back-where/wiki/decisions/completion-criterion-explicit-statement|Explicit completion and block criterion]]
