# -------------------------------------------------
# File Name: 116_banks_line.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Line chart of bank closing prices over time.
# -------------------------------------------------

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def banks_closing_chart(csv_path) -> plt.Figure:
    """Receives bancos.csv path. Creates line chart of closing price per bank."""
    df = pd.read_csv(csv_path)
    df["Date"] = pd.to_datetime(df["Date"])

    fig, ax = plt.subplots(figsize=(10, 6))
    for empresa in df["Empresa"].unique():
        sub = df[df["Empresa"] == empresa].sort_values("Date")
        ax.plot(sub["Date"], sub["Cierre"], marker="o", label=empresa, linewidth=2)

    ax.set_title("Bank Closing Prices", fontsize=14, fontweight="bold")
    ax.set_xlabel("Date")
    ax.set_ylabel("Closing Price")
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig


OUTPUT = Path(__file__).parent / "output"


if __name__ == "__main__":
    path = Path(__file__).parent.parent / "09_Pandas" / "data" / "bancos.csv"
    fig = banks_closing_chart(path)
    OUTPUT.mkdir(exist_ok=True)
    out = OUTPUT / "bancos_closing.png"
    fig.savefig(out, dpi=100, bbox_inches="tight")
    plt.close()
    print(f"Saved: {out}")
