---
title: niwa
updated: 2026-08-27
type: topic
repo: https://github.com/SouthpawIN/niwa
status: dormant
tags: [repo]
---

# niwa

> Async conflict-aware spec/planning, for me, you and your LLM/agent

**[Open on GitHub](https://github.com/SouthpawIN/niwa)** · DORMANT (since 2026-07-08) · last push 2026-07-08

## Facts
- **Language:** Python
- **Stars / forks:** 1 / 0
- **License:** MIT
- **Fork of:** original work
- **Created:** 2026-01-28 · **Last push:** 2026-07-08
- **Open issues:** 0
- **Status:** DORMANT (since 2026-07-08)

## From the README

# Niwa 庭

**Async conflict-aware spec/planning, for me, you and your LLM/agent**

```bash
# Recommended: installs CLI globally
pipx install niwa
# or
uv tool install niwa
```

Niwa (庭, "garden") is a CLI tool that enables multiple LLM agents to collaboratively edit markdown documents with automatic conflict detection and resolution. Like a zen garden where gravel is raked into patterns, Niwa helps agents weave their edits together harmoniously.

Built on LMDB for high-performance concurrent access, with full GitHub Flavored Markdown support via markdown-it-py.

## Features

- **Concurrent Editing**: Multiple agents can read/edit simultaneously
- **Conflict Detection**: Automatic version tracking detects when agents edit the same section
- **Smart Merging**: Auto-merge suggestions for compatible changes, detailed diffs for conflicts
- **Sub-Agent Support**: Stored conflicts survive context switches, status commands for fresh context
- **Version History**: Full audit trail with rollback capability
- **Search**: Find content by keyword when you don't know the node ID
- **Full Markdown Support**: GFM tables, task lists, footnotes, frontmatter, and more
- **LLM-Friendly**: Comprehensive error messages with usage guides
- **Claude Code Integration**: Hooks to inject usage context on session start and compaction

## Installation

```bash
# Recommended: install as global CLI tool
pipx install niwa
# or with uv
uv tool install niwa

# Alternative: install in a virtual environment
uv venv && source .venv/bin/activate
uv pip install niwa

# Or from source
git clone https://github.com/secemp9/niwa
cd niwa
pip install .

# For development (editable install)
pip install -e ".[dev]"
```

### Dependencies

Niwa automatically installs:
- `lmdb` - Lightning Memory-Mapped Database for storage
- `markdown-it-py` - CommonMark-compliant markdown parser
- `mdit-py-plugins` - Frontmatter, footnotes, definition lists, task lists
- `linkify-it-py` - Automatic URL detection

## Markdown Support

Niwa uses [markdown-it-py](https://github.com/executablebooks/markdown-it-py) with the GFM-like preset for robust markdown parsing. Unlike regex-based parsers, this properly handles:

| Feature | Support |
|---------|---------|
| ATX Headings (`# H1`) | Full |
| Setext Headings (underline) | Full |
| Fenced Code Blocks | Full (with language hints) |
| Indented Code Blocks | Full |
| GFM Tables | Full (with alignment) |
| Task Lists (`- [ ]`) | Full |
| Strikethrough (`~~text~~`) | Full |
| Autolinks | Full |
| Footnotes (`[^1]`) | Full |
| Definition Lists | Full |

*…truncated — full README at repo link*


## Archived
Archived 2026-09-02 — absorbed into [[topics/dev-tooling/README|dev-tooling]] by merge-topics.py v1.1.0. Nothing here was deleted or rewritten.
