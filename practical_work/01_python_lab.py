# Python Practice Lab

This script contains simple beginner-level Python exercises.

```python
# 1. Basic data types
name = "Alice"
age = 25
print(f"Name: {name}, Age: {age}")

# 2. List operations
numbers = [1, 2, 3, 4, 5]
print("Sum:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))

# 3. Dictionary operations
student = {"name": "Alice", "score": 92}
print(student)

# 4. Loop practice
for i in range(1, 6):
    print(f"Number: {i}")

# 5. Function practice

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

# 6. File writing
with open("sample_output.txt", "w") as f:
    f.write("This is a Python practice output.\n")

print("Python practice lab complete.")
```

## Exercises
- rewrite the script using functions
- add validation for invalid input
- read a CSV file and compute summary metrics
- create a small calculator app
