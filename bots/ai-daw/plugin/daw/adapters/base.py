"""Engine adapters: one file per music model, one interface for all of them."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol


@dataclass(frozen=True)
class Capabilities:
    duration_s: float
    vocals: bool
    stems: bool
    bpm_key_conditioning: bool
    local: bool
    license: str


class MusicEngine(Protocol):
    name: str
    model: str
    install_hint: str

    def capabilities(self) -> Capabilities: ...
    def health(self) -> bool: ...
    def generate(self, request: dict[str, Any]) -> dict[str, Any]: ...


def get_engine(name: str, registry: dict[str, Any] | None = None) -> MusicEngine:
    """Resolve an adapter by name. Unknown engines fail with a hint, not a stack."""
    if registry and name in registry:
        return registry[name]
    if name in ("dryrun", "dry"):
        from .dryrun import DryRunEngine
        return DryRunEngine()
    if name in ("acestep", "ace-step", "acestep-1.5"):
        from .acestep import AceStepEngine
        return AceStepEngine()
    known = ", ".join(sorted({"dryrun", "acestep"} | set(registry or {})))
    raise KeyError(f"unknown engine '{name}'; known: {known}")
