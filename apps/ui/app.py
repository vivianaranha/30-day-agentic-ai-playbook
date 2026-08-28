import streamlit as st
from agentic_ai.agents.super_agent import SuperAgent

st.set_page_config(page_title="30-Day Agentic AI Playbook", layout="wide")
st.title("30-Day Agentic AI Playbook")
st.caption("Practice routing, tools, RAG, approvals, security, and multi-agent orchestration.")

agent = SuperAgent()

examples = [
    "Find my best sales opportunities.",
    "Who should I reach out to at RedStone Energy?",
    "Which support tickets need escalation?",
    "What is our travel reimbursement policy?",
    "Draft an email to Jordan Lee about network modernization.",
]

query = st.selectbox("Try an example", [""] + examples)
custom = st.text_input("Or ask your own question")
message = custom or query

if st.button("Run Agent", disabled=not bool(message)):
    result = agent.run(message)
    st.subheader("Response")
    st.write(result.answer)

    if result.steps:
        st.subheader("Agent steps")
        for step in result.steps:
            st.write(f"- {step}")

    if result.requires_approval:
        st.warning("Human approval is required before this action can proceed.")
