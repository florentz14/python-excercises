# -------------------------------------------------
# File Name: 29_delete_attempts_column.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Deleting a column from the DataFrame.
# -------------------------------------------------

# import libraries
from pathlib import Path

import pandas as pd

csv_path = Path(__file__).parent.parent / "data" / "exam_attempts.csv"
df_delete_attempts_column = pd.read_csv(csv_path)
df_delete_attempts_column.index = list("abcdefghij")

# delete the 'attempts' column
df_delete_attempts_column = df_delete_attempts_column.drop(columns=["attempts"])
# print the DataFrame without the 'attempts' column
print("Delete the 'attempts' column from the data frame:")
print(df_delete_attempts_column)
