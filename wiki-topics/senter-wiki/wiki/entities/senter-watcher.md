---
title: senter-watcher (per-message filing)
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [tool, loop, infra]
sources:
  - raw/inbox/2026-09-05-legacy-inbox.md
  - raw/inbox/2026-09-05.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
confidence: high
---

# senter-watcher

`assets/senter-watcher.py`, launchd `com.senter.watcher`, continuous 1.5 s poll of the Hermes `state.db` messages. Files every chat message into a topic
within seconds and posts a feed card. Chris's rule: *"per message, like Cursor."* ^[raw/inbox/2026-09-05.md] ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Behaviour (2026-09-05)
- Layer 1 target moved from `.system/inbox.md` to **`raw/inbox/<day>.md`** — the immutable layer of the [[wiki-topics/senter-wiki/wiki/concepts/two-layer-llm-wiki|two-layer LLM wiki]]. Each block:
  `## <ts> · <who> · <session> · sim <score>`. ^[raw/inbox/2026-09-05-legacy-inbox.md]
- **Instant reaction to new subjects**: a substantive message that fits no topic → scaffold `wiki-topics/<slug>/` (README, `.system`, skills-capabilities/agents/loops) *and*
  dispatch a research run to an existing bot (**looker**) that writes `.system/research.md` + a Status line. *"No card, no waiting."* ^[raw/inbox/2026-09-05-legacy-inbox.md]
- Emits a `wiki` stage event for every filing so the page moves ([[wiki-topics/senter-wiki/wiki/concepts/ui-performs-the-fleet|UI performs the fleet]]). ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Known weakness
Thin-corpus misclassification: the first piece landed in `kashik` at sim 0.08 because senter's topic had no wiki pages yet. ^[raw/inbox/2026-09-05.md]

## Pitfall
TCC blocks launchd's python from `~/Documents` — run it from the venv outside Documents, *"same fix the scanner uses."* ^[raw/inbox/2026-09-05-legacy-inbox.md]

Related: [[wiki-topics/senter-wiki/wiki/decisions/2026-09-05-per-message-watcher-one-profile-one-card|every message / one profile / one card]]; skill `senter-watcher` (operate/replay/tune).
