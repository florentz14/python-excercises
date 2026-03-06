# ------------------------------------------------------------
# File: 40_sales_analysis.py
# Purpose: Store sales analyzer - business questions from CSV.
# Description: read_csv, filter, groupby, sum/mean/count, sort.
# ------------------------------------------------------------

"""
Store Sales Analyzer
Answers: best-selling product, highest revenue month, top customer
"""

import pandas as pd
from pathlib import Path

CSV_PATH = Path(__file__).parent / "data" / "store_sales.csv"


def load_and_explore():
    """Load CSV and show basic info."""
    df = pd.read_csv(CSV_PATH)
    df["date"] = pd.to_datetime(df["date"])
    df["revenue"] = df["quantity"] * df["unit_price"]
    print("[1] Load & Explore")
    print("-" * 50)
    print(f"Rows: {len(df)}, Columns: {len(df.columns)}")
    print(f"Columns: {list(df.columns)}")
    print(f"\nDate range: {df['date'].min()} to {df['date'].max()}")
    return df


def analyze(df):
    """Answer business questions."""
    print("\n[2] Business Questions")
    print("=" * 50)

    # Best-selling product (by quantity)
    by_product = df.groupby("product")["quantity"].sum().sort_values(ascending=False)
    print("\nTop product by quantity sold:")
    print(by_product.head(3).to_string())

    # Highest revenue month
    df["month"] = df["date"].dt.to_period("M")
    monthly = df.groupby("month")["revenue"].sum()
    best_month = monthly.idxmax()
    print(f"\nBest revenue month: {best_month} (${monthly[best_month]:,.2f})")

    # Top customer by revenue
    by_customer = df.groupby("customer_id")["revenue"].sum().sort_values(ascending=False)
    print("\nTop 3 customers by revenue:")
    print(by_customer.head(3).to_string())

    # Revenue by category
    print("\nRevenue by category:")
    print(df.groupby("category")["revenue"].sum().sort_values(ascending=False).to_string())


def main():
    df = load_and_explore()
    analyze(df)


if __name__ == "__main__":
    main()
