"""Approval-gated Android ADB command planner.

This module deliberately plans commands but never executes them. A future
controlled endpoint can consume the returned argv after user approval.
"""
from __future__ import annotations

from dataclasses import dataclass
import re


class BridgeError(ValueError):
    """Raised when an operation is outside the Android bridge contract."""


@dataclass(frozen=True)
class Request:
    operation: str
    args: tuple[str, ...] = ()
    approved: bool = False


_TEXT = re.compile(r"^[A-Za-z0-9 .,!?@_:/+\-=']{1,2000}$")


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


def _coords(args: tuple[str, ...]) -> tuple[str, ...]:
    if not all(x.isdigit() and int(x) >= 0 for x in args):
        raise BridgeError("coordinates and duration must be non-negative integers")
    return args
