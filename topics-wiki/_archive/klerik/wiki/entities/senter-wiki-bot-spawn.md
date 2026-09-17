---
title: senter-wiki-bot spawn — klerik's first real bot-card build (2026-09-05 18:20 → 18:49, DONE after Chris's nod; Role/First-task gaps)
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [bot, timeline, infra, pain]
sources: [raw/inbox/2026-09-05.md]
confidence: high
contested: true
---
# senter-wiki-bot spawn — klerik's first real build

**What it is.** The first bot card that went from Chris-approved to `hermes profile create` through klerik — the wire that at 17:53 was still "the next wire" ("Approving a bot card still just renames the file; the actual `hermes profile create` via klerik is the next wire." ^[raw/inbox/2026-09-05.md]). The card lives in another topic (`topics-wiki/senter-wiki/agents/senter-wiki-bot.md`, proposed 17:13, reason: "4 approved skills cluster here with no agent hosting them (umbrella rule BOT_MIN=3)"); klerik's part of it is what this page records.

**Timeline (all times CDT, 2026-09-05).**
| Time | Event | Source |
|---|---|---|
| 18:20 | Bridge writes `/tmp/apply-senter-wiki-bot-1788650447.md` — one 30-turn prompt to klerik: create profile, symlink creds, *write SOUL.md and AGENTS.md*, copy skills, voice/skin/tui, alias. Session note: "While klerik builds, the next gap…" | bridge file; ^[raw/inbox/2026-09-05.md] |
| 18:21 | `profile create` lands: dir + default 667-byte SOUL.md + stock skill tree. "Let me check klerik's bot build and the fleet feed while that runs" | disk mtimes; ^[raw/inbox/2026-09-05.md] |
| 18:22–18:34 | config.yaml (voice GuyNeural, skin tokyonight), profile.yaml, 4 topic skills copied 18:28, `herm/tui.json` 18:34 | disk mtimes |
| 18:31 | Chris: leave AGENTS.md alone (ack filed) | ^[raw/inbox/2026-09-05.md] |
| 18:33 | "Klerik is writing the SOUL now." — optimistic; SOUL.md never changed after 18:21 | ^[raw/inbox/2026-09-05.md] vs disk |
| 18:39 | klerik stamps the card: profile created, "SOUL.md/AGENTS.md writes blocked by approval gate in CLI session — full contents queued at `agents/senter-wiki-bot-applied-edits.md`, coordinator applies in desktop session" | card `## Status` |
| 18:42 | "Klerik's run ended with the profile half-made (default SOUL, no AGENTS) — the protected-file guard blocked it, as I suspected. Re-run the approval through the new deterministic path:" | ^[raw/inbox/2026-09-05.md] |
| 18:43 (compile) | SOUL.md still 667 b / default; no AGENTS.md. Re-run **not yet landed**. | disk |
| ~18:47 | Re-run fires as `mv …senter-wiki-bot.md …md.proposed && python3 -c "<POST approve>"`; the session's security gate blocks it ("sees a rename + a POST that writes SOUL files as a protected-file write"). Bridge feed: terminal `ok: false`. Card now `.md.proposed` again. | events.jsonl; ^[raw/inbox/2026-09-05.md] |
| 18:47 | "I'll stop pushing on that path and wait for you — it needs your nod once." Listed under "Blocked on you (one click each, not a decision)": approve the card in the feed, or say "go". | ^[raw/inbox/2026-09-05.md] |
| 18:48 (compile) | SOUL.md 667 b default, no AGENTS.md, card pending. **Waiting on Chris.** | disk |

**Second wall (18:47).** The deterministic path removed klerik from the protected write but not the gate itself — see [[topics-wiki/klerik/wiki/concepts/approval-security-gate|Approval security gate]] and [[topics-wiki/klerik/wiki/decisions/2026-09-05-stop-pushing-wait-for-chris-nod|Stop pushing; wait for the nod]]. Title status should now read: half-made, blocked on one click.

**Contested (dated).** 18:33 "writing the SOUL now" vs 18:42 "default SOUL" — the later reading is confirmed by disk; the earlier was a guess about a run in progress. Also the card's own `## Applied 2026-09-05 18:39 — Profile created` sits next to a Status line saying the two defining files were blocked: "created" in the file sense, not in klerik's rule-1 sense (a bot exists when it runs).

**What klerik got right.** It did not route around the gate (rule 7). It wrote the full intended SOUL.md and AGENTS.md into a handoff file (`agents/senter-wiki-bot-applied-edits.md`, "prepare-then-handoff") so nothing was lost, and it flagged "no bridge card surfaced — bridge pending was 0" as a bridge gap. That handoff file is now the human-readable spec the [[topics-wiki/klerik/wiki/concepts/deterministic-apply-path|deterministic apply path]] supersedes.

**Root cause and fix.** [[topics-wiki/klerik/wiki/concepts/protected-file-guard|Protected-file guard]] → [[topics-wiki/klerik/wiki/decisions/2026-09-05-rerun-approval-via-deterministic-path|Decision: re-run via the deterministic path]]. Whether the re-run finished: [[topics-wiki/klerik/wiki/queries/did-the-deterministic-rerun-complete|Did the deterministic re-run complete?]].

**Timeline continued.**
| Time | Event | Source |
|---|---|---|
| ~18:48 | Chris's nod lands; bridge writes SOUL.md (468 b, `# senter-wiki-bot`) and AGENTS.md (863 b), symlinks `.env` and `auth.json` | disk mtimes 18:48 |
| 18:49 | Card stamped `## Applied 2026-09-05 18:49`: "Profile created … (SOUL/AGENTS from this spec, 17 topic skills, creds linked). klerik: DONE: senter-wiki-bot setup complete (tts/skin/herm-tui.json/alias/describe all verified on disk); 6 SOUL/AGENTS gaps reported, no edits made." | card |
| 18:58 | "`senter-wiki-bot` is a real profile: GuyNeural, tokyonight, 30 skills, creds linked." | ^[raw/inbox/2026-09-05.md] |
| 19:07 (compile) | Confirmed: SOUL real, AGENTS present (Role/First task empty), 30 skill dirs. `-q` smoke not yet run. | disk |

**Closed.** The spawn that took 18:20 → 18:49 and two walls ([[topics-wiki/klerik/wiki/concepts/protected-file-guard|protected-file guard]], [[topics-wiki/klerik/wiki/concepts/approval-security-gate|security gate]]) ended the way the [[topics-wiki/klerik/wiki/concepts/deterministic-apply-path|deterministic path]] specifies: bridge authored the protected files, klerik finished and reported gaps without editing. The one open thread is klerik's six gaps — the card spec left `Role` and `First task` blank, so the bridge wrote them blank. That is a card-quality issue upstream of klerik, recorded here so the next senter-wiki card fills them in.
