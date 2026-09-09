# Injections

## [READ]

== absorbed from senter idea-wiki (2026-08-28) ==
---
title: openskills
created: 2026-07-12
updated: 2026-07-12
type: entity
tags: [entity, idea-capture, provenance]
sources: ["raw/github/openskills-340c2a92b3.md"]
confidence: medium
---

# openskills

## Current context

Universal skills loader for AI coding agents - npm i -g openskills <div align="center"> <img src="./assets/logo.svg" alt="OpenSkills" width="420" /> <br/> <br/> **Universal skills loader for AI coding agents** One CLI. Every agent. Same format as Claude Code. [](https://www.npmjs.com/package/openskills) [](https://www.npmjs.com/package/openskills) [](https://opensource.org/licenses/Apache-2.0) [Quick Start](#-quick-start) · [How It Works](#-how-it-works) · [Commands](#-commands) · [Create Skills](#-creating-your-own-skills) · [FAQ](#-faq) </div> --- ## ✨ What Is OpenSkills? OpenSkills brings **Anthropic's skills system** to every AI coding agent — Claude Code, Cursor, Windsurf, Aider, Codex, and anything that can read `AGENTS.md`. **Think of it as the universal installer for SKILL.md.** --- ## 🚀 Quick Start By default, installs are project-local (`./.claude/skills`, or `./.agent/skills` with `--universal`). Use `--global` for `~/.claude/skills`. --- ## ✅ Why OpenSkills - **Exact Claude Code compatibility** — same prompt format, same marketplace, same folder structure - **Universal** — works with Claude Code, Cursor, Windsurf, Aider, Codex, and more - **Progressive disclosure** — load skills only when needed (keeps context clean) - **Repo-friendly** — skills live in your project and can be versioned - **Private friendly** — install from local paths or private git repos --- ## 🧠 How It Works ### Claude Code System Prompt (Skills) Claude Code ships skills as **SKILL.md files** and exposes them inside a `<available_skills>` block. When the user asks for a task, Claude dynamically loads the matching skill. ### OpenSkills: Same Format, Universal Loader OpenSkills generates the **exact same `<available_skills>` XML** in your `AGENTS.md` and loads skills via: So any agent that can read `AGENTS.md` can use Claude Code skills without needing Claude Code itself. ### Side-by-Side | Aspect | Claude Code | OpenSkills | |--------|-------------|------------| | **Prompt Format** | `<available_skills>` XML | Same XML | | **Skill Storage** | `.claude/skills/` | `.claude/skills/` (default) | | **Invocation** | `Skill("name")` tool | `npx openskills read <name>` | | **Marketplace** | Anthropic marketplace | GitHub (anthropics/skills) | | **Progressive Disclosure** | ✅ | ✅ | <details> <summary><strong>Show the exact AGENTS.md format OpenSkills writes</strong></summary>…

## Version policy

The latest available update marker is canonical: `https://github.com/SouthpawIN/openskills` (`2026-06-09T21:36:35Z`). Earlier captures remain linked in the raw source inventory.

## Related concepts

- [[concepts/agent-fleet|Agent Fleet]]
- [[concepts/local-inference|Local Inference]]
