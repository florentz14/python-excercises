# -------------------------------------------------
# File Name: 01_create_dataframe.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Creates DataFrames from dictionaries, lists of dicts, and NumPy; demonstrates Series creation.
# -------------------------------------------------

import pandas as pd
import numpy as np

# 1. DataFrame from dictionary (keys = columns)
data = {
    "name": ["Anna", "Louis", "Mary"],
    "age": [25, 30, 28],
    "city": ["Madrid", "Barcelona", "Valencia"],
}
# Create a DataFrame from a dictionary
df = pd.DataFrame(data)
print("DataFrame from dictionary:\n", df)

# 2. DataFrame from list of dicts (each dict = one row)
rows = [
    {"product": "A", "price": 10},
    {"product": "B", "price": 20},
]

# Create a DataFrame from a list of dicts
df2 = pd.DataFrame(rows)
print("\nDataFrame from list of dicts:\n", df2)

# 3. Series (1D vector)
# Create a Series from a list
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print("\nSeries:\n", s)

# 4. DataFrame from NumPy array
arr = np.array([[1, 2], [3, 4], [5, 6]])
# Create a DataFrame from a NumPy array
df3 = pd.DataFrame(arr, columns=["X", "Y"])
print("\nDataFrame from NumPy:\n", df3)
