# NumPy and EDA Practice

This script loads a small dataset, summarizes it, and plots basic statistics.

```python
import numpy as np
import pandas as pd

# Example dataset
sales = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "sales": [250, 320, 290, 430, 500],
    "profit": [40, 55, 50, 80, 95]
})

print("Dataset:\n", sales)
print("\nSummary:")
print(sales.describe())

# Correlation
print("\nCorrelation matrix:\n", sales[["sales", "profit"]].corr())

# Basic numpy operations
sales_array = sales["sales"].to_numpy()
print("\nMean sales:", np.mean(sales_array))
print("Max sales:", np.max(sales_array))
print("Min sales:", np.min(sales_array))

# Simple metric
profit_margin = sales["profit"].sum() / sales["sales"].sum()
print("\nProfit margin:", round(profit_margin, 4))
```

## Tasks
- add a missing value to the dataset and handle it
- compute group-by totals by month
- plot a bar chart with matplotlib
- generate a simple report from the processed dataset
