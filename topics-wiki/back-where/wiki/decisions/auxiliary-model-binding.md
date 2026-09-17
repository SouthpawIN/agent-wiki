---
title: "Auxiliary model binding with no extra limitations"
created: 2026-09-06
updated: 2026-09-06
type: decision
tags:
  - decision
  - preference
  - tool
sources:
  - raw/inbox/2026-09-06.md
confidence: high
---

# Auxiliary model binding with no extra limitations

## Decision
Chris decided that assigning a model as auxiliary should not be blocked by additional constraints. He explicitly said he gave no limitations beyond that role.

> "You absolutely can I gave you no limitations. I said put it as the auxiliary model. That's it" ^[raw/inbox/2026-09-06.md]

## How this connects to model choice
This decision is paired with the expectation that a model chosen from the picker stays bound until real fallback is required. The auxiliary model is part of that binding, not a fallback by default.

^[raw/inbox/2026-09-06.md]

## Related
- [[topics-wiki/back-where/wiki/entities/model-picker-persistence|Model picker persistence until fallback]]
- [[topics-wiki/back-where/wiki/entities/m1-mac-performance-expectation|M1 Mac performance expectation]]
