# Gradient Descent and Optimization

Optimization is the mechanism that teaches a model how to improve.

## 1. Core idea
We define a loss function and minimize it.

```text
loss = f(parameters)
```

Gradient descent updates parameters in the direction that reduces the loss.

```text
parameter = parameter - learning_rate * gradient
```

## 2. Simple example in NumPy
```python
import numpy as np

w = 0.0
lr = 0.1
x = np.array([1.0, 2.0, 3.0])
y = np.array([1.0, 2.0, 3.0])

for _ in range(100):
    pred = w * x
    loss = np.mean((pred - y) ** 2)
    grad = np.mean(2 * x * (pred - y))
    w -= lr * grad

print(w)
```

## 3. Variants of gradient descent
- batch gradient descent
- stochastic gradient descent
- mini-batch gradient descent

## 4. Common optimizers
- SGD
- Momentum
- Adagrad
- RMSProp
- Adam
- AdamW

## 5. Learning rate and schedule
A good learning rate matters a lot. Too high: unstable. Too low: slow learning.

## 6. Why this matters
All model training depends on optimization. Without optimization, neural networks cannot learn.

## 7. Practical exercise
Compare SGD vs Adam on a toy regression task and inspect convergence speed.
