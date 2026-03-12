# -------------------------------------------------
# File Name: 18_select_columns_by_dtype.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 66 select columns by dtype.
# -------------------------------------------------

"""Practice 66: Select Columns by Data Type."""
import pandas as pd

data = {"name": ["Alberto Franco", "Gino Mcneill", "Ryan Parkes", "Eesha Hinton", "Syed Wharton"], "date_of_birth": ["17/05/2002", "16/02/1999", "25/09/1998", "11/05/2002", "15/09/1997"], "age": [18.5, 21.2, 22.5, 22.0, 23.0]}
df_practice_66 = pd.DataFrame(data)
print("Original DataFrame")
print(df_practice_66)
print("\nSelect numerical columns")
print(df_practice_66.select_dtypes(include=["number"]))
print("\nSelect string columns")
print(df_practice_66.select_dtypes(include=["object"]))
