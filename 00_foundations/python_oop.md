# Python OOP and Reusable Code

Object-oriented programming helps build clean, scalable code.

## 1. Class basics
```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def describe(self):
        return f"{self.name} scored {self.score}"

student = Student("Alice", 95)
print(student.describe())
```

## 2. Inheritance
```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}"

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade
```

## 3. Encapsulation
Use methods to control access to data.

```python
class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
```

## 4. Why OOP matters in AI
OOP is useful for:
- custom model classes
- dataset handlers
- preprocessing pipelines
- experiment tracking objects
- reusable evaluation tools

## 5. Better coding practice
Write code that is:
- modular
- reusable
- testable
- readable
- maintainable

## 6. Exercise
Create a class that loads a CSV file, clean it, and returns summary statistics.
