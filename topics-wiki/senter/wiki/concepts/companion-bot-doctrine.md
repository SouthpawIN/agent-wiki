---
title: Companion-bot doctrine (house pattern for SouthpawIN repos)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [repo, spec, bot]
sources: [raw/sources/knowledge/skill-senter-fleet-coordination.md, raw/sources/knowledge/senter-repo/README.md]
confidence: medium
---

# Companion-bot doctrine (house pattern for SouthpawIN repos)

House pattern set **2026-08-30**: every repo under `github.com/SouthpawIN` pairs with a dedicated **customer-service bot** that installs/configures on machines Chris can't test, observes from inside, connects pieces, and sends fixes upstream — "user convenience + fuzzy telemetry channel." [[topics-wiki/senter/wiki/entities/paladin|Paladin]] owns enforcing it across repos. ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

## README shape
hero → one-liner → companion-bot section with a **pet animation** (custom per bot; TurboSouth's `sovthpaw` pet is the style exemplar) → quick start → details → docs links.

## Instances
- TurboFit ↔ turbosovth (support agent, never merges) — the exemplar ([[topics-wiki/senter/wiki/entities/other-fleet-bots|other bots]]).
- hermes-agent (Chris's fork) ↔ teknium; agent-wiki ↔ the Senter fleet itself.
- The `SouthpawIN/senter` README (hero image, quick start, example prompts, "Part of the multi-agent fleet by SouthpawIN") predates the doctrine and lacks the pet section — a candidate for Paladin ([[topics-wiki/senter/wiki/entities/senter-repo|senter repo]]). ^[raw/sources/knowledge/senter-repo/README.md]

## Related rules
- Rebind identity ≠ rename repo (Sirvir → TurboSouth): repo/README/imagery to the bot's owner, profile identity via klerik.
- Companion bots follow the [[topics-wiki/senter/wiki/concepts/profile-setup-checklist|profile setup checklist]] and report through the [[topics-wiki/senter/wiki/concepts/done-signal|done signal]].
