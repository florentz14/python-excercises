# -------------------------------------------------
# File Name: 67_split_random_subsets.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 67 split random subsets.
# -------------------------------------------------

"""Practice 67: Split DataFrame into Two Random Subsets."""
import pandas as pd

data = {"name": ["Alberto Franco", "Gino Mcneill", "Ryan Parkes", "Eesha Hinton", "Syed Wharton"], "date_of_birth": ["17/05/2002", "16/02/1999", "25/09/1998", "11/05/2002", "15/09/1997"], "age": [18, 21, 22, 22, 23]}
df_practice_67 = pd.DataFrame(data)
print("Original Dataframe and shape:")
print(df_practice_67)
print(df_practice_67.shape)
n = len(df_practice_67)
subset1 = df_practice_67.sample(n=int(n * 0.6), random_state=42)
subset2 = df_practice_67.drop(subset1.index)
print("\nSubset-1 and shape:")
print(subset1)
print(subset1.shape)
print("\nSubset-2 and shape:")
print(subset2)
print(subset2.shape)
