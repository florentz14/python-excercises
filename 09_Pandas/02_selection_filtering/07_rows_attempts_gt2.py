# -------------------------------------------------
# File Name: 07_rows_attempts_gt2.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 07 rows attempts gt2.
# -------------------------------------------------

"""Practice 7: Selecting Rows Where Attempts > 2."""
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
df_practice_07 = pd.DataFrame(exam_data, index=labels)

print("Number of attempts in the examination is greater than 2:")
print(df_practice_07[df_practice_07["attempts"] > 2])
