# Agentic AI Security Checklist

- Treat user and retrieved content as untrusted.
- Never let an LLM make authorization decisions.
- Give each agent only required tools.
- Separate read and write permissions.
- Validate tool arguments.
- Use bounded retries and step budgets.
- Require approval for high-impact actions.
- Keep secrets outside prompts.
- Log sensitive actions with appropriate redaction.
- Add a kill switch for autonomous workflows.
- Protect memory from poisoning.
- Validate external tool outputs.
