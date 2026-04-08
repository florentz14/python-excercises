import pandas as pd


series1 = pd.Series([2, 4, 6, 8, 10])
series2 = pd.Series([1, 3, 5, 7, 10])

print("Using pandas built-in methods:")
print(f"series1.eq(series2)  : {series1.eq(series2).tolist()}")
print(f"series1.ne(series2)  : {series1.ne(series2).tolist()}")
print(f"series1.gt(series2)  : {series1.gt(series2).tolist()}")
print(f"series1.lt(series2)  : {series1.lt(series2).tolist()}")
print(f"series1.ge(series2)  : {series1.ge(series2).tolist()}")
print(f"series1.le(series2)  : {series1.le(series2).tolist()}")
