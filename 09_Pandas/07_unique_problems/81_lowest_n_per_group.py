# -------------------------------------------------
# File Name: 81_lowest_n_per_group.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 81 lowest n per group.
# -------------------------------------------------

"""Practice 81: Get Lowest n Records Within Each Group."""
import pandas as pd

df_practice_81 = pd.DataFrame(
    {"col1": [1, 2, 3, 4, 7, 11], "col2": [4, 5, 6, 9, 5, 0], "col3": [7, 5, 8, 12, 1, 11]}
)
print("Original DataFrame")
print(df_practice_81)
print("\nLowest n records within each group of a DataFrame:")
for col in df_practice_81.columns:
    print(df_practice_81.nsmallest(3, col))
    print()
