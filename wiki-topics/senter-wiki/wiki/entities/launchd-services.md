---
title: launchd services of the Senter Wiki stack
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [infra, pain]
sources:
  - raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md
  - raw/inbox/2026-09-05-legacy-inbox.md
  - raw/inbox/2026-09-05.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
confidence: high
---

# launchd services of the Senter Wiki stack

| Label | Runs | Cadence | Notes |
|---|---|---|---|
| `com.senter.bridge` | [[wiki-topics/senter-wiki/wiki/entities/senter-bridge|senter-bridge]] on :8643 | daemon | restart `launchctl kickstart -k gui/$(id -u)/com.senter.bridge` ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md] |
| `com.senter.scanwatch` | [[wiki-topics/senter-wiki/wiki/entities/scan-topics|scan-topics.py --watch 20]] | daemon | restart needs Chris's approval (kills running agents) ^[raw/sources/knowledge/skill-agent-wiki-vault.md] |
| (topic-worker) | [[wiki-topics/senter-wiki/wiki/entities/topic-worker|assets/topic-worker.py]] | every 5 min | ^[raw/inbox/2026-09-05-legacy-inbox.md] |
| (umbrella) | [[wiki-topics/senter-wiki/wiki/entities/umbrella|assets/umbrella.py]] | every 30 min | ^[raw/inbox/2026-09-05-legacy-inbox.md] |
| `com.senter.topic-wiki` | [[wiki-topics/senter-wiki/wiki/entities/topic-wiki-compile-loop|assets/topic-wiki.py]] | every 15 min | ^[raw/inbox/2026-09-05.md] |
| watcher | [[wiki-topics/senter-wiki/wiki/entities/senter-watcher|senter-watcher]] | per message | restarted 17:43 for the new raw layer ^[raw/inbox/2026-09-05.md] |
| cron `senter-fleet-feed` | `senter-feed-relay.py` | every 2 min | `no_agent`, `deliver=origin`; needs gateway ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md] |
| Hermes crons (approved loops) | two loops approved via cards 18:57; paladin + looker gateways auto-installed by the apply path | per loop | "Three bots now have live crons that actually fire" — names not in raw; see [[wiki-topics/senter-wiki/wiki/queries/apply-path-proven-2026-09-05|apply path proven]] ^[raw/inbox/2026-09-05.md] |

## Pain: TCC vs `~/Documents`
"TCC blocks launchd's python from `~/Documents`. Same fix the scanner uses — run it from outside Documents." Any new launchd job touching the vault must live/run outside `~/Documents`. ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Pain: curl blocked, gh fine
GitHub's API looked unreachable ("curl blocked") while pulling the spec; later "GitHub fixed (`gh` works; the raw API was fine — only `curl` was blocked)". Both repos then cloned into the wiki as knowledge ([[wiki-topics/senter-wiki/wiki/entities/agent-wiki-repo|agent-wiki repo]]). ^[raw/inbox/2026-09-05-legacy-inbox.md]
