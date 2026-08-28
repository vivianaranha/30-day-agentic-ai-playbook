from __future__ import annotations
from .metrics import task_success, tool_accuracy

def evaluate_case(case: dict, result: dict):
    return {
        "task_success": task_success(case.get("expected_contains", []), result.get("answer", "")),
        "tool_accuracy": tool_accuracy(case.get("expected_tool"), result.get("tool")),
    }
