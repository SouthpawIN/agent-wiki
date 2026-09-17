---
title: Ornith config and port state
created: 2026-09-07
updated: 2026-09-07
type: entity
tags:
  - tool
  - infra
  - question
sources:
  - raw/inbox/2026-09-07.md
confidence: high
---

# Ornith config and port state

## Port state

- Bonsai MLX was observed on **11623**.
- Ornith MLX was restarted on a different port after the conflict.
- Later entries repeat: restart Ornith, verify it is live, then update Hermes config.

## Config edit attempts

- Hermes direct config writes were reported as blocked.
- A patch attempt was made to add the Ornith entry.
- Chris's recorded preference is still to start Ornith properly and update the config after port selection.
- Colibri does not work with the MLX server format; Ornith is the only viable local runtime path in this setup. ^[raw/inbox/2026-09-07.md]

## Open questions

- Is Ornith currently running on a confirmed port?
- Did the patch or a later update succeed in changing the Hermes config?
- Are Colibri or other runtimes still referenced in config after Ornith was selected?

## Related

- [[topics/burner-phone/wiki/entities/ornith|Ornith]]
- [[topics/burner-phone/wiki/entities/burner-phone|burner-phone]]
