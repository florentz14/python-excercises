# -------------------------------------------------
# File Name: 25_sort_multiple_columns.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Sorting the DataFrame by multiple columns.
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
# create a DataFrame from the exam data with the index labels
df_sort_multiple_columns = pd.DataFrame(exam_data, index=labels)

print("Original rows:")
print(df_sort_multiple_columns)
print("\nSort the data frame first by 'name' in descending order, then by 'score' in ascending order:")
result = df_sort_multiple_columns.sort_values(by=["name", "score"], ascending=[False, True])
# print the sorted DataFrame
print(result)
