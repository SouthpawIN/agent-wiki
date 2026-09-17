---
title: Native Hermes vs custom backend — what each Senter part runs on (19:12 inventory)
created: 2026-09-05
updated: 2026-09-05
type: comparison
tags: [infra, tool, plan, spec]
sources: [raw/inbox/2026-09-05.md, raw/inbox/2026-09-05-legacy-inbox.md]
confidence: high
---

# Native Hermes vs custom backend

Ledger for [[wiki-topics/senter/wiki/decisions/2026-09-05-backend-as-builtin-hermes-plus-markdown|Chris's 19:06 decision]] ("just built in Hermes commands and markdown"). Hermes's 19:12 inventory is the baseline; each custom row carries the reason it is still custom, so the row can be retired the moment Hermes grows the capability. ^[raw/inbox/2026-09-05.md]

## Already native (Hermes command over markdown)
| Senter part | Runs as | Markdown it operates on |
|---|---|---|
| [[wiki-topics/senter/wiki/entities/topic-agent|Topic agent]] | `hermes chat -p senter` (one run per topic) | `wiki-topics/<t>/raw/` → `wiki-topics/<t>/wiki/`, `log.md` |
| Loops | `hermes cron` on the owning bot ([[wiki-topics/senter/wiki/concepts/loop-apply-path|loop apply path]], proven 18:20: cron `e6e20c22e1b9` on klerik) | the topic's pages |
| Bots | `hermes profile` (+ SOUL/AGENTS written by klerik/bridge) | `wiki-topics/senter/agents/<bot>.md` → profile files |
| Wiki | the `llm-wiki` skill layout (SCHEMA/index/log/raw/wiki) | everything under `wiki-topics/` |
| Sidebar | the `senter` profile; SOUL = sidebar spec as of 18:58 | reads `index.md` → page → section ([[wiki-topics/senter/wiki/concepts/progressive-disclosure|progressive disclosure]]) |
| Vault behaviour for any Hermes | `AGENTS.md` at the vault root (written 18:58) | — |

## Still custom, and why
| Part | Custom piece | Why not native yet | Retire when |
|---|---|---|---|
| [[wiki-topics/senter/wiki/entities/watcher|Watcher]] | launchd tail of `state.db` messages | "Hermes has no per-message hook" — only `on_session_finalize` at session end, and Chris locked **per message** ([[wiki-topics/senter/wiki/decisions/2026-09-05-per-message-watcher|decision]]) | Hermes exposes a per-message plugin/gateway event → PR-ledger candidate ([[wiki-topics/senter/wiki/decisions/2026-09-02-upstream-pr-policy|policy]]) |
| [[wiki-topics/senter/wiki/concepts/watcher-as-cutter|Cutter]] | TF-IDF sentence-group classifier; **since 19:23 the rules half is markdown** — per-topic `BRIEF.md` aliases/scope/anti-scope read by cutter and agent ([[wiki-topics/senter/wiki/concepts/topic-brief-pre-prompting|pre-prompting]]) | similarity fallback is still code; classification is not a Hermes primitive; thresholds are Chris-calibrated (.35/.50) | a native classify step exists, or the cut moves into the topic agent's own model call |
| [[wiki-topics/senter/wiki/entities/senter-bridge|Bridge]] | SSE stream + `/file` proxy for the UI (`:8643`) | the UI needs live events and vault files served to a browser pane; `hermes serve` approval.* was the mapped native path but the file/SSE proxy has no built-in | `hermes serve` (or the desktop) serves vault files + approval/event stream natively |

## What 19:09–19:12 added to the bridge row
The `/file` allowlist had to be widened to serve `wiki-topics/*/wiki/*` so the wiki pane can open the pages the topic agents write; proven live by opening the senter card via stage and firing a real diff — "1 block diffing, 2 green, 1 red." ^[raw/inbox/2026-09-05.md]

## Reading the table
- The custom column is three rows, all *plumbing between Hermes and the browser or between messages and topics*. None of the intelligence (rewrite, pitch, apply) is custom — it is `hermes chat`, `hermes cron`, `hermes profile`.
- The UI itself is out of scope by Chris's exemption: "with the UI… I'm not saying go back on anything."
- Earlier mapping (16:30, before the flow was known) lives in [[wiki-topics/senter/wiki/entities/hermes-agent|Hermes Agent]]; that table proposed `hermes kanban` claims and per-topic workers, which the [[wiki-topics/senter/wiki/decisions/2026-09-05-one-agent-per-topic-no-separation|one-agent-per-topic decision]] replaced. ^[raw/inbox/2026-09-05-legacy-inbox.md]
