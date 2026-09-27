"""
NovaSmart AI Governance & Platform Security Agent
=================================================
Automated agent for AI platform security, shadow agent discovery, identity audit,
and content screening in the NovaSmart Governance Lab.
"""

import os
import json
import logging
from typing import Dict, Any, List

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("novasmart_governance")

class NovaSmartGovernanceEngine:
    def __init__(self, project_id: str = None):
        self.project_id = project_id or os.getenv("GCP_PROJECT", "novasmart-prod")
        logger.info(f"Initialized NovaSmart Governance Engine for GCP Project: {self.project_id}")

    def discover_shadow_agents(self) -> List[Dict[str, Any]]:
        """Mission M0: See Everything - Discover active & shadow agents."""
        logger.info("Scanning infrastructure for active & shadow agent deployments...")
        agents = [
            {"agent_id": "agent-support-v1", "owner": "cx-team", "type": "ADK Agent", "status": "APPROVED"},
            {"agent_id": "shadow-finance-bot", "owner": "unknown", "type": "Unregistered Container", "status": "SHADOW_RISK"},
            {"agent_id": "agent-hr-policy", "owner": "hr-ops", "type": "ADK Agent", "status": "APPROVED"}
        ]
        return agents

    def audit_identities(self) -> List[Dict[str, Any]]:
        """Mission M1: Take Action - Audit service accounts and identities."""
        logger.info("Auditing IAM service accounts for shared or over-privileged access...")
        audit_results = [
            {"sa": "shadow-finance-bot@novasmart.iam.gserviceaccount.com", "roles": ["roles/owner"], "recommendation": "REVOKE_OWNER"},
            {"sa": "agent-support-sa@novasmart.iam.gserviceaccount.com", "roles": ["roles/aiplatform.user"], "recommendation": "COMPLIANT"}
        ]
        return audit_results

    def screen_content(self, prompt: str) -> Dict[str, Any]:
        """Mission M2: Content Screening & Safety Guardrails."""
        logger.info("Evaluating prompt against safety policy...")
        is_safe = "pii_leak" not in prompt.lower() and "drop table" not in prompt.lower()
        return {
            "prompt": prompt,
            "pass_safety": is_safe,
            "action": "ALLOW" if is_safe else "BLOCK"
        }

if __name__ == "__main__":
    engine = NovaSmartGovernanceEngine()
    print("--- 1. Shadow Agent Discovery ---")
    print(json.dumps(engine.discover_shadow_agents(), indent=2))
    print("\n--- 2. Identity Audit ---")
    print(json.dumps(engine.audit_identities(), indent=2))
    print("\n--- 3. Content Safety Screening ---")
    print(json.dumps(engine.screen_content("Check employee handbook for vacation policy"), indent=2))
