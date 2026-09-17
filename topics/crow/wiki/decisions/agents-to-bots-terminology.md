---
title: "Agents-to-bots terminology convention"
created: 2026-09-08
updated: 2026-09-10
type: decision
tags: [decision, preference, repo, infra, ui]
sources: [raw/inbox/2026-09-08.md, raw/inbox/2026-09-09.md]
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
^[raw/inbox/2026-09-08.md]

> "The comment on line 411-412 is the correct documentation that says
> 'agents/ dir name is the vault's, not UI copy'."
^[raw/inbox/2026-09-08.md]

## Rules

1. **UI-facing text** must say "bots" (users never see the internal directory name).
2. **Internal code** (variables, JSON keys) may use "agents" to reflect the
   filesystem layout.
3. **A clarifying comment** at the relevant code location (lines 411-412)
   documents the distinction so future readers are not confused.

## Additional consistency directives

### Variable renaming

> "However, I should rename the internal variable `ctx` to `wiki` to match
> the user's request for consistency."
^[raw/inbox/2026-09-08.md]

The variable `ctx` should be renamed to `wiki` throughout the relevant
JavaScript code to align with the user's consistency preference.
^[raw/inbox/2026-09-08.md]

### Data-attribute renaming

> "Now I need to update the JavaScript code that references
> `data-k=\"context\"` to use `data-k=\"wiki\"` instead."
^[raw/inbox/2026-09-08.md]

All references to `data-k="context"` must be updated to `data-k="wiki"`.
^[raw/inbox/2026-09-08.md]

### Bot-name normalization: `name_of()` fix to strip `.md`

> "In `scan_topics()` at line 139, the bot name comes from `name_of(p)` which
> for files like `context-fallback-pin.md.proposed` returns
> `context-fallback-pin.md` (because `name_of` returns `p.stem` for files,
> which strips only the last extension `.proposed`, leaving `.md`). Let me fix
> `name_of()` to strip `.md` suffix as well:"
> ^[raw/inbox/2026-09-09.md]

The fix is to update the `name_of()` function to also strip the `.md` suffix,
so that files like `context-fallback-pin.md.proposed` yield the bot name
`context-fallback-pin` rather than `context-fallback-pin.md`. This is
consistent with the existing split logic in `scan_vault_agents()` which already
uses `md.name.split(".md")[0]` — "which gives `context-fallback-pin` ✓"
^[raw/inbox/2026-09-09.md]

### Model field consistency

The root-cause bug spans three scan functions:

- `scan_topics()` creates bots with `{"name": ..., "role": ...}` — **no** `model` field.
- `scan_bots()` creates bots with `{"name": ..., "role": ..., "model": ..., ...}` — has `model`.
- `scan_vault_agents()` adds vault bots with `{"name": ..., "role": ..., ...}` — **no** `model`.

In `snapshot()`, `scan_vault_agents(scan_bots())` merges them all, but vault bots
and topic-level bots still lack `model`. The print at line 408 expects ALL bots
to have `model`. ^[raw/inbox/2026-09-09.md]

The fix requires adding `model`, `skills`, `color`, `avatar` fields to
`scan_vault_agents()` bots to match the schema produced by `scan_bots()`:
" ^[raw/inbox/2026-09-09.md]

A persistent discrepancy was noted: line 227 has `"skills": 0,` (with trailing
comma) in the source, yet the JSON output still renders `skills: []`. This may
indicate a stale cache or an output-generation path that doesn't pick up the
source edit. ^[raw/inbox/2026-09-09.md]

> "I need to add `model`, `skills`, `color`, `avatar` fields to
> `scan_vault_agents()` bots:"
> ^[raw/inbox/2026-09-09.md]

### Skills count reset: `skills: 0` on line 143 and line 227

> "Now I also need to fix line 143 to use `skills: 0` for consistency:"
> ^[raw/inbox/2026-09-09.md]

Line 143 of the relevant JavaScript file must be updated to use `skills: 0`
to align with the user's consistency preference for bot metadata display.
^[raw/inbox/2026-09-09.md] The same convention applies to line 227 for
`scan_vault_agents()` bots:

> "Line 143: `\"skills\": 0` for topic-level agents (scan_topics)
> 2. Line 227: `\"skills\": 0` for vault-level agents (scan_vault_agents)"
> ^[raw/inbox/2026-09-09.md]

The `vault-live.html` print at line 1408 handles both integer `0` and array
forms via `cnt=b.skills||0`, so using `0` everywhere with the JS `||0`
fallback is the simplified consistent approach. ^[raw/inbox/2026-09-09.md]

## See also

- [[topics/crow/wiki/concepts/bots-terminology|Bots terminology concept]]
- [[topics/crow/wiki/concepts/bots-terminology.md#related-code-conventions|Related code conventions]]
