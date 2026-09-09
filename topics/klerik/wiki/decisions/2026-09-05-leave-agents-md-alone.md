---
title: Decision — leave AGENTS.md alone (Chris, 2026-09-05 ~18:31)
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, preference, bot, spec, infra]
sources: [raw/inbox/2026-09-05.md]
confidence: low
contested: true
---
# Decision — leave AGENTS.md alone

**What.** At 18:31 on 2026-09-05 the assistant acknowledged a Chris instruction: "Noted — I'll leave AGENTS.md alone. Checking klerik's build result:" ^[raw/inbox/2026-09-05.md]. The instruction itself was not captured in this inbox (the watcher filed the ack, not the ask), so the wording is inferred from the acknowledgement. What is certain: Chris told the building session **not** to edit an `AGENTS.md`, and the session complied and moved on to checking klerik's build.

**Which AGENTS.md.** Ambiguous — two candidates, both plausible from the surrounding minutes:
1. The **live/default profile's `AGENTS.md`** (`~/.hermes/AGENTS.md`). The same window's REFLECT pass 41 in `.system/queue.md` asks klerik to "land the `## Tooling` guard on the default/live profile (`hermes`) AGENTS" — the highest-scale inline-exec violation anser has recorded. If Chris said "leave AGENTS.md alone" in reply to that, it is a **standing veto** on the pass-6/pass-41 item and klerik must not apply it.
2. **klerik's own `AGENTS.md`** (`~/.hermes/profiles/klerik/AGENTS.md`), which the build in progress ("While klerik builds" 18:20) might have rewritten. In that reading Chris is protecting the existing klerik AGENTS.md from the rebuild.

3. **The vault-root `AGENTS.md`** (`~/Documents/Projects/Projects/AGENTS.md`) — added 18:48. The 18:47 stand-up lists "Vault `AGENTS.md` (behaviour rules for any Hermes in this dir): blocked as a protected file — I have the text ready" ^[raw/inbox/2026-09-05.md] under "Blocked on you". A protected-file prompt for a *new* vault AGENTS.md appearing ~18:31, Chris declining it, and the session acking "I'll leave AGENTS.md alone" fits the timeline better than either reading above, and explains why the same file is re-offered sixteen minutes later. Most probable reading; still unconfirmed because only the ack was filed. Page: [[topics/klerik/wiki/entities/vault-agents-md|Vault AGENTS.md]].

Recorded as `confidence: low` on the *which*, high on the *that*. Until Chris clarifies, the safe reading is both: the drain loop and any klerik build leave every `AGENTS.md` untouched and edit only SOUL.md / skills / config.

**Why it matters for klerik.** klerik is the only bot allowed to edit other profiles' SOUL.md / AGENTS.md ([[topics/klerik/wiki/entities/klerik|klerik — the profile factory bot]]). A Chris veto on AGENTS.md edits narrows klerik's lane and directly collides with the top item in its own queue (REFLECT pass 41 #1, and the pass-4…40 carry "same guard on reflect.md + anser AGENTS"). When [[topics/klerik/wiki/entities/klerik-queue-drain-loop|klerik-queue-drain]] first ticks, it must skip any [AGENTS] item whose apply step edits an `AGENTS.md`, or it will do the one thing Chris just said not to.

**Standing-rule propagation.** Per the fleet convention, every standing rule from Chris goes into the owning bot's SOUL the same turn. This one has not been written into klerik's SOUL.md yet (compile-time check: SOUL.md unchanged since the build). Open — see [[topics/klerik/wiki/queries/what-did-klerik-build-result-show|What did klerik's build result show?]].

**Evidence.**
> Noted — I'll leave AGENTS.md alone. Checking klerik's build result: ^[raw/inbox/2026-09-05.md]

**New tension 18:42 (contested).** The deterministic apply path adopted eleven minutes after this veto has the *bridge* write a fresh `AGENTS.md` for every newly created bot ([[topics/klerik/wiki/concepts/deterministic-apply-path|Deterministic apply path]]). If the veto meant "no AGENTS.md changes at all", the bridge now violates it on every spawn; if it meant "don't rewrite existing AGENTS.md files" (readings 1 and 2 above), creating one for a brand-new profile is fine. Dated positions: 18:31 veto (Chris, wording inferred) vs 18:42 bridge behaviour (session). Unresolved — a one-line card question to Chris settles it. Related: [[topics/klerik/wiki/decisions/2026-09-05-rerun-approval-via-deterministic-path|Re-run via deterministic path]].
