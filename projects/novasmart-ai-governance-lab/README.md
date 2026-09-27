# NovaSmart AI Governance Lab

This directory contains the runnable security and governance tools for NovaSmart's AI Platform.

## Contents
- `governance_agent.py`: Discovery engine for shadow agents, identity auditing, and safety screening.
- `scripts/update_scorecard.py`: Script to generate and update the governance scorecard.
- `scripts/resolve_env.sh`: Environment setup helper for GCP security roles.
- `references/`: Mission guides (`m0.md` through `m5.md`) detailing governance procedures.

## Quickstart

Run the governance agent to perform discovery, identity audit, and content screening:

```bash
python3 governance_agent.py
```

Update the governance scorecard:

```bash
python3 scripts/update_scorecard.py
```
