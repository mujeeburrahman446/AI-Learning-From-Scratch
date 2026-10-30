# Python From Scratch

This module is the foundation of everything else.

## 1. Python essentials

### Variables and types
```python
name = "Alice"
age = 28
height = 5.8
is_student = True
```

### Data structures
```python
# List
items = [1, 2, 3]

# Tuple
point = (10, 20)

# Dictionary
student = {"name": "Alice", "age": 28}

# Set
seen = {1, 2, 3}
```

### Control flow
```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

### Loops
```python
for i in range(5):
    print(i)

count = 0
while count < 5:
    print(count)
    count += 1
```

### Functions
```python
def add(a, b):
    return a + b

print(add(2, 3))
```

### OOP basics
```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}"
```

## 2. File handling
```python
with open("data.txt", "w") as f:
    f.write("Hello AI")
```

## 3. Modules and packages
```python
import math
print(math.sqrt(16))
```

## 4. Errors and exceptions
```python
try:
    value = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

## 5. Project ideas
- calculator
- todo app
- file organizer
- number guessing game
- simple data parser

## 6. Why Python matters in AI
Python is the default language for:
- data analysis
- machine learning
- deep learning
- statistics
- web APIs
- automation
- AI infrastructure

## 7. Milestone
By the end of this module, you should be able to write scripts, structure logic, and solve small real-world problems in Python.
