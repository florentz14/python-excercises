# -------------------------------------------------
# File Name: 18_change_james_to_suresh.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 18 change james to suresh.
# -------------------------------------------------

"""Practice 18: Changing a Specific Name Value."""
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
df_practice_18 = pd.DataFrame(exam_data, index=labels)

df_practice_18["name"] = df_practice_18["name"].replace("Sergio", "Suresh")
print("Change the name 'Sergio' to 'Suresh':")
print(df_practice_18)
