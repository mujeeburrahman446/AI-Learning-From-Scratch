# Numpy Linear Regression Example

import numpy as np

X = np.array([[1.0], [2.0], [3.0], [4.0]], dtype=float)
y = np.array([1.0, 2.0, 3.0, 4.0], dtype=float)

# simple linear model y = m * x + b
# solve using normal equation
A = np.hstack([X, np.ones_like(X)])
coef = np.linalg.inv(A.T @ A) @ A.T @ y

print("Model coefficients:", coef)
