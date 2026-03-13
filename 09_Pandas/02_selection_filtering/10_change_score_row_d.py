# -------------------------------------------------
# File Name: 10_change_score_row_d.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Updates a specific score value by row label.
# -------------------------------------------------

# import libraries
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
# create a DataFrame from the dictionary
df = pd.DataFrame(exam_data, index=labels)

# update the score for row 'd'
df.loc["d", "score"] = 11.5

# print updated DataFrame
print("Change the score in row 'd' to 11.5:")
print(df)
