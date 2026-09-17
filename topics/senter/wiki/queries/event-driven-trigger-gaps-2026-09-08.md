---
title: Event-driven trigger gaps (2026-09-08 investigation)
created: 2026-09-08
updated: 2026-09-08
type: query
tags: [question, loop, bug, gap, investigation]
sources: [raw/inbox/2026-09-07.md, raw/inbox/2026-09-08.md, raw/inbox/2026-09-08-from-hermes-agent.md, raw/inbox/2026-09-09.md]
confidence: medium
---

# Event-driven trigger gaps (2026-09-08 investigation)

**The gap.** The topic agent (`assets/topic-agent.py`) should fire on new watcher cuts (event-driven) not on a 5-minute timer. This was identified as work at 2026-09-05 18:18 but the exact landing state was unclear. The investigation on 2026-09-08 09:22–09:56 provides new evidence.

## What Chris said
2026-09-05 18:16: *"per message, just like when you talk to cursor… this is like a auto wiki, a live acting second brain."*

## What was decided (Hermes analysis, 2026-09-08 09:22)

### Investigation stages

**09:22** — Good - the senter-bridge wiki entity exists. Let me check the scan-topics.py script to understand the scanning pipeline.

**09:27** — Looking at `scan_vault_agents()` in `scan-topics.py`: The function reads BOTH `.md` AND `.md.proposed` files from `agents/` directories. The bot names are being counted but the parsing uses `md.name.split(".md")[0]` at line 218.

**09:50** — The bridge/agent-wiki-bot is supposed to serve a `senter-wiki` topic, but that topic folder doesn't exist. Looking at the data:
- The `senter` topic has bots from the `agents/` directory (proposed bots) and one real bot: `fleet-orchestrator`
- The `senter-wiki-bot` profile exists but has no topic to serve

### Key findings

1. **scan-topics.py bot name parsing (line 218):** `name = md.name.split(".md")[0]` — For a file like `context-fallback-pin.md`, this gives `context-fallback-pin.md` after split (wait, no — `"foo.md".split(".md")[0]` = `"foo"`). On 2026-09-08 09:51, kashik verified: `"context-fallback-pin.md".split(".md")[0]` = `"context-fallback-pin"` ✓

2. **The real confusion:** The Hermes agent's initial analysis was confused about the actual bug. The `.md` suffix appearing in output would come from a different code path. The investigation revealed that the actual issue is the **inconsistency** between:
   - `scan_vault_agents()` line 218: `md.name.split(".md")[0]`
   - `scan_topics()` line 139: `name_of(p)` which uses `Path.stem`

3. **senter-wiki-bot topic folder missing:** The `senter-wiki-bot` profile exists but has no topic folder with proper structure. This is a structural gap that blocks the wiki's ability to serve its own content.

## Current state evidence

| Time | Finding | Implication |
|---|---|---|
| 09:22 | Bridge/wiki entity exists | Good — UI is connected |
| 09:27 | scan-topics.py reading vault agents | Live data pipeline active |
| 09:43 | Bridge restarted with patched code | Server is live |
| 09:51 | kashik `.split(".md")` test confirms correct behavior | Parsing works for simple cases |
| 09:56 | senter-wiki-bot topic folder missing | Structure gap needs scaffolding |

## 2026-09-08 resolution
Item 1 (senter-wiki folder) was resolved on 2026-09-08 — the folder already existed with proper structure (see [[topics/senter/wiki/decisions/2026-09-08-senter-wiki-bot-topic-folder-missing|decision]]). The proposal to create it is **superseded**.

Want a bot that checks if the event-driven topic-agent trigger has landed? Or want me to look into the `scan-topics.py` / launchd configuration to implement it?

## Related

- [[topics/senter/wiki/entities/topic-agent|topic agent]]
- [[topics/senter/wiki/entities/watcher|watcher]] 
- [[topics/senter/wiki/entities/senter-bridge|senter-bridge]]
- [[topics/senter/wiki/concepts/watcher-as-cutter|watcher as cutter]]
- [[topics/senter/wiki/entities/umbrella|umbrella]] (syncs WatchPaths with new topics)
- [[topics/senter/wiki/concepts/vault-agents-vs-profile-bots|vault agents vs profile bots]]
- [[topics/senter/wiki/entities/senter|siten]]

|^[raw/inbox/2026-09-07.md] ^[raw/inbox/2026-09-08.md] ^[raw/inbox/2026-09-09.md]