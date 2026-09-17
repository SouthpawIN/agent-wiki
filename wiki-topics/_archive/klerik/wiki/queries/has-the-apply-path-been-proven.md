---
title: Query — has the proposal apply path been proven with one real approval? (YES — loop branch ticked 18:50; bot made 18:48)
created: 2026-09-05
updated: 2026-09-05
type: query
tags: [question, infra, loop, bot, timeline]
sources: [raw/inbox/2026-09-05.md]
confidence: medium
---
# Has the apply path been proven with one real approval?

**Status: attempted — proof is NEGATIVE.** The instruction at 18:18 was to "prove the apply path with one real approval" ^[raw/inbox/2026-09-05.md]. One real approval was run the same minute (the `klerik-queue-drain` loop). Its apply step, `hermes -p klerik cron create …`, FAILED, and no cron job exists for the klerik profile at compile time. The path is therefore proven *broken* at the loop → cron branch, and the loop file still says LIVE. See [[wiki-topics/klerik/wiki/entities/klerik-queue-drain-loop|klerik-queue-drain loop]].

**Update 18:32.** A retry of the cron create succeeded (job `e6e20c22e1b9` listed, next run 18:49:52) but `cron runs` shows zero executions and the CLI warns "Gateway is not running — jobs won't fire automatically." The loop branch has moved from *broken at create* to *registered, never fired*. Still not proven — proof is a first tick in `cron runs` plus a `.system/session.md` entry. Details: [[wiki-topics/klerik/wiki/queries/what-did-klerik-build-result-show|What did klerik's build result show?]].

**Per branch** (from [[wiki-topics/klerik/wiki/concepts/proposal-apply-path|Proposal apply path]]):
- skill → proven (bot-card-approval-spawn written and auto-applied 18:01) — trivial branch, a file write.
- loop → FAILED 18:18.
- bot / agent → not attempted; the queued `agents/klerik.md.proposed` card has no file on disk.
- research → not attempted; `wiki/queries/planner-runs-against-vault.md.proposed` still pending.

**What would flip this to "yes".** Any one non-trivial branch producing its proof artifact: a cron job visible in `hermes -p klerik cron list` and a first tick logged in `.system/session.md`; or a profile whose `-q` smoke emits `bridge/loaded`; or the planner query page carrying a dated answer. Then the flag on the source card is set *from* that proof, not before it.

**Why the answer matters to Chris.** His standard is that a fix he cannot see is not done, and "routed/queued" reads as stalling. A pipeline that marks LIVE on a failed apply would tell him things are running when they are not — the exact failure klerik's rule 1 exists to stop (paladin "spawned" twice before it existed). Decision record: [[wiki-topics/klerik/wiki/decisions/2026-09-05-prove-apply-path-with-one-real-approval|Prove the apply path with one real approval]].

**Update 18:42 — bot branch attempted, result: half-made.** The bot/agent branch was exercised for real on `senter-wiki-bot`: profile created, but "half-made (default SOUL, no AGENTS) — the protected-file guard blocked it" ^[raw/inbox/2026-09-05.md]. So the branch is now *broken at the protected writes* rather than *not attempted*; the fix ("Re-run the approval through the new deterministic path") moves those writes into the bridge. Proof for the branch is unchanged — `-q` emits `bridge/loaded` — and the card's `## Applied … Profile created` stamp is again a flag set before the proof. See [[wiki-topics/klerik/wiki/entities/senter-wiki-bot-spawn|senter-wiki-bot spawn]], [[wiki-topics/klerik/wiki/queries/did-the-deterministic-rerun-complete|Did the deterministic re-run complete?]].

**Update 18:58 / verified 19:07 — YES on the loop branch; bot branch made, smoke pending.** "Approvals apply end-to-end (proven three times)" ^[raw/inbox/2026-09-05.md]:
- loop → **proven**: `klerik-queue-drain` executed at 18:50:25 (`cron runs` shows `completed`; output file 18:56:40; `.system/session.md` has a dated "klerik-queue-drain tick" entry that applied authoring rule 16 and bumped the spawn skill to v0.3.0). Two more loops registered on paladin and looker with gateways auto-installed — first ticks pending ([[wiki-topics/klerik/wiki/queries/did-the-kept-loops-tick|Did the two kept loops tick?]]). Root cause of the earlier silence: [[wiki-topics/klerik/wiki/concepts/gateway-was-the-missing-ticker|Gateway was the missing ticker]].
- bot → **made**: senter-wiki-bot SOUL/AGENTS written by the bridge after Chris's nod; klerik finished voice/skin/tui/alias and reported 6 gaps. `-q` → `bridge/loaded` still unrun, so "a bot exists when it runs" is not yet ticked.
- research → claimed ("looker writes the answer into the query page") — not verified in this topic.
- skill → proven earlier.
The flag on each source card was, this time, set after the artifact existed — the standard this page asked for.
