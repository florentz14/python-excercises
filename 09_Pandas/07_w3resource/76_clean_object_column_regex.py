"""W3Resource 76: Clean Object Column with Regex."""
import pandas as pd
import re

df = pd.DataFrame({"agent": ["a001", "a002", "a003", "a003", "a004"], "purchase": [4500, 7500, "$3000.25", "$1250.35", "9000.00"]})
print("Original dataframe:")
print(df)
print("Data Types:")
print(df["purchase"].apply(type))
df["purchase"] = df["purchase"].replace(r"[\$,]", "", regex=True).astype(float)
print("New Data Types:")
print(df["purchase"].apply(type))
