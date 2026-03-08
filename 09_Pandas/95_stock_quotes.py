# -------------------------------------------------
# File Name: 95_stock_quotes.py
# Author: Florentino Báez
# Date: Pandas
# Description: Stock quotes summary: min, max, mean per column.
# -------------------------------------------------

from pathlib import Path

import pandas as pd


def quote_summary(path) -> pd.DataFrame:
    """Builds DataFrame from file and returns min, max, mean of each numeric column."""
    df = pd.read_csv(path)
    numeric = df.select_dtypes(include="number").columns
    return df[numeric].agg(["min", "max", "mean"])


if __name__ == "__main__":
    path = Path(__file__).parent / "data" / "cotizacion.csv"
    summary = quote_summary(path)
    print("Quote summary (min, max, mean):")
    print(summary)
