# Transformer Theory

Transformers are the architecture behind modern LLMs and many multimodal systems.

## 1. Why transformers?
Traditional recurrent models struggled with long-range dependencies. Transformers solve this with attention.

## 2. Self-attention
Each token looks at all other tokens and decides how much attention to pay to them.

### Attention formula
```text
Attention(Q, K, V) = softmax((Q K^T) / sqrt(d_k)) V
```

where:
- Q = queries
- K = keys
- V = values

## 3. Multi-head attention
Instead of one attention mechanism, multiple heads learn different relationships in parallel.

## 4. Positional encoding
Because transformers do not process sequences in order like RNNs, position information must be added explicitly.

## 5. Residual connections
Residual links help gradients flow through deeper models.

## 6. Feed-forward networks
Each transformer block includes a feed-forward network that transforms token representations.

## 7. Training objectives
Language models often learn by predicting the next token.

## 8. Why this matters
Transformers enabled:
- LLMs
- vision transformers
- multimodal models
- agents and reasoning systems

## Summary
The transformer is the core architecture behind modern generative AI and a foundational concept for frontier AI systems.
