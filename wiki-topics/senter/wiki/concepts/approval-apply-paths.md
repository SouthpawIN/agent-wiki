---
title: Approval apply paths (a card's approve button does the thing — loop → cron, bot → profile, research → answer in the page)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [decision, spec, loop, bot, infra]
sources: [raw/sources/2026-09-05-umbrella-still-runs.md, raw/inbox/2026-09-05.md]
confidence: high
---

# Approval apply paths

**Decided 2026-09-05 (Chris, 18:0x: "stop asking me for so many decisions"): approvals APPLY.** An approved card is not a note in a queue and not a second question — it executes. ^[raw/sources/2026-09-05-umbrella-still-runs.md]

| Card type | Approve → | Who finishes |
|---|---|---|
| **Loop** | `hermes cron create` on the bot named in the pitch, with the pitch's cadence and prompt | — (proven 18:20: cron `e6e20c22e1b9` on klerik, see [[wiki-topics/senter/wiki/concepts/loop-apply-path|loop apply path]]) |
| **Bot** | `hermes profile create` + SOUL.md / AGENTS.md written from the card's spec | [[wiki-topics/senter/wiki/entities/klerik|klerik]] finishes voice, skin, alias ([[wiki-topics/senter/wiki/concepts/profile-setup-checklist|profile setup checklist]]) |
| **Research** | [[wiki-topics/senter/wiki/entities/looker|looker]] researches and **writes the answer into the wiki page** the question came from | — |

## What this replaces
Under the 2026-08-30 model ([[wiki-topics/senter/wiki/decisions/2026-08-30-conversation-first-operating-model|conversation-first]]) a bot or loop was "suggested to Chris, never spawned silently" and approval fed a routing step. Under the 2026-09-02 cards ruling ([[wiki-topics/senter/wiki/decisions/2026-09-02-fleet-decisions-as-wiki-cards|decision]]) the card was the channel. The 18:0x decision closes the gap between *approved* and *exists*: the card **is** the routing step. This is also why the `senter-bridge` approval webhook matters — it is the only wire from a button to a shell ([[wiki-topics/senter/wiki/entities/senter-bridge|senter-bridge]]).

## Consequences
- Every pitch must be **executable as written**: a loop pitch carries `agent`, `cadence`, `prompt`; a bot pitch carries a SOUL draft and a first task; a research pitch names the page the answer lands in. A pitch that cannot apply is not a pitch.
- Skills and wiki edits never reach this table — they need no approval at all ([[wiki-topics/senter/wiki/decisions/2026-09-05-no-approval-for-wiki-edits|decision]]).
- Irreversible acts (spend, delete, publish) remain outside — the [[wiki-topics/senter/wiki/decisions/2026-08-30-standing-approval|standing approval]] boundary was never loosened.
- "Verify the wiki picks it up" is part of every apply: the created cron / profile / answer must be visible in the wiki, per [[wiki-topics/senter/wiki/concepts/live-data-contract|spawn = visible]].
