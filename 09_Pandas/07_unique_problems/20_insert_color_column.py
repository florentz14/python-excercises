# -------------------------------------------------
# File Name: 20_insert_color_column.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 20 insert color column.
# -------------------------------------------------

"""Practice 20: Inserting a New Column."""
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
df_practice_20 = pd.DataFrame(exam_data, index=labels)

colors = ["Red", "Blue", "Orange", "Red", "White", "White", "Blue", "Green", "Green", "Red"]
df_practice_20["color"] = colors
print("New DataFrame after inserting the 'color' column")
print(df_practice_20)
