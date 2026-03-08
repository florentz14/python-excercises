"""W3Resource 31: Select Row by Integer Index."""
import pandas as pd

df = pd.DataFrame({"col1": [1, 4, 3, 4, 5], "col2": [4, 5, 6, 7, 8], "col3": [7, 8, 9, 0, 1]})
print("Original DataFrame")
print(df)
print("\nIndex-2: Details")
print(df.iloc[[2]])
