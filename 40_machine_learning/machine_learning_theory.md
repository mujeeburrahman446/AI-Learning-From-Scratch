# Machine Learning Theory

Machine learning is the process of learning patterns from data and making predictions or decisions without being explicitly programmed for every rule.

## 1. What is a model?
A model is a function that maps input features to output values.

```text
f(x) -> y
```

Examples:
- regression model predicts a continuous number
- classification model predicts a class label

## 2. Supervised learning
The model sees labeled examples.

Examples:
- spam detection
- house price prediction
- image classification

### Key components
- inputs X
- targets y
- training data
- validation data
- test data

## 3. Unsupervised learning
The model learns patterns without labels.

Examples:
- clustering
- anomaly detection
- dimensionality reduction

## 4. Overfitting and underfitting
### Underfitting
The model is too simple and fails to capture patterns.

### Overfitting
The model memorizes training data and does not generalize well.

## 5. Bias-variance tradeoff
There is a tradeoff between:
- bias: simplifying assumptions
- variance: sensitivity to data

## 6. Loss functions
Loss measures error between prediction and target.

Examples:
- MSE for regression
- cross-entropy for classification

## 7. Gradient descent
Models learn by updating parameters using gradients.

```text
parameter = parameter - learning_rate * gradient
```

This is the driving force behind neural networks and many classical models.

## 8. Evaluation metrics
- accuracy
- precision
- recall
- F1 score
- AUC
- RMSE

## 9. Important principles
- clean data matters more than fancy models
- baselines matter
- simple models can beat complex ones on weak data
- evaluation must be honest

## Summary
Machine learning theory explains how learning works from examples, how error is measured, and how optimization leads to better models.
