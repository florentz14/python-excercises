# -------------------------------------------------
# File Name: 62_sort_by_multiple_columns.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Sorts a DataFrame by multiple columns.
# -------------------------------------------------

# import libraries
from pathlib import Path

import pandas as pd

csv_path = Path(__file__).parent.parent / "data" / "exam_attempts.csv"
df = pd.read_csv(csv_path)
df.index = list("abcdefghij")

# print the original DataFrame
print("Original DataFrame:")
print(df)

# sort the DataFrame by the attempts and name columns
sorted_df = df.sort_values(by=["attempts", "name"])

# print the sorted DataFrame
print("Sort the above DataFrame on attempts, name:")
print(sorted_df)
