from pathlib import Path

import pandas as pd


csv_path = Path(__file__).parent.parent / "data" / "chipotle_orders.csv"
df = pd.read_csv(csv_path)
df["item_price"] = df["item_price"].str.replace("$", "", regex=False).astype(float)

print("Rows where quantity > 1:")
print(df[df["quantity"] > 1])
