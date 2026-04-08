import pandas as pd


indexed_series = pd.Series([100, 200, 300], index=["a", "b", "c"])
indexed_list = indexed_series.tolist()

print("Series with Custom Index to List:")
print(f"  Series :\n{indexed_series}")
print(f"  List   : {indexed_list}  ->  Type: {type(indexed_list)}")
