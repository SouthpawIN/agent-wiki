---
title: click-options
created: 2026-09-17
updated: 2026-09-17
type: wiki
sources:
  - index.md
  - wiki/
  - raw/inbox/
  - .system/
---

# click-options

Last updated: 2026-09-17 | Total pages: 11

---

## INTEGRATIONS

This wiki is fed by:

- **Raw inbox:** `raw/inbox/` — daily cuts from Hermes sessions
- **Sessions:** `.system/sessions/` — full conversation transcripts
- **Wiki pages:** `wiki/` — structured knowledge base

---

## README

### Entities

- [TurboFit Picker-Registration Gap](wiki/turbofit-picker-registration-gap.md) — TurboFit models work **through the Hermes runtime** (confirmed 13:21 on 2026-09-15), but they never **persist into the Hermes desktop provider/model picker** —

### Concepts

- [Obsidian Index Refresh (2026-09-16)](wiki/obsidian-index-refresh-2026-09-16.md) — On **2026-09-16 18:28** a Hermes working message (transcript `20260914_200308_f9b029`) advised refreshing the Obsidian vault view.
- [Runtime Config Fix — wayvnc + Provider Endpoints](wiki/runtime-config-fix-2026-09-15.md) — Two `hermes` working entries on **2026-09-15** documenting runtime/config problems Chris was stepping through:
- [Tab Opening Quick Fixes](wiki/tab-opening-quick-fixes.md) — A `hermes` working log recorded the **quick fixes for opening a new tab** — how the new-tab affordance works and the failure modes that leave you with no visibl
- [TurboFit Models Grouped Under the TurboFit Provider](wiki/turbofit-models-under-provider.md) — On **2026-09-15 12:40** Chris stated how he wants his models organized inside Hermes: **all TurboFit models live under the TurboFit provider**, alongside detect
- [TurboFit Provider Disappeared](wiki/turbofit-provider-disappeared.md) — On **2026-09-13 17:20** Chris reported a new problem: TurboFit is **no longer showing as a provider**. It had previously been there, holding his models, and now
- [TurboFit Provider Still Missing from the Desktop Picker (2026-09-15)](wiki/turbofit-provider-still-missing-2026-09-15.md) — On **2026-09-15**, after the runtime/config fixes (wayvnc systemd service, and the Hermes `https://`-on-plain-HTTP scheme correction) and after both models were

### Decisions

- [Model Zoo Models for the TurboFit List](wiki/model-zoo-models-for-turbofit-list.md) — On **2026-09-16 20:40** Chris said he had handed over a list of models from the **Model Zoo** to be added to the **TurboFit list**, and that the result was inco
- [Recovery Mode Password Reset](wiki/recovery-mode-password-reset.md) — Chris worked through a macOS **Recovery Mode** password reset. The steps he was following (and instructing/confirming):
- [Test Through Hermes, Not Straight to the Endpoint](wiki/test-through-hermes-not-endpoint.md) — On **2026-09-15 12:40** Chris set the acceptance criterion for testing TurboFit models: they must be exercised **through Hermes itself**, not against the raw en

### Comparisons

- [TurboFit Provider — Recurring Disappearance Pattern](wiki/turbofit-provider-recurring-disappearance.md) — Across three days the TurboFit provider (and the models nested under it) has failed to survive in the Hermes **desktop provider/model picker** — the arrow-on-de

---

## SKILLS

Topic skills stored in this wiki:

- **[click-options-turbofit-user-path-verify](skills/click-options-turbofit-user-path-verify/SKILL.md) — TurboFit works at the backend but never persists into the Hermes desktop provider/model picker (arrow-on-desktop next to the input bar). Confirmed wor

---

## BOTS

Proposed bots:

- **[turbofit-picker-watch](agents/turbofit-picker-watch.md.proposed) — **I see TurboFit keeps dropping out of the Hermes picker like it did on 09-13 — want a watcher that pings you the moment TurboFit or any of its models
- **[turbofit-provider-watch](agents/turbofit-provider-watch.md.proposed) — **I see you're keeping all your TurboFit models grouped under the TurboFit provider in Hermes — want a bot that watches the provider/model picker and 
- **[turbofit-roster-check](agents/turbofit-roster-check.md.proposed) — **I see you handed over a Model Zoo list for the TurboFit list and it came back incomplete — want a bot that reconciles your Model Zoo roster against 
- **[turbofit-roster-reconcile](agents/turbofit-roster-reconcile.md.proposed) — **I see your Model Zoo roster came back incomplete on the TurboFit list — want a bot that diffs your full roster against what's actually registered un


---

## LOOPS

Proposed loops:

- **[turbofit-picker-watch-daily](loops/turbofit-picker-watch-daily.md.proposed) — owner: looker · cadence: daily · status: SUGGESTED
- **[turbofit-picker-watch](loops/turbofit-picker-watch.md.proposed) — owner: looker · cadence: every 2h · status: SUGGESTED
- **[turbofit-roster-daily](loops/turbofit-roster-daily.md.proposed) — owner: turbosovth · cadence: daily · status: SUGGESTED
