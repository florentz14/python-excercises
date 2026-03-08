"""W3Resource 42: Rename Specific Column."""
import pandas as pd

df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6], "col3": [7, 8, 9]})
print("Original DataFrame")
print(df)
df = df.rename(columns={"col2": "Column2"})
print("\nNew DataFrame after renaming second column:")
print(df)
