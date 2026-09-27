# Project Brief: Vertex AI RAG Engine Agent

## Overview
This project demonstrates how to ground an ADK (Agent Development Kit) agent on custom documents using Vertex AI RAG Engine in serverless mode.

## Architecture & Integration
- **Serverless RAG Corpus**: Uses Vertex AI RAG Engine for document indexing and vector search.
- **Function Tool Pattern**: Exposes document retrieval as a standard Python function tool (`search_documents`), allowing co-existence with A2UI card formatting and other agent tools.
- **Validation**: Includes compatibility test scripts (`test_rag_a2ui_compat.py`) ensuring non-conflicting tool call execution.
