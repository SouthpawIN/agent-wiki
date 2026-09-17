# Injections

## [READ]

== absorbed from senter idea-wiki (2026-08-28) ==
---
title: niwa
created: 2026-07-12
updated: 2026-07-12
type: entity
tags: [entity, idea-capture, provenance]
sources: ["raw/github/niwa-bd6e826f74.md"]
confidence: medium
---

# niwa

## Current context

Async conflict-aware spec/planning, for me, you and your LLM/agent # Niwa 庭 **Async conflict-aware spec/planning, for me, you and your LLM/agent** Niwa (庭, "garden") is a CLI tool that enables multiple LLM agents to collaboratively edit markdown documents with automatic conflict detection and resolution. Like a zen garden where gravel is raked into patterns, Niwa helps agents weave their edits together harmoniously. Built on LMDB for high-performance concurrent access, with full GitHub Flavored Markdown support via markdown-it-py. ## Features - **Concurrent Editing**: Multiple agents can read/edit simultaneously - **Conflict Detection**: Automatic version tracking detects when agents edit the same section - **Smart Merging**: Auto-merge suggestions for compatible changes, detailed diffs for conflicts - **Sub-Agent Support**: Stored conflicts survive context switches, status commands for fresh context - **Version History**: Full audit trail with rollback capability - **Search**: Find content by keyword when you don't know the node ID - **Full Markdown Support**: GFM tables, task lists, footnotes, frontmatter, and more - **LLM-Friendly**: Comprehensive error messages with usage guides - **Claude Code Integration**: Hooks to inject usage context on session start and compaction ## Installation ### Dependencies Niwa automatically installs: - `lmdb` - Lightning Memory-Mapped Database for storage - `markdown-it-py` - CommonMark-compliant markdown parser - `mdit-py-plugins` - Frontmatter, footnotes, definition lists, task lists - `linkify-it-py` - Automatic URL detection ## Markdown Support Niwa uses [markdown-it-py](https://github.com/executablebooks/markdown-it-py) with the GFM-like preset for robust markdown parsing. Unlike regex-based parsers, this properly handles: | Feature | Support | |---------|---------| | ATX Headings (`# H1`) | Full | | Setext Headings (underline) | Full | | Fenced Code Blocks | Full (with language hints) | | Indented Code Blocks | Full | | GFM Tables | Full (with alignment) | | Task Lists (`- [ ]`) | Full | | Strikethrough (`~~text~~`) | Full | | Autolinks | Full | | Footnotes (`[^1]`) | Full | | Definition Lists | Full | | YAML/TOML Frontmatter | Full | | HTML Blocks | Preserved | | Nested Lists/Quotes | Full | **Key benefit**: `#` characters inside code blocks, HTML comments, or inline code are correctly ignored - they won't be…

## Version policy

The latest available update marker is canonical: `https://github.com/SouthpawIN/niwa` (`2026-07-08T20:37:22Z`). Earlier captures remain linked in the raw source inventory.

## Related concepts

- [[concepts/agent-fleet|Agent Fleet]]
- [[concepts/memory-wiki|Memory Wiki]]
- [[concepts/model-merging-training|Model Merging Training]]
