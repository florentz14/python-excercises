from pathlib import Path

import pandas as pd


csv_path = Path(__file__).parent.parent / "data" / "chipotle_orders.csv"
df = pd.read_csv(csv_path)
df["item_price"] = df["item_price"].str.replace("$", "", regex=False).astype(float)

print("Filter: item_price > 10")
print(df[df["item_price"] > 10])
print("\nFilter: Chicken Bowl only")
print(df[df["item_name"] == "Chicken Bowl"])
