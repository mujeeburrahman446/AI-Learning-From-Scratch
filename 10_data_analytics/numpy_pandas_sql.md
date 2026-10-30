# NumPy, Pandas, and SQL for Data Work

This module teaches the core tools for data analysis and preparation.

## 1. NumPy fundamentals

### Arrays
```python
import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr)
print(arr.shape)
```

### Vector operations
```python
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print(x + y)
print(x * 2)
```

### Matrix operations
```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A @ B)
```

### Broadcasting
```python
x = np.array([[1, 2, 3]])
print(x + 5)
```

## 2. Pandas fundamentals

### DataFrame creation
```python
import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob"],
    "score": [90, 80]
})
print(df)
```

### Filtering
```python
df[df["score"] > 85]
```

### Grouping
```python
df.groupby("name").sum()
```

### Missing values
```python
df.isnull().sum()
```

## 3. SQL basics
```sql
SELECT name, score
FROM students
WHERE score > 80
ORDER BY score DESC;
```

Common SQL operations:
- SELECT
- WHERE
- ORDER BY
- GROUP BY
- JOIN
- UNION
- HAVING
- CASE
- subqueries

## 4. EDA workflow
- inspect the data
- find missing values
- check distributions
- detect outliers
- compute correlations
- create charts

## 5. Example data analysis use cases
- sales data analysis
- customer behavior analysis
- product performance analysis
- churn analysis

## 6. Goal
This module develops the essential skill of turning raw data into usable structures for model training and business insight.
