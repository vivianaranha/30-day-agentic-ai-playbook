from __future__ import annotations
from agentic_ai.core.types import AgentResponse
from agentic_ai.rag.answer import grounded_answer

class KnowledgeAgent:
    name = "knowledge"

    def run(self, query: str) -> AgentResponse:
        result = grounded_answer(query)
        source_text = ", ".join(result["sources"])
        return AgentResponse(
            answer=f"{result['answer']}\n\nSources: {source_text}" if source_text else result["answer"]
        )
