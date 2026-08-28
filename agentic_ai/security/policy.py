from __future__ import annotations

HIGH_RISK_TERMS = {
    "delete", "transfer money", "terminate employee", "send email",
    "change password", "approve payment", "issue refund"
}

def requires_approval(text: str) -> bool:
    value = text.lower()
    return any(term in value for term in HIGH_RISK_TERMS)

def detect_prompt_injection(text: str) -> bool:
    patterns = [
        "ignore previous instructions",
        "reveal your system prompt",
        "bypass security",
        "ignore all rules",
        "send secrets",
    ]
    value = text.lower()
    return any(p in value for p in patterns)
