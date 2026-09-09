---
title: "Mistakes Made"
created: 2026-09-06
updated: 2026-09-06
type: entity
tags: [repo, pain, tool, plan, preference]
sources: ["raw/inbox/2026-09-06.md"]
confidence: medium
---

# Mistakes Made

This page records the specific lost or overwritten pieces Chris referenced after the unrecoverable overwrite. It is treated as the current known damage set and the minimum recovery target.

## Known lost state

These were the pieces the Hermes message said no longer existed on disk:

- `window.mdRender`
- `--orbShift`
- `BRIEF.md`
- `load(topic)`

## Quote

> "The backups are older snapshots that don't contain the recent good edits (no `window.mdRender`, no `--orbShift`, no `BRIEF.md`, no `load(topic)`). Those pieces existed only in the live in-memory page, and my thrashing overwrote them." ^[raw/inbox/2026-09-06.md]

## Role in recovery

Chris explicitly required the rebuild to start from the center vault's intended structure and process, not from ad hoc fixes. See [[center-vault-rebuild]], [[pre-planning-and-recovery]], and [[proactive-repair-over-workarounds]].
