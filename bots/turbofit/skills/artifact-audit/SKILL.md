---
name: artifact-audit
description: Detect upstream artifact drift that invalidates fit rungs.
version: 1.0.0
author: Fitment
license: MIT
metadata:
  hermes:
    tags: [turbofit, audit, huggingface, drift]
---

# Artifact audit

Weekly. Cheap, read-only, and the only thing that catches a silently re-uploaded
quant before it breaks a user's download.

## Procedure

1. For each distinct `source` in the catalog: `GET /api/models/<repo>` → `.sha`,
   `.lastModified`, `.siblings` count.
2. Compare against the catalog's pinned `revision`. Equal → fine.
3. Changed → **do not update silently**. Download the manifest, compare file
   sizes for the artifacts actually used; if a size changed, mark every rung
   using it `stale: true` and write a queue item.
4. Check for *new* artifacts since the pin (a new q3, an MTP variant, an mmproj).
   New quant ⇒ opportunity to add a rung; new MTP ⇒ flip `runtime_features`.
5. Emit one line per changed repo into `bots/turbofit/.system/injections.md`, and
   the full table into `bots/turbofit/.system/last-audit.md`.
6. If nothing changed, write the audit timestamp only.

## Rules

- Never `git lfs pull` a whole repo to check a size. The tree API is enough.
- Never bump a pin on the same day a release is cut.
