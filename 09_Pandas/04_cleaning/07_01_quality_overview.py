from pathlib import Path

import pandas as pd


data_dir = Path(__file__).parent.parent / "data"
df = pd.read_csv(data_dir / "store_sales.csv")

print("Data quality overview:")
print(f"Rows: {len(df)}, Columns: {len(df.columns)}")
print("\nDtypes:")
print(df.dtypes)
