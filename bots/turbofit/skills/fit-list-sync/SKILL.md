---
name: fit-list-sync
description: Reconcile fit ladders with the catalog and keep both honest.
version: 1.0.0
author: Fitment
license: MIT
metadata:
  hermes:
    tags: [turbofit, fit, ladders, hardware]
---

# Fit list sync

Run whenever a catalog variant changes, and before any release.

## Procedure

1. Load `references/model-catalog.json` and `references/fit-lists.json`.
2. **Coverage**: every `roles: ["main"]` variant appears on at least one rung, or
   carries an explicit reason it does not (too large, no q3, awaiting conversion).
3. **Orphans**: every rung `model` resolves to a catalog `family`. A rung naming a
   model that was renamed is a silent 404 at serve time — fix the name, not the rung.
4. **Monotonicity**: within a ladder, as the tier grows, context must not shrink
   and quant must not get smaller. Violations mean two rows were edited out of order.
5. **Power rule** (Chris's constraint): if a rung sits at IQ3_S and that quant is
   near-lossless for the family, do not push a heavier quant onto the same tier
   for benchmark vanity — note "power bill stays on IQ3_S".
6. **Dense/unified policy**: unified is MoE-only by default. Dense entries there
   must be tagged `dense-exception` and carry a measured tok/s floor.
7. **Write** the ladder, then append a delta table to `bots/turbofit/matrix.md`
   (tier, old model, new model, why).
8. **Gate**: `pytest -q` and a `fit_check` dry run against the current machine's
   budget. Report the first tier where the ladder disagrees with physics.
