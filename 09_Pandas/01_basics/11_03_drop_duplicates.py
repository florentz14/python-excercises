import pandas as pd


df_dup = pd.DataFrame({"x": [1, 1, 2, 2], "y": [3, 3, 4, 5]})
df_unique = df_dup.drop_duplicates()

print("Without duplicates:")
print(df_unique)
