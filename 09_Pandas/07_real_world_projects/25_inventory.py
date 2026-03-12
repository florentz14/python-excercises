# -------------------------------------------------
# File Name: 51_inventory.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Reorder alerts, turnover, unsold products from inventory data.
# -------------------------------------------------

"""
Inventory Dashboard
Answers: products needing reorder, fastest-moving category, products not sold
"""

import pandas as pd
from pathlib import Path

MOVEMENTS_PATH = Path(__file__).parent.parent / "data" / "inventory_movements.csv"
STOCK_PATH = Path(__file__).parent.parent / "data" / "inventory_stock.csv"


def main():
    moves = pd.read_csv(MOVEMENTS_PATH)
    stock = pd.read_csv(STOCK_PATH)
    moves["date"] = pd.to_datetime(moves["date"])

    # Compute net stock change per product
    moves["qty_signed"] = moves["quantity"] * moves["movement_type"].map({"in": 1, "out": -1})
    net = moves.groupby("product_id")["qty_signed"].sum()

    # Current stock = initial + net
    stock = stock.merge(net.rename("net_change"), on="product_id", how="left")
    stock["net_change"] = stock["net_change"].fillna(0)
    stock["current_stock"] = stock["initial_stock"] + stock["net_change"].astype(int)

    print("[1] Products needing reorder (below min_stock):")
    print("-" * 50)
    low = stock[stock["current_stock"] < stock["min_stock"]]
    if len(low) > 0:
        print(low[["product_name", "current_stock", "min_stock"]].to_string(index=False))
    else:
        print("  None")

    # Most moved (out) by quantity
    outs = moves[moves["movement_type"] == "out"]
    by_product = outs.groupby("product_name")["quantity"].sum().sort_values(ascending=False)
    print("\n[2] Most sold products (by quantity):")
    print(by_product.head(5).to_string())

    # Category with most movement
    by_cat = outs.groupby("category")["quantity"].sum().sort_values(ascending=False)
    print("\n[3] Fastest-moving category:")
    print(by_cat.to_string())

    # Products with no out movements (not sold)
    sold_ids = outs["product_id"].unique()
    not_sold = stock[~stock["product_id"].isin(sold_ids)]
    print("\n[4] Products with no sales:")
    if len(not_sold) > 0:
        print(not_sold[["product_name", "current_stock"]].to_string(index=False))
    else:
        print("  None")


if __name__ == "__main__":
    main()
