# -------------------------------------------------
# File Name: 34_set_value_by_index.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 34 set value by index.
# -------------------------------------------------

"""Practice 34: Set Value in Cell by Index."""
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
df_practice_34 = pd.DataFrame(exam_data, index=labels)

df_practice_34.loc["i", "score"] = 10.2
print("Set a given value for particular cell in the DataFrame")
print(df_practice_34)
