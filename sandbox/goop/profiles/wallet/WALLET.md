# WALLET.md — GOOP profile

## Purpose

Describe safe handling of masked wallet metadata and secret-manager references.

## Allowed

- Read masked metadata
- Prepare reports that never contain full payment credentials

## Forbidden

- Reveal full card numbers
- Reveal CVVs or security codes
- Make purchases without explicit approval
- Put credentials in Markdown, Docker images, logs, or chat

## Approval

- Any transaction
- Any external transmission
- Any modification to stored secrets

## Secret References

- secret-manager://wallet/cards

## Lifecycle

Collect → Generate → Evaluate → Apply.

This profile is a policy declaration only. It does not grant access to secrets or create an agent.
