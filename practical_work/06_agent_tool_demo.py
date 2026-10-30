# Agent Tool Demo

This script simulates a basic agent that uses tools to answer questions.

```python
def calculator(a, b, op):
    if op == "add":
        return a + b
    elif op == "subtract":
        return a - b
    elif op == "multiply":
        return a * b
    elif op == "divide":
        return a / b
    else:
        return "Unsupported operation"


def search_knowledge(topic):
    knowledge = {
        "python": "Python is widely used for AI, automation, and backend services.",
        "machine learning": "Machine learning learns patterns from data to make predictions.",
        "cuda": "CUDA allows GPU-parallel processing for high-performance AI workloads."
    }
    return knowledge.get(topic.lower(), "No direct information found.")


def agent_main(query):
    q = query.lower()
    if "calculate" in q or "add" in q or "subtract" in q or "multiply" in q:
        return calculator(10, 5, "add")
    if "python" in q or "machine learning" in q or "cuda" in q:
        return search_knowledge(q)
    return "I can answer questions about AI, ML, Python, and CUDA."


print(agent_main("Tell me about machine learning"))
print(agent_main("Calculate 10 + 5"))
print(agent_main("What is CUDA?"))
```

## Tasks
- add a tool registry
- implement more tool actions
- build a loop that decides which tool to use
- add memory and multi-step reasoning
