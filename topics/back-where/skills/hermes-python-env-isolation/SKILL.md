---
name: hermes-python-env-isolation
description: Use when debugging scan-topics.py or any Hermes tooling change. The execute_code kernel and command-line run in different Python environments.
version: 0.1.0
distilled: 2026-09-10 12:20
topic: back-where
---
# hermes-python-env-isolation
execute_code runs in a separate Python kernel with different sys.path than command-line. When fixes don't propagate, verify from the command line directly: python3 scan-topics.py. Clear __pycache__ when behavior diverges. Treat execute_code output as kernel-context evidence only.

## Evidence
> Wait - the issue is that my execute_code runs in a DIFFERENT Python environment (kernel) with different sys.path! That kernel's run_scan-topics.py.py might be using cached bytecode.
> Good, the changes are in the file (lines 143 and 227). But there might be a cached bytecode file. Let me check:
