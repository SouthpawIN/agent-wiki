---
title: agent-wiki
updated: 2026-08-27
type: topic
repo: https://github.com/SouthpawIN/agent-wiki
status: dormant
tags: [ai-wiki, goop, hermes-agent, markdown, multi-agent]
---

# agent-wiki

> A self-documenting, self-extending multi-agent system. Topics are miniature GOOP instances. Markdown is the API between human and machine. Built on Hermes Agent by Nous Research.

**[Open on GitHub](https://github.com/SouthpawIN/agent-wiki)** · DORMANT (since 2026-07-14) · last push 2026-07-14

## Facts
- **Language:** Python
- **Stars / forks:** 22 / 3
- **License:** MIT
- **Fork of:** original work
- **Created:** 2026-07-07 · **Last push:** 2026-07-14
- **Open issues:** 0
- **Status:** DORMANT (since 2026-07-14)
- **Topics:** ai-wiki, goop, hermes-agent, markdown, multi-agent, nous-research, self-documenting

## From the README

# Senter Agent

> **Senter is the three-eyed owl: a self-documenting, self-extending multi-agent system. The wiki IS the coordination layer.**
>
> Built on [Hermes Agent](https://github.com/NousResearch/hermes-agent) by [Nous Research](https://nousresearch.com).
> Topics are miniature GOOP instances. `SENTER.md` is the language/context layer; Senter Agent is the interpreter and orchestrator.

## What is Agent Wiki?

Agent Wiki organizes a multi-agent AI fleet as **a well-organized markdown vault**. Every topic you care about gets its own directory containing the full stack:

- **Context** — what the system understands about your goal
- **Loops** — cron jobs and workflows that run over time
- **Agents** — AI profiles that do the work
- **Skills** — reusable procedures agents load on demand

You chat with Senter through an unnamed, low-intelligence, tool-free speech-to-speech auxiliary task. Senter watches conversations, comprehends what you want, and proposes the skills, agents, and workflows to make it happen. Progress flows back naturally in conversation.

**Every part of the system is a markdown file you can edit.** No config dashboards. No YAML wizards. Open the wiki, change what you want, and the system picks it up.

## Quick Start

```bash
# Clone the wiki
git clone https://github.com/SouthpawIN/agent-wiki.git ~/.hermes/wiki

# Senter's front-end surface is an unnamed STS auxiliary task.
# The three-eyed owl is Senter's Herm TUI identity.

# Start the factory crons
hermes cron create "every 30m" --name "context-factory" --prompt "..."
hermes cron create "every 15m" --name "skills-factory" --prompt "..."
hermes cron create "every 15m" --name "agents-factory" --prompt "..."
hermes cron create "every 15m" --name "loops-factory" --prompt "..."

# Start chatting
hermes --tui
```

→ Full setup: [[spec|Agent Wiki Specification]]

## The Four Primitives

| Primitive | Factory | What It Is |
|---|---|---|
| **Context** | Context | Wiki pages — raw understanding from chat, structured into knowledge |
| **Loops** | Loops | Cron jobs, kanban tasks — execution that runs over time |
| **Agents** | Agents | Hermes profiles — named entities with personality, tools, and skills |
| **Skills** | Skills | SKILL.md bundles — reusable procedures loaded on demand |

Primitives nest: **Context** contains **Loops** which invoke **Agents** which load **Skills**.

## The Flywheel

From idea to working system — driven entirely by markdown reads and writes:

1. **Chat** — You tell Senter about an idea
2. **Comprehend** — Context reads the chat, writes wiki pages

*…truncated — full README at repo link*
