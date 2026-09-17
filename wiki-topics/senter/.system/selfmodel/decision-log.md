---
title: Decision Log
updated: 2026-08-31
type: selfmodel-decision-log
---

# Decision Log — Senter's self-model

Append-only. Every fleet decision with its rationale. One-line conclusions flush into memory.

## 2026-08-30 — Operating model: conversation-first
- decided-by: Chris
- rationale: Chris wants single-surface intake — free conversation with Senter; interests sort into topics; momentum triggers proactive bot/cron/skill proposals; nothing spawns silently.
- outcome: locked into senter SOUL.md (applied 2026-08-30 in desktop session after two headless approval-gate timeouts proved the klerik-prepare→senter-apply pattern).

## 2026-08-30 — Standing approval granted
- decided-by: Chris
- rationale: "when I ask for things I want you to assume that you have my approval" — act first, report after.
- outcome: Senter acts on requests without re-confirming; exceptions = irreversible/high-stakes (spending, deletion, public publishing, disk writes).

## 2026-08-30 — Sirvir → TurboSouth rebrand
- decided-by: Chris (name) + turbosovth (plan), approved via senter
- rationale: TurboFit = the project; TurboSouth = dedicated customer-service bot (install, configure, upstream fixes). Repo SouthpawIN/turbosouth, sovthpaw pet default.
- outcome: rename executed repo-wide; 19 stale refs replaced; README callout moved up top.

## 2026-08-30 — 11-lane hardware roster approved
- decided-by: Chris (via senter recommendation)
- rationale: closes the 32 GB gap (most common Apple unified class), fixes coarse 200/300 buckets, aligns lanes to usable-memory+topology fingerprint instead of VRAM-only.
- outcome: TIERS = 8/16/24/32/48/64/96/128/192/256/384, 200/300 aliases; campaign priority 48→32→24→64→16→96→128.

## 2026-08-30 — Tiel Coder identified and lane-pinned
- decided-by: Chris (clue: "same crew who makes Dirk 27B") → identified by senter, pinned by turbosovth
- rationale: audition candidate for new lanes without contaminating the 48 GB Unleashed winner.
- outcome: peculiar-ragdoll/Tiel-Coder-35B-A3B (Saga crew); isolated TIERS_TIEL lanes; Q4_K_XL→24GB, MTP→32GB, MLX oQ4e→128GB.

## 2026-08-30 — Paladin: repo standardization bot
- decided-by: Chris (spawn + name; working name Stanzo replaced by Paladin)
- rationale: every repo pairs with a companion support bot + pet (TurboFit+TurboSouth exemplar); repos standardized; vault mirrors as single source of truth.
- outcome: spawned via klerik; audit plan pending Chris approval before mass rewrite.

## 2026-08-30 — Anser onboarded as fleet redundancy gate
- decided-by: Chris ("useful for considering what is already built within Hermes to prevent redundancies")
- rationale: complement senter's surface roster-check with a deep built-in-capability check before anything new gets built.
- outcome: installed (v0.2.0), boot fixed (33 *** YAML placeholders → null), Role 3 internalized; self-knowledge audit delivered same day.

## 2026-08-31 — Self-model doctrine adopted (Anser's 5-point spec)
- decided-by: Chris (adopted wholesale)
- rationale: audit proved the vault fills the declarative-self-model gap without duplicating memory/skills-capabilities/session_search/AGENTS.md.
- outcome: llm-wiki substrate + curator lifecycle + query-on-demand + memory-flush + cron shared-sink. This directory is the implementation.

## 2026-08-31 — "Cursor for Obsidian" north star
- decided-by: Chris
- rationale: vault = knowledge base + orchestration + review layer, watched live in Obsidian; this chat = side window; approvals + project updates route to chat.
- outcome: build in progress — selfmodel scaffold (this), approval routing, update stream, template system.
