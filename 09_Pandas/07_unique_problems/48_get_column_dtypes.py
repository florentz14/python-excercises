# -------------------------------------------------
# File Name: 48_get_column_dtypes.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 48 get column dtypes.
# -------------------------------------------------

"""Practice 48: Get Column DataTypes."""
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
df_practice_48 = pd.DataFrame(exam_data, index=labels)

print("Data types of the columns of the said DataFrame:")
print(df_practice_48.dtypes)
