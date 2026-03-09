# -------------------------------------------------
# File Name: 19_series_to_list.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Converts pandas Series to Python lists using tolist().
# -------------------------------------------------

import pandas as pd

# Create a Pandas Series
series = pd.Series([10, 20, 30, 40, 50])
print("Original Pandas Series:")
print(series)
print(f"Type of Series : {type(series)}")
print()

# Convert Series to Python List using .tolist()
converted_list = series.tolist()
print("Converted Python List:")
print(converted_list)
print(f"Type of List   : {type(converted_list)}")
print()

# -------------------------------------------
# Additional examples with different data types
# -------------------------------------------

# Float Series
float_series = pd.Series([1.1, 2.2, 3.3, 4.4, 5.5])
float_list = float_series.tolist()
print("Float Series to List:")
print(f"  Series : {float_series.values}  ->  Type: {type(float_series)}")
print(f"  List   : {float_list}  ->  Type: {type(float_list)}")
print()

# String Series
str_series = pd.Series(["apple", "banana", "cherry", "date"])
str_list = str_series.tolist()
print("String Series to List:")
print(f"  Series : {str_series.values}  ->  Type: {type(str_series)}")
print(f"  List   : {str_list}  ->  Type: {type(str_list)}")
print()

# Series with custom index (index is NOT included in list)
indexed_series = pd.Series([100, 200, 300], index=["a", "b", "c"])
indexed_list = indexed_series.tolist()
print("Series with Custom Index to List:")
print(f"  Series :\n{indexed_series}")
print(f"  List   : {indexed_list}  ->  Type: {type(indexed_list)}")
print()

# Element-wise type verification
print("Element-wise type check (int Series -> list):")
for i, val in enumerate(converted_list):
    print(f"  list[{i}] = {val}  ->  Type: {type(val)}")
