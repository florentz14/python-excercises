# -------------------------------------------------
# File Name: 25_sort_multiple_columns.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Sorting the DataFrame by multiple columns.
# -------------------------------------------------

# import libraries
from pathlib import Path

import pandas as pd

csv_path = Path(__file__).parent.parent / "data" / "exam_attempts.csv"
df_sort_multiple_columns = pd.read_csv(csv_path)
df_sort_multiple_columns.index = list("abcdefghij")

print("Original rows:")
print(df_sort_multiple_columns)
print("\nSort the data frame first by 'name' in descending order, then by 'score' in ascending order:")
result = df_sort_multiple_columns.sort_values(by=["name", "score"], ascending=[False, True])
# print the sorted DataFrame
print(result)
