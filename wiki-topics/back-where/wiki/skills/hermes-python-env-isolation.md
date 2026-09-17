---
title: "hermes-python-env-isolation"
description: "Use when debugging scan-topics.py or any Hermes tooling change. The execute_code kernel and command-line run in different Python environments."
---

# Hermes Python environment isolation

## Problem
The `execute_code` tool runs in a separate Python kernel with a different `sys.path` than command-line execution. Changes saved to a file (including `.pyc` bytecode caches) in one environment may not be visible in the other.

## Symptom
A fix applied via `execute_code` shows the changes in the file, but running the script from the command line does not reflect them. Or vice versa — the command-line run works but `execute_code` shows stale output.

## Debug procedure
1. Check the file was actually saved — confirm line numbers match.
2. Check for cached bytecode: `__pycache__/*.pyc` files in the same directory.
3. Recognize the kernel/environment boundary: `execute_code` kernel `sys.path` ≠ shell `sys.path`.
4. Run the script from the actual command line to bypass kernel caching:
   ```bash
   python3 scan-topics.py
   ```
5. If command-line shows different behavior than `execute_code`, the environment mismatch is the cause.

## Prevention
- When testing fixes to `scan-topics.py` or similar tooling, always verify from the command line, not just from `execute_code`.
- Clear `__pycache__` directories when behavior diverges between environments.
- Treat `execute_code` output as kernel-context evidence only — not a substitute for end-to-end Hermes surface testing.

## Evidence
> "Wait - the issue is that my execute_code runs in a DIFFERENT Python environment (kernel) with different sys.path! That kernel's run_scan-topics.py.py might be using cached bytecode." ^[raw/inbox/2026-09-09.md]

> "Good, the changes are in the file (lines 143 and 227). But there might be a cached bytecode file. Let me check:" ^[raw/inbox/2026-09-09.md]

## Related
- [[wiki-topics/back-where/wiki/concepts/end-to-end-verification|End-to-end verification before declaring done]]
- [[wiki-topics/back-where/wiki/entities/recovery-repair-plan|Recovery repair plan]]
