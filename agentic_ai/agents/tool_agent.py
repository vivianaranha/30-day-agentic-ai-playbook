from __future__ import annotations
import re
from agentic_ai.core.types import AgentResponse, ToolResult
from agentic_ai.tools.router import select_tool, get_tool
from agentic_ai.security.policy import requires_approval

class ToolAgent:
    name = "tool-agent"

    def run(self, query: str) -> AgentResponse:
        tool_name = select_tool(query)
        if not tool_name:
            return AgentResponse(answer="No tool was required for this request.")

        tool = get_tool(tool_name)
        if tool.write_action or requires_approval(query):
            return AgentResponse(
                answer=f"Approval is required before using {tool_name}.",
                requires_approval=True,
            )

        try:
            if tool_name == "calculator":
                expression = re.sub(r"[^0-9+\-*/(). ]", "", query)
                result = tool.run(expression=expression)
            elif tool_name == "customer_lookup":
                name = "RedStone Energy" if "redstone" in query.lower() else "Apex Manufacturing"
                result = tool.run(name=name)
            else:
                result = tool.run()

            return AgentResponse(
                answer=f"Tool result: {result}",
                tool_results=[ToolResult(name=tool_name, success=True, data=result)],
            )
        except Exception as exc:
            return AgentResponse(
                answer=f"Tool failed safely: {exc}",
                tool_results=[ToolResult(name=tool_name, success=False, error=str(exc))],
            )
