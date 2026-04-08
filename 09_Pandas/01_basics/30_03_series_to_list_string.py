import pandas as pd


str_series = pd.Series(["apple", "banana", "cherry", "date"])
str_list = str_series.tolist()

print("String Series to List:")
print(f"  Series : {str_series.values}  ->  Type: {type(str_series)}")
print(f"  List   : {str_list}  ->  Type: {type(str_list)}")
