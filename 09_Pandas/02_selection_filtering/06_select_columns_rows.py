# -------------------------------------------------
# File Name: 06_select_columns_rows.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 06 select columns rows.
# -------------------------------------------------

"""Practice 6: Selecting Specific Columns and Rows."""
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
df_practice_06 = pd.DataFrame(exam_data, index=labels)

# Select 'score' and 'qualify' columns in rows 1, 3, 5, 6 (labels b, d, f, g)
print("Select specific columns and rows:")
print(df_practice_06.loc[["b", "d", "f", "g"], ["score", "qualify"]])
