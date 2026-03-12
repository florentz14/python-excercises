# -------------------------------------------------
# File Name: 19_local_variable_in_query.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 75 local variable in query.
# -------------------------------------------------

"""Practice 75: Use Local Variable Within a Query."""
import pandas as pd

data = {"W": [68, 75, 86, 80, 66], "X": [78, 85, 96, 80, 86], "Y": [84, 94, 89, 83, 86], "Z": [86, 97, 96, 72, 83]}
df_practice_75 = pd.DataFrame(data)
print("Original DataFrame")
print(df_practice_75)
max_w = df_practice_75["W"].max()
result = df_practice_75.query("W < @max_w")
print("\nValues which are less than maximum value of 'W' column")
print(result)
