import pandas as pd


series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print("Distribution shape:")
print(f"Skewness : {series.skew():.6f}")
print(f"Kurtosis : {series.kurt():.6f}")
print()
print("describe() summary:")
print(series.describe())
