# ------------------------------------------------------------
# Basic case: Create DataFrame and Series
# ------------------------------------------------------------

import pandas as pd
import numpy as np

# 1. DataFrame from dictionary (keys = columns)
data = {
    "name": ["Anna", "Louis", "Mary"],
    "age": [25, 30, 28],
    "city": ["Madrid", "Barcelona", "Valencia"],
}
df = pd.DataFrame(data)
print("DataFrame from dictionary:\n", df)

# 2. DataFrame from list of dicts (each dict = one row)
rows = [
    {"product": "A", "price": 10},
    {"product": "B", "price": 20},
]
df2 = pd.DataFrame(rows)
print("\nDataFrame from list of dicts:\n", df2)

# 3. Series (1D vector)
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print("\nSeries:\n", s)

# 4. DataFrame from NumPy
arr = np.array([[1, 2], [3, 4], [5, 6]])
df3 = pd.DataFrame(arr, columns=["X", "Y"])
print("\nDataFrame from NumPy:\n", df3)
