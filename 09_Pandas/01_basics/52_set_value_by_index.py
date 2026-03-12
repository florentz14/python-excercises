# -------------------------------------------------
# File Name: 52_set_value_by_index.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Sets a value for a particular cell in a DataFrame by index.
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

# Create a list of labels
labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

# Create a DataFrame with the exam data and the labels
df = pd.DataFrame(exam_data, index=labels)

# Set the value for the cell at index "i" and column "score"
df.loc["i", "score"] = 10.2

# Print the DataFrame
print("Set a given value for particular cell in the DataFrame")
print(df)
