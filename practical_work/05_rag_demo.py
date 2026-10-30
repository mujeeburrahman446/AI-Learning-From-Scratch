# Simple Retrieval-Augmented Generation Demo

This script demonstrates a basic RAG-style workflow using a tiny in-memory document store.

```python
documents = {
    "doc1": "Artificial intelligence studies how machines can reason and learn.",
    "doc2": "Machine learning uses data to train predictive models.",
    "doc3": "Deep learning uses neural networks with many layers.",
    "doc4": "Transformers are the core architecture behind modern LLMs."
}

query = "What architecture powers modern LLMs?"

# simple keyword match
matches = []
for doc_id, content in documents.items():
    score = 0
    for keyword in ["llm", "transformer", "modern", "architecture"]:
        if keyword.lower() in content.lower():
            score += 1
    if score > 0:
        matches.append((doc_id, score, content))

matches = sorted(matches, key=lambda x: x[1], reverse=True)
if matches:
    print("Relevant document:")
    print(matches[0][2])
else:
    print("No relevant document found.")
```

## Tasks
- add embeddings with a basic sentence similarity function
- support user queries with different keywords
- build a small vector database simulation
- combine retrieval with a prompt template
