"""W3Resource 25: Changing the Order of DataFrame Columns."""
import pandas as pd

df = pd.DataFrame({"col1": [1, 4, 3, 4, 5], "col2": [4, 5, 6, 7, 8], "col3": [7, 8, 9, 0, 1]})
print("Original DataFrame")
print(df)
df = df[["col3", "col2", "col1"]]
print("\nAfter altering col1 and col3")
print(df)
