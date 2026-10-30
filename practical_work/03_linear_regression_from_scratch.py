# Linear Regression From Scratch

This script demonstrates simple linear regression using gradient descent.

```python
import numpy as np

# Training data
X = np.array([1.0, 2.0, 3.0, 4.0, 5.0], dtype=float)
y = np.array([2.0, 4.0, 5.0, 4.0, 5.0], dtype=float)

# Initialize parameters
m = 0.0
b = 0.0
learning_rate = 0.01
n_iterations = 1000

for _ in range(n_iterations):
    predictions = m * X + b
    error = predictions - y
    m_gradient = np.mean(2 * X * error)
    b_gradient = np.mean(2 * error)
    m -= learning_rate * m_gradient
    b -= learning_rate * b_gradient

print(f"Learned slope: {m}")
print(f"Learned intercept: {b}")
print(f"Predicted value for x=6: {m * 6 + b}")
```

## Exercises
- plot the regression line versus actual data
- modify this to multiple linear regression
- change the learning rate and see the effect
- compare with a closed-form solution
