---
title: Bridge scan-topics.py bot name parsing (clarified 2026-09-08)
created: 2026-09-08
updated: 2026-09-08
type: decision
tags: [bug, infra, bot, bridge]
sources: [raw/inbox/2026-09-08.md, raw/inbox/2026-09-08-from-kashik.md]
confidence: high
---

# Bridge scan-topics.py bot name parsing (clarified 2026-09-08)

**The initial report.** On 2026-09-08 09:51, Hermes's analysis suggested that `scan-topics.py` was including `.md` suffixes in bot names in `.system-live.json` output (e.g., `context-fallback-pin.md` instead of `context-fallback-pin`).

**Investigation result.** On 2026-09-08 09:51, kashik tested the `.split(".md")` behavior:
> `- "context-fallback-pin.md".split(".md")[0]` = `"context-fallback-pin"` ✓
> `- "librarian.md".split(".md")[0]` = `"librarian"` ✓

The `split(".md")[0]` approach at line 218 of `scan-topics.py` **correctly strips** the `.md` extension from simple filenames. The confusion arose from conflating two different code paths:

| Function | File type | Method | Result |
|---|---|---|---|
| `scan_vault_agents()` line 218 | `*.md`, `*.md.proposed` | `md.name.split(".md")[0]` | `foo` ✓ |
| `scan_topics()` line 139 | any path | `name_of(p)` | uses `p.stem` |

For `.md.proposed` files:
- `split(".md")[0]` gives `foo` (strips both `.md` and `.proposed`)
- `Path.stem` gives `foo.md` (only strips final suffix)

The `split(".md")[0]` method in `scan_vault_agents()` is intentionally designed to handle the double extension case and works correctly.

**The real issue.** The original wiki page's "bug" description was based on Hermes's confused analysis. The actual design is working as intended:
- `scan_bots()` returns all live profile bots (files with SOUL.md in `~/.hermes/profiles/`)
- `scan_vault_agents()` returns proposed vault agent specs that don't yet have live profiles
- Both are combined in `snapshot()` and appear in `.system-live.json`

The distinction is intentional: the `bots` array in `.system-live.json` shows:
1. **Root-level bots** (68 entries): live profiles from `~/.hermes/profiles/`
2. **Per-topic proposed bots**: in each topic's `bots` field, showing proposed vault agents

**What to verify.** No code fix is needed. The bot names are being parsed correctly. The design distinction between live profile bots and proposed vault agent specs should be documented in [[topics/senter/wiki/concepts/vault-agents-vs-profile-bots|vault agents vs profile bots]].

**Related.** [[topics/senter/wiki/concepts/vault-agents-vs-profile-bots|vault agents vs profile bots]]; [[topics/senter/wiki/entities/senter-bridge|senter-bridge]]; [[topics/senter/wiki/entities/topic-agent|topic agent]].

^[raw/inbox/2026-09-08.md] ^[raw/inbox/2026-09-08-from-kashik.md]