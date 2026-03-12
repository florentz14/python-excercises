# -------------------------------------------------
# File Name: 15_attempts_lt2_score_gt15.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Pandas exercise: 11 attempts lt2 score gt15.
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
df_attempts_lt2_score_gt15 = pd.DataFrame(exam_data, index=labels)

# print the DataFrame with the number of attempts in the examination is less than 2 and score greater than 15
print(
    "Number of attempts in the examination is less than 2 and score greater than 15:"
)
print(df_attempts_lt2_score_gt15[(df_attempts_lt2_score_gt15["attempts"] < 2) & (df_attempts_lt2_score_gt15["score"] > 15)])
