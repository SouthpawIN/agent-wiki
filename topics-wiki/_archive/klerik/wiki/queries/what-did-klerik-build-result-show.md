---
title: Query — what did klerik's build result show (18:20–18:31)?
created: 2026-09-05
updated: 2026-09-05
type: query
tags: [question, bot, infra, timeline]
sources: [raw/inbox/2026-09-05.md]
confidence: medium
---
# What did klerik's build result show?

**Status: unanswered in raw; partially answered by the machine files.** Three blocks bracket a klerik build on 2026-09-05: "While klerik builds, the next gap: …" (18:20), "Let me check klerik's bot build and the fleet feed while that runs" (18:21), and "Noted — I'll leave AGENTS.md alone. Checking klerik's build result:" (18:31) ^[raw/inbox/2026-09-05.md]. The result itself was never filed to this inbox.

**What "klerik builds" most likely refers to.** The only apply action taken on klerik at that hour was the loop approval: `hermes -p klerik cron create "every 30m" --name klerik-queue-drain` ([[topics-wiki/klerik/wiki/entities/klerik-queue-drain-loop|klerik-queue-drain loop]]). "Build" here is the same-window session running klerik in the background (a `-q`/`-p klerik` turn) to make the profile do its first real work — consistent with klerik's rule 1, "a bot exists when it runs".

**What the machine files show at 18:32 (compile time).**
- `hermes -p klerik cron list` → job `e6e20c22e1b9 klerik-queue-drain`, every 30m, active, next run 18:49:52, **"Gateway is not running — jobs won't fire automatically."**
- `hermes -p klerik cron runs e6e20c22e1b9` → "No cron execution attempts recorded."
- `~/.hermes/profiles/klerik/cron/ticker_heartbeat` touched 18:32 — a klerik process was alive and ticking at compile time (the build turn itself), so the job *can* fire from an in-session ticker even without the gateway, but only while that process lives.
- `agents/` still holds only `.gitkeep`; `.system/session.md` last entry is 2026-09-02 — no klerik session entry was written for today's build.
- `~/.hermes/profiles/klerik/AGENTS.md` and `SOUL.md` exist (plus `SOUL.md.orig`); per [[topics-wiki/klerik/wiki/decisions/2026-09-05-leave-agents-md-alone|leave AGENTS.md alone]] the AGENTS.md must not have been touched.

**So the honest build result is:** profile present, cron job registered, zero ticks executed, gateway down, no session line written. "Built" in the file sense; not yet "running" in klerik's own rule-1 sense. It flips to answered when `cron runs` shows a first execution and `.system/session.md` gains a 2026-09-05 entry — tracked in [[topics-wiki/klerik/wiki/queries/has-the-apply-path-been-proven|Has the apply path been proven?]].

**Answered 18:42 (2026-09-05).** "Klerik's run ended with the profile half-made (default SOUL, no AGENTS) — the protected-file guard blocked it, as I suspected." ^[raw/inbox/2026-09-05.md] Disk at 18:43 agrees: `senter-wiki-bot/SOUL.md` = stock 667-byte default (mtime 18:21), no `AGENTS.md`, everything unprotected (config voice/skin, tui.json, 4 topic skills, symlinks, alias) done. The build was the `senter-wiki-bot` card, not the cron loop as guessed above — see [[topics-wiki/klerik/wiki/entities/senter-wiki-bot-spawn|senter-wiki-bot spawn]] and [[topics-wiki/klerik/wiki/concepts/protected-file-guard|Protected-file guard]]. Next: [[topics-wiki/klerik/wiki/queries/did-the-deterministic-rerun-complete|Did the deterministic re-run complete?]].
