# -------------------------------------------------
# File Name: 60_get_column_dtypes.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Gets the data types of the columns in a DataFrame.
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

# create a DataFrame from the exam data with the index labels
df = pd.DataFrame(exam_data, index=labels)

# print the data types of the columns
print("Data types of the columns of the said DataFrame:")
print(df.dtypes)
