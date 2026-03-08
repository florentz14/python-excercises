"""W3Resource 43: Column to List."""
import pandas as pd

df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6], "col3": [7, 8, 9]})
print("Original DataFrame")
print(df)
print("\nCol2 of the DataFrame to list:")
print(df["col2"].tolist())
