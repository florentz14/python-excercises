# -------------------------------------------------
# File Name: 94_balance_months.py
# Author: Florentino Báez
# Date: Pandas
# Description: Balance (sales - expenses) total for given months.
# -------------------------------------------------

import pandas as pd


def balance_months(df: pd.DataFrame, months: list) -> float:
    """Receives DataFrame (Month, Sales, Expenses) and month list. Returns total balance."""
    filtered = df[df["Month"].isin(months)]
    return (filtered["Sales"] - filtered["Expenses"]).sum()


if __name__ == "__main__":
    df = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr"],
        "Sales": [30500, 35600, 28300, 33900],
        "Expenses": [22000, 23400, 18100, 20700],
    })
    months = ["Jan", "Mar"]
    total = balance_months(df, months)
    print(f"Total balance for {months}: {total}")
