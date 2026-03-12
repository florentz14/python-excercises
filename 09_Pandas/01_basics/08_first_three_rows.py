# -------------------------------------------------
# File Name: 08_first_three_rows.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Select the first three rows of a DataFrame.
# -------------------------------------------------

# import libraries
import pandas as pd
import numpy as np

# create a dictionary of exam data
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

# create a DataFrame from the dictionary with specified index labels
df = pd.DataFrame(exam_data, index=labels)

# print the DataFrame
print("First three rows of the data frame:")
print(df.head(3))
