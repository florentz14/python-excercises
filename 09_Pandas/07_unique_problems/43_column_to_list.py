# -------------------------------------------------
# File Name: 43_column_to_list.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 43 column to list.
# -------------------------------------------------

"""Practice 43: Column to List."""
import pandas as pd

data = {"col1": [1, 2, 3], "col2": [4, 5, 6], "col3": [7, 8, 9]}
df_practice_43 = pd.DataFrame(data)
print("Original DataFrame")
print(df_practice_43)
print("\nCol2 of the DataFrame to list:")
print(df_practice_43["col2"].tolist())
