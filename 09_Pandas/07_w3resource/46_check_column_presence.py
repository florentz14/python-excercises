"""W3Resource 46: Check Column Presence."""
import pandas as pd

df = pd.DataFrame(
    {"col1": [1, 2, 3, 4, 7], "col2": [4, 5, 6, 9, 5], "col3": [7, 8, 12, 1, 11]}
)
print("Original DataFrame")
print(df)
for col in ["col4", "col1"]:
    if col in df.columns:
        print(f"{col} is present in DataFrame.")
    else:
        print(f"{col} is not present in DataFrame.")
