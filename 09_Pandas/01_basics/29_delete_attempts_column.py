# -------------------------------------------------
# File Name: 29_delete_attempts_column.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Deleting a column from the DataFrame.
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
df_delete_attempts_column = pd.DataFrame(exam_data, index=labels)

# delete the 'attempts' column
df_delete_attempts_column = df_delete_attempts_column.drop(columns=["attempts"])
# print the DataFrame without the 'attempts' column
print("Delete the 'attempts' column from the data frame:")
print(df_delete_attempts_column)
