from __future__ import annotations

def route(query: str) -> str:
    text = query.lower()
    if any(x in text for x in ["sales", "lead", "opportunit", "account", "redstone", "apex"]):
        return "sales"
    if any(x in text for x in ["ticket", "support", "incident", "escalat"]):
        return "support"
    if any(x in text for x in ["policy", "document", "knowledge", "reimbursement"]):
        return "knowledge"
    if any(x in text for x in ["research", "compare", "investigate"]):
        return "research"
    return "tool"
