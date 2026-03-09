# -------------------------------------------------
# File Name: 54_list_of_lists_to_dataframe.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 54 list of lists to dataframe.
# -------------------------------------------------

"""Practice 54: Convert List of Lists into DataFrame."""
import pandas as pd

data = [[2, 4], [1, 3]]
print("Original list of lists:")
print(data)
df_practice_54 = pd.DataFrame(data, columns=["col1", "col2"])
print("\nNew DataFrame")
print(df_practice_54)
