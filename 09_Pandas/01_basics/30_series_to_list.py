# -------------------------------------------------
# File Name: 30_series_to_list.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Converts pandas Series to Python lists using tolist().
# -------------------------------------------------

# import libraries
import pandas as pd

# create a Series (int)
series = pd.Series([10, 20, 30, 40, 50])
print("Original Series:")
print(series)
print(f"Type of Series : {type(series)}")
print()

# convert Series to Python List using .tolist() (int)
converted_list = series.tolist()
print("Converted Python List:")
print(converted_list)
print(f"Type of List   : {type(converted_list)}")
print()

# create a Series (float)
float_series = pd.Series([1.1, 2.2, 3.3, 4.4, 5.5])
# convert Series to Python List using .tolist() (float)
float_list = float_series.tolist()
# print the Series and List
print("Float Series to List:")
print(f"  Series : {float_series.values}  ->  Type: {type(float_series)}")
print(f"  List   : {float_list}  ->  Type: {type(float_list)}")
print()

# create a Series (string)
str_series = pd.Series(["apple", "banana", "cherry", "date"])
# convert Series to Python List using .tolist() (string)
str_list = str_series.tolist()
print("String Series to List:")
print(f"  Series : {str_series.values}  ->  Type: {type(str_series)}")
print(f"  List   : {str_list}  ->  Type: {type(str_list)}")
print()

# create a Series with custom index (index is NOT included in list)
indexed_series = pd.Series([100, 200, 300], index=["a", "b", "c"])
# convert Series to Python List using .tolist() (custom index)
indexed_list = indexed_series.tolist()
print("Series with Custom Index to List:")
print(f"  Series :\n{indexed_series}")
print(f"  List   : {indexed_list}  ->  Type: {type(indexed_list)}")
print()

# element-wise type verification (int Series -> list)
print("Element-wise type check (int Series -> list):")

# print the element-wise type verification
for index, value in enumerate(converted_list):
    print(f"  list[{index}] = {value}  ->  Type: {type(value)}")
