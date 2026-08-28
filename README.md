# 30-Day Agentic AI Playbook

A hands-on, progressive repository for learning how to design and build **agentic AI systems in 30 days**.

This playbook moves from a single tool-using agent to a production-style multi-agent platform with:

- Planning and reasoning
- Structured outputs
- Tool calling
- REST APIs
- Memory
- Retrieval-Augmented Generation (RAG)
- Human-in-the-loop approvals
- Multi-agent orchestration
- Agent routing
- Security controls
- Evaluation
- Observability
- Reliability
- Cost controls
- FastAPI
- Streamlit
- Optional local models with Ollama

The goal is not to memorize frameworks. The goal is to understand the architecture patterns behind reliable agentic systems.

---

## 30-Day Learning Path

### Week 1 — Agent Foundations
1. What Is an AI Agent?
2. The Agent Loop
3. Structured Agent Responses
4. Planning and Task Decomposition
5. Tool Calling
6. Tool Routing
7. Build Your First Useful Agent

### Week 2 — Memory, Knowledge, and External Systems
8. Short-Term Memory
9. Long-Term Memory
10. Embeddings and Semantic Search
11. Retrieval-Augmented Generation
12. Grounded Answers and Citations
13. REST API Tools
14. Build a Knowledge + Tool Agent

### Week 3 — Autonomous and Multi-Agent Systems
15. Agent Autonomy
16. Reflection and Self-Correction
17. Human-in-the-Loop
18. Agent Routing
19. Supervisor + Specialist Agents
20. Multi-Agent Collaboration
21. Build an Enterprise Super Agent

### Week 4 — Production Agentic AI
22. Agent Security
23. Prompt Injection Defense
24. Agent Evaluation
25. Observability and Tracing
26. Reliability and Failure Recovery
27. Cost and Performance
28. FastAPI Agent Service
29. Streamlit Agent Interface
30. Capstone: Production-Style Agent Platform

---

## Repository Structure

```text
30-day-agentic-ai-playbook/
├── days/
│   ├── day-01-what-is-an-agent/
│   ├── day-02-agent-loop/
│   └── ...
│   └── day-30-capstone/
├── agentic_ai/
│   ├── agents/
│   ├── core/
│   ├── memory/
│   ├── rag/
│   ├── security/
│   ├── tools/
│   └── evaluation/
├── apps/
│   ├── api/
│   └── ui/
├── data/
├── knowledge/
├── examples/
├── tests/
└── docs/
```

---

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python examples/01_simple_agent.py
```

Run the API:

```bash
uvicorn apps.api.main:app --reload
```

Run the UI:

```bash
streamlit run apps/ui/app.py
```

Optional local LLM support:

```bash
ollama serve
ollama pull llama3.2
```

Set:

```bash
export USE_OLLAMA=true
export OLLAMA_MODEL=llama3.2
```

If Ollama is unavailable, the repository still works using deterministic demo logic for the learning labs.

---

## Final Capstone

By Day 30 you will have built:

```text
User
  |
  v
Enterprise Super Agent
  |
  +--> Research Agent
  +--> Sales Agent
  +--> Support Agent
  +--> Knowledge Agent
  |
  v
Enterprise Tool Layer
  |
  +--> REST API
  +--> Local Knowledge
  +--> SQLite Memory
  +--> Approval Layer
  |
  v
Evaluation + Observability + Security
```

---

## Design Principles

- Start simple.
- Use deterministic logic where deterministic logic is better.
- Give agents only the tools they need.
- Treat external content as untrusted.
- Require approval for risky actions.
- Evaluate outcomes, not just fluent text.
- Preserve traceability.
- Put critical business rules outside prompts.
- Add autonomy gradually.
- Always design a stopping condition.

## License

MIT
