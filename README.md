# 🤖 REACT AI Agent

A reasoning-based AI agent built using:

- FastAPI
- Ollama
- Python
- REACT (Reason + Act) Architecture

This project demonstrates how modern AI agents perform:

- reasoning
- tool selection
- parameter extraction
- observation handling
- final response synthesis

using a structured autonomous workflow.

---

# 🚀 Project Overview

Unlike traditional chatbots, this AI agent follows a reasoning loop:

```text
Thought → Action → Observation → Final Answer

The agent can:

Think step-by-step
Decide which tool to use
Extract required parameters
Execute tools dynamically
Observe tool outputs
Generate intelligent final responses
🧠 REACT Architecture

This project implements a simplified version of the REACT (Reason + Act) agent architecture used in modern AI systems.

🏗️ Agent Workflow
User Input
    ↓
LLM Reasoning
    ↓
Tool Selection
    ↓
Parameter Extraction
    ↓
Tool Execution
    ↓
Observation
    ↓
Final Reasoning
    ↓
Response
🔥 Features

✅ REACT reasoning loop
✅ Dynamic tool selection
✅ Parameter extraction
✅ Weather tool
✅ Calculator tool
✅ Time tool
✅ Ollama integration
✅ FastAPI backend
✅ Modular architecture
✅ Structured prompting

🧰 Tech Stack
Component	Technology
Backend API	FastAPI
LLM Runtime	Ollama
AI Model	Llama3
Environment Config	python-dotenv
Language	Python
📁 Project Structure
react-agent/
│
├── app.py
├── agent.py
├── tools.py
├── prompts.py
├── requirements.txt
├── .env
└── README.md
