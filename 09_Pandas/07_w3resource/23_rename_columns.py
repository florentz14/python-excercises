"""W3Resource 23: Renaming DataFrame Columns."""
import pandas as pd

df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6], "col3": [7, 8, 9]})
print("Original DataFrame")
print(df)

df = df.rename(columns={"col1": "Column1", "col2": "Column2", "col3": "Column3"})
print("\nNew DataFrame after renaming columns:")
print(df)
