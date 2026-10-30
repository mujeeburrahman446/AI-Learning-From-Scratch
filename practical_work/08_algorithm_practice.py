# Algorithm Practice: Search and Sort

This script demonstrates simple algorithmic thinking in Python.

```python
# Linear search
numbers = [10, 5, 8, 7, 2, 9]

def linear_search(items, target):
    for i, value in enumerate(items):
        if value == target:
            return i
    return -1

print("Index of 8:", linear_search(numbers, 8))

# Bubble sort

def bubble_sort(items):
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items

print("Sorted:", bubble_sort([4, 2, 9, 1, 7]))
```

## Exercises
- implement binary search
- implement merge sort
- compare performance of built-in sort vs bubble sort
- explain time complexity in comments
