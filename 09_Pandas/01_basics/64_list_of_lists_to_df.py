# -------------------------------------------------
# File Name: 64_list_of_lists_to_dataframe.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Converts a list of lists into a DataFrame.
# -------------------------------------------------

# import libraries
import pandas as pd

# create a list of lists
data = [[2, 4], [1, 3]]

# print the original list of lists
print("Original list of lists:")
print(data)

# create a DataFrame from the list of lists
df = pd.DataFrame(data, columns=["col1", "col2"])

# print the new DataFrame
print("\nNew DataFrame")
print(df)
