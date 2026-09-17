---
title: Decision 2026-09-10 — bot schema consistency fix (skills as int, model field)
created: 2026-09-10
updated: 2026-09-10
type: decision
tags: [decision, infra, ui, bot-schema]
sources:
  - raw/inbox/2026-09-10.md
confidence: high
---

# Decision 2026-09-10 — bot schema consistency fix

**What.** The JSON emitted by `scan-topics.py` had inconsistent bot schemas across `scan_topics()` and `scan_vault_agents()`: some bots carried `skills` as a list (`skills: []`) while the UI expected an integer count (`skills: 0`). Additionally, `name_of()` was not stripping the `.md` suffix from topic-level agent/loop spec filenames, and a `model` field was missing from bot entries. ^[raw/inbox/2026-09-10.md]

**Fixes applied** (per Hermes 10:51 summary):
1. **`name_of()` function** — strips `.md` suffix from topic-level agent/loop spec filenames (e.g., `foo.md` → `foo`) so display names are clean.
2. **Bot schema consistency** — added `model: ""` and `skills: 0` (integer) to all bot entries in both `scan_topics()` and `scan_vault_agents()`.
3. **Scan script print format** — changed `skills=b['skills']:<3` to `skills=len(b['skills']):<3` to handle both int and list types gracefully.

**Why.** The UI's `renderBots()` and `mkTopic()` functions read `skills` as an integer for orb counts and layout. When the JSON emitted a list (`[]`), the orb math broke, contributing to the layout issue Chris reported on 2026-09-10.^ [raw/inbox/2026-09-10.md]

## Root cause
`scan_topics()` and `scan_vault_agents()` evolved independently — one path populated `skills` as a list of skill references, the other as an integer count. The mismatch propagated into `.system-live.json` and surfaced as broken row rendering in vault-live.html ([[topics-wiki/senter-wiki/wiki/entities/vault-live-html|vault-live.html]]).

## Verification
A stale `--watch` process was overwriting `.system-live.json` with pre-fix fields. The watch process was killed and `scan-topics.py` was restarted against the corrected scanner. ^[raw/inbox/2026-09-10.md]

## Related
- [[topics-wiki/senter-wiki/wiki/entities/scan-topics|scan-topics.py]]
- [[topics-wiki/senter-wiki/wiki/entities/orb-label-renaming|orb label renaming]]
- [[topics-wiki/senter-wiki/wiki/decisions/2026-09-10-layout-and-update-fix|layout and update fix]]

^[raw/inbox/2026-09-10.md]
