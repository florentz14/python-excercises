# -------------------------------------------------
# File Name: 73_custom_aggregations.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Custom aggregation functions.
# -------------------------------------------------

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "cat": ["A", "A", "B", "B", "B"],
    "val": [1, 5, 2, 8, 4],
})

print("=== ORIGINAL ===")
print(df)
print()

# Named aggregation
result = df.groupby("cat").agg(
    total=("val", "sum"),
    mean=("val", "mean"),
    count=("val", "count"),
    first=("val", "first"),
)
print("=== Named aggregations ===")
print(result)
print()

# Custom function
def range_val(s):
    return s.max() - s.min()

result2 = df.groupby("cat")["val"].agg([("range", range_val), ("sum", "sum")])
print("=== Custom range() ===")
print(result2)
print()

# Multiple columns, different aggs
result3 = df.groupby("cat").agg({"val": ["sum", "mean", range_val]})
print("=== Multi-agg ===")
print(result3)
print()

# agg with list of functions
print("=== agg(['sum','mean']) ===")
print(df.groupby("cat")["val"].agg(["sum", "mean"]))
