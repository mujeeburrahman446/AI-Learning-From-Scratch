# Deep Learning with PyTorch

This module introduces the building blocks of modern deep learning.

## 1. Neural network basics
A neural network is a function approximator.

It learns weights that map input features to target outputs through:
- forward pass
- loss calculation
- backward pass
- gradient descent

## 2. Perceptron
```python
import numpy as np

x = np.array([1.0, 2.0])
w = np.array([0.5, -0.3])
b = 0.1

output = np.dot(x, w) + b
print(output)
```

## 3. Activation functions
- ReLU
- Sigmoid
- Tanh
- Softmax

## 4. PyTorch basics
```python
import torch

x = torch.tensor([1.0, 2.0, 3.0])
print(x)
```

### Linear layer
```python
layer = torch.nn.Linear(3, 4)
output = layer(x)
print(output)
```

### Simple training loop
```python
model = torch.nn.Sequential(
    torch.nn.Linear(10, 20),
    torch.nn.ReLU(),
    torch.nn.Linear(20, 1)
)
```

## 5. Loss functions
- MSELoss
- CrossEntropyLoss
- BCELoss

## 6. Optimizers
- SGD
- Adam
- RMSProp

## 7. Common deep learning tasks
- image classification
- sentiment analysis
- named entity recognition
- time-series forecasting
- audio processing
- multimodal understanding

## 8. Why deep learning matters
Deep learning is useful when:
- features are not easy to handcraft
- data is high dimensional
- patterns are complex and nonlinear
- models must generalize across raw inputs like images, text, and audio

## 9. Goal
This module gives the learner the ability to understand neural networks, training loops, and PyTorch-based model building.
