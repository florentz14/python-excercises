# -------------------------------------------------
# File Name: 76_chunk_processing.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: read_csv with chunksize for large file processing.
# -------------------------------------------------

import pandas as pd
from pathlib import Path

DATA = Path(__file__).parent.parent / "data"
csv_path = DATA / "chipotle_orders.csv"

# Read in chunks
chunk_size = 100
chunks = []
for chunk in pd.read_csv(csv_path, chunksize=chunk_size):
    # Process each chunk (e.g. filter, agg)
    chunk["item_price_float"] = chunk["item_price"].str.replace("$", "", regex=False).astype(float)
    total = chunk["quantity"] * chunk["item_price_float"]
    chunks.append({"rows": len(chunk), "revenue": total.sum()})

# Aggregate chunk results
df_chunks = pd.DataFrame(chunks)
print("=== CHUNK PROCESSING (chunksize=100) ===")
print(df_chunks)
print()
print(f"Total rows processed: {df_chunks['rows'].sum()}")
print(f"Total revenue: ${df_chunks['revenue'].sum():.2f}")
print()

# Alternative: iterator + get_chunk
reader = pd.read_csv(csv_path, chunksize=50)
chunk1 = reader.get_chunk()
print("=== First chunk (50 rows) ===")
print(chunk1.shape)
print(chunk1.head(3))
