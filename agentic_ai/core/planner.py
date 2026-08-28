from __future__ import annotations

def plan_task(goal: str) -> list[str]:
    text = goal.lower()
    steps = ["Understand the request"]

    if any(word in text for word in ["research", "find", "compare", "investigate"]):
        steps.append("Collect relevant information")

    if any(word in text for word in ["customer", "account", "sales", "lead"]):
        steps.append("Retrieve business context")

    if any(word in text for word in ["policy", "document", "knowledge"]):
        steps.append("Retrieve grounded knowledge")

    if any(word in text for word in ["email", "update", "create", "delete", "send"]):
        steps.append("Validate action and approval requirements")

    steps.append("Synthesize the result")
    return steps
