"""W3Resource 58: Select All Except One Column."""
import pandas as pd

df = pd.DataFrame(
    {"col1": [1, 2, 3, 4, 7], "col2": [4, 5, 6, 9, 5], "col3": [7, 8, 12, 1, 11]}
)
print("Original DataFrame")
print(df)
print("\nAll columns except 'col3':")
print(df.drop(columns=["col3"]))
