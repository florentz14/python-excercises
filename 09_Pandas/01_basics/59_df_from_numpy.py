# -------------------------------------------------
# File Name: 59_dataframe_from_numpy.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Creates a DataFrame from a NumPy array.
# -------------------------------------------------

# import libraries
import pandas as pd
import numpy as np

# create a NumPy array with 15 rows and 3 columns
arr = np.zeros((15, 3))

# create a list of column names
column_names = ["Column1", "Column2", "Column3"]

# create a list of index labels
index_labels = [f"Index{i}" for i in range(1, 16)]

# create a DataFrame from the NumPy array with the index labels and column names
df = pd.DataFrame(arr, index=index_labels, columns=column_names)

# print the DataFrame with the index labels and column names
print(df)
