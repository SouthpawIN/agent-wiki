# Senter Agent

> **Senter is the three-eyed owl.** The speech-to-speech interface is an unnamed, tool-free auxiliary task of Senter, not a separate agent.

Senter Agent is the runtime concept for a markdown-native GOOP system:

```text
Markdown source → Context → Skills → Agents → proposed Loops
       ↑                                        │
       └────────── summaries, results, failures ┘
```

The Wiki is the shared comprehension layer. Markdown is the source language; Hermes is the execution substrate; Senter is the comprehension, proposal, and orchestration layer.

## Markdown as GOOP

All-caps markdown files are user-authored system declarations. For example, `MEDIA.md` can describe a media domain without immediately creating a profile or schedule. Ordinary markdown pages provide evidence and continuity. Explicit frontmatter can type a document:

```yaml
---
type: skill
tags: [video, editing]
---
```

Supported typed objects are:

- `context`: knowledge, goals, constraints, relationships
- `skill`: reusable procedure
- `agent`: role, behavior, tools, and workflow
- `loop`: repeatable execution design

The first implementation is deliberately proposal-only. It parses markdown and produces typed proposals; it does not create Hermes profiles, cron jobs, webhooks, or skills implicitly. This is the safety boundary for the MVP.

## GEPA Lifecycle

Each primitive follows the same conceptual lifecycle:

1. **Collect** evidence from markdown, sessions, existing artifacts, and outcomes.
2. **Generate** candidate context updates or typed artifacts.
3. **Evaluate** against existing knowledge, contradictions, quality, and observed outcomes.
4. **Apply** only an approved winner through the appropriate Hermes mechanism.

Context reconciliation should merge into existing topics rather than create redundant pages. Skills should emerge from repeated procedures. Agents should be proposed only when a coherent skill cluster exists. Loops should be proposed only after an agent workflow is stable enough to execute repeatedly.

## Safety Boundaries

- The planner is read-only and proposal-only.
- Sensitive all-caps domains such as `WALLET.md` must reference secret-manager entries rather than contain raw card numbers, CVVs, tokens, or private keys.
- Hermes profile creation, cron/webhook deployment, and live skill writes require a later approval/enforcement layer.
- Never modify the live Hermes installation. Framework changes belong in a fork or sandbox, with tests and a verifiable patch before consideration for adoption.

## Local CLI

From this repository:

```bash
python -m senter_agent.cli . --json --queue .system/proposals.md
```

The CLI inspects markdown and can write/update a human-editable proposal queue. It never creates Hermes objects or changes the source documents.

## Roadmap

- topic reconciliation and redundancy detection
- user-editable rule manifests for all-caps system documents
- persistent proposal queue and audit trail
- Kanban integration
- safe Hermes adapters behind explicit approval gates
- modified Herm frontend with Senter's owl Eikon and live Wiki sidebar
- STS auxiliary surface for Android and other clients
- media/video pipeline as a topic that grows skills, agents, and loops from evidence

## Identity

The Herm TUI identity for Senter is the three-eyed owl. The current owl animation reference and six-state mapping are tracked in the local Agent Wiki topic `topics/senter-agent/`.
