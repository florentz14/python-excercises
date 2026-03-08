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

CSV_PATH = Path(__file__).parent / "data" / "personal_budget.csv"


def main():
    df = pd.read_csv(CSV_PATH)
    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M")

    print("[1] Load & Explore")
    print("-" * 50)
    print(f"Transactions: {len(df)}")

    # Where do you spend most (by category)
    expenses = df[df["type"] == "expense"]
    by_cat = expenses.groupby("category")["amount"].sum().abs().sort_values(ascending=False)
    print("\n[2] Spending by category (total):")
    print(by_cat.to_string())

    # Which month spent most
    monthly_exp = expenses.groupby("month")["amount"].sum().abs()
    worst_month = monthly_exp.idxmax()
    print(f"\n[3] Month with highest spending: {worst_month} (${monthly_exp[worst_month]:,.2f})")

    # Monthly savings
    income = df[df["type"] == "income"].groupby("month")["amount"].sum()
    monthly_exp = expenses.groupby("month")["amount"].sum().abs()
    savings = income - monthly_exp
    print("\n[4] Monthly savings:")
    for m in savings.index:
        print(f"  {m}: ${savings[m]:,.2f}")

    # Total balance
    total_inc = df[df["type"] == "income"]["amount"].sum()
    total_exp = df[df["type"] == "expense"]["amount"].sum()
    print(f"\n[5] Total income: ${total_inc:,.2f}")
    print(f"    Total expenses: ${abs(total_exp):,.2f}")
    print(f"    Net balance: ${total_inc + total_exp:,.2f}")


if __name__ == "__main__":
    main()
