from __future__ import annotations
from fastapi import FastAPI
from pydantic import BaseModel
from agentic_ai.agents.super_agent import SuperAgent

app = FastAPI(
    title="30-Day Agentic AI Playbook API",
    version="1.0.0",
    description="A learning API for agentic AI patterns.",
)

agent = SuperAgent()

class ChatRequest(BaseModel):
    message: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat")
def chat(req: ChatRequest):
    result = agent.run(req.message)
    return {
        "answer": result.answer,
        "steps": result.steps,
        "requires_approval": result.requires_approval,
        "tool_results": [r.__dict__ for r in result.tool_results],
    }
