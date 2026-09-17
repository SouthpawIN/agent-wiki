---
name: runtime-python-compat
description: "Use when Python version mismatch breaks a local runtime."
version: 1.0.0
author: turbosovth
license: MIT
tags: [python, macos, compatibility, venv, runtime]
---

# Runtime Python Compatibility (macOS & Local Stacks)

## Use when
- `./scripts/foo` crashes with `TypeError: unsupported operand type(s) for |: 'type' and 'type'` on import
- System `/usr/bin/python3` is 3.9 but project declares `requires-python >=3.10`
- `PyYAML is required` or similar dep error when invoked via system python despite `.venv` existing
- Local inference gateways (Turbofit, llama.cpp, vLLM) fail before the server even starts

## Core distinction: annotations vs. runtime assignments

`from __future__ import annotations` postpones **function annotations** only. These are safe on 3.9:

```python
def f(x: int | str) -> dict[str, int] | None: ...   # stored as string, not evaluated
```

These are **evaluated at import time** and crash on 3.9 (PEP 604 / PEP 585 + pipe):

```python
RuntimeResolutions = dict[str, dict[str, dict[str, int | str]]]   # evaluated
Transport = Callable[[str, str, dict | None, float], tuple[int, dict]]
```

Both use `X | Y` (3.10+). On macOS `/usr/bin/python3` == 3.9.6 they raise.

## Fix recipe

### 1) Make top-level aliases 3.9-compatible

Replace pipe unions and bare `dict[str, ...]` assignments with `typing` imports:

```python
# before (3.10+ only)
RuntimeResolutions = dict[str, dict[str, dict[str, dict[str, int | str]]]]
Transport = Callable[[str, str, dict | None, float], tuple[int, dict]]

# after (3.9+)
from typing import Dict, Union, Optional
RuntimeResolutions = Dict[str, Dict[str, Dict[str, Dict[str, Union[int, str]]]]]
Transport = Callable[[str, str, Optional[dict], float], tuple[int, dict]]
```

Keep pipe unions inside annotated signatures — they remain safe under `from __future__ import annotations`.

### 2) Bootstrap CLI scripts to the project venv

Add at the top of `scripts/*` after `SRC` setup, **before** importing project deps:

```python
# Prefer project venv when system python lacks deps or is too old (macOS ships 3.9).
if sys.version_info < (3, 10):
    _venv = ROOT / ".venv" / "bin" / "python"
    if _venv.is_file() and Path(sys.executable).resolve() != _venv.resolve():
        os.execv(str(_venv), [str(_venv), str(Path(__file__).resolve()), *sys.argv[1:]])
try:
    import yaml  # noqa: F401
    # any other hard dep
    pass
except ImportError:
    _venv = ROOT / ".venv" / "bin" / "python"
    if _venv.is_file() and Path(sys.executable).resolve() != _venv.resolve():
        os.execv(str(_venv), [str(_venv), str(Path(__file__).resolve()), *sys.argv[1:]])
```

That makes documented `./scripts/foo` work via system python while preserving `requires-python >=3.10`.

### 3) Verify

```bash
/usr/bin/python3 --version               # expect 3.9.6 on macOS 14-15
/usr/bin/python3 ./scripts/turbofit-runtime status   # should re-exec into .venv 3.12
.venv/bin/python -m pytest tests/test_runtime_profile.py -q
curl -fsS http://127.0.0.1:8091/v1/models            # gateway healthy
```

## Turbofit reference

On 2026-08-30 this pattern fixed `src/turbofit_runtime/routes.py` and `src/turbofit_runtime/runtime_backends.py` and two scripts, restoring `turbofit-runtime`/`turbofit-controller` on a 32 GB M-series Mac (unified 24.5 GB). Full repro is in `references/macos-python39.md`.

## Pitfalls

- Do not "fix" by changing the shebang to `#!/usr/bin/env python3.12` — that breaks Linux/CI where 3.12 is not installed. The re-exec approach is portable.
- Do not use `dict[str, X]` as a value assignment on 3.9 without `from __future__ import annotations` + `typing.Dict` for runtime aliases.
- Do not capture transient `command not found` / `module not installed` as a permanent rule. Capture the **install / bootstrap** fix instead.
