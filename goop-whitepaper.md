---
title: GOOP Whitepaper v1
created: 2026-07-04
updated: 2026-07-07
type: concept
tags: [goop, whitepaper, architecture, history]
sources: [goop-whitepaper-v1-20260704]
---

# GOOP: Gentic Object-Oriented Programming

> The original architectural vision that Agent Wiki implements.
> **Authors:** Anser + sovthpaw · **Date:** July 4, 2026

## Summary

GOOP reframes multi-agent AI fleets as object-oriented programming with three primitives:

- **Skills** = methods (reusable procedures)
- **Agents** = classes (named entities with identity)
- **Loops** = main/workflow (execution infrastructure)

Three factory meta-agents (Skrypt, Klerik, Kadens) produce new instances using a unified
DSLy/GEPA optimization pipeline. A shared Continuity Stream + Wiki provides the memory substrate.

## What Agent Wiki Changes

Agent Wiki is the **practical implementation** of GOOP. Key differences:

| GOOP v1 | Agent Wiki |
|---|---|
| 6 persistent profiles | 1 profile + 4 cron jobs |
| Continuity = separate JSONL daemon | Continuity = Hermes session DB |
| Injection = bespoke plugin | Injection = `.system/injections.md` |
| Factories as named agents | Factories as cron-triggered roles |
| 3 primitives | 4 primitives (+ Context) |

## Original Text

→ Full whitepaper: [[goop-whitepaper-v1-20260704]]
