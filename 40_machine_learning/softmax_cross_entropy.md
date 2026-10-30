# Softmax, Cross-Entropy, and Classification Basics

This section is central to modern AI training.

## 1. Why softmax matters
Softmax converts raw scores (logits) into probabilities.

```python
import numpy as np

logits = np.array([2.0, 1.0, 0.1])
exp_logits = np.exp(logits - np.max(logits))
probs = exp_logits / np.sum(exp_logits)
print(probs)
```

This is used in classification where a model must decide among several classes.

## 2. Softmax formula

```text
softmax(z_i) = exp(z_i) / sum_j exp(z_j)
```

## 3. Numerical stability
A stable implementation subtracts the maximum logit before exponentiation.

This prevents overflow and keeps training stable.

## 4. Cross-entropy loss
Cross-entropy measures how far the predicted probability is from the true labels.

```text
CE = -sum(y_true * log(y_pred))
```

This is one of the most used loss functions in classification and language modeling.

## 5. Intuition
If the model is confident and correct, loss is low. If uncertain or wrong, loss is high.

## 6. Practical use in AI
Used in:
- image classification
- sentiment analysis
- named entity recognition
- text generation output layers
- large language model token prediction

## 7. Practical exercise
Train a small classifier and inspect the output probabilities from softmax.

## 8. Why this matters in training
The model updates its weights to reduce cross-entropy using gradient descent.
