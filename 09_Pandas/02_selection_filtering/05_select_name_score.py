# -------------------------------------------------
# File Name: 05_select_name_score.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Selects the name and score columns from a DataFrame.
# -------------------------------------------------

# import libraries
import pandas as pd
import numpy as np

# create a dictionary with sample data
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

# create a DataFrame from the dictionary with the index labels
df = pd.DataFrame(exam_data, index=labels)

# print the original DataFrame
print("Original DataFrame:")
print(df)

# print the selected columns
print("Selected columns:")
print(df[["name", "score"]])
