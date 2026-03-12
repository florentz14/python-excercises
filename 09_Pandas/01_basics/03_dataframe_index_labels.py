# -------------------------------------------------
# File Name: 03_dataframe_index_labels.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Create a DataFrame with specified index labels.
# -------------------------------------------------

# import libraries
import pandas as pd
import numpy as np

# create a dictionary of exam data
data = {
    "name": ["Valeria", "Thiago", "Camila", "Sergio", "Daniela", "Bruno", "Renata", "Nicolas", "Aitana", "Gael"],
    "score": [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    "attempts": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    "qualify": ["yes", "no", "yes", "no", "no", "yes", "yes", "no", "no", "yes"],
}

# create a list of index labels
labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

# create a DataFrame from the dictionary with specified index labels
df = pd.DataFrame(data, index=labels)

# print the DataFrame
print(df)
