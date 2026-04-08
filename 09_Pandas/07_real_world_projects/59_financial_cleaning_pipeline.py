# -------------------------------------------------
# File Name: 59_financial_cleaning_pipeline.py
# Author: Florentino Baez
# Date: 12/03/2026
# Description: Clean synthetic financial transactions and export curated outputs.
# -------------------------------------------------

from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "data"
EXPORT_DIR = DATA_DIR / "exports"

RAW_INPUT = DATA_DIR / "financial_transactions_raw.csv"
CLEAN_OUTPUT = DATA_DIR / "financial_transactions_clean.csv"
ANOMALY_OUTPUT = EXPORT_DIR / "financial_anomalies.csv"


def normalize_category(value: str) -> str:
    if pd.isna(value):
        return "Uncategorized"
    normalized = str(value).strip().title()
    mapping = {
        "Food": "Food",
        "Housing": "Housing",
        "Transport": "Transport",
        "Leisure": "Leisure",
        "Health": "Health",
        "Utilities": "Utilities",
        "Education": "Education",
    }
    return mapping.get(normalized, normalized)


def main() -> None:
    if not RAW_INPUT.exists():
        raise FileNotFoundError(
            f"Raw input not found: {RAW_INPUT}. Run 58_financial_data_generator.py first."
        )

    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(RAW_INPUT)

    initial_rows = len(df)

    # Parse mixed date formats
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Normalize categories and handle missing
    df["category"] = df["category"].apply(normalize_category)
    df["payment_method"] = df["payment_method"].fillna("Unknown")

    # Numeric cleanup
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    median_amount = df["amount"].median(skipna=True)
    df["amount"] = df["amount"].fillna(median_amount)
    df["amount"] = df["amount"].abs()

    # Drop invalid dates and duplicates by transaction key
    invalid_date_count = int(pd.Series(df["date"].isna()).sum())
    df = df.dropna(subset=["date"])
    df = df.drop_duplicates(subset=["transaction_id"], keep="first")

    # Create anomaly flags (global threshold + per-category z-score)
    p99 = df["amount"].quantile(0.99)
    std_by_cat = df.groupby("category")["amount"].transform("std").replace(0, pd.NA)
    mean_by_cat = df.groupby("category")["amount"].transform("mean")
    df["z_score"] = ((df["amount"] - mean_by_cat) / std_by_cat).fillna(0.0)
    df["anomaly_flag"] = (df["amount"] > p99) | (df["z_score"].abs() > 3.0)

    # Export cleaned dataset
    df.to_csv(CLEAN_OUTPUT, index=False)

    anomalies = df[df["anomaly_flag"]].copy()
    anomalies.to_csv(ANOMALY_OUTPUT, index=False)

    print("=" * 68)
    print("            FINANCIAL CLEANING PIPELINE COMPLETED")
    print("=" * 68)
    print(f"Input rows                    : {initial_rows}")
    print(f"Dropped invalid dates         : {invalid_date_count}")
    print(f"Clean rows                    : {len(df)}")
    print(f"Unique transaction_id         : {df['transaction_id'].nunique()}")
    print(f"Anomalies flagged             : {len(anomalies)}")
    print(f"Clean output                  : {CLEAN_OUTPUT}")
    print(f"Anomaly output                : {ANOMALY_OUTPUT}")


if __name__ == "__main__":
    main()
