# -------------------------------------------------
# File Name: 68_rename_columns_pattern.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 68 rename columns pattern.
# -------------------------------------------------

"""Practice 68: Rename All Columns with Same Pattern."""
import pandas as pd

df_practice_68 = pd.DataFrame(
    {
        "Name": ["Alberto Franco", "Gino Mcneill", "Ryan Parkes", "Eesha Hinton", "Syed Wharton"],
        "Date_Of_Birth": ["17/05/2002", "16/02/1999", "25/09/1998", "11/05/2002", "15/09/1997"],
        "Age": [18.5, 21.2, 22.5, 22.0, 23.0],
    }
)
print("Original DataFrame")
print(df_practice_68)
df_practice_68.columns = df_practice_68.columns.str.strip().str.lower()
print("\nRemove trailing whitespace and convert to lowercase of the columns name")
print(df_practice_68)
