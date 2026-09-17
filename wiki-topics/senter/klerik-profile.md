---
title: klerik
updated: 2026-08-27
type: topic
repo: https://github.com/SouthpawIN/klerik
status: dormant
tags: [repo]
---

# klerik

> Hermes Agent meta-profile for reviewing and correcting other agent profiles

**[Open on GitHub](https://github.com/SouthpawIN/klerik)** · DORMANT (since 2026-07-08) · last push 2026-07-08

## Facts
- **Language:** Python
- **Stars / forks:** 9 / 2
- **License:** MIT
- **Fork of:** original work
- **Created:** 2026-06-21 · **Last push:** 2026-07-08
- **Open issues:** 0
- **Status:** DORMANT (since 2026-07-08)

## From the README

# Klerik — Quality Assurance & Standards Enforcer

## What Klerik Does
- **Reviews** code, configs, and outputs from other agents against quality standards
- **Catches** issues before deployment — security, performance, style, and correctness checks
- **Runs** linters, tests, and static analysis tools
- **Verifies** agent outputs meet their stated requirements
- **Blocks** substandard work and demands fixes before approval

## Quick Start

### Install
```bash
hermes profile install https://github.com/SouthpawIN/klerik
```

### Verify
```bash
hermes profile list
```

### Run
```bash
hermes chat --profile klerik
```

## Example Prompts

- *"Review Chizul's latest PR for the authentication API"*
- *"Check this Docker image for security vulnerabilities before we deploy it"*
- *"Run the linter on the new codebase and report any issues"*
- *"Verify the database migration doesn't have any data loss risks"*
- *"Make sure this config follows our security standards"*
- *"Test the new API endpoint Chizul built — does it handle edge cases properly?"*

## Key Features
- Multi-tool verification — linters, tests, security scanners, static analysis
- Opinionated standards — enforces best practices consistently across all agents
- Clear failure reports — tells you exactly what failed and why, not just "something's wrong"
- No false passes — will block work that doesn't meet standards, demands fixes

## Integration with Other Agents
Klerik sits between Chizul (builder) and deployment/production. It reviews Chizul's output and must approve before anything goes live. Senter can dispatch review tasks to Klerik. Anser can defer to Klerik when asked "is this working correctly?"

## Configuration
`~/.hermes/profiles/klerik/config.yaml`

Key settings:
- `strictness` — enforcement level (lenient/standard/strict, default: standard)
- `required_checks` — which checks must pass (tests/lint/security/docs)
- `auto_block_on_failure` — block PRs/deployments automatically on failure (default: true)

## Troubleshooting

**Checks failing to run:** Klerik needs access to the same tools as Chizul (linters, test runners). Ensure these are installed in the environment.

**Too many false positives:** Lower `strictness` to `lenient` or adjust `required_checks` to exclude noisy checks.
**Part of the multi-agent fleet by SouthpawIN**

---

## 2026-08-29 — Klerik role update (profile factory)

Klerik's scope now: DSPy/GEPA profile factory + QA. Working notes folded from vault klerik topic during Senter consolidation. The klerik GitHub repo merges into Senter; this file preserves its identity.
