from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class ToolCall:
    name: str
    arguments: dict[str, Any] = field(default_factory=dict)

@dataclass
class ToolResult:
    name: str
    success: bool
    data: Any = None
    error: str | None = None

@dataclass
class AgentResponse:
    answer: str
    steps: list[str] = field(default_factory=list)
    tool_results: list[ToolResult] = field(default_factory=list)
    requires_approval: bool = False
