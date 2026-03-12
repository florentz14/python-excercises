# -------------------------------------------------
# File Name: 35_column_headers_list.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Getting a list of column headers from a DataFrame.
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
labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
df_column_headers_list = pd.DataFrame(exam_data, index=labels)

print(df_column_headers_list.columns.tolist())
# print the list of column headers
print(f"List of column headers: {df_column_headers_list.columns.tolist()}")