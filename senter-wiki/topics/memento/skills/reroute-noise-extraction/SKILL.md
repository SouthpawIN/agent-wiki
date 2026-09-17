---
name: reroute-noise-extraction
description: Use when a raw item contains duplicated Hermes-state reroute or port-conflict noise. Retain only substantive Chris statements, treat duplicated infra as misrouted.
version: 0.1.0
distilled: 2026-09-07 21:07
topic: memento
---
# reroute-noise-extraction
1. Read the raw item.
2. Identify duplicated `Port conflict.` lines, reroute headers, or compacted summaries.
3. Extract only unique substantive Chris quotes or decisions.
4. Update existing concept/entity pages rather than creating new noise pages.
5. Route the raw item to `senter` in the compile log.

## Evidence
> 2026-09-07 18:15 Chris quote on progressive-disclosure librarian
> Repeated `Port conflict. Let me kill everything and restart fresh.` lines across multiple reroute blocks in raw/inbox/2026-09-07-from-senter.md
