# Optimizers and Training Dynamics

This section explains the optimizers used across machine learning and deep learning.

## 1. SGD
Stochastic gradient descent updates with noisy gradients from mini-batches.

## 2. Momentum
Momentum smooths updates and speeds convergence.

## 3. Adam
Adam combines:
- momentum-like first-order moments
- adaptive learning rates from second-order moments

It is one of the most common optimizers in deep learning.

## 4. AdamW
AdamW separates weight decay from the gradient update. This is often preferred in transformer training.

## 5. Learning rate scheduling
Common strategies:
- step decay
- cosine decay
- warmup + decay
- ReduceLROnPlateau

## 6. Regularization
- L1 regularization
- L2 regularization
- dropout
- weight decay

## 7. Initialization strategies
- Xavier / Glorot
- He initialization

## 8. Training stability issues
- vanishing gradients
- exploding gradients
- unstable learning rates
- poor initialization

## 9. Practical code example in PyTorch
```python
import torch
import torch.optim as optim

model = torch.nn.Linear(10, 1)
optimizer = optim.AdamW(model.parameters(), lr=1e-3, weight_decay=1e-2)
```

## 10. Why this matters in practice
The optimizer and schedule can make the difference between a model that trains and a model that fails.
