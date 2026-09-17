---
title: Progressive disclosure — INDEX → file → section
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [skill, spec]
sources:
  - raw/inbox/2026-09-05-legacy-inbox.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
confidence: medium
---

# Progressive disclosure — INDEX → file → section

## What it is
The reading protocol for the [[topics/senter-wiki/wiki/entities/sidebar-agent|sidebar]] and workers: consult `INDEX.md` (regenerated over `raw/sources/knowledge/`) first, open one file, then one section — never bulk-load. Written as the `progressive-disclosure` SKILL.md on 2026-09-05 ([[topics/senter-wiki/wiki/entities/senter-wiki-skills|topic skills]]); the sidebar SOUL "reads INDEX first". ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Why it matters here
- The preview and readers have hard caps (`desktop_preview read` ≈ 24k chars; `acted` strings ~80 chars) — see [[topics/senter-wiki/wiki/concepts/pane-driving-and-verification|verification]]. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- The scanner folds only `concept/rules/context/continuity/hermes-native-map.md` into similarity text, never `session.md`/`queue.md` (100k+ churn), with a 40k cap. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- With the LLM-wiki layer, `index.md` is the disclosure entry for every topic ([[topics/senter-wiki/wiki/concepts/llm-wiki-topic-layout|LLM-wiki layout]]). ^[raw/inbox/2026-09-05.md]

Confidence medium: the skill text itself is not in this topic's raw yet — only its announcement.
