from __future__ import annotations
from .base import Tool

CUSTOMERS = {
    "redstone energy": {
        "industry": "Energy",
        "priority": "High",
        "opportunity": "Network modernization",
        "contacts": ["Jordan Lee - VP Infrastructure", "Priya Shah - Director Network Engineering"],
    },
    "apex manufacturing": {
        "industry": "Manufacturing",
        "priority": "High",
        "opportunity": "Smart factory expansion",
        "contacts": ["Marcus Reed - CIO", "Elena Park - VP Operations"],
    },
}

def calculator(expression: str):
    allowed = set("0123456789+-*/(). ")
    if not set(expression) <= allowed:
        raise ValueError("Unsafe expression")
    return eval(expression, {"__builtins__": {}}, {})

def customer_lookup(name: str):
    return CUSTOMERS.get(name.lower(), {"error": "Customer not found"})

def current_inventory():
    return [
        {"sku": "EDGE-100", "stock": 14, "reorder_point": 20},
        {"sku": "RTR-420", "stock": 75, "reorder_point": 30},
        {"sku": "SENSOR-X", "stock": 8, "reorder_point": 15},
    ]

def draft_email(recipient: str, topic: str):
    return f"Draft email to {recipient}: I'd like to connect regarding {topic}."

TOOLS = {
    "calculator": Tool("calculator", "Evaluate basic arithmetic.", calculator),
    "customer_lookup": Tool("customer_lookup", "Retrieve customer context.", customer_lookup),
    "inventory": Tool("inventory", "Retrieve current inventory.", current_inventory),
    "draft_email": Tool("draft_email", "Draft an outbound email.", draft_email, write_action=True),
}
