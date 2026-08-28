from __future__ import annotations
from .retriever import LocalRetriever
from agentic_ai.core.llm import generate

def grounded_answer(query: str, retriever: LocalRetriever | None = None):
    retriever = retriever or LocalRetriever()
    results = retriever.search(query)
    if not results:
        return {"answer": "I could not find grounded knowledge for that question.", "sources": []}

    context = "\n\n".join(r["content"] for r in results)
    fallback = results[0]["content"].split("\n")[0:4]
    fallback_text = " ".join(x.strip("# ").strip() for x in fallback if x.strip())
    prompt = f"Answer using only this context.\nContext:\n{context}\n\nQuestion: {query}"
    answer = generate(prompt, fallback=fallback_text)
    return {"answer": answer, "sources": [r["source"] for r in results]}
