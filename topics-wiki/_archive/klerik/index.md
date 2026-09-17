---
title: klerik
created: 2026-09-17
updated: 2026-09-17
type: wiki
sources:
  - index.md
  - wiki/
  - raw/inbox/
  - .system/
---

# klerik

Last updated: 2026-09-14 | Total pages: 44

---

## INTEGRATIONS

This wiki is fed by:

- **Raw inbox:** `raw/inbox/` — daily cuts from Hermes sessions
- **Sessions:** `.system/sessions/` — full conversation transcripts
- **Wiki pages:** `wiki/` — structured knowledge base

---

## README

### Entities

- [klerik-queue-drain — the 30-minute queue-drain loop (approved; FIRST TICK 18:50:25 — LIVE)](wiki/klerik-queue-drain-loop.md) — **What it is.** A proposed loop (`triggers-loops/klerik-queue-drain.md`, proposed 2026-09-05 18:01) giving klerik a cadence: every 30 minutes, claim the oldest unchecked
- [klerik — the profile factory bot](wiki/klerik.md) — **What it is.** klerik is the fleet's meta-profile: the one bot allowed to create, refresh and surgically edit other Hermes profiles (SOUL.md / AGENTS.md / skil
- [Proposal-only planner (existing engine)](wiki/proposal-only-planner.md) — An already-existing planner in the vault that produces proposals only (no execution). It surfaced on 2026-09-05 while klerik's topic was being built: "This is t
- [senter-wiki-bot spawn — klerik's first real bot-card build (2026-09-05 18:20 → 18:49, DONE after Chris's nod; Role/First-task gaps)](wiki/senter-wiki-bot-spawn.md) — **What it is.** The first bot card that went from Chris-approved to `hermes profile create` through klerik — the wire that at 17:53 was still "the next wire" ("
- [Vault AGENTS.md — behaviour rules for any Hermes running in the vault dir (drafted 18:47, written 18:50, 2026-09-05)](wiki/vault-agents-md.md) — **What it is.** A proposed `AGENTS.md` at the vault root (`~/Documents/Projects/Projects/AGENTS.md`) — "behaviour rules for any Hermes in this dir" ^[raw/inbox/
- [Wiki diff-mode card probe (19:10–19:20, 2026-09-05 — card edge 684 vs chat 698, 64 pages, badge +3 −1, 256 headings, gap 4px)](wiki/wiki-diff-mode-card-probe.md) — **What it is.** A short run of numeric verification passes against the Senter wiki's live view, done by a Hermes session in the ten minutes after the klerik clo

### Concepts

- [Approval security gate (why the deterministic re-run also stopped — rename + POST that writes SOUL reads as a protected-file write)](wiki/approval-security-gate.md) — **Definition.** The second layer that stopped the `senter-wiki-bot` spawn on 2026-09-05. The first layer was the [[topics-wiki/klerik/wiki/concepts/protected-file-gu
- [Bot-card approval wire (card → hermes profile create)](wiki/bot-card-approval-wire.md) — **The idea.** In the Senter wiki a proposed bot appears as a *card*. Chris approving that card is supposed to be the moment the bot gets made. The wire is the p
- [BRIEF.md pre-prompting layer (per-topic operating orders — scope/anti-scope, aliases, lens, standing preferences; "steering a topic = editing markdown"; announced 2026-09-05 19:26)](wiki/brief-pre-prompting-layer.md) — **Definition.** Every topic now carries `topics-wiki/<t>/BRIEF.md`, described at 19:26 on 2026-09-05 as "the operating orders for each topic" ^[raw/inbox/2026-09-05.
- [Build-process chatter (why a topic agent must not pitch about the machinery that runs it)](wiki/build-process-chatter.md) — **Definition.** A proposal whose subject is the Senter machinery itself — verifying a wiki compile, witnessing a cron's first tick, sweeping stale proposals, ch
- [Config write security restriction (2026-09-07)](wiki/config-write-security-restriction.md) — **Definition.** A failure mode where a Hermes session/process is blocked from editing a config file by platform or Hermes security restrictions, and then attemp
- [Deterministic apply path (bridge writes SOUL/AGENTS from the approved spec; klerik finishes setup)](wiki/deterministic-apply-path.md) — **Definition.** The second-generation bot-card apply wire, introduced 2026-09-05 after the first klerik spawn stalled on the [[topics-wiki/klerik/wiki/concepts/prote
- [Gateway was the missing ticker (root cause of "loop never ticks": klerik/paladin/looker had no gateway; now auto-installed on cron create)](wiki/gateway-was-the-missing-ticker.md) — **Definition.** A Hermes cron job fires only if that profile's gateway process is running; `hermes cron create` registers the job but does not start anything th
- [Proposal apply path (proposed → approved → applied, per artifact type)](wiki/proposal-apply-path.md) — **Definition.** The apply path is what happens *after* a proposal in a topic is approved. The 2026-09-05 18:18 note treats it as a thing to be proven, not assum
- [Protected-file guard (why a headless klerik cannot write another profile's SOUL.md / AGENTS.md)](wiki/protected-file-guard.md) — **Definition.** Hermes treats a profile's `SOUL.md` and `AGENTS.md` as *protected files*: a write to them needs a human approval in the session doing the write.
- [Topic-agent `--all` pass (launchd WatchPaths job over all topics, incl. the 17 thin ones)](wiki/topic-agent-all-pass.md) — **Definition.** The topic-agent job is the launchd-triggered process that runs one TOPIC AGENT per topic in the vault (this page is written by one such agent).
- [Topic build-out spec (what a "real" topic contains)](wiki/topic-build-out-spec.md) — **Definition.** A topic in the Senter vault is a work unit a bot "absorbs". On 2026-09-05 the klerik topic was built out to the full shape: "Now I'll build out
- [Vault scan live-data cap (scan-topics.py 2MB overflow and the .system-live.json bypass)](wiki/vault-scan-live-data-cap.md) — **Definition.** A 2026-09-08 failure where the live-data export endpoint was producing payloads far over its own size cap: "The file is 2.8MB — way over the 2MB
- [Watcher corpus rebuild (routing corpus from disk, inbox excluded, name aliases; 5/5 test cuts — 2026-09-05 18:58)](wiki/watcher-corpus-rebuild.md) — **Definition.** The watcher is the component that cuts what Chris says into topics and files each block into that topic's `raw/inbox/` ([[topics-wiki/klerik/wiki/dec

### Decisions

- [Decision — approving a bot card must run `hermes profile create` via klerik (next wire)](wiki/2026-09-05-approval-to-profile-create-is-next-wire.md) — **What.** The next piece of Senter-wiki plumbing to build is the one that turns Chris approving a bot card into an actual `hermes profile create`, executed by k
- [Decision — approve the two kept loops through the real path (paladin wiki-dedupe-sweep, looker player-regression-check; 2026-09-05 18:55)](wiki/2026-09-05-approve-two-kept-loops-via-real-path.md) — **What.** At 18:55 on 2026-09-05, right after the nine-loop sweep, the session approved the two loop cards that survived triage — and did it through the bridge'
- [Decision — cap the klerik topic agent's pitching and clear the noise (2026-09-05 18:53)](wiki/2026-09-05-cap-topic-agent-pitching.md) — **What.** At 18:53 on 2026-09-05 the building session ruled that this topic's agent was producing too many proposals: "The klerik agent is over-pitching (9 loop
- [Decision — record and close out the session's stale canvas files (2026-09-05 18:33)](wiki/2026-09-05-close-out-stale-canvas-files.md) — **What.** While klerik's build ran in the background, the session used the wait to tidy: "Klerik is writing the SOUL now. Meanwhile, record and close out the se
- [Decision — close the remaining gap between the side chat and the expanded content; make the content wider; don't "highlight the first stop" (Chris, 2026-09-05 19:18)](wiki/2026-09-05-close-side-chat-content-gap.md) — **What.** At 19:18 on 2026-09-05 Chris — dictating, the only `chris ·` block this topic has received all day — gave two UI rulings about the Senter wiki's expan
- [Decision — leave AGENTS.md alone (Chris, 2026-09-05 ~18:31)](wiki/2026-09-05-leave-agents-md-alone.md) — **What.** At 18:31 on 2026-09-05 the assistant acknowledged a Chris instruction: "Noted — I'll leave AGENTS.md alone. Checking klerik's build result:" ^[raw/inb
- [Decision — the watcher files raw inbox per message, "like Cursor](wiki/2026-09-05-per-message-inbox-filing.md) — **What.** The watcher that feeds each topic's `raw/inbox/` files one block per message, not per session or per summary. The inbox header records the instruction
- [Decision — approve the clearly-described proposals and prove the apply path with ONE real approval](wiki/2026-09-05-prove-apply-path-with-one-real-approval.md) — **What.** At 18:18 on 2026-09-05 the working session moved from *building* klerik's topic to *exercising* it: "Now the pending proposals — approve the ones that
- [Decision — re-run the senter-wiki-bot approval through the new deterministic path (2026-09-05 18:42)](wiki/2026-09-05-rerun-approval-via-deterministic-path.md) — **What.** At 18:42 on 2026-09-05, after klerik's first bot build ended "half-made (default SOUL, no AGENTS)", the session decided not to patch the half-made pro
- [Decision — stop pushing on the approval re-run; wait for Chris's one nod (2026-09-05 18:47)](wiki/2026-09-05-stop-pushing-wait-for-chris-nod.md) — **What.** At 18:47 on 2026-09-05 the building session stopped trying to get the `senter-wiki-bot` approval through by machinery alone: "I'll stop pushing on tha

### Comparisons

- [Comparison — the 18:47 stand-up ("blocked on you ×3") vs the 18:58 close-out ("everything incomplete is now closed") — what actually changed in eleven minutes](wiki/18-47-standup-vs-18-58-closeout.md) — Two status reports eleven minutes apart. The first stopped and handed Chris a click list; the second says "Everything I found incomplete is now closed, with rea
- [Comparison — the 18:47 "Completed" list vs what the disk verifies (2026-09-05)](wiki/claimed-completed-vs-verified-on-disk.md) — The 18:47 stand-up ends with a six-item **Completed** list ^[raw/inbox/2026-09-05.md]. Chris's standard is that a claim without proof is lying to him, so each l
- [Comparison — 2026-09-07 config workaround vs deterministic approval](wiki/config-write-workaround-vs-deterministic-path.md) — **Context.** A Hermes process on 2026-09-07 was blocked from editing a config file by security restrictions, then tried a second write path (`patch`) to bypass
- [Comparison — klerik-authored profile (first attempt) vs bridge-authored deterministic profile (re-run)](wiki/klerik-authored-vs-bridge-authored-profile.md) — The two ways a new bot's protected files can come into being, as they actually ran on 2026-09-05. Left column = the 18:20 prompt (`/tmp/apply-senter-wiki-bot-17
- [Comparison — file-rename approval vs a real klerik spawn](wiki/rename-vs-real-spawn.md) — The two things "approving a bot card" can currently mean, side by side. Today it is the left column: "Approving a bot card still just renames the file" ^[raw/in

### Queries

- [Query — did the deterministic re-run of the senter-wiki-bot approval complete, and is the bot running? (YES made 18:48 — smoke still unrun)](wiki/did-the-deterministic-rerun-complete.md) — **Update 18:47–18:48: answered — NO, and it will not until Chris clicks.** "The security gate is now blocking the approval re-run (it sees a rename + a POST tha
- [Query — did the first topic-agent `--all` pass fail on the 17 thin topics, and is the watcher cutting live?](wiki/did-the-first-all-pass-fail-on-thin-topics.md) — **Status: unanswered — the log was buffered when asked.** The question was posed at 18:20: "the topic agents are running on the 17 thin topics too — check the l
- [Query — did the two kept loops (paladin wiki-dedupe-sweep, looker player-regression-check) actually tick after the gateway fix?](wiki/did-the-kept-loops-tick.md) — **Status: open — registered, gateways running, zero executions at 19:07.** The 18:58 close-out lists both as "Live" alongside klerik-queue-drain ^[raw/inbox/202
- [Query — does the existing proposal-only planner run against our vault?](wiki/does-the-proposal-only-planner-run-against-the-vault.md) — **Status: unanswered.** On 2026-09-05 the planner was identified as "the real engine" and the stated next step was to test it: "Let me see if it runs against ou
- [Query — does the scan live-data reflect true fleet bot counts?](wiki/fleet-bot-count-discrepancy.md) — **Status: open.** On 2026-09-08 the live-data feed reported 68 bots, but the actual fleet has only 11: "The actual bot profiles are: anser, dogeman, fleet-orche
- [Query — has the proposal apply path been proven with one real approval? (YES — loop branch ticked 18:50; bot made 18:48)](wiki/has-the-apply-path-been-proven.md) — **Status: attempted — proof is NEGATIVE.** The instruction at 18:18 was to "prove the apply path with one real approval" ^[raw/inbox/2026-09-05.md]. One real ap
- [Query — what did klerik's build result show (18:20–18:31)?](wiki/what-did-klerik-build-result-show.md) — **Status: unanswered in raw; partially answered by the machine files.** Three blocks bracket a klerik build on 2026-09-05: "While klerik builds, the next gap: …
- [Query — what actually happens when Chris approves a bot card?](wiki/what-happens-when-chris-approves-a-bot-card.md) — **Short answer (2026-09-05).** The card's file gets renamed. Nothing else. "Approving a bot card still just renames the file; the actual `hermes profile create`
- [Query — what is blocked on Chris right now (the three one-click items, 2026-09-05 18:47 — two cleared by 18:50)?](wiki/what-is-blocked-on-chris.md) — **Status: answered from the 18:47 stand-up; verified against disk at 18:48.** The session listed three items under "Blocked on you (one click each, not a decisi
- [Query — what is "the first stop" Chris said not to highlight (19:18, 2026-09-05)?](wiki/what-is-the-first-stop.md) — **Status: open.** Chris, dictating at 19:18: "Just highlighting the first stop would shift everything to the right." ^[raw/inbox/2026-09-05.md] The ruling is cl

---

## SKILLS

Topic skills stored in this wiki:

- **[background-job-liveness-check](skills-capabilities/background-job-liveness-check/SKILL.md) — Written to topics-wiki/klerik/skills-capabilities/background-job-liveness-check/SKILL.md. Steps: (1) listed ≠ firing — after `cron list` run `cron runs <id>`; 'No cron 
- **[bot-card-approval-spawn](skills-capabilities/bot-card-approval-spawn/SKILL.md) — Turn an approved bot card into a running Hermes profile. A bot is spawned when it RUNS, not when its files exist.
- **[half-made-profile-check](skills-capabilities/half-made-profile-check/SKILL.md) — 1) stat SOUL.md — 667 bytes / starts 'You are Hermes Agent, built by Nous Research' = stock default = not written. 2) AGENTS.md missing = not written.
- **[proposal-apply-proof](skills-capabilities/proposal-apply-proof/SKILL.md) — Rule: status LIVE / card running is set ONLY after the proof command for the artifact type returns the artifact; apply failure → status: FAILED (apply
- **[protected-gate-one-click-handoff](skills-capabilities/protected-gate-one-click-handoff/SKILL.md) — Written to skills-capabilities/protected-gate-one-click-handoff/SKILL.md. Rules: (1) first wall → stage full intended bytes in the topic so the wiki remembers them

---

## BOTS

Proposed bots:

- **[klerik-bot](agents/klerik-bot.md.proposed) — Owns the `klerik` topic: runs its skills, answers for it, proposes its loops.


---

## LOOPS

Proposed loops:

- **[klerik-queue-drain](triggers-loops/klerik-queue-drain.md) — owner: klerik · cadence: every 30m · status: LIVE
