# AI Training Fundamentals

This section covers the core concepts behind training machine learning and deep learning models.

## 1. Data and labels
Every model learns from data. Training data must be:
- relevant
- clean
- correctly labeled
- representative of the target task

## 2. Training objective
The model learns by trying to reduce a loss function.

Examples:
- MSE for regression
- cross-entropy for classification
- next-token prediction for language models

## 3. Softmax and classification
Softmax converts logits into probabilities.

```python
import numpy as np

logits = np.array([2.0, 1.0, 0.1])
probs = np.exp(logits - np.max(logits))
probs = probs / probs.sum()
print(probs)
```

Softmax is used in classification and final output layers of language models.

## 4. Cross-entropy loss
Cross-entropy measures how different the predicted distribution is from the true distribution.

```text
H(y, p) = -sum(y * log(p))
```

This is a central loss used in classification and language modeling.

## 5. Gradient descent
The training process updates model parameters using gradients.

```text
w = w - learning_rate * gradient
```

## 6. Batch, epoch, and iteration
- one batch: a small subset of data
- one epoch: full pass over dataset
- one iteration: one batch update

## 7. Backpropagation
Backpropagation computes gradients layer by layer using the chain rule.

This is the engine behind neural network learning.

## 8. Initialization and stability
Important issues:
- weight initialization
- vanishing gradients
- exploding gradients
- learning rate sensitivity
- regularization

## 9. Regularization
- L2 regularization
- dropout
- weight decay
- early stopping

## 10. Train/validation/test split
To evaluate properly:
- train on training data
- tune on validation data
- test on unseen data

## 11. Practical exercise
Train a small logistic regression model on toy data and inspect the loss over iterations.

## 12. Why this matters
Without understanding training fundamentals, it is impossible to reason about model quality, failure cases, or efficient training.
