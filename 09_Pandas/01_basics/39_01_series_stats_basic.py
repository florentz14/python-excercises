import pandas as pd


series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print("Series Data:", series.tolist())
print(f"Mean               : {series.mean()}")
print(f"Standard Deviation : {series.std():.6f}")
print(f"Variance           : {series.var():.6f}")
print(f"Median             : {series.median()}")
print(f"Mode               : {series.mode().tolist()}")
print(f"Minimum            : {series.min()}")
print(f"Maximum            : {series.max()}")
print(f"Sum                : {series.sum()}")
print(f"Product            : {series.prod()}")
print(f"Count              : {series.count()}")
print(f"Size               : {series.size}")
