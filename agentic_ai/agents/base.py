from __future__ import annotations
from agentic_ai.core.planner import plan_task
from agentic_ai.core.trace import Trace
from agentic_ai.core.types import AgentResponse, ToolResult

class BaseAgent:
    name = "base"

    def run(self, query: str) -> AgentResponse:
        trace = Trace()
        plan = plan_task(query)
        for step in plan:
            trace.add("plan", step)
        return AgentResponse(answer=f"{self.name} processed: {query}", steps=plan)
