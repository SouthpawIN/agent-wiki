---
title: "Agents-to-bots terminology convention"
created: 2026-09-08
updated: 2026-09-08
type: decision
tags: [decision, preference, repo, infra]
sources: [raw/inbox/2026-09-08.md]
confidence: high
---

# Agents-to-bots terminology convention

The fleet standard is **"bots"** — but internal JavaScript variable names and
data-structure keys may retain **"agents"** because they map to the on-disk
`agents/` directory (the vault's name, not UI copy). ^[raw/inbox/2026-09-08.md]

## Rationale

> "I see there are still some 'agents' references in the JavaScript code.
> These are internal variable names and data structure keys that correctly
> map the old 'agents' directory to 'bots' in the UI."
> ^[raw/inbox/2026-09-08.md]

> "The comment on line 411-412 is the correct documentation that says
> 'agents/ dir name is the vault's, not UI copy'."
> ^[raw/inbox/2026-09-08.md]

## Rules

1. **UI-facing text** must say "bots" (users never see the internal directory name).
2. **Internal code** (variables, JSON keys) may use "agents" to reflect the
   filesystem layout.
3. **A clarifying comment** at the relevant code location (lines 411-412)
   documents the distinction so future readers are not confused.

## See also

- [[topics/crow/wiki/concepts/bots-terminology|Bots terminology concept]]
- [[topics/crow/index.md|crow index]]
