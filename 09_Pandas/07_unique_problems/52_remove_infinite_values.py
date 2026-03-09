# -------------------------------------------------
# File Name: 52_remove_infinite_values.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 52 remove infinite values.
# -------------------------------------------------

"""Practice 52: Remove Infinite Values."""
import pandas as pd
import numpy as np

df_practice_52 = pd.DataFrame({"col": [1000, 2000, 3000, -4000, np.inf, -np.inf]})
print("Original DataFrame:")
print(df_practice_52)
df_practice_52 = df_practice_52.replace([np.inf, -np.inf], np.nan)
print("\nRemoving infinite values:")
print(df_practice_52)
