---
title: Protected-file guard (why a headless klerik cannot write another profile's SOUL.md / AGENTS.md)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [infra, pain, bot, tool]
sources: [raw/inbox/2026-09-05.md]
confidence: high
---
# Protected-file guard

**Definition.** Hermes treats a profile's `SOUL.md` and `AGENTS.md` as *protected files*: a write to them needs a human approval in the session doing the write. When klerik runs headless (the bridge spawns it with `chat -p klerik --query-file … --oneshot -Q --yolo`), there is no human in that session, so the approval gate cannot be answered and the write is refused. Skills, config, symlinks, `herm/tui.json`, aliases — all unprotected — go through fine. ^[raw/inbox/2026-09-05.md]

**How it surfaced (2026-09-05, 18:20 → 18:42).** The first real bot-card approval (`senter-wiki-bot`) was handed to klerik as one big "build the profile" prompt. Twenty minutes later: "Klerik's run ended with the profile half-made (default SOUL, no AGENTS) — the protected-file guard blocked it, as I suspected." ^[raw/inbox/2026-09-05.md] The phrase *as I suspected* matters: the guard was a known risk before the run, not a surprise — the earlier note "Klerik is writing the SOUL now" (18:33) ^[raw/inbox/2026-09-05.md] was an optimistic read of a run that was actually stuck at the gate. Timeline in [[topics/klerik/wiki/entities/senter-wiki-bot-spawn|senter-wiki-bot spawn]].

**What "half-made" looks like on disk (compile-time check, 18:43).** `~/.hermes/profiles/senter-wiki-bot/SOUL.md` = 667 bytes, mtime 18:21:01, content = the stock Hermes default persona; no `AGENTS.md` at all; but `config.yaml` has voice `en-US-GuyNeural` + skin `tokyonight`, `herm/tui.json` written 18:34, four topic skills copied 18:28, `.env`/`auth.json` symlinked, alias made. Exactly the split the guard predicts: everything unprotected done, both protected files untouched. klerik itself wrote the honest version into the card: "SOUL.md/AGENTS.md writes blocked by approval gate in CLI session — full contents queued at `agents/senter-wiki-bot-applied-edits.md`, coordinator applies in desktop session."

**Why it is a root-cause, not a klerik bug.** klerik did what its checklist says; the environment it was run in cannot satisfy the gate. Any fix that makes klerik "try harder" (retry, `--yolo`, routing around) is a band-aid — and klerik's own rule 7 forbids routing around a failed gate. The structural fix is to move the protected writes to a place that *does* have authority: the approval Chris already gave in the wiki. That is the [[topics/klerik/wiki/concepts/deterministic-apply-path|deterministic apply path]]. The same guard is presumably why the fleet's earlier "paladin spawned twice before it existed" happened — the pattern klerik's rule 1 ("a bot exists when it runs") was written against.

**Relation to Chris's AGENTS.md veto.** Same afternoon, Chris said to leave AGENTS.md alone ([[topics/klerik/wiki/decisions/2026-09-05-leave-agents-md-alone|Leave AGENTS.md alone]]). The guard and the veto point the same way for *existing* profiles: klerik must not be rewriting AGENTS.md files in the background. For a *new* profile the bridge now writes AGENTS.md from the approved spec — see the open question in [[topics/klerik/wiki/decisions/2026-09-05-rerun-approval-via-deterministic-path|Re-run via deterministic path]].
