"""W3Resource 57: Count Number of Columns."""
import pandas as pd

df = pd.DataFrame(
    {"col1": [1, 2, 3, 4, 7], "col2": [4, 5, 6, 9, 5], "col3": [7, 8, 12, 1, 11]}
)
print("Original DataFrame")
print(df)
print(f"\nNumber of columns:")
print(len(df.columns))
