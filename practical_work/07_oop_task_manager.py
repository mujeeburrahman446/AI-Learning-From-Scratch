# Python Practice: OOP and Data Structures

This script demonstrates better coding habits using OOP and basic data structures.

```python
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def list_tasks(self):
        return self.tasks

manager = TaskManager()
manager.add_task("Learn Python")
manager.add_task("Train a small model")

print(manager.list_tasks())
```

## Exercises
- add task completion flags
- create a priority queue-like behavior
- store tasks in a dictionary with IDs
- write tests for the manager class
