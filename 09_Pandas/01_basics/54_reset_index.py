# -------------------------------------------------
# File Name: 54_reset_index.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 37 reset index.
# -------------------------------------------------

# Import pandas and numpy libraries
import pandas as pd
import numpy as np

# Create a dictionary with the data
exam_data = {
    "name": ["Aisha Hassan", "Mateo Rodriguez", "Hiroshi Tanaka", "Kwame Mensah", "Sofia Petrova", "Liam OConnor", "Fatima Alzahra", "Chen Wei", "Ananya Sharma", "Lucas Silva", "Noah Johnson", "Yuki Nakamura", "Zara Khan", "Victor Dubois"],
    "score": [12.5, 9.0, 16.5, np.nan, 9.0, 20.0, 14.5, np.nan, 8.0, 19.0, 11.5, 17.3, 13.8, 15.2],
    "attempts": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1, 2, 2, 1, 3],
    "qualify": ["yes", "no", "yes", "no", "no", "yes", "yes", "no", "no", "yes", "no", "yes", "yes", "yes"],
}

# Create a DataFrame with the data and the labels
labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]
df = pd.DataFrame(exam_data, index=labels)

# Remove the first and second rows
df = df.iloc[2:]

# Print the original DataFrame
print(df)

# Reset the index
df = df.reset_index()

# Print the new DataFrame
print(df)