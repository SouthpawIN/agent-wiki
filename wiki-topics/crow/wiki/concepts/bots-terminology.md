---
title: "Bots terminology"
created: 2026-09-08
updated: 2026-09-10
type: concept
tags: [concept, preference, infra]
sources: [raw/inbox/2026-09-08.md, raw/inbox/2026-09-09.md, README.md]
confidence: high
---

# Bots terminology

Across the Hermes/Senter fleet the user-facing term is **"bots"**, not
"agents". The word "agents" survives only in internal code as a reflection
of the legacy `agents/` directory on disk. ^[raw/inbox/2026-09-08.md]

## Fleet convention

> "Crow — deep research agent for Hermes Agent."
> ^[README.md]

Even though Chris sometimes calls Crow the "deep research **agent**", the
canonical fleet vocabulary (see [[wiki-topics/crow/../../senter/BRIEF.md|Senter BRIEF]])
and the wiki UI itself use **"bots"**. The distinction is documented in:

- [[wiki-topics/crow/wiki/decisions/agents-to-bots-terminology.md|Agents-to-bots terminology decision]]

## Key distinction

| Layer | Term | Reason |
|-------|------|--------|
| UI / prose | bots | matches fleet vocabulary |
| Internal JS vars | agents | maps to `agents/` dir on disk |
| Data attributes | wiki | renamed from `context` to `wiki` to match user's consistency request |

## Related code conventions

### Variable renaming: `ctx` → `wiki`

Hermes noted the need to rename the internal variable `ctx` to `wiki` for
consistency with the user's request. ^[raw/inbox/2026-09-08.md] The comment
at lines 411-412 of the relevant JavaScript file correctly documents that
the `agents/` directory name is the vault's internal name, not UI copy.
^[raw/inbox/2026-09-08.md]

### Data-attribute renaming: `data-k="context"` → `data-k="wiki"`

The JavaScript code that references `data-k="context"` needs to be updated
to `data-k="wiki"` to align with the user's consistency preference.
^[raw/inbox/2026-09-08.md]

### Bot-name bug: `.md` suffix in names

A sim-0.06 observation noted: "So the split logic is correct. But then why
does the data show `context-fallback-pin.md` (with the .md) as the bot name?"
This indicates that file extensions are not being stripped when bot names
are derived from filenames, causing raw filenames like
`context-fallback-pin.md` to appear as bot names instead of the expected
`context-fallback-pin`. ^[raw/inbox/2026-09-08.md]

The root cause is in `scan_topics()` at line 139, where the bot name comes
from `name_of(p)`. For a file like `context-fallback-pin.md.proposed`,
`name_of` returns `p.stem`, which strips only the last extension `.proposed`,
leaving `.md` intact. The fix is to update `name_of()` to also strip the
`.md` suffix. ^[raw/inbox/2026-09-09.md]

**Trace for `context-fallback-pin.md.proposed`:**

| Step | Expression | Value |
|------|-----------|-------|
| `md.name` | — | `context-fallback-pin.md.proposed` |
| `md.name.split(".md")` | — | `['context-fallback-pin', '.proposed']` |
| `md.name.split(".md")[0]` | — | `context-fallback-pin` ✓ |

The `split(".md")[0]` approach in `scan_vault_agents()` already produces the
correct result for this case, which the `name_of()` fix must match.
^[raw/inbox/2026-09-09.md]

A formatting observation: line 227 has `"skills": 0,` with a trailing comma,
but line 230 ends with `})` without a trailing comma — a possible contributor
to the JSON still rendering `skills: []` despite the edit being present in the
source. ^[raw/inbox/2026-09-09.md]

### Skills count reset: `skills: 0` on line 143 and line 227

Hermes noted a follow-up consistency fix: line 143 must use `skills: 0`
to align with the user's preference for consistent bot metadata display.
^[raw/inbox/2026-09-09.md] The same `skills: 0` convention applies to line 227
for vault-level agents created by `scan_vault_agents()`:

> "Line 143: `\"skills\": 0` for topic-level agents (scan_topics)
> 2. Line 227: `\"skills\": 0` for vault-level agents (scan_vault_agents)"
> ^[raw/inbox/2026-09-09.md]

The reason the integer `0` works (not an array) is that `vault-live.html`
line 1408 uses an `||0` fallback:

> "Line 1408: `const name=b.name, desc=b.role||b.desc||'', model=b.model||'—',
> cnt=b.skills||0, col=b.color||'#b8b8b8';`"
> ^[raw/inbox/2026-09-09.md]

This means the JavaScript handles `skills` being truthy/falsy, defaulting to 0,
so `len(b['skills'])` would fail for integers. Using `0` everywhere with the
`||0` fallback in the JS is the simplified, consistent approach. ^[raw/inbox/2026-09-09.md]

## See also

- [[wiki-topics/crow/wiki/decisions/agents-to-bots-terminology.md|Terminology decision]]
- [[wiki-topics/crow/README.md|crow README]]
