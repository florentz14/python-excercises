# -------------------------------------------------
# File Name: 70_continuous_to_categorical.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 70 continuous to categorical.
# -------------------------------------------------

"""Practice 70: Convert Continuous Column to Categorical."""
import pandas as pd

data = {"Name": ["Alberto Franco", "Gino Mcneill", "Ryan Parkes", "Eesha Hinton", "Syed Wharton", "Extra"], "Age": [18, 22, 40, 50, 80, 5]}
df_practice_70 = pd.DataFrame(data)
bins = [0, 18, 60, 100]
labels = ["kids", "adult", "elderly"]
df_practice_70["age_groups"] = pd.cut(df_practice_70["Age"], bins=bins, labels=labels)
print("Age group:")
print(df_practice_70["age_groups"])
