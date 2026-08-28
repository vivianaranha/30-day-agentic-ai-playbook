from __future__ import annotations
from agentic_ai.core.types import AgentResponse

class ResearchAgent:
    name = "research"

    def run(self, query: str) -> AgentResponse:
        return AgentResponse(
            answer=(
                "Research plan created. In a production implementation this agent would "
                "query approved search or enterprise data tools, collect sources, remove "
                "duplicates, assess reliability, and synthesize findings."
            )
        )
