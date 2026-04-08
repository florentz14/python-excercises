# -------------------------------------------------
# File Name: 31_insert_color_column.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Inserting a new column into the DataFrame.
# -------------------------------------------------

# import libraries
from pathlib import Path

import pandas as pd

csv_path = Path(__file__).parent.parent / "data" / "exam_attempts.csv"
df_insert_color_column = pd.read_csv(csv_path)
df_insert_color_column.index = list("abcdefghij")

colors = ["Red", "Blue", "Orange", "Red", "White", "White", "Blue", "Green", "Green", "Red"]
df_insert_color_column["color"] = colors
# print the DataFrame with the new 'color' column
print("New DataFrame after inserting the 'color' column")
print(df_insert_color_column)
