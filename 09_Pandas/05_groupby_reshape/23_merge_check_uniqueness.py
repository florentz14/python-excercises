# -------------------------------------------------
# File Name: 23_merge_check_uniqueness.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 69 merge check uniqueness.
# -------------------------------------------------

"""Practice 69: Merge Datasets and Check Uniqueness."""
import pandas as pd

data = {"Name": ["Alberto Franco", "Gino Mcneill", "Ryan Parkes", "Eesha Hinton", "Syed Wharton"], "Date_Of_Birth": ["17/05/2002", "16/02/1999", "25/09/1998", "11/05/2002", "15/09/1997"], "Age": [18.5, 21.2, 22.5, 22.0, 23.0]}
df1 = pd.DataFrame(data)
df2 = df1.iloc[[2, 3, 4]]
df3 = df1.iloc[[0, 1, 3, 4]]
print("Original DataFrame:")
print(df1)
print("\nNew DataFrames:")
print(df2)
print(df3)
merged = pd.merge(df2, df3, how="inner", on=["Name", "Date_Of_Birth", "Age"])
print('\n"one_to_one": check if merge keys are unique in both left and right datasets:')
print(merged)
print('\n"one_to_many" or "1:m": check if merge keys are unique in left dataset:')
print(merged)
print('\n"any_to_one" or "m:1": check if merge keys are unique in right dataset:')
print(merged)
