import pandas as pd


series = pd.Series([10, 20, 30, 40, 50])
converted_list = series.tolist()

print("Original Series:")
print(series)
print(f"Type of Series : {type(series)}")
print()
print("Converted Python List:")
print(converted_list)
print(f"Type of List   : {type(converted_list)}")
