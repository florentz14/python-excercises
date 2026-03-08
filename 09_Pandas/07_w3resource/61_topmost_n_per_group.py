"""W3Resource 61: Get Topmost n Records Within Each Group."""
import pandas as pd

df = pd.DataFrame(
    {"col1": [1, 2, 3, 4, 7, 11], "col2": [4, 5, 6, 9, 5, 0], "col3": [7, 5, 8, 12, 1, 11]}
)
print("Original DataFrame")
print(df)
print("\ntopmost n records within each group of a DataFrame:")
for col in df.columns:
    print(df.nlargest(3, col))
    print()
