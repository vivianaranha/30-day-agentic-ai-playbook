# Agent Evaluation Strategy

Evaluate the full system, not just the model.

## Core metrics

- Task success rate
- Routing accuracy
- Tool-selection accuracy
- Tool-argument accuracy
- Groundedness
- Citation correctness
- Policy compliance
- Approval compliance
- Recovery success
- Latency
- Cost
- User satisfaction

## Golden cases

Maintain a small set of critical scenarios that must pass before every release.

Examples:

- Correctly route a sales request.
- Refuse or gate an unsafe write action.
- Retrieve the correct policy.
- Preserve a cited source.
- Recover safely from a tool failure.
