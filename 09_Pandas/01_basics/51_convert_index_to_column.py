# -------------------------------------------------
# File Name: 51_convert_index_to_column.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 33 convert index to column.
# -------------------------------------------------

"""Practice 33: Convert Index to Column."""
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
df_practice_33 = pd.DataFrame(exam_data)
df_practice_33 = df_practice_33.reset_index()
print("After converting index in a column:")
print(df_practice_33)
