# -------------------------------------------------
# File Name: 51_convert_index_to_column.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Converts the index of a DataFrame to a column.
# -------------------------------------------------

# Import pandas and numpy libraries
import pandas as pd
import numpy as np

# Create a dictionary with the exam data
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

# Create a DataFrame with the exam data
df = pd.DataFrame(exam_data)

# Reset the index to convert it to a column
df = df.reset_index()
print("After converting index in a column:")
print(df)
