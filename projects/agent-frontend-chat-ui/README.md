# Agent Frontend Chat UI with A2UI

A production-ready FastAPI proxy and glassmorphism web interface for Google ADK agents supporting A2UI (Agent-to-User Interface) display cards.

## Setup & Running

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment**:
   ```bash
   export AGENT_ENDPOINT="https://your-agent-engine-endpoint"
   ```

3. **Launch Web App**:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

4. **Access Web Chat**:
   Open `http://localhost:8000` in your browser.
