# -------------------------------------------------
# File Name: 87_customer_segmentation.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: RFM analysis for customer segmentation.
# -------------------------------------------------

from pathlib import Path

import pandas as pd

DATA = Path(__file__).parent / "data"
df = pd.read_csv(DATA / "store_sales.csv", parse_dates=["date"])

# RFM per customer
df["revenue"] = df["quantity"] * df["unit_price"]
max_date = df["date"].max()

rfm = df.groupby("customer_id").agg(
    recency=("date", lambda x: (max_date - x.max()).days),
    frequency=("date", "count"),
    monetary=("revenue", "sum"),
).reset_index()

print("=== RFM AGGREGATION ===")
print(rfm.head(10))
print()

# Quartiles (1=low, 4=high) — for Recency lower is better, so invert
rfm["R_score"] = pd.qcut(rfm["recency"], 4, labels=[4, 3, 2, 1])
rfm["F_score"] = pd.qcut(rfm["frequency"].rank(method="first"), 4, labels=[1, 2, 3, 4])
rfm["M_score"] = pd.qcut(rfm["monetary"], 4, labels=[1, 2, 3, 4])

rfm["RFM"] = rfm["R_score"].astype(str) + rfm["F_score"].astype(str) + rfm["M_score"].astype(str)
print("=== RFM SCORES ===")
print(rfm.head(10))
print()

# Top customers (high F, M)
top = rfm[(rfm["F_score"] == 4) & (rfm["M_score"] == 4)]
print("=== TOP CUSTOMERS (F=4, M=4) ===")
print(top[["customer_id", "recency", "frequency", "monetary"]])
