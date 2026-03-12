# -------------------------------------------------
# File Name: 22_numeric_representation_distinct.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 77 numeric representation distinct.
# -------------------------------------------------

"""Practice 77: Get Numeric Representation from Distinct Values."""
import pandas as pd
import numpy as np

data = {"Name": ["Alberto Franco", "Gino Mcneill", "Ryan Parkes", "Eesha Hinton", "Gino Mcneill"], "Date_Of_Birth": ["17/05/2002", "16/02/1999", "25/09/1998", "11/05/2002", "15/09/1997"], "Age": [18.5, 21.2, 22.5, 22.0, 23.0]}
df_practice_77 = pd.DataFrame(data)
print("Original DataFrame:")
print(df_practice_77)
encoded, uniques = pd.factorize(df_practice_77["Name"])
print("\nNumeric representation of an array by identifying distinct values:")
print(encoded)
print(uniques)
