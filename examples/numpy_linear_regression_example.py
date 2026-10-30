# Simple Linear Regression in NumPy

import numpy as np

X = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([2.0, 4.0, 5.0, 4.0, 5.0])

# Fit y = m * x + b
X_mean = X.mean()
y_mean = y.mean()

m = np.sum((X - X_mean) * (y - y_mean)) / np.sum((X - X_mean) ** 2)
b = y_mean - m * X_mean

print(f"Estimated slope: {m}")
print(f"Estimated intercept: {b}")
print(f"Prediction for x=6: {m * 6 + b}")
