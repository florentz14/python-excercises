# -------------------------------------------------
# File Name: 02_create_from_dict.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Creates a DataFrame from a dictionary.
# -------------------------------------------------

import pandas as pd

# Define the data
# Create a dictionary with the data
data = {"X": [78, 85, 96, 80, 86], "Y": [84, 94, 89, 83, 86], "Z": [86, 97, 96, 72, 83]}

# Create a DataFrame from the dictionary
# The keys of the dictionary are the columns of the DataFrame
# The values of the dictionary are the rows of the DataFrame
df = pd.DataFrame(data)

# Print the DataFrame
print(df)
