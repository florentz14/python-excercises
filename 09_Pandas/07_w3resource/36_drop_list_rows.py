"""W3Resource 36: Drop Rows from DataFrame."""
import pandas as pd

df = pd.DataFrame({"col1": [1, 4, 3, 4, 5], "col2": [4, 5, 6, 7, 8], "col3": [7, 8, 9, 0, 1]})
print("Original DataFrame")
print(df)
df = df.drop([2, 4])
print("\nNew DataFrame after removing 2nd & 4th rows:")
print(df)
