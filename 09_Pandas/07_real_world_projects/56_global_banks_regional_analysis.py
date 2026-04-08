# -------------------------------------------------
# File Name: 56_global_banks_regional_analysis.py
# Author: Florentino Baez
# Date: 09_Pandas
# Description: Regional and country analysis for global banks.
# -------------------------------------------------

from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "data"
CSV_PATH = DATA_DIR / "bancos.csv"
EXPORTS_DIR = DATA_DIR / "exports"


def load_data() -> pd.DataFrame:
    """Load banks dataset and ensure numeric types are ready for analysis."""
    df = pd.read_csv(CSV_PATH)
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    numeric_cols = ["Apertura", "Maximo", "Minimo", "Cierre", "Volumen"]

    # Normalize column names because source uses accents.
    if "Máximo" in df.columns:
        df = df.rename(columns={"Máximo": "Maximo", "Mínimo": "Minimo"})

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def main() -> None:
    df = load_data()
    EXPORTS_DIR.mkdir(parents=True, exist_ok=True)

    ranking_by_region = pd.DataFrame(
        df.groupby(["Region", "Empresa"], as_index=False).agg(
            avg_close=("Cierre", "mean"),
            total_volume=("Volumen", "sum"),
            records=("Date", "count"),
        )
    )
    ranking_rows = sorted(
        ranking_by_region.itertuples(index=False),
        key=lambda row: (str(row[0]), -float(row[2]), -float(row[3])),
    )
    ranking_by_region = pd.DataFrame(
        ranking_rows, columns=["Region", "Empresa", "avg_close", "total_volume", "records"]
    )

    volume_by_country = pd.DataFrame(
        df.groupby("Pais", as_index=False).agg(
            total_volume=("Volumen", "sum"),
            avg_close=("Cierre", "mean"),
            banks=("Empresa", "nunique"),
        )
    )
    country_rows = sorted(
        volume_by_country.itertuples(index=False),
        key=lambda row: float(row[1]),
        reverse=True,
    )
    volume_by_country = pd.DataFrame(
        country_rows, columns=["Pais", "total_volume", "avg_close", "banks"]
    )

    leader_by_region = (
        ranking_by_region.sort_values(["Region", "avg_close", "total_volume"], ascending=[True, False, False])
        .groupby("Region", as_index=False)
        .first()
    )

    print("=" * 70)
    print("            GLOBAL BANKS ANALYSIS BY REGION")
    print("=" * 70)
    print(f"Rows: {len(df)} | Banks: {df['Empresa'].nunique()} | Countries: {df['Pais'].nunique()}")

    print("\n--- TOP BANKS BY REGION (avg close) ---")
    for region, group in ranking_by_region.groupby("Region"):
        print(f"\n{region}:")
        print(group.head(5).to_string(index=False))

    print("\n--- TOTAL VOLUME BY COUNTRY ---")
    print(volume_by_country.to_string(index=False))

    print("\n--- LEADER BANK PER REGION ---")
    print(leader_by_region[["Region", "Empresa", "avg_close", "total_volume"]].to_string(index=False))

    ranking_path = EXPORTS_DIR / "banks_ranking_by_region.csv"
    country_path = EXPORTS_DIR / "banks_volume_by_country.csv"
    leaders_path = EXPORTS_DIR / "banks_leader_by_region.csv"

    ranking_by_region.to_csv(ranking_path, index=False)
    volume_by_country.to_csv(country_path, index=False)
    leader_by_region.to_csv(leaders_path, index=False)

    print("\n--- EXPORTED FILES ---")
    print(f"- {ranking_path}")
    print(f"- {country_path}")
    print(f"- {leaders_path}")


if __name__ == "__main__":
    main()
