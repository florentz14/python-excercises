# -------------------------------------------------
# File Name: 18_select_columns_by_dtype.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Selects columns by numeric and string data types.
# -------------------------------------------------

# import libraries
import pandas as pd

# create a dictionary with sample data
data = {
    "name": ["Alberto Franco", "Gino Mcneill", "Ryan Parkes", "Eesha Hinton", "Syed Wharton"],
    "date_of_birth": ["17/05/2002", "16/02/1999", "25/09/1998", "11/05/2002", "15/09/1997"],
    "age": [18.5, 21.2, 22.5, 22.0, 23.0],
}

# create a DataFrame from the dictionary
df = pd.DataFrame(data)

# print the original DataFrame
print("Original DataFrame")
print(df)

# print numeric columns
print("\nSelect numerical columns")
print(df.select_dtypes(include=["number"]))

# print string/object columns
print("\nSelect string columns")
print(df.select_dtypes(include=["object"]))
