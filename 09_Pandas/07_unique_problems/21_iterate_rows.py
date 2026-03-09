# -------------------------------------------------
# File Name: 21_iterate_rows.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 21 iterate rows.
# -------------------------------------------------

"""Practice 21: Iterating Over DataFrame Rows."""
import pandas as pd

exam_data = [
    {"name": "Valeria", "score": 12.5},
    {"name": "Thiago", "score": 9},
    {"name": "Camila", "score": 16.5},
]
df_practice_21 = pd.DataFrame(exam_data)

for _, row in df_practice_21.iterrows():
    print(row["name"], row["score"])
