# -------------------------------------------------
# File Name: 113_sales_pie.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Pie chart of quarterly sales saved as PNG.
# -------------------------------------------------

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

OUTPUT = Path(__file__).parent / "output"


def sales_pie(sales_series: pd.Series, title: str) -> str:
    """Receives Series with sales per month (quarter) and title. Saves pie as PNG. Returns filename."""
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.pie(sales_series.values, labels=sales_series.index, autopct="%1.1f%%", startangle=90)
    ax.set_title(title, fontsize=14, fontweight="bold")
    plt.tight_layout()
    filename = f"{title.replace(' ', '_')}.png"
    OUTPUT.mkdir(exist_ok=True)
    fig.savefig(OUTPUT / filename, dpi=100, bbox_inches="tight")
    plt.close()
    return filename


if __name__ == "__main__":
    sales = pd.Series({"Jan": 120, "Feb": 150, "Mar": 180}, name="Q1")
    fn = sales_pie(sales, "Q1 Sales")
    print(f"Saved: {fn}")
