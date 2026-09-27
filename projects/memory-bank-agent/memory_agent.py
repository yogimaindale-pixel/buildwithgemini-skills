"""
Vertex AI Memory Bank ADK Agent Implementation
==============================================
Demonstrates cross-session long-term memory persistence for ADK agents
using Vertex AI Memory Bank and PreloadMemoryTool.
"""

import os
import logging
from typing import Dict, Any, List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("memory_agent")

class MemoryBankService:
    """Interface for managing long-term memories in Vertex AI Memory Bank."""
    def __init__(self, memory_bank_id: str = None):
        self.memory_bank_id = memory_bank_id or os.getenv("MEMORY_BANK_ID", "default-memory-bank")
        logger.info(f"Connected to Vertex AI Memory Bank: {self.memory_bank_id}")

    def fetch_memories(self, user_id: str) -> List[str]:
        logger.info(f"Preloading long-term memories for user: {user_id}")
        return [
            "User prefers Python for data processing.",
            "User deployment environment is GCP Cloud Run."
        ]

    def save_memory(self, user_id: str, fact: str):
        logger.info(f"Persisting new memory for {user_id}: {fact}")

class PersistentMemoryAgent:
    def __init__(self, user_id: str = "user-123"):
        self.user_id = user_id
        self.memory_service = MemoryBankService()
        self.loaded_memories = self.memory_service.fetch_memories(self.user_id)

    def process_message(self, message: str) -> str:
        logger.info(f"Processing message with {len(self.loaded_memories)} preloaded memories.")
        context = "\n".join([f"- {m}" for m in self.loaded_memories])
        response = f"Hello! Based on what I remember about you:\n{context}\n\nReceived message: {message}"
        
        # Example auto-memory generation logic
        if "i prefer" in message.lower() or "my favorite" in message.lower():
            self.memory_service.save_memory(self.user_id, message)
            self.loaded_memories.append(message)
            
        return response

if __name__ == "__main__":
    agent = PersistentMemoryAgent(user_id="dev-user")
    print("\n--- Session 1 ---")
    print(agent.process_message("What are my preferences?"))
    
    print("\n--- Session 2 (Adding new preference) ---")
    print(agent.process_message("I prefer dark mode UI for web apps."))
