---
title: Query — did the deterministic re-run of the senter-wiki-bot approval complete, and is the bot running? (YES made 18:48 — smoke still unrun)
created: 2026-09-05
updated: 2026-09-05
type: query
tags: [question, bot, infra, timeline]
sources: [raw/inbox/2026-09-05.md]
confidence: medium
---
# Did the deterministic re-run complete?

**Update 18:47–18:48: answered — NO, and it will not until Chris clicks.** "The security gate is now blocking the approval re-run (it sees a rename + a POST that writes SOUL files as a protected-file write). I'll stop pushing on that path and wait for you — it needs your nod once." ^[raw/inbox/2026-09-05.md] Disk at 18:48: SOUL.md still 667 b default, no AGENTS.md, and the card has been renamed back to `senter-wiki-bot.md.proposed` (the `mv` half of the re-run ran, the approve POST did not; bridge feed logs the terminal call `ok: false`). Chris's two doors: approve the card in the wiki feed, or say "go". Root cause: [[topics-wiki/klerik/wiki/concepts/approval-security-gate|Approval security gate]]; decision: [[topics-wiki/klerik/wiki/decisions/2026-09-05-stop-pushing-wait-for-chris-nod|Stop pushing; wait for the nod]]; standing list: [[topics-wiki/klerik/wiki/queries/what-is-blocked-on-chris|What is blocked on Chris?]]. The six-point proof below is unchanged and still the bar once he nods.

**Earlier status (18:43): unanswered — re-run ordered 18:42, not landed at compile time.** The 18:42 instruction was "Re-run the approval through the new deterministic path" ^[raw/inbox/2026-09-05.md]. One minute later the disk still shows the half-made state: `~/.hermes/profiles/senter-wiki-bot/SOUL.md` 667 bytes (stock default, mtime 18:21:01), no `AGENTS.md`, and the only `/tmp/apply-senter-wiki-bot-*` prompt file is the 18:20 one. The re-run either had not fired or was still in flight.

**What "complete" means (proof, not stamp).**
1. `SOUL.md` content is the card's draft + Voice block, not the default persona (size ≠ 667, first line `# senter-wiki-bot`).
2. `AGENTS.md` exists with `## Role`, `## First task`, `## Skills carried`.
3. A second `/tmp/apply-senter-wiki-bot-<ts>.md` exists whose text begins "Finish setup of the Hermes profile" (the narrow klerik prompt).
4. klerik's gap report (last line of its output) is appended to the card's new `## Applied`.
5. `hermes -p senter-wiki-bot -q` emits `bridge/loaded` (klerik rule 1) — this is the only line that makes it a *running* bot.
6. Fleet `changed` event with `what: ["bots"]` in `~/.hermes/senter-bridge/events.jsonl`.

**Known risk while waiting.** The bridge marks the card `done` if `SOUL.md` exists — true even before the re-run. So a green card is not evidence; check items 1 and 5. See [[topics-wiki/klerik/wiki/concepts/deterministic-apply-path|Deterministic apply path]] weak spots.

**Why Chris cares.** This is the first time the wire from *approve a card* to *a bot answers* runs end to end. If it completes, [[topics-wiki/klerik/wiki/queries/has-the-apply-path-been-proven|Has the apply path been proven?]] flips to yes on the bot branch and [[topics-wiki/klerik/wiki/queries/what-happens-when-chris-approves-a-bot-card|What happens when Chris approves a bot card?]] changes its short answer from "the file gets renamed" to "a profile is written and klerik finishes it". Timeline: [[topics-wiki/klerik/wiki/entities/senter-wiki-bot-spawn|senter-wiki-bot spawn]].

**Update 18:58 / verified 19:07: YES — the bot is a real profile.** Chris's nod landed at ~18:48 and the deterministic path ran: "`senter-wiki-bot` is a real profile: GuyNeural, tokyonight, 30 skills, creds linked." ^[raw/inbox/2026-09-05.md] Against the six-point proof above:
1. `SOUL.md` 468 b, mtime 18:48, first line `# senter-wiki-bot`, body names the topic and the four skills to load — **pass** (not the 667 b default).
2. `AGENTS.md` 863 b with `## Role`, `## Read first`, `## First task`, `## Skills carried`, `## Rules` — **pass on structure, weak on content**: `## Role` is empty and `## First task` is "—". klerik's own gap report flagged this ("6 SOUL/AGENTS gaps reported, no edits made").
3. Narrow klerik finish prompt — not re-checked in `/tmp`; klerik's DONE line on the card covers it: "tts/skin/herm-tui.json/alias/describe all verified on disk".
4. Gap report appended to the card's `## Applied 2026-09-05 18:49` — **pass**.
5. `hermes -p senter-wiki-bot -q` → `bridge/loaded` — **not run this compile**; still the only line that makes it a *running* bot.
6. Fleet `changed` event — not checked.
Verdict: made, not yet smoked. Timeline closes in [[topics-wiki/klerik/wiki/entities/senter-wiki-bot-spawn|senter-wiki-bot spawn]]; side-by-side of both status reports in [[topics-wiki/klerik/wiki/comparisons/18-47-standup-vs-18-58-closeout|18:47 stand-up vs 18:58 close-out]].
