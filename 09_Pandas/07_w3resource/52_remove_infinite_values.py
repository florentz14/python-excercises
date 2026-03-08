"""W3Resource 52: Remove Infinite Values."""
import pandas as pd
import numpy as np

df = pd.DataFrame({"col": [1000, 2000, 3000, -4000, np.inf, -np.inf]})
print("Original DataFrame:")
print(df)
df = df.replace([np.inf, -np.inf], np.nan)
print("\nRemoving infinite values:")
print(df)
