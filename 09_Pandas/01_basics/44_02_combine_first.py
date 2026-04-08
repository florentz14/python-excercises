import numpy as np
import pandas as pd


df1 = pd.DataFrame({"a": [1, np.nan, 5, np.nan], "b": [np.nan, 2, np.nan, 6]})
df2 = pd.DataFrame({"a": [5, 4, np.nan, 3, 7], "b": [np.nan, 3, 4, 6, 8]})

combined = df1.combine_first(df2)

print("COMBINE FIRST:")
print(combined)
