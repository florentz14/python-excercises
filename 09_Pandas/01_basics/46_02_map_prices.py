import pandas as pd


df = pd.DataFrame({"item": ["ball", "pencil", "pencil", "ashtray"], "status": [1, 1, 1, 2]})
prices = {"ball": 10, "pencil": 5, "ashtray": 20}
df["price"] = df["item"].apply(lambda item: prices.get(item))

print("Map prices into new column:")
print(df)
