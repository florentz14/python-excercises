import pandas as pd


series1 = pd.Series([2, 4, 6, 8, 10])
series2 = pd.Series([1, 3, 5, 7, 9])

print("Series 1:", series1.tolist())
print("Series 2:", series2.tolist())

print("\nAddition (Series1 + Series2):")
print((series1 + series2).to_string())

print("\nSubtraction (Series1 - Series2):")
print((series1 - series2).to_string())

print("\nMultiplication (Series1 * Series2):")
print((series1 * series2).to_string())

print("\nDivision (Series1 / Series2):")
print((series1 / series2).to_string())
