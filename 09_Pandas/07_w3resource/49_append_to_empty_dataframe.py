"""W3Resource 49: Append Data to Empty DataFrame."""
import pandas as pd

df = pd.DataFrame()
print("Original DataFrame:")
print(df)
df = pd.concat([df, pd.DataFrame({"col1": [0, 1, 2], "col2": [0, 1, 2]})], ignore_index=True)
print("\nAfter appending some data:")
print(df)
