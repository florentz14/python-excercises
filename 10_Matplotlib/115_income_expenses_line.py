# -------------------------------------------------
# File Name: 115_income_expenses_line.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Line chart of income and expenses by month.
# -------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd


def income_expenses_chart(df: pd.DataFrame):
    """Receives DataFrame with income and expenses by month. Returns line chart."""
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(df.index, df["income"], marker="o", label="Income", linewidth=2)
    ax.plot(df.index, df["expenses"], marker="s", label="Expenses", linewidth=2)
    ax.set_title("Income and Expenses Evolution", fontsize=14, fontweight="bold")
    ax.set_xlabel("Month")
    ax.set_ylabel("Amount")
    ax.legend()
    ax.set_ylim(bottom=0)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    return fig


if __name__ == "__main__":
    df = pd.DataFrame({
        "income": [30000, 32000, 28000, 35000, 33000],
        "expenses": [22000, 24000, 21000, 25000, 23000],
    }, index=["Jan", "Feb", "Mar", "Apr", "May"])
    fig = income_expenses_chart(df)
    plt.show()
