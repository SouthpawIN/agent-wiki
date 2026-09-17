---
title: Vault agents vs profile bots (proposed vs live)
created: 2026-09-08
updated: 2026-09-09
type: concept
tags: [concept, bot, infra, spec]
sources: [raw/inbox/2026-09-08.md, raw/inbox/2026-09-09.md]
confidence: high
---

# Vault agents vs profile bots (proposed vs live)

The scan-topics.py investigation on 2026-09-08 clarified the distinction between **vault agent specs** (proposed bots) and **profile bots** (live, running bots). ^[raw/inbox/2026-09-08.md]

## Vault agent specs

Files in `wiki-topics/<topic>/agents/` — these are **proposed** bot specifications, not live bots:
- `*.md` — approved bot proposals (e.g. `sidebar-soul-rewrite.md`, `fleet-orchestrator.md`)
- `*.md.proposed` — unapproved proposals pending Chris's sign-off

Example from the senter topic's `agents/` directory:
- `context-fallback-pin.md` — proposed bot spec
- `fleet-orchestrator.md` — proposed bot spec
- `hermes-runtime-guard.md` — proposed bot spec
- `librarian.md` — proposed bot spec
- `project-topic-scaffolder.md` — proposed bot spec
- `sidebar-soul-rewrite.md` — proposed bot spec
- `vault-librarian.md` — proposed bot spec

These are **not** live profile bots. They are specifications that may or may not have been approved and turned into actual Hermes profiles via `hermes profile create`.

## Profile bots (live)

Actual running bots live in `~/.hermes/profiles/<name>/` — each has a SOUL.md and is a real Hermes profile. These are the bots listed in `scan_bots()` output (68 total as of 2026-09-08 09:43).

## The `.system-live.json` structure

The live data snapshot distinguishes:

- **`bots`** (root array, 68 entries): all live profile bots with SOUL.md
- **`<topic>.bots`** (per-topic array): vault agent specs from `wiki-topics/<topic>/agents/` — these are *proposed* bots that may not yet be live profiles

The 2026-09-09 pipeline verification confirmed the live data serving is healthy: `com.senter.bridge` running on `127.0.0.1:8643`, `/system-live.json` served correctly via the `/file` endpoint, data showing **35 topics / 69 bots / 201 skills / 81 loops**, and the `senter-wiki` topic properly populated. ^[raw/inbox/2026-09-09.md]

Hermes noted the confusion on 2026-09-08 09:47: *"Looking at `scan_vault_agents()`: This function reads BOTH `.md` AND `.md.proposed` files from `agents/` directories. But the current output shows it's picking up ALL `.md` files, not just the agent specs."* ^[raw/inbox/2026-09-08.md]

The issue: vault agent specs are being included in the topic's `bots` array in `.system-live.json`, which pollutes the data with proposed bots that don't match any actual profile.

## The `name_of()` vs `split(".md")` inconsistency

Hermes's analysis on 2026-09-08 09:51 identified the bot name parsing issue:

> *"The `name = md.name.split(".md")[0]` gives `something` for `something.md.md` but gives `something.md` for `something.md` (since `.md` is not a separator that gets removed)."*

However, on 2026-09-08 09:51, kashik tested the `.split(".md")` behavior:

> *`- "context-fallback-pin.md".split(".md")[0]` = `"context-fallback-pin"` ✓*
> *`- "librarian.md".split(".md")[0]` = `"librarian"` ✓*
> *Actually the split should work.*

^[raw/inbox/2026-09-08-from-kashik.md]

The kashik test confirms that `split(".md")` **does correctly strip** the `.md` extension from simple filenames. The actual bug is that `scan_vault_agents()` at line 218 uses `md.name.split(".md")[0]` for the name, while `scan_topics()` at line 139 uses `name_of(p)` which relies on `Path.stem`. For `.md.proposed` files, `Path.stem` returns `foo.md` (keeping the inner `.md`), whereas `split(".md")` correctly returns `foo`. The inconsistency between these two approaches means some vault agents get the right name and some get `.md` suffixes.

## What needs fixing

1. Standardize on `stem`-based parsing: use `md.stem` for `.md` files and `md.name.rsplit(".md.proposed", 1)[0]` for `.proposed` files — or just handle both with a single regex
2. The `scan_vault_agents()` function should use `name_of()` (which already handles the path correctly) rather than raw `md.name.split(".md")[0]`

## Related

- [[wiki-topics/senter/wiki/entities/senter-bridge|senter-bridge]] — serves `.system-live.json` via the `/file` endpoint
- [[wiki-topics/senter/wiki/entities/topic-agent|topic agent]] — consumes the live data
- [[wiki-topics/senter/wiki/decisions/2026-09-08-bridge-scan-topics-bot-name-parsing|bridge scan-topics bot name parsing bug]] — the existing decision tracking this issue
