---
name: new-subject-early-trigger
description: Use when a chat message introduces a subject with no owning topic. Propose research/scaffold immediately, reusing a prior research bot before creating one.
version: 0.1.0
distilled: 2026-09-05 17:24
topic: senter
---
# new-subject-early-trigger
# New-subject early trigger

## When
A filed message has similarity below the propose threshold (.35) to every existing topic, OR names a domain no topic owns.

## Steps
1. Detect on the FIRST mention — do not wait for recurrence. Early trigger is the point.
2. Immediately emit a side-feed card: 'New subject: <X>. Research it / Scaffold a topic / Ignore'.
3. Before naming an executor, scan catalogs/agent-roster.md for a bot that has ALREADY done research on another subject; propose reusing it with the new subject as its goal.
4. Only if no research-capable bot exists, propose creating one (via klerik) — say explicitly why none fit.
5. On accept, scaffold topics/<slug>/ with README + .system/{inbox,continuity,INDEX} and file the triggering message into its inbox.
6. Log the trigger + decision in the new topic's .system/session.md and log.md same turn.

## Rules
- Wiki self-edits from this trigger need no approval; only the research/spawn choice is a card.
- One card per subject; deduplicate against _inbox/unsorted.md.

## Pitfalls
- Don't re-derive thresholds (.35 propose / .5 auto-route are locked).
- Don't treat 'new subject' as 'new bot' — reuse first.

## Evidence
> if I talk about a new subject then it should suggest maybe researching it or maybe scaffolding it or something like that
> it should use maybe a bot that we've used before to research a different subject, or create a new one, there isn't one like that
> bots need to trigger a lot sooner. Like when I want the side feed to be constantly going
