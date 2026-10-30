# Deep Learning Theory

Deep learning is a subfield of machine learning built on artificial neural networks with many layers.

## 1. Biological inspiration
Artificial neurons are inspired by biological neurons, but they are simplified computational units.

## 2. Perceptron
A perceptron computes a weighted sum and applies an activation function.

```text
output = activation(dot(x, w) + b)
```

## 3. Neural network architecture
A neural network is composed of layers:
- input layer
- hidden layers
- output layer

## 4. Forward pass
Input is passed through each layer. The network produces predictions.

## 5. Backpropagation
Backpropagation computes gradients of loss with respect to weights using the chain rule.

This is how the network learns.

## 6. Activation functions
- ReLU
- Sigmoid
- Tanh
- Softmax

Why they matter:
- introduce nonlinearity
- allow complex function learning

## 7. Loss functions
- MSE for regression
- cross-entropy for classification
- BCE for binary tasks

## 8. Optimization
Gradient descent and variants like Adam are used to minimize loss.

## 9. Why deep learning works
It learns hierarchical features:
- lower layers detect simple patterns
- higher layers compose them into complex concepts

## 10. Limits and challenges
- lack of interpretability
- need for large data
- expensive compute
- overfitting
- training instability

## Summary
Deep learning theory explains how layered nonlinear functions learn meaningful representations from raw data like images, audio, and text.
