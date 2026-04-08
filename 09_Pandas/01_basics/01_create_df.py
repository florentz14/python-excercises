# -------------------------------------------------
# File Name: 01_create_dataframe.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Creates DataFrames from dictionaries, lists of dicts, and NumPy; demonstrates Series creation.
# -------------------------------------------------

# Import pandas and numpy libraries
import pandas as pd
import numpy as np

# Define the data
# Create a dictionary with the data
data = {
    "name": ["Anna", "Louis", "Mary"],
    "age": [25, 30, 28],
    "city": ["Madrid", "Barcelona", "Valencia"],
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)
print("DataFrame from dictionary:\n", df)

# Create a list of dicts with the data
rows = [
    {"product": "A", "price": 10},
    {"product": "B", "price": 20},
]

# Create a DataFrame from the list of dicts
df2 = pd.DataFrame(rows)
print("\nDataFrame from list of dicts:\n", df2)

# Create a Series from a list
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print("\nSeries:\n", s)

# Create a DataFrame from a NumPy array
arr = np.array([[1, 2], [3, 4], [5, 6]])

# Define the columns of the DataFrame
columns = ["X", "Y"]

# Create a DataFrame from the NumPy array with the columns
df3 = pd.DataFrame(arr, columns=columns)

# Print the DataFrame
print("\nDataFrame from NumPy:\n", df3)
