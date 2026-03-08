"""W3Resource 56: Get Column Index by Column Name."""
import pandas as pd

df = pd.DataFrame(
    {"col1": [1, 2, 3, 4, 7], "col2": [4, 5, 6, 9, 5], "col3": [7, 8, 12, 1, 11]}
)
print("Original DataFrame")
print(df)
idx = df.columns.get_loc("col2")
print(f"\nIndex of 'col2'")
print(idx)
