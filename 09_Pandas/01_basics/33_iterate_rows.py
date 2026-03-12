# -------------------------------------------------
# File Name: 33_iterate_rows.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Iterating over the rows of a DataFrame.
# -------------------------------------------------

# import libraries
import pandas as pd

# create a DataFrame with the exam data
exam_data = [
    {"name": "Valeria", "score": 12.5},
    {"name": "Thiago", "score": 9},
    {"name": "Camila", "score": 16.5},
]
# create a DataFrame from the exam data
df_iterate_rows = pd.DataFrame(exam_data)

# iterate over the rows of the DataFrame
for _, row in df_iterate_rows.iterrows():
    # print the name and score of the row
    print(f"Name: {row['name']}, Score: {row['score']}")
