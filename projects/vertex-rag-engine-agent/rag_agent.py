"""
Vertex AI RAG Engine ADK Agent Implementation
==============================================
Demonstrates integrating serverless Vertex AI RAG Engine retrieval
as a clean function tool inside an ADK agent with A2UI compatibility.
"""

import os
import logging
from typing import Dict, Any, List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("rag_agent")

def search_documents(query: str, corpus_id: str = None) -> List[Dict[str, Any]]:
    """Function tool exposing document retrieval from Vertex AI RAG Corpus."""
    corpus_id = corpus_id or os.getenv("RAG_CORPUS_ID", "default-corpus")
    logger.info(f"Querying Vertex AI RAG Corpus ({corpus_id}) for: {query}")
    
    # Mock retrieval payload matching RAG Engine response format
    results = [
        {
            "doc_id": "doc-001",
            "title": "NovaSmart Security Standard",
            "snippet": f"Grounding response for '{query}': All production agents must use dedicated service accounts.",
            "score": 0.92
        }
    ]
    return results

class VertexRAGAgent:
    def __init__(self):
        self.model_name = "gemini-2.5-flash"
        self.tools = [search_documents]

    def query(self, user_prompt: str) -> Dict[str, Any]:
        logger.info(f"Processing query: {user_prompt}")
        docs = search_documents(user_prompt)
        response_text = f"Based on retrieved documentation:\n- {docs[0]['snippet']}"
        return {
            "response": response_text,
            "retrieved_docs": docs
        }

if __name__ == "__main__":
    agent = VertexRAGAgent()
    res = agent.query("What are the service account requirements for agents?")
    print("\n--- Agent Response ---")
    print(res["response"])
