import pandas as pd


df = pd.DataFrame({"item": ["ball", "pencil", "pencil", "ashtray"], "status": [1, 1, 1, 2]})
prices = {"ball": 10, "pencil": 5, "ashtray": 20}
df["price"] = df["item"].apply(lambda item: prices.get(item))
df["status"] = df["status"].replace({1: "active", 2: "old"})
df = df.rename(index={0: "first", 1: "second"})

print("Replace values and rename index:")
print(df)
