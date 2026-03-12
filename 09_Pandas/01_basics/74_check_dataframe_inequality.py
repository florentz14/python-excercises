# -------------------------------------------------
# File Name: 74_check_dataframe_inequality.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Checks cell-by-cell inequality between two DataFrames.
# -------------------------------------------------

# import libraries
import pandas as pd
import numpy as np

# create first DataFrame
df1 = pd.DataFrame(
    {
        "W": [68, 75, 86, 80, np.nan],
        "X": [78, 85, np.nan, 80, 86],
        "Y": [84, 94, 89, 83, 86],
        "Z": [86, 97, 96, 72, 83],
    }
)

# create second DataFrame
df2 = pd.DataFrame(
    {
        "W": [78, 75, 86, 80, np.nan],
        "X": [78, 85, 96, 80, 76],
        "Y": [84, 84, 89, 83, 86],
        "Z": [86, 97, 96, 72, 83],
    }
)

# print both original DataFrames
print("Original DataFrames:")
print(df1)
print(df2)

# print DataFrame showing inequality by position
print("\nCheck for inequality of the said dataframes:")
print(df1.ne(df2))
