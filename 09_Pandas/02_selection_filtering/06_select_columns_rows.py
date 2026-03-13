# -------------------------------------------------
# File Name: 06_select_columns_rows.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Selects specific columns and rows using label indexing.
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

# print the selected columns and rows
print("\nSelected columns and rows:")
# select 'score' and 'qualify' columns in rows 1, 3, 5, 6 (labels b, d, f, g)
selected_df = df.loc[["b", "d", "f", "g"], ["score", "qualify"]]

# print the selected DataFrame
print("Selected DataFrame:")
print(selected_df)
