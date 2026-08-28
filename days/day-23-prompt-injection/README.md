# Day 23: Prompt Injection Defense

## Objective

Treat retrieved and user-provided content as untrusted.

## Core concepts

- Prompt injection
- Indirect injection
- Isolation

## Why it matters

Agentic AI becomes useful when autonomy is introduced deliberately. Each capability in this playbook is added only after the previous layer is understandable and testable.

## Hands-on

Run the included injection detector against adversarial prompts.

## Suggested exercise

1. Read the concept notes.
2. Run the referenced repository example.
3. Modify one behavior.
4. Test one normal case.
5. Test one failure case.
6. Write down one production risk.

## Reflection questions

- What should remain deterministic?
- What could fail?
- What data or permission does the agent need?
- How would you measure success?
- What would you change before production?
