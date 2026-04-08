import pandas as pd


s1 = pd.Series([0, 1], index=["a", "b"])
s2 = pd.Series([2, 3, 4], index=["c", "d", "e"])
concatenated = pd.concat([s1, s2])

print("CONCAT SERIES:")
print(concatenated)
