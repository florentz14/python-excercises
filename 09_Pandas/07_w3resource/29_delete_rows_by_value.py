"""W3Resource 29: Delete Rows by Column Value."""
import pandas as pd

df = pd.DataFrame({"col1": [1, 4, 3, 4, 5], "col2": [4, 5, 6, 7, 8], "col3": [7, 8, 9, 0, 1]})
print("Original DataFrame")
print(df)
df = df[df["col2"] != 5]
print("\nNew DataFrame")
print(df)
