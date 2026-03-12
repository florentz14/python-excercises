# -------------------------------------------------
# File Name: 58_financial_data_generator.py
# Author: Florentino Baez
# Date: 12/03/2026
# Description: Generate synthetic finance transactions with controlled noise.
# -------------------------------------------------

from pathlib import Path

import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "data"
RAW_OUTPUT = DATA_DIR / "financial_transactions_raw.csv"


def main() -> None:
    np.random.seed(42)
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    n_rows = 2500
    start = pd.Timestamp("2025-01-01")
    dates = start + pd.to_timedelta(np.random.randint(0, 365, n_rows), unit="D")

    categories = np.random.choice(
        ["Housing", "Food", "Transport", "Leisure", "Health", "Utilities", "Education"],
        size=n_rows,
        p=[0.20, 0.26, 0.15, 0.14, 0.08, 0.12, 0.05],
    )

    # Category-based amount distributions
    base_ranges = {
        "Housing": (600, 2200),
        "Food": (8, 180),
        "Transport": (5, 140),
        "Leisure": (10, 220),
        "Health": (15, 420),
        "Utilities": (25, 320),
        "Education": (20, 650),
    }

    amounts = []
    for cat in categories:
        low, high = base_ranges[cat]
        amounts.append(round(float(np.random.uniform(low, high)), 2))

    df = pd.DataFrame(
        {
            "transaction_id": [f"TX-{i+1:06d}" for i in range(n_rows)],
            "date": dates,
            "description": [f"{cat} transaction {i+1}" for i, cat in enumerate(categories)],
            "category": categories,
            "amount": amounts,
            "payment_method": np.random.choice(
                ["Card", "Cash", "Transfer", "Digital Wallet"],
                size=n_rows,
                p=[0.56, 0.11, 0.24, 0.09],
            ),
            "account": np.random.choice(["Checking", "Savings", "Credit"], size=n_rows, p=[0.48, 0.22, 0.30]),
            "is_recurring": np.random.choice([True, False], size=n_rows, p=[0.30, 0.70]),
        }
    )

    # Introduce realistic noise for cleaning exercises
    neg_idx = np.random.choice(df.index, size=80, replace=False)
    df.loc[neg_idx, "amount"] = -df.loc[neg_idx, "amount"]  # sign errors

    outlier_idx = np.random.choice(df.index.difference(neg_idx), size=45, replace=False)
    df.loc[outlier_idx, "amount"] = df.loc[outlier_idx, "amount"] * np.random.uniform(6, 15, size=len(outlier_idx))

    null_amount_idx = np.random.choice(df.index, size=120, replace=False)
    null_cat_idx = np.random.choice(df.index, size=95, replace=False)
    null_pay_idx = np.random.choice(df.index, size=70, replace=False)
    df.loc[null_amount_idx, "amount"] = np.nan
    df.loc[null_cat_idx, "category"] = np.nan
    df.loc[null_pay_idx, "payment_method"] = np.nan

    # Inconsistent category labels
    food_idx = df[df["category"] == "Food"].sample(60, random_state=7).index
    df.loc[food_idx[:20], "category"] = "food"
    df.loc[food_idx[20:40], "category"] = "FOOD"
    df.loc[food_idx[40:], "category"] = "Food "

    # Mixed date formats for a subset
    text_date_idx = np.random.choice(df.index, size=150, replace=False)
    df.loc[text_date_idx[:50], "date"] = pd.to_datetime(df.loc[text_date_idx[:50], "date"]).dt.strftime("%m/%d/%Y")
    df.loc[text_date_idx[50:100], "date"] = pd.to_datetime(df.loc[text_date_idx[50:100], "date"]).dt.strftime("%Y/%m/%d")
    df.loc[text_date_idx[100:], "date"] = pd.to_datetime(df.loc[text_date_idx[100:], "date"]).dt.strftime("%d-%m-%Y")

    # Duplicate rows
    duplicates = df.sample(25, random_state=24)
    df_raw = pd.concat([df, duplicates], ignore_index=True)

    df_raw.to_csv(RAW_OUTPUT, index=False)

    print("=" * 68)
    print("           FINANCIAL DATA GENERATOR COMPLETED")
    print("=" * 68)
    print(f"Rows generated (with duplicates): {len(df_raw)}")
    print(f"Unique transaction_id count      : {df_raw['transaction_id'].nunique()}")
    print(f"Output file                      : {RAW_OUTPUT}")


if __name__ == "__main__":
    main()
