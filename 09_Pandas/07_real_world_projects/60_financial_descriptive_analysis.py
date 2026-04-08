# -------------------------------------------------
# File Name: 60_financial_descriptive_analysis.py
# Author: Florentino Baez
# Date: 12/03/2026
# Description: Build descriptive KPIs from cleaned financial transactions.
# -------------------------------------------------

from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "data"
EXPORT_DIR = DATA_DIR / "exports"

CLEAN_INPUT = DATA_DIR / "financial_transactions_clean.csv"
CATEGORY_OUTPUT = EXPORT_DIR / "financial_summary_by_category.csv"
ACCOUNT_OUTPUT = EXPORT_DIR / "financial_summary_by_account.csv"
RECURRING_OUTPUT = EXPORT_DIR / "financial_summary_recurring_vs_discretionary.csv"
PARETO_OUTPUT = EXPORT_DIR / "financial_pareto_by_category.csv"


def main() -> None:
    if not CLEAN_INPUT.exists():
        raise FileNotFoundError(
            f"Clean input not found: {CLEAN_INPUT}. Run 59_financial_cleaning_pipeline.py first."
        )

    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(CLEAN_INPUT)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df = df.dropna(subset=["amount"])

    amount_series = pd.Series(df["amount"])
    total_spend = float(amount_series.sum())

    category_summary = pd.DataFrame(
        df.groupby("category", as_index=False).agg(
            total_amount=("amount", "sum"),
            avg_amount=("amount", "mean"),
            transactions=("amount", "count"),
        )
    )
    category_rows = sorted(
        category_summary.itertuples(index=False),
        key=lambda row: float(row[1]),
        reverse=True,
    )
    category_summary = pd.DataFrame(
        category_rows, columns=["category", "total_amount", "avg_amount", "transactions"]
    )
    category_summary["pct_of_total"] = (category_summary["total_amount"] / total_spend).round(4)
    category_summary["rank"] = range(1, len(category_summary) + 1)
    category_summary.to_csv(CATEGORY_OUTPUT, index=False)

    pareto = category_summary.copy()
    pareto["cum_total"] = pareto["total_amount"].cumsum()
    pareto["cum_pct"] = (pareto["cum_total"] / total_spend).round(4)
    pareto.to_csv(PARETO_OUTPUT, index=False)

    account_summary = pd.DataFrame(
        df.groupby("account", as_index=False).agg(
            total_amount=("amount", "sum"),
            avg_amount=("amount", "mean"),
            transactions=("amount", "count"),
        )
    )
    account_rows = sorted(
        account_summary.itertuples(index=False),
        key=lambda row: float(row[1]),
        reverse=True,
    )
    account_summary = pd.DataFrame(
        account_rows, columns=["account", "total_amount", "avg_amount", "transactions"]
    )
    account_summary["pct_of_total"] = (account_summary["total_amount"] / total_spend).round(4)
    account_summary.to_csv(ACCOUNT_OUTPUT, index=False)

    recurring_summary = pd.DataFrame(
        df.groupby("is_recurring", as_index=False).agg(
            total_amount=("amount", "sum"),
            avg_amount=("amount", "mean"),
            transactions=("amount", "count"),
        )
    )
    recurring_rows = sorted(
        recurring_summary.itertuples(index=False),
        key=lambda row: float(row[1]),
        reverse=True,
    )
    recurring_summary = pd.DataFrame(
        recurring_rows,
        columns=["is_recurring", "total_amount", "avg_amount", "transactions"],
    )
    recurring_summary["type"] = recurring_summary["is_recurring"].apply(
        lambda value: "Recurring" if bool(value) else "Discretionary"
    )
    recurring_summary["pct_of_total"] = (recurring_summary["total_amount"] / total_spend).round(4)
    recurring_summary = recurring_summary[
        ["type", "is_recurring", "total_amount", "avg_amount", "transactions", "pct_of_total"]
    ]
    recurring_summary.to_csv(RECURRING_OUTPUT, index=False)

    overall_stats = df["amount"].describe(percentiles=[0.25, 0.5, 0.75, 0.95, 0.99]).round(2)

    print("=" * 68)
    print("          FINANCIAL DESCRIPTIVE ANALYSIS COMPLETED")
    print("=" * 68)
    print(f"Rows analyzed                 : {len(df)}")
    print(f"Total spending                : {total_spend:,.2f}")
    print(f"Top category                  : {category_summary.iloc[0]['category']}")
    print(f"Top account                   : {account_summary.iloc[0]['account']}")
    print("\nAmount distribution stats:")
    print(overall_stats.to_string())
    print("\nExported files:")
    print(f"- {CATEGORY_OUTPUT}")
    print(f"- {PARETO_OUTPUT}")
    print(f"- {ACCOUNT_OUTPUT}")
    print(f"- {RECURRING_OUTPUT}")


if __name__ == "__main__":
    main()
