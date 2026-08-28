from agentic_ai.tools.builtin import calculator, customer_lookup

def test_calculator():
    assert calculator("12 * 7") == 84

def test_customer_lookup():
    result = customer_lookup("RedStone Energy")
    assert result["priority"] == "High"
