# SENTER.md — GOOP Language and Context Layer

> **SENTER.md is the declarative language/context layer. Senter Agent is the agent that interprets and operates on it.**
>
> Senter is personified in Herm by the three-eyed owl Eikon. The speech-to-speech interface is an unnamed, tool-free auxiliary task of Senter, not a separate agent.

## Mental Model

```text
SENTER.md / Markdown source
          ↓
   Senter Agent reads, reconciles, and understands
          ↓
       Context
          ↓
       Skills
          ↓
       Agents
          ↓
   proposed / approved Loops
          ↓
 Hermes sandbox or explicitly approved runtime
```

`SENTER.md` is not an executable script and does not grant permissions by itself. It is human-readable source code for the GOOP system: intent, context, relationships, constraints, declarations, and desired evolution. Senter Agent is the runtime/compiler/orchestrator that interprets this source and produces proposals.

## Language Layers

### Context

Markdown pages and topic directories express what the system understands:

- goals and visions
- entities and concepts
- relationships and dependencies
- decisions and unresolved questions
- evidence, outcomes, and failures
- summaries that reconcile related pages

### Skill

A skill is a repeatable procedure. A typed document may declare one explicitly:

```yaml
---
type: skill
tags: [video, editing]
---
```

Skills should emerge from repeated evidence, not be created merely because a capability was mentioned once.

### Agent

An agent is a coherent role composed from a meaningful cluster of skills:

```yaml
---
type: agent
---
```

Agent declarations describe identity, responsibilities, tools, constraints, and workflow. Senter proposes an Agent only when the skill cluster is strong enough to justify a separate role.

### Loop

A Loop is a repeatable execution design:

```yaml
---
type: loop
---
```

Loops are proposed only after an Agent's workflow is sufficiently stable. The application target may be Kanban, webhook, cron, delegation, or a hybrid. Senter does not deploy a Loop merely because a schedule appears in prose.

## All-Caps Modules

An all-caps Markdown filename is a user-authored GOOP module and context boundary:

```text
MEDIA.md
WALLET.md
RESEARCH.md
```

The filename signals that the document is an active system declaration rather than an ordinary note. Its sections remain Markdown and are directly editable by the user:

```markdown
# WALLET

## Purpose
- Track masked financial-card metadata

## Allowed
- Read secret-manager references
- Prepare a masked expiration report

## Forbidden
- Reveal full card numbers
- Reveal CVVs
- Make purchases without approval

## Approval
- Any transaction
- Any external transmission

## Secret References
- bitwarden://wallet/cards
```

The Markdown declares policy; Hermes and the sandbox must enforce it. Raw card numbers, CVVs, API keys, recovery codes, and private keys do not belong in SENTER.md or any Markdown module. Store sensitive values in a secret manager and reference them by identifier.

## GEPA for Every Primitive

Senter applies the same lifecycle to Context, Skills, Agents, and Loops:

1. **Collect** evidence from Markdown, sessions, existing artifacts, and outcomes.
2. **Generate** candidate summaries or typed objects.
3. **Evaluate** for redundancy, contradictions, evidence alignment, quality, and safety.
4. **Apply** only an approved winner to the appropriate sandbox/runtime artifact.

The system continuously summarizes new material into existing topics. It should merge equivalent context, preserve user corrections, flag contradictions, and avoid duplicate objects.

## Safety and Sandbox Contract

SENTER.md is never permission to modify the live Hermes installation. All Herm TUI and Hermes-Agent development happens in a disposable, separate sandbox:

```text
live Hermes installation       protected; powers the current conversation
        │
        └── clean sandbox       separate Hermes-Agent checkout + Herm frontend checkout
                │
                ├── local configuration and test HERMES_HOME
                ├── Senter Agent / GOOP objects
                ├── modified Herm frontend with owl Eikon + Wiki sidebar
                ├── tests and verification
                └── Docker image(s) for sharing
```

A sandbox image is a reproducible development/runtime package. It must not contain host credentials or live session databases. Credentials are injected at runtime through documented secrets or environment configuration, never baked into an image.

Different preconfigured GOOP systems can be distributed as separate image tags or mounted Markdown bundles:

```text
senter-agent:base
senter-agent:media
senter-agent:wallet
senter-agent:research
```

The image should contain the Senter runtime and safe defaults; the selected `*.md` modules, skills, and context may be mounted or copied into an isolated workspace.

## Source of Truth

- `SENTER.md`: language/context contract
- `SENTER_AGENT.md`: Senter Agent runtime and roadmap
- `senter_agent/`: local parser, planner, and proposal queue implementation
- `topics/`: evolving topic context and summaries
- Hermes sandbox: experimental frontend/runtime integration
- GitHub: versioned, reviewable source and release history

## Current MVP Boundary

The current implementation parses Markdown and writes a human-editable proposal queue. It does not implicitly create Hermes profiles, skills, cron jobs, webhooks, or containers. Application adapters are a later phase and must remain approval-gated.

## Identity

- **Senter Agent:** the agent/runtime, represented by the three-eyed owl.
- **SENTER.md:** the language/context specification interpreted by Senter Agent.
- **STS auxiliary:** unnamed, tool-free speech interface of Senter Agent.
- **Herm frontend:** future sandboxed UI with the owl Eikon and live Wiki sidebar.

This separation is intentional: the language is portable and inspectable; the agent is the interpreter; Hermes is the execution substrate.

## Related

- [Senter Agent runtime](SENTER_AGENT.md)
- [Agent Wiki specification](spec.md)
- [GOOP whitepaper](goop-whitepaper.md)
- [Hermes Agent](https://github.com/NousResearch/hermes-agent)
- [Hermes TUI documentation](https://hermes-agent.nousresearch.com/docs/user-guide/tui)
