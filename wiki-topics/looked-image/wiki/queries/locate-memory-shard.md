---
title: Locate memory shard for revert target
created: 2026-09-06
updated: 2026-09-06
type: query
tags: [question, infra]
sources:
  - raw/inbox/2026-09-06.md
confidence: 0.7
---

# Locate memory shard for revert target

## Question
Is there a local memory shard for the desired UI state that can be used to revert instead of recreating from scratch?

## Context
Chris asked for recovery before recreation when a state diverged from a known screenshot.^[raw/inbox/2026-09-06.md]
The target visual is [[wiki-topics/looked-image/wiki/entities/screenshot-2026-09-05-4-38-59-pm|Screenshot 2026-09-05 4.38.59 PM]].
This is the recovery branch of [[wiki-topics/looked-image/wiki/concepts/visual-revert-target|visual revert target]] and must be evaluated before [[wiki-topics/looked-image/wiki/decisions/revert-or-recreate|revert-or-recreate decision]].

## Success criteria
- A concrete local artifact with sufficient state to revert the broken output.
- If none exists, a verified recreation that matches the referenced screenshot.
