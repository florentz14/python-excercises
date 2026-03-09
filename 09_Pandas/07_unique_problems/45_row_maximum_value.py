# -------------------------------------------------
# File Name: 45_row_maximum_value.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 45 row maximum value.
# -------------------------------------------------

"""Practice 45: Row with Maximum Value."""
import pandas as pd

data = {"col1": [1, 2, 3, 4, 7], "col2": [4, 5, 6, 9, 5], "col3": [7, 8, 12, 1, 11]}
df_practice_45 = pd.DataFrame(data)
print("Original DataFrame")
print(df_practice_45)
print("\nRow where col1 has maximum value:")
print(df_practice_45["col1"].idxmax())
print("Row where col2 has maximum value:")
print(df_practice_45["col2"].idxmax())
print("Row where col3 has maximum value:")
print(df_practice_45["col3"].idxmax())
