# -------------------------------------------------
# File Name: 72_dataframes_mixed_values.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Creates DataFrames with different value types.
# -------------------------------------------------

# import libraries
import pandas as pd
import numpy as np

# print DataFrame with random values
print("DataFrame: Contains random values:")
df1 = pd.DataFrame(np.random.randn(5, 4), columns=["A", "B", "C", "D"])
df1.index = ["".join(np.random.choice(list("abcdefghij"), 10)) for _ in range(5)]
print(df1)

# print DataFrame with missing values
print("\nDataFrame: Contains missing values:")
df2 = pd.DataFrame(np.random.randn(5, 4), columns=["A", "B", "C", "D"])
df2.index = ["".join(np.random.choice(list("abcdefghij"), 10)) for _ in range(5)]
df2.iloc[1, 0] = np.nan
print(df2)

# print DataFrame with datetime index
print("\nDataFrame: Contains datetime values:")
df3 = pd.DataFrame(np.random.randn(5, 4), columns=["A", "B", "C", "D"])
df3.index = pd.date_range("2000-01-01", periods=5, freq="D")
print(df3)

# print DataFrame with mixed value types
print("\nDataFrame: Contains mixed values:")
df4 = pd.DataFrame(
    {
        "A": [0, 1, 2, 3, 4],
        "B": [0, 1, 0, 1, 0],
        "C": ["foo1", "foo2", "foo3", "foo4", "foo5"],
        "D": pd.date_range("2009-01-01", periods=5, freq="D"),
    }
)
print(df4)
