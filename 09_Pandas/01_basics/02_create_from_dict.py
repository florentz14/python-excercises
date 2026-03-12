# -------------------------------------------------
# File Name: 02_create_from_dict.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 01 create from dict.
# -------------------------------------------------

import pandas as pd

# Create a DataFrame from a dictionary
data = {"X": [78, 85, 96, 80, 86], "Y": [84, 94, 89, 83, 86], "Z": [86, 97, 96, 72, 83]}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Print the DataFrame
print(df)
