# Injections

## [READ]

== absorbed from senter idea-wiki (2026-08-28) ==
---
title: klerik
created: 2026-07-12
updated: 2026-07-12
type: entity
tags: [entity, idea-capture, provenance]
sources: ["raw/github/klerik-371cef7bad.md"]
confidence: medium
---

# klerik

## Current context

Hermes Agent meta-profile for reviewing and correcting other agent profiles # Klerik — Quality Assurance & Standards Enforcer ## What Klerik Does - **Reviews** code, configs, and outputs from other agents against quality standards - **Catches** issues before deployment — security, performance, style, and correctness checks - **Runs** linters, tests, and static analysis tools - **Verifies** agent outputs meet their stated requirements - **Blocks** substandard work and demands fixes before approval ## Quick Start ### Install ### Verify ### Run ## Example Prompts - *"Review Chizul's latest PR for the authentication API"* - *"Check this Docker image for security vulnerabilities before we deploy it"* - *"Run the linter on the new codebase and report any issues"* - *"Verify the database migration doesn't have any data loss risks"* - *"Make sure this config follows our security standards"* - *"Test the new API endpoint Chizul built — does it handle edge cases properly?"* ## Key Features - Multi-tool verification — linters, tests, security scanners, static analysis - Opinionated standards — enforces best practices consistently across all agents - Clear failure reports — tells you exactly what failed and why, not just "something's wrong" - No false passes — will block work that doesn't meet standards, demands fixes ## Integration with Other Agents Klerik sits between Chizul (builder) and deployment/production. It reviews Chizul's output and must approve before anything goes live. Senter can dispatch review tasks to Klerik. Anser can defer to Klerik when asked "is this working correctly?" ## Configuration `~/.hermes/profiles/klerik/config.yaml` Key settings: - `strictness` — enforcement level (lenient/standard/strict, default: standard) - `required_checks` — which checks must pass (tests/lint/security/docs) - `auto_block_on_failure` — block PRs/deployments automatically on failure (default: true) ## Troubleshooting **Checks failing to run:** Klerik needs access to the same tools as Chizul (linters, test runners). Ensure these are installed in the environment. **Too many false positives:** Lower `strictness` to `lenient` or adjust `required_checks` to exclude noisy checks. **Part of the multi-agent fleet by SouthpawIN**

## Version policy

The latest available update marker is canonical: `https://github.com/SouthpawIN/klerik` (`2026-07-09T00:04:04Z`). Earlier captures remain linked in the raw source inventory.

## Related concepts

- [[concepts/agent-fleet|Agent Fleet]]
- [[concepts/product-experiments|Product Experiments]]
