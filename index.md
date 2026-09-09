---
title: Index
updated: 2026-09-02
type: index
---

# Vault Index

> The wiki IS the coordination layer. Markdown is the API. Structure follows [[agent-wiki-spec]].

## Catalogs
- [[catalogs/fleet-dashboard|Fleet Dashboard]] — everything at a glance
- [[catalogs/topic-index|Topic Index]] — 20 topics · 60 repos
- [[catalogs/agent-roster|Agent Roster]] · [[catalogs/skill-registry|Skill Registry]] · [[catalogs/loop-registry|Loop Registry]]

## Inbox & meta
- [[Ideas]] — raw ideas, triaged into topics
- [[agent-wiki-spec]] — structure conventions
- [[Sources]] · [[log]]

Each topic under `topics/` is a self-contained GOOP instance:
`README.md` (dashboard) · `.system/` (continuity, queue, injections) · `wiki/` · `skills/` · `bots/` · `loops/`.
Edit any file — that's the steering wheel.

## Terminology (locked 2026-09-02)
**Bots** = the individual Hermes profiles we create (senter, turbosovth, klerik, anser, teknium, dogeman, paladin). **Hermes Agent** = the whole runtime they live in. Say *bots*, not *agents*, in all UI, docs, and chat. The vault directory `topics/<name>/agents/` keeps its name for GOOP-spec compatibility; it holds bots.

## Consolidation (2026-09-02)
63 topic dirs → 20 continuities per [[topics/senter/plans/topic-consolidation-2026-09-02|the consolidation plan]]. Absorbed originals are archived verbatim under `topics/_archive/<name>/`; every merged README lists them under `## Absorbed`.
