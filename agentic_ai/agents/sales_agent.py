from __future__ import annotations
from agentic_ai.core.types import AgentResponse

class SalesAgent:
    name = "sales"

    def run(self, query: str) -> AgentResponse:
        text = query.lower()
        if "opportunit" in text or "lead" in text:
            return AgentResponse(
                answer=(
                    "Top opportunities:\n"
                    "1. RedStone Energy — Network modernization — High priority\n"
                    "2. Apex Manufacturing — Smart factory expansion — High priority\n"
                    "Recommended next step: validate stakeholder readiness and schedule discovery."
                )
            )
        if "redstone" in text:
            return AgentResponse(
                answer=(
                    "RedStone Energy stakeholders:\n"
                    "- Jordan Lee — VP Infrastructure\n"
                    "- Priya Shah — Director Network Engineering\n"
                    "Suggested motion: network modernization discovery."
                )
            )
        return AgentResponse(answer="Sales Agent can help with accounts, leads, opportunities, stakeholders, and next-best actions.")
