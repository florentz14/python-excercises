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
    movement_sign = {"in": 1, "out": -1}
    moves["qty_signed"] = moves["quantity"] * moves["movement_type"].apply(
        lambda value: movement_sign.get(str(value), 0)
    )
    net = pd.DataFrame(
        moves.groupby("product_id", as_index=False).agg(net_change=("qty_signed", "sum"))
    )

    # Current stock = initial + net
    stock = pd.merge(stock, net, on="product_id", how="left")
    stock["net_change"] = stock["net_change"].fillna(0)
    stock["current_stock"] = stock["initial_stock"] + stock["net_change"].astype(int)

    print("[1] Products needing reorder (below min_stock):")
    print("-" * 50)
    low = stock[stock["current_stock"] < stock["min_stock"]]
    if len(low) > 0:
        low_df = pd.DataFrame(low.loc[:, ["product_name", "current_stock", "min_stock"]])
        print(low_df.to_string(index=False))
    else:
        print("  None")

    # Most moved (out) by quantity
    outs = moves[moves["movement_type"] == "out"]
    by_product = pd.DataFrame(
        outs.groupby("product_name", as_index=False).agg(total_quantity=("quantity", "sum"))
    )
    by_product_rows = sorted(
        by_product.itertuples(index=False),
        key=lambda row: float(row[1]),
        reverse=True,
    )
    by_product = pd.DataFrame(by_product_rows, columns=["product_name", "total_quantity"])
    print("\n[2] Most sold products (by quantity):")
    print(by_product.head(5).set_index("product_name")["total_quantity"].to_string())

    # Category with most movement
    by_cat = pd.DataFrame(
        outs.groupby("category", as_index=False).agg(total_quantity=("quantity", "sum"))
    )
    by_cat_rows = sorted(
        by_cat.itertuples(index=False),
        key=lambda row: float(row[1]),
        reverse=True,
    )
    by_cat = pd.DataFrame(by_cat_rows, columns=["category", "total_quantity"])
    print("\n[3] Fastest-moving category:")
    print(by_cat.set_index("category")["total_quantity"].to_string())

    # Products with no out movements (not sold)
    sold_ids_df = pd.DataFrame(outs.loc[:, ["product_id"]]).drop_duplicates()
    sold_ids = [int(value) for value in sold_ids_df["product_id"]]
    not_sold = stock[~stock["product_id"].apply(lambda value: int(value) in sold_ids)]
    print("\n[4] Products with no sales:")
    if len(not_sold) > 0:
        not_sold_df = pd.DataFrame(not_sold.loc[:, ["product_name", "current_stock"]])
        print(not_sold_df.to_string(index=False))
    else:
        print("  None")


if __name__ == "__main__":
    main()
