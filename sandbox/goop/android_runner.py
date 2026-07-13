"""Constrained subprocess runner for planner-produced Android commands.

This is intentionally separate from Hermes. The bridge remains disabled until
an approval-aware endpoint explicitly calls this runner with planner output.
"""
from __future__ import annotations

import subprocess
from collections.abc import Sequence


MAX_OUTPUT = 10_000_000
TIMEOUT = 15


class RunnerError(RuntimeError):
    """Raised when the constrained runner rejects or cannot complete a call."""


def run(argv: Sequence[str]) -> bytes:
    """Run a planner-produced ADB argv without shell interpretation."""
    args = tuple(argv)
    if not args or args[0] != "adb":
        raise RunnerError("runner accepts planner-produced adb argv only")
    if any(token in args for token in ("shell", "exec", "install", "push", "pull", "root", "remount")):
        # `shell` and `exec-out` are legitimate planner operations, so reject
        # only raw shell/exec forms; planner output is checked structurally.
        valid = len(args) >= 5 and (
            (args[3:5] == ("exec-out", "screencap"))
            or (args[3:5] == ("shell", "input"))
        )
        if not valid:
            raise RunnerError("argv is outside the Android bridge allowlist")
    try:
        result = subprocess.run(
            args,
            shell=False,
            check=False,
            capture_output=True,
            timeout=TIMEOUT,
        )
    except subprocess.TimeoutExpired as exc:
        raise RunnerError("Android bridge timed out") from exc
    if result.returncode != 0:
        detail = result.stderr[:1000].decode("utf-8", errors="replace")
        raise RunnerError(f"Android bridge failed: {detail}")
    if len(result.stdout) > MAX_OUTPUT:
        raise RunnerError("bridge output exceeds 10 MB limit")
    return result.stdout
