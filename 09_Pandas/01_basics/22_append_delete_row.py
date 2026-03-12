# -------------------------------------------------
# File Name: 22_append_delete_row.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Appending and deleting a new row.
# -------------------------------------------------

# import libraries
import numpy as np
import pandas as pd

# create a DataFrame with the exam data
exam_data = {
    "name": [
        "Valeria",
        "Thiago",
        "Camila",
        "Sergio",
        "Daniela",
        "Bruno",
        "Renata",
        "Nicolas",
        "Aitana",
        "Gael",
    ],
    "score": [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    "attempts": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    "qualify": ["yes", "no", "yes", "no", "no", "yes", "yes", "no", "no", "yes"],
}
# create a list of index labels
labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# create a DataFrame from the exam data with the index labels
df_append_delete_row = pd.DataFrame(exam_data, index=labels)

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
