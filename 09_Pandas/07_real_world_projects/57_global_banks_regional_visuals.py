# -------------------------------------------------
# File Name: 57_global_banks_regional_visuals.py
# Author: Florentino Baez
# Date: 12/03/2026
# Description: Visual dashboards for global banks by region and country.
# -------------------------------------------------

# Import pathlib library
from pathlib import Path

# Import matplotlib and pandas libraries
import matplotlib.pyplot as plt
import pandas as pd

# Define the base directory and the data directory
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "data"
CSV_PATH = DATA_DIR / "bancos.csv"
# Define the exports directory
EXPORTS_DIR = DATA_DIR / "exports"


def load_data() -> pd.DataFrame:
    """Load banks CSV with normalized numeric columns."""
    df = pd.read_csv(CSV_PATH)
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    if "Máximo" in df.columns:
        df = df.rename(columns={"Máximo": "Maximo", "Mínimo": "Minimo"})
    for col in ["Apertura", "Maximo", "Minimo", "Cierre", "Volumen"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def main() -> None:
    EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
    df = load_data()

    volume_region = (
        df.groupby("Region", as_index=False)["Volumen"]
        .sum()
        .sort_values("Volumen", ascending=False)
    )
    volume_country = (
        df.groupby("Pais", as_index=False)["Volumen"]
        .sum()
        .sort_values("Volumen", ascending=False)
        .head(10)
    )
    top_banks = (
        df.groupby("Empresa", as_index=False)
        .agg(avg_close=("Cierre", "mean"), total_volume=("Volumen", "sum"))
        .sort_values(["avg_close", "total_volume"], ascending=[False, False])
        .head(10)
    )

    region_plot = EXPORTS_DIR / "banks_volume_by_region.png"
    country_plot = EXPORTS_DIR / "banks_top10_countries_volume.png"
    banks_plot = EXPORTS_DIR / "banks_top10_avg_close.png"

    # Chart 1: total volume by region
    plt.figure(figsize=(8.5, 4.8))
    plt.bar(volume_region["Region"], volume_region["Volumen"], color="#4C78A8")
    plt.title("Total Trading Volume by Region")
    plt.xlabel("Region")
    plt.ylabel("Volume")
    plt.xticks(rotation=20, ha="right")
    plt.tight_layout()
    plt.savefig(region_plot, dpi=120)
    plt.close()

    # Chart 2: top 10 countries by volume
    plt.figure(figsize=(9.5, 5.2))
    plt.barh(volume_country["Pais"], volume_country["Volumen"], color="#72B7B2")
    plt.title("Top 10 Countries by Total Trading Volume")
    plt.xlabel("Volume")
    plt.ylabel("Country")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(country_plot, dpi=120)
    plt.close()

    # Chart 3: top 10 banks by average close
    plt.figure(figsize=(10, 5.5))
    plt.bar(top_banks["Empresa"], top_banks["avg_close"], color="#F58518")
    plt.title("Top 10 Banks by Average Close Price")
    plt.xlabel("Bank")
    plt.ylabel("Average Close")
    plt.xticks(rotation=35, ha="right")
    plt.tight_layout()
    plt.savefig(banks_plot, dpi=120)
    plt.close()

    print("=" * 68)
    print("              GLOBAL BANKS REGIONAL VISUALS")
    print("=" * 68)
    print(f"Rows: {len(df)} | Banks: {df['Empresa'].nunique()} | Regions: {df['Region'].nunique()}")
    print("\nGenerated charts:")
    print(f"- {region_plot}")
    print(f"- {country_plot}")
    print(f"- {banks_plot}")


if __name__ == "__main__":
    main()
