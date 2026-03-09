# -------------------------------------------------
# File Name: 15_append_delete_row.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 15 append delete row.
# -------------------------------------------------

"""Practice 15: Appending and Deleting a New Row."""
import pandas as pd
import numpy as np

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
labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
df_practice_15 = pd.DataFrame(exam_data, index=labels)

print("Append a new row:")
df_practice_15.loc["k"] = ["Suresh", 15.5, 1, "yes"]
print("\nPrint all records after insert a new record:")
print(df_practice_15)

print("\nDelete the new row and display the original rows:")
df_practice_15 = df_practice_15.drop("k")
print(df_practice_15)
