# -------------------------------------------------
# File Name: 55_divide_dataframe_ratio.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 38 divide dataframe ratio.
# -------------------------------------------------

"""Practice 38: Divide DataFrame by Ratio."""
import pandas as pd
import numpy as np

np.random.seed(42)
df_practice_38 = pd.DataFrame(np.random.randn(10, 2))
print("Original DataFrame:")
print(df_practice_38)
n = len(df_practice_38)
train_size = int(0.7 * n)
train_df = df_practice_38.sample(n=train_size, random_state=42)
test_df = df_practice_38.drop(train_df.index)
print("\n70% of the said DataFrame:")
print(train_df)
print("\n30% of the said DataFrame:")
print(test_df)
