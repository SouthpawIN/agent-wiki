"""Approval-gated Android ADB command planner and executor.

The default path only plans commands. Execution requires explicit approval and
an injected runner, so this module never silently reaches the host or device.
"""
from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Callable, Sequence


class BridgeError(ValueError):
    """Raised when an operation is outside the Android bridge contract."""


@dataclass(frozen=True)
class Request:
    operation: str
    args: tuple[str, ...] = ()
    approved: bool = False


@dataclass(frozen=True)
class Result:
    argv: tuple[str, ...]
    output: bytes = b""


_TEXT = re.compile(r"^[A-Za-z0-9 .,!?@_:/+\-=']{1,2000}$")
Runner = Callable[[Sequence[str]], bytes]


def plan(req: Request, serial: str = "android:5555") -> tuple[str, ...]:
    """Return one approved, bounded ADB argv; never invokes a process."""
    if not req.approved:
        raise BridgeError("user approval required")
    if not serial or any(x in serial for x in (" ", ";", "|", "&")):
        raise BridgeError("invalid device endpoint")
    if req.operation == "screenshot":
        if req.args:
            raise BridgeError("screenshot takes no arguments")
        return ("adb", "-s", serial, "exec-out", "screencap", "-p")
    if req.operation == "tap":
        if len(req.args) != 2:
            raise BridgeError("tap requires x and y")
        return ("adb", "-s", serial, "shell", "input", "tap", *_coords(req.args))
    if req.operation == "swipe":
        if len(req.args) != 5:
            raise BridgeError("swipe requires x1 y1 x2 y2 duration_ms")
        return ("adb", "-s", serial, "shell", "input", "swipe", *_coords(req.args))
    if req.operation == "text":
        if len(req.args) != 1 or not _TEXT.fullmatch(req.args[0]):
            raise BridgeError("text must be 1-2000 safe characters")
        return ("adb", "-s", serial, "shell", "input", "text", req.args[0])
    raise BridgeError(f"operation is forbidden: {req.operation}")


def execute(req: Request, runner: Runner, serial: str = "android:5555") -> Result:
    """Execute exactly one planned command through an injected runner.

    The caller owns the approval decision. A production runner must use
    subprocess with `shell=False`, a timeout, and an output-size limit.
    """
    argv = plan(req, serial)
    output = runner(argv)
    if not isinstance(output, bytes):
        raise BridgeError("runner must return bytes")
    if len(output) > 10_000_000:
        raise BridgeError("bridge output exceeds 10 MB limit")
    return Result(argv, output)


def _coords(args: tuple[str, ...]) -> tuple[str, ...]:
    if not all(x.isdigit() and int(x) >= 0 for x in args):
        raise BridgeError("coordinates and duration must be non-negative integers")
    return args
