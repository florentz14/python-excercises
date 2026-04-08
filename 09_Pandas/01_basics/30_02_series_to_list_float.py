import pandas as pd


float_series = pd.Series([1.1, 2.2, 3.3, 4.4, 5.5])
float_list = float_series.tolist()

print("Float Series to List:")
print(f"  Series : {float_series.values}  ->  Type: {type(float_series)}")
print(f"  List   : {float_list}  ->  Type: {type(float_list)}")
