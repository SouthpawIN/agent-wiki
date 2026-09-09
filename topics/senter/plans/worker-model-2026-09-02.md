---
title: Worker model — decision (anser review)
updated: 2026-09-02
type: plan
status: adopted — item 4 (CLAIM v2 + sentinel) RETIRED 2026-09-05 (kanban t_f1b1eba1)
owner: senter
reviewer: anser
---

# Worker model — one-and-done dispatch (anser, 2026-09-02)

Chris: "don't queue, don't make me wait minutes, conversation keeps going, many in parallel, Meeseeks-style." Sources: `tools/delegate_tool.py`, `hermes_cli/plugins.py`, `tools/approval.py`, `plugins/senter-bridge/__init__.py`, `plugins/kanban/`, `~/.hermes/senter-bridge/events.jsonl`.

## 1. Passing a ROLE to a `delegate_task` child

A child gets **no SOUL/AGENTS** by construction (`_build_child_system_prompt`: `skip_context_files=True`, "SOUL.md is skipped — identity belongs to the parent"). Identity must ride in `context`, one string, 5 blocks:

```
ROLE: weaver — you ARE this bot for one item (Meeseeks: one item, then exit).
=== SOUL (verbatim, trimmed) ===          ~2,300 chars
=== AGENTS (verbatim, trimmed) ===        ~6,300 chars
=== SKILL bot-verify-loop (verbatim) ===   3,503 chars
=== ITEM === id · Chris's exact words · seam · file + LINE ANCHORS (Senter's
             `grep -n`) · the ONE ledger assertion                 ~900 chars
=== CONTRACT === 1st tool call = mkdir CLAIM + bridge POST (bot:"weaver",
   status:"working"); VERIFY LIGHT per edit, FULL once; last line DONE/BLOCKED
   + bridge POST; progress line at 5 min, BLOCKED at 8 min.        ~600 chars
```

Measured: SOUL 3,564 · AGENTS 8,575 · bot-verify-loop 3,503 = **15,642 raw → ≈13,600 chars (~3.5K tokens)** after trims. Fine. `agent-wiki-vault-ui` is **64,287 chars — never inline**; the child runs `skill_view('agent-wiki-vault-ui')` (senter's profile has it). `bot-verify-loop` is NOT in senter's profile → must be inlined.

Trim: both Fleet tables (~1,200), both "Live bridge" blocks (~450), wake-sequence steps 2–3 (the child gets ONE item), "run the ledger before every report" (superseded). Keep verbatim: Hard rules, Diagnose-before-fix, CLAIM v2, Tooling (no `-c`/heredoc), Boundaries, done signal.

## 2. Dispatch mechanisms

| | `delegate_task` (thread) | `hermes -p bot chat -q` (process) | kanban | cron |
|---|---|---|---|---|
| First action | spawn event instant; first tool call = one LLM round-trip (10–25 s) | 30–60 s (57-plugin discovery + skill index + LLM) | dispatcher poll 60 s, runs in gateway — **gateway not running** | ≥1 min; gateway not running → never |
| Parallelism | `max_concurrent_children` (10); `background=true` returns at once, one consolidated result later | unbounded; sentinel caps | DB claim lock (duplicates CLAIM v2) | n/a |
| Plugins | **yes — same process/plugin manager**; hooks run in the child thread via `copy_context()` | yes, from the bot's HERMES_HOME (symlink + `plugins.enabled`) | yes | yes |
| Bridge attribution | **`bot=senter`** — `_profile()` reads process-global `HERMES_HOME`; no role hook. Measured worse: **0 tool events from this child (~90 calls) and 0 from Senter's desktop turns since 18:30**; pid 26520 only emitted during the 18:00 cron turn | `bot=<role>` correct (675 weaver events this hour) | — | — |
| Protected-write cards | desktop process is a gateway context (`_enable_gateway_prompts`); child inherits the parent's session key → card lands in **Senter's desktop chat, not the wiki** (bridge arms only on `-q/-Q/SENTER_BRIDGE_FORCE`). CLI dangerous-command path: `subagent_auto_approve=false` → auto-deny | **wiki card**, bot-attributed (proven E2E) | `cron_mode` deny | deny |
| Durability | dies with parent session; `child_timeout_seconds` 0 = none | survives Senter; dies on 429 / parked card | DB-durable | durable |
| Failure modes | no `clarify`/`delegate_task`/`memory`/`cronjob`; N long summaries pressure parent (spilled to `cache/delegation/`) | free-tier 429; parked card = dead worker; empty brief | needs gateway | needs gateway |

## 3. Why a small CSS item costs 20–33 min / 120–160 calls

Weaver tool mix (events.jsonl): terminal 750 · patch 443 · read_file 331 · write_file 112 · vision_analyze 100 · search_files 86 · computer_use 54. Turns of 99 tools/3 min and 84 tools/1 min show tools are cheap; the minutes are LLM latency on a bloated context (Senter's own log: 27.6 s/call at 186K tokens).

| Cost | Cause | Cut |
|---|---|---|
| ~40% of calls, most tokens | `vault-live.html` 309 KB / 2,490 lines (CSS 6–622, JS 831–2,488); `read_file` caps at 2,000 lines → "read the file" = 3–4 calls, ~80K tokens per edit | **line anchors in the brief** + `read_file(offset, limit≤80)`; **split** into `assets/wiki/style.css` + `assets/wiki/{core,feed,stream,bots}.js`, thin HTML loader → child reads 10–30 KB |
| 20–30 calls per edit | full ledger (33 assertions) + Playwright ×2 sizes + `computer_use` + `vision_analyze` after **every** edit | **VERIFY LIGHT** per edit = `node --check` + the ONE assertion + one Playwright PNG at 1456×914; **FULL once** before the done-line; drop `computer_use` (wrong-window bugs; Playwright at the user's size is the same pixels) |
| ~10 calls, 90K chars | wake-up reads: README, queue, session.md, 64 KB skill | Senter pre-reads; brief carries the 5 relevant session.md lines; skill only when the item touches the locked design |
| 3–5 min | approval cards from `-c`/heredoc; parked = dead | Tooling rule in the pack; vault files aren't protected |
| unbounded | no cap; 12/20-min caps not honored | `delegation.child_timeout_seconds: 600`, `max_iterations: 60`, contract 5/8 min |

Expected: 15–25 calls, 3–6 min per small item (5–8×) before the split; the split cuts another ~30% of tokens.

## 4. Recommendation

**Primary: `delegate_task`, role pack in `context`, `background=true`, one child per item, batched via `tasks=[…]` when several arrive.** Only path with ~0 s dispatch, real parallelism, results re-entering this conversation, and a live subagent tree in the desktop. **Fallback: `HERMES_HOME=~/.hermes/profiles/<bot> hermes chat -q "<pack>"`** for protected-file writes (klerik SOUL/AGENTS — wiki cards work there), anything >8 min, or work that must outlive Senter. **Retire for dispatch:** DM runner, kanban, cron.

Contract — **visible action ≤5 s:** Senter POSTs `{bot:<role>, text:"CLAIM <item> → spawning", status:"working"}` to the bridge (curl, <1 s) *before* `delegate_task`; the child's first tool call is the `mkdir` CLAIM + its own POST. **Done-line ≤8 min:** progress line at 5 min, `BLOCKED — <diff so far>` at 8; enforced by `child_timeout_seconds: 600` plus the CONTRACT block. Done-lines reach the wiki from the child's POST, not Senter narrating.

Gaps stated plainly: child tool events are attributed `senter` (and the desktop process emits nothing right now); child protected-write cards go to the desktop chat, not the wiki. Both go to teknium; neither blocks CSS/JS work.

## 5. Do today, in order

1. **`~/.hermes/profiles/senter/scripts/rolepack.py <bot> <item-id>`** — emits the 5-block context (trimmed SOUL/AGENTS, inlined `bot-verify-loop`, item + `grep -n` anchors, CONTRACT).
2. **senter `config.yaml`** (not protected): `delegation: {max_iterations: 60, child_timeout_seconds: 600, max_concurrent_children: 6}`.
3. **Turn checklist:** item arrives → bridge POST → `delegate_task(background=true)` same turn → reply → keep talking. Sentinel spawns `-q` only for items unclaimed >3 min.
4. **Verify now:** one background delegate on a trivial item; confirm the result re-enters chat and the child's POSTs show as `weaver` in the wiki.
5. **teknium (bridge):** (a) why pid 26520 emits no tool events since 18:30; (b) stamp child events by role — map `subagent_start.child_goal`/`ROLE:` header → `subagent_id`; (c) register the wiki notify on the child's session key so its cards reach the wiki.
6. **weaver (via delegate):** item SPLIT — CSS 6–622 → `assets/wiki/style.css`, JS 831–2,488 → `assets/wiki/*.js`; ledger 33/33 still green; README lists files.
7. **klerik:** builder AGENTS: VERIFY LIGHT/FULL replaces "ledger before every report"; caps 12/20 → 5/8.

DONE — delegate_task + ~13.6K-char inlined role pack is primary, `-q` spawn is the fallback for protected writes; child bridge attribution/approvals are `senter`/desktop-chat today (teknium); 7 ordered changes listed.
