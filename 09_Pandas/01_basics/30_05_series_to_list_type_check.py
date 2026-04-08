import pandas as pd


series = pd.Series([10, 20, 30, 40, 50])
converted_list = series.tolist()

print("Element-wise type check (int Series -> list):")
for index, value in enumerate(converted_list):
    print(f"  list[{index}] = {value}  ->  Type: {type(value)}")
