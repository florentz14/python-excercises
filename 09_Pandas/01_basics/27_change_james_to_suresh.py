# -------------------------------------------------
# File Name: 27_change_james_to_suresh.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Changing a Specific Name Value.
# -------------------------------------------------

# import libraries
import pandas as pd
import numpy as np

# create a DataFrame with the exam data
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
# create a list of index labels
labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# create a DataFrame from the exam data with the index labels
df_change_james_to_suresh = pd.DataFrame(exam_data, index=labels)

# change the name 'Sergio' to 'Suresh'
df_change_james_to_suresh["name"] = df_change_james_to_suresh["name"].replace("Sergio", "Suresh")
# print the DataFrame with the changed name
print("Change the name 'Sergio' to 'Suresh':")
print(df_change_james_to_suresh)
