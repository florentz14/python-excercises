# -------------------------------------------------
# File Name: 31_insert_color_column.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Inserting a new column into the DataFrame.
# -------------------------------------------------

# import libraries
import numpy as np
import pandas as pd

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
df_insert_color_column = pd.DataFrame(exam_data, index=labels)

colors = ["Red", "Blue", "Orange", "Red", "White", "White", "Blue", "Green", "Green", "Red"]
df_insert_color_column["color"] = colors
# print the DataFrame with the new 'color' column
print("New DataFrame after inserting the 'color' column")
print(df_insert_color_column)
