# -------------------------------------------------
# File Name: 22_append_delete_row.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Appending and deleting a new row.
# -------------------------------------------------

# import libraries
from pathlib import Path

import pandas as pd

csv_path = Path(__file__).parent.parent / "data" / "exam_attempts.csv"
df_append_delete_row = pd.read_csv(csv_path)
df_append_delete_row.index = list("abcdefghij")

print("Append a new row:")

# append a new row
df_append_delete_row.loc["k"] = ["Suresh", 15.5, 1, "yes"]
print("\nPrint all records after insert a new record:")
print(df_append_delete_row)

print("\nDelete the new row and display the original rows:")

# delete the new row
df_append_delete_row = df_append_delete_row.drop("k")

# print the DataFrame without the new row
print(df_append_delete_row)
