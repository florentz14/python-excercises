# -------------------------------------------------
# File Name: 15_replace_qualify.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 17 replace qualify.
# -------------------------------------------------

"""Practice 17: Replacing Column Values (qualify)."""
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
df_practice_17 = pd.DataFrame(exam_data, index=labels)

df_practice_17["qualify"] = df_practice_17["qualify"].map({"yes": True, "no": False})
print("Replace the 'qualify' column contains the values 'yes' and 'no' with True and False:")
print(df_practice_17)
