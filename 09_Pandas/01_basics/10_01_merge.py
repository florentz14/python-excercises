import pandas as pd


df1 = pd.DataFrame({"id": [1, 2], "name": ["Anna", "Louis"]})
df2 = pd.DataFrame({"id": [1, 2], "city": ["Madrid", "Barcelona"]})

merged = pd.merge(df1, df2, on="id")

print("Merge (inner join):")
print(merged)
