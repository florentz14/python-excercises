import pandas as pd


series1 = pd.Series([2, 4, 6, 8, 10])
series2 = pd.Series([1, 3, 5, 7, 9])

print("Floor Division (Series1 // Series2):")
print((series1 // series2).to_string())

print("\nModulus (Series1 % Series2):")
print((series1 % series2).to_string())

print("\nPower (Series1 ** Series2):")
print((series1 ** series2).to_string())
