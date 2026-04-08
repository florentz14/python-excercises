import pandas as pd


df = pd.DataFrame({"key": ["A", "B", "C", "A", "B", "C"], "data": range(6)})
group_sum = df.groupby("key")["data"].transform("sum")
df["total_for_key"] = group_sum

print("Transform result:")
print(df)
