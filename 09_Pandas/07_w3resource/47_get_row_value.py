"""W3Resource 47: Get Row Value."""
import pandas as pd

df = pd.DataFrame(
    {"col1": [1, 2, 3, 4, 7], "col2": [4, 5, 6, 9, 5], "col3": [7, 8, 12, 1, 11]}
)
print("Original DataFrame")
print(df)
print("\nValue of Row 0")
print(df.iloc[0])
print("\nValue of Row4")
print(df.iloc[3])
