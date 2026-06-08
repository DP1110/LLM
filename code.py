# Install required libraries silently
!pip install -q langgraph langchain-core

import time
from typing import TypedDict, List
from langgraph.graph import StateGraph, END

# Define the shared state for our agentic workflow
class AgentState(TypedDict):
    query: str
    history: List[str]
    next_agent: str
    research_data: str
    code_data: str
    final_response: str

# --- Node 1: Supervisor (Orchestrator) ---
# Simulates a GPT-4o-mini router analyzing task complexity and routing dynamically
def supervisor_node(state: AgentState):
    print("\n[Supervisor] Analyzing query and routing task...")
    time.sleep(1)
    query = state["query"].lower()
    history = state.get("history", [])
    
    # Dynamic routing logic based on state and query content
    if "research" in query and not state.get("research_data"):
        history.append("Supervisor routed to Research Agent.")
        return {"history": history, "next_agent": "researcher"}
    elif "code" in query and not state.get("code_data"):
        history.append("Supervisor routed to Coding Agent.")
        return {"history": history, "next_agent": "coder"}
    else:
        history.append("Supervisor routed to Aggregator.")
        return {"history": history, "next_agent": "aggregator"}

# --- Node 2: Research Agent (Specialized Sub-Agent) ---
# Simulates a fast, web-retrieval model (e.g., Haiku/GPT-3.5) with tool calling
def research_agent_node(state: AgentState):
    print("[Research Agent] Executing web search tool...")
    time.sleep(1)
    simulated_retrieval = (
        "Found: LangGraph is a library for building stateful, multi-actor applications with LLMs, "
        "ideal for agentic workflows with cycles and state management."
    )
    history = state["history"]
    history.append("Research Agent successfully retrieved documentation.")
    return {
        "research_data": simulated_retrieval,
        "history": history,
        "next_agent": "supervisor" # Route back to supervisor for self-correction/next steps
    }

# --- Node 3: Coding Agent (Specialized Sub-Agent) ---
# Simulates a high-reasoning coding model (e.g., Claude Sonnet) generating snippets
def coding_agent_node(state: AgentState):
    print("[Coding Agent] Generating optimized Python code snippet...")
    time.sleep(1)
    simulated_code = (
        "```python\n"
        "from langgraph.graph import StateGraph\n"
        "workflow =