# -------------------------------------------------
# File Name: 05_shuffle_rows.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 40 shuffle rows.
# -------------------------------------------------

"""Practice 40: Shuffle DataFrame Rows."""
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
df_practice_40 = pd.DataFrame(exam_data, index=labels)

df_practice_40 = df_practice_40.sample(frac=1, random_state=42)
print("New DataFrame:")
print(df_practice_40)
