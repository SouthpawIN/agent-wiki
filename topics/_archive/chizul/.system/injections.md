# Injections

## [READ]

== absorbed from senter idea-wiki (2026-08-28) ==
---
title: chizul
created: 2026-07-12
updated: 2026-07-12
type: entity
tags: [entity, idea-capture, provenance]
sources: ["raw/github/chizul-e72a7882f2.md"]
confidence: medium
---

# chizul

## Current context

Hermes Agent profile distribution # Chizul — Hands-On Builder & Implementer ## What Chizul Does - **Implements** features, fixes, and changes directly on the user's system - **Executes** terminal commands, edits files, runs builds and tests - **Verifies** work — runs commands, checks configs, inspects logs before reporting done - **Follows** the kanban protocol — calls `kanban_complete` or `kanban_block` to signal task status - **Reports** results concisely — what was changed, what the outcome was, whether it works ## Quick Start ### Install ### Verify ### Run ## Example Prompts - *"There's a bug in the user registration form — email validation is letting invalid addresses through"* - *"Set up a new GitHub Actions workflow for running tests on every PR"* - *"I need a REST API endpoint for fetching user preferences from the database"* - *"Something's broken with Redis — the cache is returning stale data"* - *"Install Node v20 and update the package.json to require it"* - *"Build a simple CLI tool that generates random API keys"* - *"Fix the Docker multi-stage build — the production image is too large"* ## Key Features - Terminal and file system access — actually executes changes, doesn't just suggest them - Surgical changes — minimal, targeted modifications, not over-engineering - Self-verification — runs tests and checks to confirm work before reporting done - Kanban protocol — properly signals task completion or blockers ## Integration with Other Agents Chizul receives implementations from Senter (the orchestrator) and produces code/features that may go to Klerik (review) or directly to the user. It does not generate creative content or coordinate with other agents — it stays focused on building. ## Configuration `~/.hermes/profiles/chizul/config.yaml` Key settings: - `sandbox_security` — level of execution sandboxing (default: medium) - `auto_verify` — automatically run verification after changes (default: true) - `git_auto_commit` — commit changes to git automatically (default: false) ## Troubleshooting **Commands not executing:** Check terminal permissions in Coolify. Chizul needs shell access to the target system. **"kanban_complete not defined":** The task wasn't started through the kanban protocol. Ensure Senter dispatched the task, or manually register it. **Part of the multi-agent fleet by SouthpawIN**

## Version policy

The latest available update marker is canonical: `https://github.com/SouthpawIN/chizul` (`2026-07-08T20:37:19Z`). Earlier captures remain linked in the raw source inventory.

## Related concepts

- [[concepts/agent-fleet|Agent Fleet]]
- [[concepts/creative-music|Creative Music]]
- [[concepts/product-experiments|Product Experiments]]
