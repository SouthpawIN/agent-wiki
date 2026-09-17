---
title: Bridge scan-topics.py bot name parsing (clarified 2026-09-08)
created: 2026-09-08
updated: 2026-09-10
type: decision
tags: [bug, infra, bot, bridge, schema]
sources: [raw/inbox/2026-09-08.md, raw/inbox/2026-09-08-from-kashik.md, raw/inbox/2026-09-09.md, raw/inbox/2026-09-09-from-wiki-want.md, raw/inbox/2026-09-09-from-legacy-bots.md, raw/inbox/2026-09-10-from-legacy-bots.md, raw/inbox/2026-09-10.md]
confidence: high
---

# Bridge scan-topics.py bot name parsing (clarified 2026-09-08)

**The initial report.** On 2026-09-08 09:51, Hermes's analysis suggested that `scan-topics.py` was including `.md` suffixes in bot names in `.system-live.json` output (e.g., `context-fallback-pin.md` instead of `context-fallback-pin`).

**Investigation result.** On 2026-09-08 09:51, kashik tested the `.split(".md")` behavior:
> `- "context-fallback-pin.md".split(".md")[0]` = `"context-fallback-pin"` ✓
> `- "librarian.md".split(".md")[0]` = `"librarian"` ✓

The `split(".md")[0]` approach at line 218 of `scan-topics.py` **correctly strips** the `.md` extension from simple filenames. The confusion arose from conflating two different code paths:

|| Function | File type | Method | Result |
||---|---|---|---|---|
|| `scan_vault_agents()` line 218 | `*.md`, `*.md.proposed` | `md.name.split(".md")[0]` | `foo` ✓ |
|| `scan_topics()` line 139 | any path | `name_of(p)` | uses `p.stem` |

For `.md.proposed` files:
- `split(".md")[0]` gives `foo` (strips both `.md` and `.proposed`)
- `Path.stem` gives `foo.md` (only strips final suffix)

The `split(".md")[0]` method in `scan_vault_agents()` is intentionally designed to handle the double extension case and works correctly.

**The real issue.** The original wiki page's "bug" description was based on Hermes's confused analysis. The actual design is working as intended:
- `scan_bots()` returns all live profile bots (files with SOUL.md in `~/.hermes/profiles/`)
- `scan_vault_agents()` returns proposed vault agent specs that don't yet have live profiles

Both are combined in `snapshot()` and appear in `.system-live.json`.

The distinction is intentional: the `bots` array in `.system-live.json` shows:
1. **Root-level bots** (68 entries): live profiles from `~/.hermes/profiles/`
2. **Per-topic proposed bots**: in each topic's `bots` field, showing proposed vault agents

**What to verify.** No code fix is needed for the original naming report. The bot names are being parsed correctly. The design distinction between live profile bots and proposed vault agent specs should be documented in [[topics/senter/wiki/concepts/vault-agents-vs-profile-bots|vault agents vs profile bots]].

**Related.** [[topics/senter/wiki/concepts/vault-agents-vs-profile-bots|vault agents vs profile bots]]; [[topics/senter/wiki/entities/senter-bridge|senter-bridge]]; [[topics/senter/wiki/entities/topic-agent|topic agent]].

^[raw/inbox/2026-09-08.md] ^[raw/inbox/2026-09-08-from-kashik.md]

## 2026-09-09 follow-up — snapshot schema inconsistencies

On 2026-09-09 20:05-20:33, Hermes returned to the same bridge scan output with a new finding: the live snapshot is not just a naming display bug — it also has **schema inconsistencies** that break consumers expecting uniform bot objects.

Findings from `raw/inbox/2026-09-09.md` and `raw/inbox/2026-09-09-from-wiki-want.md`:
- `scan_topics()` creates topic bots with only `name`/`role`; `scan_bots()` creates profile bots with `name`/`role`/`model`; `snapshot()` then assumes every bot has `model`.
- `scan_vault_agents()` is meant to add proposed vault bots, but after edits its `skills` type became inconsistent (`[]` vs integer), and one vault bot still rendered as `skills=[]` in JSON even after attempted fixes.
- The bridge serves `.system-live.json` from `FILE_ROOTS`; Hermes Desktop `loadLive()` calls `fetch(BASE+'/.system-live.json')` on `http://127.0.0.1:8643`. The session ended before Hermes confirmed which `.system-live.json` the UI was actually reading or whether the schema patch had landed.

Contested point: the 2026-09-08 page closed the original `.md` suffix concern as "not a bug, by design." The 2026-09-09 evidence keeps that naming claim, but adds a real schema/merge bug in `snapshot()` that the earlier page did not address.

^[raw/inbox/2026-09-09.md] ^[raw/inbox/2026-09-09-from-wiki-want.md]

## 2026-09-09 21:31 follow-up — legacy-bots raw item evidence

`raw/inbox/2026-09-09-from-legacy-bots.md` is Hermes working output from the same bridge scan session. It adds no new Chris decision, but it does confirm the code paths involved in the schema inconsistency:

- 2026-09-09 20:10: "Now let me also add the `model` field to `scan_topics()` bots" ^[raw/inbox/2026-09-09-from-legacy-bots.md]
- 2026-09-09 20:25: "The `scan_topics()` function creates bots with `skills: 0` but those bots are stored in the `topics` dict, not in the main `bots` list. The main `bots` list comes from `scan_vault_agents(scan_bots())`." ^[raw/inbox/2026-09-09-from-legacy-bots.md]
- 2026-09-09 20:27: "When `live.update(snap)` runs, it replaces `live['bots']` with `snap['bots']`. So the new bots list should be used. Unless..." ^[raw/inbox/2026-09-09-from-legacy-bots.md]

These lines are evidence, not a new request from Chris. They reinforce the earlier finding: the bug is in `snapshot()`/schema merge, not in bot-name parsing.

^[raw/inbox/2026-09-09-from-legacy-bots.md]

## 2026-09-10 continuation — scan-topics.py debugging output (hermes working)

`raw/inbox/2026-09-10-from-legacy-bots.md` (1189 b) and `raw/inbox/2026-09-10.md` (1335 b) are Hermes working output from the same debugging session that began 2026-09-09 20:05. They add no new Chris decision.

From `raw/inbox/2026-09-10-from-legacy-bots.md`:
- 20:10: "Now let me also add the `model` field to `scan_topics()` bots" ^[raw/inbox/2026-09-10-from-legacy-bots.md]
- 20:25: "The `scan_topics()` function creates bots with `skills: 0` but those bots are stored in the `topics` dict, not in the main `bots` list. The main `bots` list comes from `scan_vault_agents(scan_bots())`." ^[raw/inbox/2026-09-10-from-legacy-bots.md]
- 20:27: "When `live.update(snap)` runs, it replaces `live['bots']` with `snap['bots']`. So the new bots list should be used. Unless..." ^[raw/inbox/2026-09-10-from-legacy-bots.md]

From `raw/inbox/2026-09-10.md`:
- 10:23: "The update mechanism is the git repository. The git repo is there. Let me verify the current JSON file has the correct structure by checking if the bridge can serve it:" ^[raw/inbox/2026-09-10.md]
- 10:29: "Let me check the bots section of the JSON file for the senter-wiki-readme-live bot:" ^[raw/inbox/2026-09-10.md]
- 10:30: "The issue might be that the Hermes Desktop is showing old data because the bridge might be serving a cached version, or there's something wrong with how the BOTS view renders in vault-live.html. Let me check the vault-live.html to see if there are any issues with the renderBots function:" ^[raw/inbox/2026-09-10.md]

### Status: fix landed in committed code

The schema normalization debug from 2026-09-09 produced a real patch to `assets/scan-topics.py`. The committed code now shows:

- `scan_topics()` line 143: `{"name": name_of(p), "role": role(md), "model": "", "skills": 0}` — has both `model` (default `""`) and `skills` (integer `0`).
- `scan_vault_agents()` line 227: `{"name": name, "role": ..., "model": "", "skills": 0, ...}` — same consistent schema.
- `scan_bots()` line 185: `{"name": name, "role": r, "desc": r, "model": model, "skills": nskills, ...}` — `model` from config, `skills` as integer count.

All three scan paths now produce uniform bot objects with `name`, `role`, `model` (string), `skills` (integer). The `name_of()` function (line 71-76) strips `.md` from `p.stem` when needed, and `scan_vault_agents()` uses `md.name.split(".md")[0]` (line 222) which correctly handles both `foo.md` and `foo.md.proposed`.

The `snapshot()` print at line 410 (`Bot {b['name']:<12} {b['model']:<36} skills={b['skills']:<3}`) and line 408 (`bots=[b['name'] for b in v['bots']]`) now work against uniform bot objects — no `KeyError` on `model`, no `TypeError` on `skills` type mismatch.

The bot/sessions layout visibility inspection (the 10:30 Hermes line about `renderBots` in `vault-live.html`) remains the open item — that belongs to senter-wiki per BRIEF anti-scope.

^[raw/inbox/2026-09-10-from-legacy-bots.md] ^[raw/inbox/2026-09-10.md]
