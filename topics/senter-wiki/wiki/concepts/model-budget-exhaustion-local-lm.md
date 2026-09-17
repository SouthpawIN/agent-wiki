---
title: Model budget exhaustion — local LM 500-hour limit
created: 2026-09-09
updated: 2026-09-09
type: concept
tags:
  - infra
  - decision
  - model
confidence: high
sources:
  - raw/inbox/2026-09-08.md
  - raw/inbox/2026-09-09.md
  - raw/inbox/2026-09-09-from-turbofit.md
---

Model budget exhaustion — local LM 500-hour limit
Chris noted he was hitting a 500-hour limit on the local model and redirected general Hermes work off that model. The local model should be reserved for local-model-as-deliverable work only; ordinary general work should use free cloud models instead.

Hardware context
- Host is an M1 MacBook 32GB unified memory. That hardware is relevant because it makes fast 131K-context inference unrealistic for daily general use and reinforces budget conservation.

Boundary
- This is a model-budget/route decision, not a wiki-surface bug. It still belongs here because it affects which profile/model Hermes runs the senter-wiki agent under and how future wiki UI work is staffed.

See also
[[topics/senter-wiki/wiki/entities/senter-agent-sandbox|senter-agent sandbox]]
[[topics/senter-wiki/wiki/decisions/2026-09-09-vault-git-init|2026-09-09 vault git init]]

^[raw/inbox/2026-09-08.md]
^[raw/inbox/2026-09-09.md]
^[raw/inbox/2026-09-09-from-turbofit.md]
