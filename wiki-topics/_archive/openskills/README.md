---
title: openskills
updated: 2026-08-27
type: topic
repo: https://github.com/SouthpawIN/openskills
status: dormant
tags: [repo]
---

# openskills

> Universal skills loader for AI coding agents - npm i -g openskills

**[Open on GitHub](https://github.com/SouthpawIN/openskills)** · DORMANT (since 2026-01-18) · last push 2026-01-18

## Facts
- **Language:** —
- **Stars / forks:** 1 / 0
- **License:** NOASSERTION
- **Fork of:** original work
- **Created:** 2026-01-19 · **Last push:** 2026-01-18
- **Open issues:** 0
- **Status:** DORMANT (since 2026-01-18)

## From the README

## ✨ What Is OpenSkills?

OpenSkills brings **Anthropic's skills system** to every AI coding agent — Claude Code, Cursor, Windsurf, Aider, Codex, and anything that can read `AGENTS.md`.

**Think of it as the universal installer for SKILL.md.**

## 🚀 Quick Start

```bash
npx openskills install anthropics/skills
npx openskills sync
```

By default, installs are project-local (`./.claude/skills`, or `./.agent/skills` with `--universal`). Use `--global` for `~/.claude/skills`.

## ✅ Why OpenSkills

- **Exact Claude Code compatibility** — same prompt format, same marketplace, same folder structure
- **Universal** — works with Claude Code, Cursor, Windsurf, Aider, Codex, and more
- **Progressive disclosure** — load skills only when needed (keeps context clean)
- **Repo-friendly** — skills live in your project and can be versioned
- **Private friendly** — install from local paths or private git repos

## 🧠 How It Works

### Claude Code System Prompt (Skills)

Claude Code ships skills as **SKILL.md files** and exposes them inside a `` block. When the user asks for a task, Claude dynamically loads the matching skill.

```xml

pdf
Comprehensive PDF manipulation toolkit for extracting text and tables...
plugin

```

### OpenSkills: Same Format, Universal Loader

OpenSkills generates the **exact same `` XML** in your `AGENTS.md` and loads skills via:

```bash
npx openskills read
```

So any agent that can read `AGENTS.md` can use Claude Code skills without needing Claude Code itself.

### Side-by-Side

| Aspect | Claude Code | OpenSkills |
|--------|-------------|------------|
| **Prompt Format** | `` XML | Same XML |
| **Skill Storage** | `.claude/skills-capabilities/` | `.claude/skills-capabilities/` (default) |
| **Invocation** | `Skill("name")` tool | `npx openskills read ` |
| **Marketplace** | Anthropic marketplace | GitHub (anthropics/skills) |
| **Progressive Disclosure** | ✅ | ✅ |

Show the exact AGENTS.md format OpenSkills writes

```xml

## Available Skills

When users ask you to perform tasks, check if any of the available skills below can help complete the task more effectively.

How to use skills:
- Invoke: `npx openskills read ` (run in your shell)
- The skill content will load with detailed instructions
- Base directory provided in output for resolving bundled resources

Usage notes:
- Only use skills listed in  below
- Do not invoke a skill that is already loaded in your context

pdf
Comprehensive PDF manipulation toolkit for extracting text and tables, creating new PDFs, merging/splitting documents, and handling forms...
project

```

## 🔧 Install Skills


*…truncated — full README at repo link*


## Archived
Archived 2026-09-02 — absorbed into [[wiki-topics/hermes-agent/README|hermes-agent]] by merge-topics.py v1.1.0. Nothing here was deleted or rewritten.
