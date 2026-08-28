from __future__ import annotations
from .builtin import TOOLS

def select_tool(query: str) -> str | None:
    text = query.lower()
    if any(x in text for x in ["calculate", "+", "-", "*", "/"]):
        return "calculator"
    if any(x in text for x in ["customer", "account", "redstone", "apex"]):
        return "customer_lookup"
    if any(x in text for x in ["inventory", "stock", "sku"]):
        return "inventory"
    if "email" in text:
        return "draft_email"
    return None

def get_tool(name: str):
    return TOOLS.get(name)
