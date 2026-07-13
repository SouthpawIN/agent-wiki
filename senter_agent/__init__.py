"""Senter Agent: a markdown-native GOOP planner."""

__version__ = "0.1.0"

from .model import GoopDocument, Proposal
from .parser import parse_markdown
from .planner import build_plan

__all__ = ["GoopDocument", "Proposal", "parse_markdown", "build_plan"]
