# -------------------------------------------------
# File Name: 16_sort_multiple_columns.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 16 sort multiple columns.
# -------------------------------------------------

"""Practice 16: Sorting the DataFrame by Multiple Columns."""
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
df_practice_16 = pd.DataFrame(exam_data, index=labels)

print("Original rows:")
print(df_practice_16)
print("\nSort the data frame first by 'name' in descending order, then by 'score' in ascending order:")
result = df_practice_16.sort_values(by=["name", "score"], ascending=[False, True])
print(result)
