# -------------------------------------------------
# File Name: 03_dataframe_index_labels.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Create a DataFrame with specified index labels.
# -------------------------------------------------

# import libraries
import pandas as pd
import numpy as np

# Define the data
# Create a dictionary with the data
data = {
    "name": ["Aisha Hassan", "Mateo Rodriguez", "Hiroshi Tanaka", "Kwame Mensah", "Sofia Petrova", "Liam OConnor", "Fatima Alzahra", "Chen Wei", "Ananya Sharma", "Lucas Silva", "Noah Johnson", "Yuki Nakamura", "Zara Khan", "Victor Dubois"],
    "score": [12.5, 9.0, 16.5, np.nan, 9.0, 20.0, 14.5, np.nan, 8.0, 19.0, 11.5, 17.3, 13.8, 15.2],
    "attempts": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1, 2, 2, 1, 3, 2, 2, 1, 3],
    "qualify": ["yes", "no", "yes", "no", "no", "yes", "yes", "no", "no", "yes", "no", "yes", "yes", "yes"],
}

# Create a list of index labels
labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]

# Create a DataFrame from the dictionary with the index labels
df = pd.DataFrame(data, index=labels)

# print the DataFrame
print(df)
