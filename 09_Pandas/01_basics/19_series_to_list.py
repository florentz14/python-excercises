# -------------------------------------------------
# File Name: 19_series_to_list.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Converts pandas Series to Python lists using tolist().
# -------------------------------------------------

import pandas as pd

# Create a Pandas Series (int)
series = pd.Series([10, 20, 30, 40, 50])
print("Original Pandas Series:")
print(series)
print(f"Type of Series : {type(series)}")
print()

# Convert Series to Python List using .tolist() (int)
converted_list = series.tolist()
print("Converted Python List:")
print(converted_list)
print(f"Type of List   : {type(converted_list)}")
print()

# Create a Pandas Series (float)
float_series = pd.Series([1.1, 2.2, 3.3, 4.4, 5.5])
# Convert Series to Python List using .tolist() (float)
float_list = float_series.tolist()
# Print the Series and List
print("Float Series to List:")
print(f"  Series : {float_series.values}  ->  Type: {type(float_series)}")
print(f"  List   : {float_list}  ->  Type: {type(float_list)}")
print()

# Create a Pandas Series (string)
str_series = pd.Series(["apple", "banana", "cherry", "date"])
# Convert Series to Python List using .tolist() (string)
str_list = str_series.tolist()
print("String Series to List:")
print(f"  Series : {str_series.values}  ->  Type: {type(str_series)}")
print(f"  List   : {str_list}  ->  Type: {type(str_list)}")
print()

# Create a Pandas Series with custom index (index is NOT included in list)
indexed_series = pd.Series([100, 200, 300], index=["a", "b", "c"])
# Convert Series to Python List using .tolist() (custom index)
indexed_list = indexed_series.tolist()
print("Series with Custom Index to List:")
print(f"  Series :\n{indexed_series}")
print(f"  List   : {indexed_list}  ->  Type: {type(indexed_list)}")
print()

# Element-wise type verification (int Series -> list)
print("Element-wise type check (int Series -> list):")
for i, val in enumerate(converted_list):
    print(f"  list[{i}] = {val}  ->  Type: {type(val)}")
