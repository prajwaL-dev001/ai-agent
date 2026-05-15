from langgraph.graph import StateGraph, END
from langchain_ollama import ChatOllama

# Ollama LLM (local model)
llm = ChatOllama(model="llama3")

# Node function
def call_llm(state):
    response = llm.invoke(state["input"])
    return {"output": response.content}

# Create graph
graph = StateGraph(dict)

# Add node
graph.add_node("agent", call_llm)

# Set entry point
graph.set_entry_point("agent")

# Connect flow
graph.add_edge("agent", END)

# Compile app
app = graph.compile()

# Run directly
if __name__ == "__main__":
    result = app.invoke({"input": "Hello, who are you?"})
    print(result)