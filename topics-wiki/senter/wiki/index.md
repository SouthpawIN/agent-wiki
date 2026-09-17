---
title: Senter Wiki Index
description: Everything Chris has said, built, decided or worried about regarding senter — the fleet of Hermes bots, how they coordinate, the watcher/topic-agent/umbrella pipeline, approvals, profiles, crons, the sidebar's role, and Chris's architecture decisions.
---

# Senter Wiki Index

## Purpose
The Senter wiki is the memory layer for Chris's live-acting second brain. Markdown is the API; the watcher cuts messages by topic, each topic has one agent that rewrites context into structured knowledge, and the fleet pitches bots-profiles/triggers-loops/research that serve Chris's actual work.

## Key Concepts
- [[topics-wiki/senter/wiki/concepts/five-part-architecture|Five-part architecture]] — Sidebar, Watcher, Topics, Per-topic loops, Approvals
- [[topics-wiki/senter/wiki/concepts/watcher-as-cutter|Watcher as cutter]] — per-message filing
- [[topics-wiki/senter/wiki/concepts/context-to-skills-to-bots-to-loops|Context → skills → bots → loops]] — the flywheel
- [[topics-wiki/senter/wiki/concepts/topic-agent-pitch-caps|Topic-agent pitch caps]] — 1 bot / 2 loops / 1 research max
- [[topics-wiki/senter/wiki/concepts/approval-apply-paths|Approval apply paths]] — bot→profile+SOUL, loop→cron, research→wiki
- [[topics-wiki/senter/wiki/concepts/look-loop-verification|LOOK loop verification]] — proof = Chris's real window
- [[topics-wiki/senter/wiki/concepts/vault-agents-vs-profile-bots|Vault agents vs profile bots]] — proposed specs vs live profiles
- [[topics-wiki/senter/wiki/concepts/bridge-server-restart-via-launchd|Bridge server restart]] — launchd lifecycle

## Entity Pages
- [[topics-wiki/senter/wiki/entities/senter|Senter (the bot)]] — the coordinator, Chris's sidebar
- [[topics-wiki/senter/wiki/entities/chris|Chris]] — owner, voice dictation, preferences
- [[topics-wiki/senter/wiki/entities/watcher|Watcher]] — per-message filer/cutter
- [[topics-wiki/senter/wiki/entities/topic-agent|Topic agent]] — one intelligence per topic
- [[topics-wiki/senter/wiki/entities/umbrella|Umbrella]] — cross-topic governance owner
- [[topics-wiki/senter/wiki/entities/anser|Anser]] — redundancy gate / Discord support
- [[topics-wiki/senter/wiki/entities/klerik|Klerik]] — creates/adjusts bots, her voice
- [[topics-wiki/senter/wiki/entities/looker|Looker]] — UI verification via screenshots
- [[topics-wiki/senter/wiki/entities/paladin|Paladin]] — bot QA / fleet auditor
- [[topics-wiki/senter/wiki/entities/weaver|Weaver]] — wiki UI (not senter's job)
- [[topics-wiki/senter/wiki/entities/senter-bridge|Senter bridge]] — routes approvals to wiki
- [[topics-wiki/senter/wiki/entities/senter-wiki-ui|Senter Wiki UI]] — the vault-live.html
- [[topics-wiki/senter/wiki/entities/hermes-agent|Hermes Agent]] — the runtime
- [[topics-wiki/senter/wiki/entities/teknium|Teknium]] — Hermes-Agent builder
- [[topics-wiki/senter/wiki/entities/dogeman|Dogeman]] — YouTube/content studio
- [[topics-wiki/senter/wiki/entities/turbosovth|TurboSovth]] — TurboFit support
- [[topics-wiki/senter/wiki/entities/librarian|Librarian]] — proposed progressive discovery loop

## Standing Decisions
- [[topics-wiki/senter/wiki/decisions/2026-08-30-standing-approval|2026-08-30 standing approval]] — Chris grants autonomous completion
- [[topics-wiki/senter/wiki/decisions/2026-08-30-conversation-first-operating-model|2026-08-30 conversation-first model]]
- [[topics-wiki/senter/wiki/decisions/2026-09-02-senter-never-builds|2026-09-02 Senter never builds]] — route to owning bot
- [[topics-wiki/senter/wiki/decisions/2026-09-02-fleet-decisions-as-wiki-cards|2026-09-02 fleet decisions as wiki cards]]
- [[topics-wiki/senter/wiki/decisions/2026-09-05-per-message-watcher|2026-09-05 per-message watcher]]
- [[topics-wiki/senter/wiki/decisions/2026-09-05-one-agent-per-topic-no-separation|2026-09-05 one agent per topic]]
- [[topics-wiki/senter/wiki/decisions/2026-09-05-no-approval-for-wiki-edits|2026-09-05 no approval for wiki edits]]
- [[topics-wiki/senter/wiki/decisions/2026-09-05-preempt-decisions-complete-the-incomplete|2026-09-05 preempt decisions]]
- [[topics-wiki/senter/wiki/decisions/2026-09-05-backend-as-builtin-hermes-plus-markdown|2026-09-05 backend as built-in Hermes]]
- [[topics-wiki/senter/wiki/decisions/2026-09-08-complete-senter-wiki-autonomously|2026-09-08 complete Senter Wiki autonomously]]
- [[topics-wiki/senter/wiki/decisions/2026-09-08-autonomous-completion-standing-approval-extended|2026-09-08 extended standing approval]]
- [[topics-wiki/senter/wiki/decisions/2026-09-08-senter-wiki-bot-topic-folder-missing|2026-09-08 senter-wiki-bot topic folder missing]]
- [[topics-wiki/senter/wiki/decisions/2026-09-08-bridge-scan-topics-bot-name-parsing|2026-09-08 bridge scan-topics.py bot name parsing]]
- [[topics-wiki/senter/wiki/decisions/2026-09-06-model-picker-sticky-and-tts-gateway|2026-09-06 model picker sticky]]
- [[topics-wiki/senter/wiki/decisions/2026-09-08-context-fallback-threshold|2026-09-08 context fallback threshold]]
- [[topics-wiki/senter/wiki/decisions/2026-09-09-autonomous-senter-wiki-completion-continuation|2026-09-09 autonomous completion continuation]]
- [[topics-wiki/senter/wiki/decisions/2026-09-09-live-data-pipeline-verification|2026-09-09 live data pipeline verification]]

## Open Questions
- [[topics-wiki/senter/wiki/queries/event-driven-trigger-gaps-2026-09-08|Event-driven trigger gaps]]
- [[topics-wiki/senter/wiki/queries/verify-apply-paths-and-watchpaths-landed|Verify apply paths and WatchPaths landed]]

## Timeline
[[topics-wiki/senter/wiki/queries/senter-timeline|Senter timeline (2026-08-27 → present)]]

## Log
[[topics-wiki/senter/wiki/log.md|Wiki Log]] — compile records and changes