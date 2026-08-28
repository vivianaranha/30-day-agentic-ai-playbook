from agentic_ai.agents.router import route

def test_sales_route():
    assert route("Find my best sales opportunities") == "sales"

def test_support_route():
    assert route("Which support tickets need escalation?") == "support"

def test_knowledge_route():
    assert route("What is the travel reimbursement policy?") == "knowledge"
