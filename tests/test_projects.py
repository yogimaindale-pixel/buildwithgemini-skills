import sys
import os
import pytest

sys.path.insert(0, os.path.abspath("projects/agent-frontend-chat-ui"))
sys.path.insert(0, os.path.abspath("projects/memory-bank-agent"))
sys.path.insert(0, os.path.abspath("projects/novasmart-ai-governance-lab"))
sys.path.insert(0, os.path.abspath("projects/vertex-rag-engine-agent"))

from memory_agent import PersistentMemoryAgent, MemoryBankService
from governance_agent import NovaSmartGovernanceEngine
from rag_agent import VertexRAGAgent, search_documents


class TestMemoryAgent:
    def test_memory_bank_service_fetch(self):
        svc = MemoryBankService(memory_bank_id="test-bank")
        memories = svc.fetch_memories(user_id="user-1")
        assert len(memories) >= 2
        assert "Python" in memories[0]

    def test_persistent_memory_agent_process(self):
        agent = PersistentMemoryAgent(user_id="user-42")
        res = agent.process_message("I prefer dark mode UI for web apps.")
        assert "user-42" in agent.user_id or res is not None
        assert len(agent.loaded_memories) >= 3


class TestGovernanceAgent:
    def test_discover_shadow_agents(self):
        engine = NovaSmartGovernanceEngine(project_id="test-project")
        agents = engine.discover_shadow_agents()
        assert len(agents) == 3
        statuses = [a["status"] for a in agents]
        assert "SHADOW_RISK" in statuses

    def test_audit_identities(self):
        engine = NovaSmartGovernanceEngine(project_id="test-project")
        audit = engine.audit_identities()
        assert len(audit) >= 2
        assert audit[0]["recommendation"] == "REVOKE_OWNER"

    def test_screen_content_safe(self):
        engine = NovaSmartGovernanceEngine(project_id="test-project")
        res = engine.screen_content("Check employee handbook")
        assert res["pass_safety"] is True
        assert res["action"] == "ALLOW"

    def test_screen_content_unsafe(self):
        engine = NovaSmartGovernanceEngine(project_id="test-project")
        res = engine.screen_content("DROP TABLE users; -- pii_leak")
        assert res["pass_safety"] is False
        assert res["action"] == "BLOCK"


class TestRAGAgent:
    def test_search_documents(self):
        results = search_documents("security policy")
        assert len(results) == 1
        assert results[0]["doc_id"] == "doc-001"

    def test_vertex_rag_agent_query(self):
        agent = VertexRAGAgent()
        res = agent.query("What are the service account requirements?")
        assert "retrieved_docs" in res
        assert "Based on retrieved documentation" in res["response"]
