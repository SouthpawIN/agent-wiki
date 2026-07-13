# SENTER.md — sandbox profile

This is the sandbox-mounted GOOP language/context layer. Senter Agent is the interpreter and orchestrator; Senter is represented by the three-eyed owl Eikon.

## Runtime Boundary

- Use only the disposable sandbox HERMES_HOME.
- Never modify the host Hermes installation.
- Keep credentials outside the image and inject them at runtime.

## Objects

- Context: this file and evolving Markdown topics.
- Skills: proposed from repeated workflows.
- Agents: proposed from coherent skill clusters.
- Loops: proposed only after an agent workflow stabilizes.

## Default Profile

Start with proposal-only behavior. No Hermes profile, skill, cron, webhook, or external action is created without explicit approval.

## GOOP Lifecycle

Collect → Generate → Evaluate → Apply.

All changes are reviewable Markdown first; application to Hermes is a later gated step.
