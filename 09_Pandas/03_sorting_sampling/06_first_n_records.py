# -------------------------------------------------
# File Name: 06_first_n_records.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 59 first n records.
# -------------------------------------------------

"""Practice 59: Get First n Records."""
import pandas as pd

data = {"col1": [1, 2, 3, 4, 7, 11], "col2": [4, 5, 6, 9, 5, 0], "col3": [7, 5, 8, 12, 1, 11]}
df_practice_59 = pd.DataFrame(data)
print("Original DataFrame")
print(df_practice_59)
print("\nFirst 3 rows of the said DataFrame:")
print(df_practice_59.head(3))
