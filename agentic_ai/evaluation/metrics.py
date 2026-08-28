from __future__ import annotations

def task_success(expected_contains: list[str], answer: str) -> float:
    if not expected_contains:
        return 1.0
    value = answer.lower()
    matched = sum(1 for item in expected_contains if item.lower() in value)
    return matched / len(expected_contains)

def tool_accuracy(expected_tool: str | None, actual_tool: str | None) -> float:
    return 1.0 if expected_tool == actual_tool else 0.0
