# -------------------------------------------------
# File Name: 62_sort_by_multiple_columns.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 50 sort by multiple columns.
# -------------------------------------------------

"""Practice 50: Sort DataFrame by Multiple Columns."""
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
df_practice_50 = pd.DataFrame(exam_data, index=labels)

print("Sort the above DataFrame on attempts, name:")
print(df_practice_50.sort_values(by=["attempts", "name"]))
