# -------------------------------------------------
# File Name: 17_astype_and_conversion.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Convert column data types safely
# -------------------------------------------------

# import libraries
import pandas as pd

# create a DataFrame with the a, b, and c data
df = pd.DataFrame({"a": [1, 2, 3], "b": ["4", "5", "6"], "c": [1.1, 2.2, 3.3]})
# print the original dtypes
print("Original dtypes:", df.dtypes.to_dict())
# convert the b column to int
df["b"] = df["b"].astype(int)
# convert the c column to int
df["c"] = df["c"].astype(int)
# print the dtypes after the conversion
print("After astype:", df.dtypes.to_dict())
