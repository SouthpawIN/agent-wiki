---
title: README as Orchestration Layer
created: 2026-09-17
updated: 2026-09-17
type: concept
tags: [tool, infra, idea]
sources: [raw/inbox/2026-09-17.md]
confidence: low
---

# README as Orchestration Layer

The vault README.md plays a dual role: it is a human-facing README **and** the orchestration layer that Hermes agents consume.

hermes: It serves as both README for humans and orchestration layer for Hermes agents. ^[raw/inbox/2026-09-17.md]

This is the design behind the recent README/TurboFit refactor: the wiki README doubles as the orchestration layer that coordinates Hermes agents across simultaneous projects, rather than being documentation alone. The README is therefore the coordination contract the agents read, not just a description of the system.

Ties to the broader goal of the center wiki as a live orchestrator across many simultaneous projects, and to the pain of reverts/stale state that must be cleared before it can serve that safely.

See also: [[topics-wiki/beyond-pissed/wiki/concepts/readme-rendering-issue|README Rendering Issue]], [[topics-wiki/beyond-pissed/wiki/concepts/multi-project-orchestration|Multi-Project Orchestration]], [[topics-wiki/beyond-pissed/wiki/entities/center-wiki|Center Wiki]], [[topics-wiki/beyond-pissed/wiki/decisions/finish-center-wiki-and-orchestrate|Finish Center Wiki and Orchestrate]]
