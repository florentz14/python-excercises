# -------------------------------------------------
# File Name: 70_continuous_to_categorical.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Converts a continuous column into categorical groups.
# -------------------------------------------------

# import libraries
import pandas as pd

# create a dictionary with sample data
data = {
    "Name": ["Alberto Franco", "Gino Mcneill", "Ryan Parkes", "Eesha Hinton", "Syed Wharton", "Extra"],
    "Age": [18, 22, 40, 50, 80, 5],
}

# create a DataFrame from the dictionary
df = pd.DataFrame(data)

# define bins and labels for age groups
bins = [0, 18, 60, 100]
labels = ["kids", "adult", "elderly"]

# convert continuous age values to categories
df["age_groups"] = pd.cut(df["Age"], bins=bins, labels=labels)

# print the new categorical column
print("Age group:")
print(df["age_groups"])
