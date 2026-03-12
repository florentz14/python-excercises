# -------------------------------------------------
# File Name: 69_rename_columns_pattern.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Normalizes column names with a consistent pattern.
# -------------------------------------------------

# import libraries
import pandas as pd

# create a DataFrame with sample data
df = pd.DataFrame(
    {
        "Name": ["Alberto Franco", "Gino Mcneill", "Ryan Parkes", "Eesha Hinton", "Syed Wharton"],
        "Date_Of_Birth": ["17/05/2002", "16/02/1999", "25/09/1998", "11/05/2002", "15/09/1997"],
        "Age": [18.5, 21.2, 22.5, 22.0, 23.0],
    }
)

# print the original DataFrame
print("Original DataFrame")
print(df)

# normalize column names (strip spaces and lowercase)
df.columns = df.columns.str.strip().str.lower()

# print the DataFrame with normalized columns
print("\nRemove trailing whitespace and convert to lowercase of the columns name")
print(df)
