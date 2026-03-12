# -------------------------------------------------
# File Name: 08_count_rows_columns.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 08 count rows columns.
# -------------------------------------------------

"""Practice 8: Counting Rows and Columns."""
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
df_practice_08 = pd.DataFrame(exam_data, index=labels)

print(f"Number of Rows: {df_practice_08.shape[0]}")
print(f"Number of Columns: {df_practice_08.shape[1]}")
