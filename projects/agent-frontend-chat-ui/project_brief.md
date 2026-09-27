# Project Brief: Agent Frontend Web Chat UI with A2UI Renderer

## Overview
This project provides a complete, modern web chat UI and FastAPI proxy for interacting with deployed ADK / Agent Engine agents using the **A2A protocol**.

## Key Features
1. **A2A Proxy**: Secure FastAPI backend (`main.py`) forwarding chat streams to deployed Agent Engine instances.
2. **A2UI Renderer**: Native web renderer (`static/index.html`) displaying text responses, rich UI cards, data tables, and images.
3. **A2UI Formatter Callback**: Python utility (`a2ui_utils.py`) for ADK agents to emit structured display payloads.
