# -------------------------------------------------
# File Name: 62_financial_anomaly_detection.py
# Author: Florentino Baez
# Date: 12/03/2026
# Description: Detect suspicious transactions using multiple anomaly methods.
# -------------------------------------------------

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "data"
EXPORT_DIR = DATA_DIR / "exports"

CLEAN_INPUT = DATA_DIR / "financial_transactions_clean.csv"
ANOMALY_OUTPUT = EXPORT_DIR / "financial_anomalies_flagged.csv"
ANOMALY_OUTPUT_COMPAT = EXPORT_DIR / "anomalies_flagged.csv"
BOXPLOT_OUTPUT = EXPORT_DIR / "financial_outlier_detection.png"


def main() -> None:
    if not CLEAN_INPUT.exists():
        raise FileNotFoundError(
            f"Clean input not found: {CLEAN_INPUT}. Run 59_financial_cleaning_pipeline.py first."
        )

    EXPORT_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(CLEAN_INPUT)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df = df.dropna(subset=["amount"]).copy()

    p95 = df["amount"].quantile(0.95)
    p99 = df["amount"].quantile(0.99)

    q1 = df["amount"].quantile(0.25)
    q3 = df["amount"].quantile(0.75)
    iqr = q3 - q1
    iqr_upper = q3 + (1.5 * iqr)

    mean_by_cat = df.groupby("category")["amount"].transform("mean")
    std_by_cat = df.groupby("category")["amount"].transform("std").replace(0, pd.NA)
    df["z_score"] = ((df["amount"] - mean_by_cat) / std_by_cat).fillna(0.0)

    df["flag_p95"] = df["amount"] > p95
    df["flag_p99"] = df["amount"] > p99
    df["flag_iqr"] = df["amount"] > iqr_upper
    df["flag_zscore"] = df["z_score"].abs() > 3.0
    df["anomaly_flag"] = df[["flag_p95", "flag_iqr", "flag_zscore"]].any(axis=1)

    anomalies = df[df["anomaly_flag"]].copy()
    anomalies["trigger_count"] = anomalies[["flag_p95", "flag_p99", "flag_iqr", "flag_zscore"]].sum(axis=1)
    anomaly_rows = sorted(
        anomalies.itertuples(index=False),
        key=lambda row: (-int(row[-1]), -float(row[5])),
    )
    anomalies = pd.DataFrame(anomaly_rows, columns=list(anomalies.columns))

    cols = [
        "transaction_id",
        "date",
        "description",
        "category",
        "account",
        "is_recurring",
        "amount",
        "z_score",
        "flag_p95",
        "flag_p99",
        "flag_iqr",
        "flag_zscore",
        "trigger_count",
    ]
    anomalies = anomalies[cols]
    anomalies.to_csv(ANOMALY_OUTPUT, index=False)
    anomalies.to_csv(ANOMALY_OUTPUT_COMPAT, index=False)

    # Category boxplot (top 6 by transaction count)
    top_categories = [str(value) for value in df["category"].value_counts().head(6).index.tolist()]
    plot_df = df[df["category"].isin(top_categories)].copy()
    grouped_data = [plot_df.loc[plot_df["category"] == cat, "amount"].values for cat in top_categories]

    plt.figure(figsize=(11, 5.5))
    plt.boxplot(grouped_data, tick_labels=top_categories, showfliers=True)
    plt.title("Outlier Detection by Category (Boxplot)")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.xticks(rotation=20, ha="right")
    plt.tight_layout()
    plt.savefig(BOXPLOT_OUTPUT, dpi=120)
    plt.close()

    print("=" * 68)
    print("             FINANCIAL ANOMALY DETECTION COMPLETED")
    print("=" * 68)
    print(f"Rows analyzed                 : {len(df)}")
    print(f"P95 threshold                 : {p95:,.2f}")
    print(f"P99 threshold                 : {p99:,.2f}")
    print(f"IQR upper bound               : {iqr_upper:,.2f}")
    print(f"Anomalies flagged             : {len(anomalies)}")
    print("\nExported files:")
    print(f"- {ANOMALY_OUTPUT}")
    print(f"- {ANOMALY_OUTPUT_COMPAT}")
    print(f"- {BOXPLOT_OUTPUT}")


if __name__ == "__main__":
    main()
