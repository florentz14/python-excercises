# -------------------------------------------------
# File Name: 61_financial_time_series_analysis.py
# Author: Florentino Baez
# Date: 12/03/2026
# Description: Time-series KPIs and charts for cleaned finance transactions.
# -------------------------------------------------

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "data"
EXPORT_DIR = DATA_DIR / "exports"

CLEAN_INPUT = DATA_DIR / "financial_transactions_clean.csv"
MONTHLY_OUTPUT = EXPORT_DIR / "financial_monthly_totals.csv"
WEEKDAY_OUTPUT = EXPORT_DIR / "financial_weekday_totals.csv"
MOM_OUTPUT = EXPORT_DIR / "financial_mom_growth.csv"
CAT_MONTHLY_OUTPUT = EXPORT_DIR / "financial_category_monthly_trend.csv"

MONTHLY_PLOT = EXPORT_DIR / "financial_monthly_totals.png"
DAILY_ROLLING_PLOT = EXPORT_DIR / "financial_daily_rolling4w.png"


def main() -> None:
    if not CLEAN_INPUT.exists():
        raise FileNotFoundError(
            f"Clean input not found: {CLEAN_INPUT}. Run 59_financial_cleaning_pipeline.py first."
        )

    EXPORT_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(CLEAN_INPUT)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df = df.dropna(subset=["date", "amount"]).copy()

    df["month"] = df["date"].dt.to_period("M").astype(str)
    df["weekday"] = df["date"].dt.day_name()
    df["week"] = df["date"].dt.isocalendar().week.astype(int)
    df["quarter"] = df["date"].dt.quarter

    monthly = (
        df.groupby("month", as_index=False)["amount"]
        .sum()
        .rename(columns={"amount": "total_amount"})
        .sort_values("month")
    )
    monthly["mom_growth_pct"] = monthly["total_amount"].pct_change().mul(100).round(2)
    monthly.to_csv(MONTHLY_OUTPUT, index=False)

    weekday_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekday = (
        df.groupby("weekday", as_index=False)["amount"]
        .sum()
        .rename(columns={"amount": "total_amount"})
    )
    weekday["weekday"] = pd.Categorical(weekday["weekday"], categories=weekday_order, ordered=True)
    weekday = weekday.sort_values("weekday")
    weekday.to_csv(WEEKDAY_OUTPUT, index=False)

    mom = monthly[["month", "total_amount", "mom_growth_pct"]].copy()
    mom.to_csv(MOM_OUTPUT, index=False)

    cat_monthly = (
        df.groupby(["month", "category"], as_index=False)["amount"]
        .sum()
        .rename(columns={"amount": "total_amount"})
        .sort_values(["month", "total_amount"], ascending=[True, False])
    )
    cat_monthly.to_csv(CAT_MONTHLY_OUTPUT, index=False)

    daily = (
        df.groupby("date", as_index=False)["amount"]
        .sum()
        .rename(columns={"amount": "total_amount"})
        .sort_values("date")
    )
    daily["rolling_4w_avg"] = daily["total_amount"].rolling(window=28, min_periods=7).mean()

    # Monthly totals chart
    plt.figure(figsize=(10, 5))
    plt.plot(monthly["month"], monthly["total_amount"], marker="o", color="#4C78A8")
    plt.title("Monthly Total Spending")
    plt.xlabel("Month")
    plt.ylabel("Total Amount")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(MONTHLY_PLOT, dpi=120)
    plt.close()

    # Daily trend vs rolling 4-week average
    plt.figure(figsize=(11, 5.5))
    plt.plot(daily["date"], daily["total_amount"], alpha=0.35, label="Daily total", color="#72B7B2")
    plt.plot(daily["date"], daily["rolling_4w_avg"], linewidth=2.2, label="Rolling 4-week average", color="#F58518")
    plt.title("Daily Spending and Rolling 4-Week Average")
    plt.xlabel("Date")
    plt.ylabel("Total Amount")
    plt.legend()
    plt.tight_layout()
    plt.savefig(DAILY_ROLLING_PLOT, dpi=120)
    plt.close()

    print("=" * 68)
    print("          FINANCIAL TIME-SERIES ANALYSIS COMPLETED")
    print("=" * 68)
    print(f"Rows analyzed                 : {len(df)}")
    print(f"Date range                    : {df['date'].min().date()} to {df['date'].max().date()}")
    print(f"Months covered                : {df['month'].nunique()}")
    print("\nExported tables:")
    print(f"- {MONTHLY_OUTPUT}")
    print(f"- {WEEKDAY_OUTPUT}")
    print(f"- {MOM_OUTPUT}")
    print(f"- {CAT_MONTHLY_OUTPUT}")
    print("\nExported charts:")
    print(f"- {MONTHLY_PLOT}")
    print(f"- {DAILY_ROLLING_PLOT}")


if __name__ == "__main__":
    main()
