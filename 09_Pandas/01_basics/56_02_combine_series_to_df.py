import pandas as pd


s1 = pd.Series([100, 200, "python", 300.12, 400])
s2 = pd.Series([10, 20, "php", 30.12, 40])
df = pd.concat([s1, s2], axis=1)

print("New DataFrame combining two series:")
print(df)
