# -------------------------------------------------
# File Name: 50_personal_budget.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Spending by category, monthly savings, budget balance analysis.
# -------------------------------------------------

"""
Personal Budget Analyzer
Answers: where do I spend most, which month spent most, monthly savings
"""

import pandas as pd
from pathlib import Path

CSV_PATH = Path(__file__).parent.parent / "data" / "personal_budget.csv"


def main():
    df = pd.read_csv(CSV_PATH)
    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M")

    print("[1] Load & Explore")
    print("-" * 50)
    print(f"Transactions: {len(df)}")

    # Where do you spend most (by category)
    expenses = df[df["type"] == "expense"]
    by_cat_df = pd.DataFrame(
        expenses.groupby("category", as_index=False).agg(amount_sum=("amount", "sum"))
    )
    by_cat_df["amount_abs"] = by_cat_df["amount_sum"].apply(lambda value: abs(float(value)))
    by_cat_rows = sorted(
        by_cat_df.itertuples(index=False),
        key=lambda row: float(row[2]),
        reverse=True,
    )
    by_cat = pd.DataFrame(by_cat_rows, columns=["category", "amount_sum", "amount_abs"])
    print("\n[2] Spending by category (total):")
    print(by_cat[["category", "amount_abs"]].set_index("category").to_string())

    # Which month spent most
    monthly_exp = pd.DataFrame(
        expenses.groupby("month", as_index=False).agg(amount_sum=("amount", "sum"))
    )
    monthly_exp["amount_abs"] = monthly_exp["amount_sum"].apply(lambda value: abs(float(value)))
    worst_month_row = max(
        monthly_exp.itertuples(index=False),
        key=lambda row: float(row[2]),
    )
    print(f"\n[3] Month with highest spending: {worst_month_row[0]} (${float(worst_month_row[2]):,.2f})")

    # Monthly savings
    income_df = pd.DataFrame(
        df[df["type"] == "income"].groupby("month", as_index=False).agg(
            income_amount=("amount", "sum")
        )
    )
    expense_df = pd.DataFrame(
        expenses.groupby("month", as_index=False).agg(
            expense_amount=("amount", "sum")
        )
    )
    monthly_mix = pd.merge(income_df, expense_df, on="month", how="outer").fillna(0.0)
    monthly_mix["expense_abs"] = monthly_mix["expense_amount"].apply(lambda value: abs(float(value)))
    monthly_mix["savings"] = monthly_mix["income_amount"] - monthly_mix["expense_abs"]
    print("\n[4] Monthly savings:")
    for row in monthly_mix.itertuples(index=False):
        print(f"  {row[0]}: ${float(row[4]):,.2f}")

    # Total balance
    total_inc = df[df["type"] == "income"]["amount"].sum()
    total_exp = df[df["type"] == "expense"]["amount"].sum()
    print(f"\n[5] Total income: ${total_inc:,.2f}")
    print(f"    Total expenses: ${abs(total_exp):,.2f}")
    print(f"    Net balance: ${total_inc + total_exp:,.2f}")


if __name__ == "__main__":
    main()
