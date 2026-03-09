# -------------------------------------------------
# File Name: 12_change_score_row_d.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 12 change score row d.
# -------------------------------------------------

"""Practice 12: Changing the Score in a Specific Row."""
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
df_practice_12 = pd.DataFrame(exam_data, index=labels)

df_practice_12.loc["d", "score"] = 11.5
print("Change the score in row 'd' to 11.5:")
print(df_practice_12)
