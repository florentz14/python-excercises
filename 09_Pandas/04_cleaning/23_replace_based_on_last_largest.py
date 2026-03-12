# -------------------------------------------------
# File Name: 23_replace_based_on_last_largest.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 78 replace based on last largest.
# -------------------------------------------------

"""Practice 78: Replace Value Based on Last Largest Value."""
import pandas as pd
import numpy as np

np.random.seed(42)
df_practice_78 = pd.DataFrame({"rnum": np.random.randint(15, 36, 15)})
print("Original DataFrame:")
print(df_practice_78)
cummax = df_practice_78["rnum"].cummax()
df_practice_78["rnum"] = np.where(df_practice_78["rnum"] >= cummax, df_practice_78["rnum"], 0)
print("\nReplace current value in a dataframe column based on last largest value:")
print(df_practice_78)
