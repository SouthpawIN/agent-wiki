---
title: SouthpawIN/agent-wiki → Senter repo (spec + sandbox)
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [repo, spec, infra]
sources:
  - raw/sources/knowledge/agent-wiki-repo/README.md
  - raw/sources/knowledge/agent-wiki-repo/spec.md
  - raw/sources/knowledge/agent-wiki-repo/SENTER.md
  - raw/sources/knowledge/agent-wiki-repo/SENTER_AGENT.md
  - raw/sources/knowledge/agent-wiki-repo/INTEGRATED_STATUS.md
  - raw/sources/knowledge/agent-wiki-repo/sandbox/README.md
  - raw/sources/knowledge/agent-wiki-repo/log.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
confidence: high
---

# agent-wiki repo (SouthpawIN/agent-wiki, consolidated into SouthpawIN/Senter)

Created 2026-07-07 (repo log). On 2026-08-29 the org was consolidated — Chris: *"this should combine senter, agent wiki, and klerik … replace all with Senter"*
— `agent-wiki` + `klerik` + `senter` → one repo **Senter**; old URLs redirect. Both repos were cloned into this topic's `raw/sources/knowledge/` on 2026-09-05
(`gh` works; only `curl` to the API was blocked). ^[raw/sources/knowledge/agent-wiki-repo/log.md] ^[raw/sources/knowledge/skill-agent-wiki-vault.md] ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Tagline
*"Senter is the three-eyed owl: a self-documenting, self-extending multi-agent system. The wiki IS the coordination layer."* Topics are miniature GOOP instances;
`SENTER.md` is the language/context layer; Senter Agent is the interpreter and orchestrator. ^[raw/sources/knowledge/agent-wiki-repo/README.md]

## Key documents
| File | What it declares |
|---|---|
| `spec.md` | four primitives, topic structure, flywheel, queue/injection formats, four factory crons, Hermes primitives table, setup commands ([[topics/senter-wiki/wiki/concepts/goop-four-primitives|GOOP primitives]]) |
| `SENTER.md` | GOOP language layer: Context/Skill/Agent/Loop typed frontmatter, all-caps modules (`MEDIA.md`, `WALLET.md`…), GEPA for every primitive, sandbox contract |
| `SENTER_AGENT.md` | runtime: proposal-only MVP, CLI `python -m senter_agent.cli . --json --queue .system/proposals.md`, roadmap (kanban, Herm frontend with owl Eikon + Wiki sidebar, Android STS) |
| `INTEGRATED_STATUS.md` | verification matrix: unified wiki `~/.hermes/wiki/`, Herm TUI `sandbox/herm-sovth/`, Petdex, Android prototype/APK/bridge, STS, Eikon |
| `catalogs/*` | fleet-dashboard, agent-roster, skill-registry, loop-registry, topic-index (templates, mostly empty at creation) |
| `goop-whitepaper.md`, `goop-nesting.md` | GOOP v1 (Anser + sovthpaw, 2026-07-04) and the nesting chain ([[topics/senter-wiki/wiki/comparisons/goop-v1-vs-agent-wiki|GOOP v1 vs Agent Wiki]]) |
^[raw/sources/knowledge/agent-wiki-repo/spec.md] ^[raw/sources/knowledge/agent-wiki-repo/SENTER.md] ^[raw/sources/knowledge/agent-wiki-repo/SENTER_AGENT.md] ^[raw/sources/knowledge/agent-wiki-repo/INTEGRATED_STATUS.md]

## Sandbox (`sandbox/`)
Rule: *"Never modify `~/.hermes/hermes-agent/` or the running Hermes installation."* Pinned clean checkouts as submodules: upstream Hermes-Agent, Southpaw's
`herm-sovth` OpenTUI frontend, `hermes-android` (prebuilt APK + Termux only, no Gradle source). Docker compose with disposable `hermes-home/`, `goop/` mounted
read-only, image tags `senter-agent:{base,media,wallet,research}`, secrets never baked in. Optional Android emulator sidecar (`docker-android:api-33`, ADB 5555),
approval-gated bridge: one screenshot/tap/swipe/text per request, 15 s timeout, 10 MB cap, no raw ADB/shell/install. Details:
[[topics/senter-wiki/wiki/concepts/sandbox-and-safety-contract|sandbox & safety contract]]. ^[raw/sources/knowledge/agent-wiki-repo/sandbox/README.md]

## Known blockers (repo)
No Gradle source in the Android checkout; owl reference HTML expected by `validate_owl_source.py` absent. ^[raw/sources/knowledge/agent-wiki-repo/INTEGRATED_STATUS.md]

## Design principles (verbatim list)
Markdown is the API · the wiki is the system · user-editable everything · dot-prefix for machine internals · topics are self-contained · factories are thin ·
injections keep you in the loop · no self-edit. ^[raw/sources/knowledge/agent-wiki-repo/README.md]
