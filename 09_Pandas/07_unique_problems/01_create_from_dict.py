# -------------------------------------------------
# File Name: 01_create_from_dict.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 01 create from dict.
# -------------------------------------------------

"""Practice 1: Creating a DataFrame from a Dictionary."""
import pandas as pd

data = {"X": [78, 85, 96, 80, 86], "Y": [84, 94, 89, 83, 86], "Z": [86, 97, 96, 72, 83]}
df_practice_01 = pd.DataFrame(data)
print(df_practice_01)
