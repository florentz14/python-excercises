"""W3Resource 26: Add One Row to a DataFrame."""
import pandas as pd

df = pd.DataFrame({"col1": [1, 4, 3, 4, 5], "col2": [4, 5, 6, 7, 8], "col3": [7, 8, 9, 0, 1]})
print("Original DataFrame")
print(df)
df.loc[len(df)] = [10, 11, 12]
print("\nAfter add one row:")
print(df)
