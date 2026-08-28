from __future__ import annotations
from agentic_ai.agents.router import route
from agentic_ai.agents.sales_agent import SalesAgent
from agentic_ai.agents.support_agent import SupportAgent
from agentic_ai.agents.knowledge_agent import KnowledgeAgent
from agentic_ai.agents.research_agent import ResearchAgent
from agentic_ai.agents.tool_agent import ToolAgent
from agentic_ai.security.policy import detect_prompt_injection
from agentic_ai.core.types import AgentResponse

AGENTS = {
    "sales": SalesAgent(),
    "support": SupportAgent(),
    "knowledge": KnowledgeAgent(),
    "research": ResearchAgent(),
    "tool": ToolAgent(),
}

class SuperAgent:
    name = "super-agent"

    def run(self, query: str) -> AgentResponse:
        if detect_prompt_injection(query):
            return AgentResponse(answer="Request blocked by prompt-injection policy.")

        specialist = route(query)
        result = AGENTS[specialist].run(query)
        result.steps.insert(0, f"Routed to {specialist} agent")
        return result
