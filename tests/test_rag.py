from agentic_ai.rag.retriever import LocalRetriever

def test_travel_policy_retrieval():
    r = LocalRetriever("knowledge")
    results = r.search("travel reimbursement receipts")
    assert results
    assert "travel-policy.md" in results[0]["source"]
