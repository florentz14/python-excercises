import pandas as pd


series1 = pd.Series([2, 4, 6, 8, 10])
series2 = pd.Series([1, 3, 5, 7, 9])

print("Using Pandas built-in methods:")
print(f"series1.add(series2)      : {series1.add(series2).tolist()}")
print(f"series1.sub(series2)      : {series1.sub(series2).tolist()}")
print(f"series1.mul(series2)      : {series1.mul(series2).tolist()}")
print(f"series1.div(series2)      : {[round(x, 2) for x in series1.div(series2).tolist()]}")
print(f"series1.floordiv(series2) : {series1.floordiv(series2).tolist()}")
print(f"series1.mod(series2)      : {series1.mod(series2).tolist()}")
print(f"series1.pow(series2)      : {series1.pow(series2).tolist()}")
