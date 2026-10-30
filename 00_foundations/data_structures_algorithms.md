# Data Structures and Algorithms for AI

AI developers benefit from understanding both data structures and algorithmic thinking.

## 1. Data structures
### Lists
Fast for sequential data and indexing.

### Dictionaries
Fast lookup by key.

### Sets
Useful for uniqueness and membership tests.

### Queues and stacks
Important for process flows and recursion-based problems.

### Trees and graphs
Used in search, decision-making, and some graph-based AI workflows.

## 2. Algorithms
Core topics:
- linear search
- binary search
- sorting
- recursion
- divide and conquer
- breadth-first search
- depth-first search
- dynamic programming

## 3. Complexity analysis
Important metrics:
- time complexity
- space complexity
- O(1), O(log n), O(n), O(n log n), O(n^2)

## 4. Why this matters in AI
- efficient data access improves runtime
- model pipeline performance depends on indexing and storage
- search and optimization rely on algorithmic thinking
- graph and tree structures show up in planning and search-based agents

## 5. Example
```python
# Linear search
numbers = [4, 7, 2, 9, 1]

for index, value in enumerate(numbers):
    if value == 9:
        print("Found at index:", index)
        break
```

## 6. Exercise
Write a function that sorts a list using bubble sort, then compare with Python's built-in sort.
