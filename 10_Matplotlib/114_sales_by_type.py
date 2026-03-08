# -------------------------------------------------
# File Name: 114_sales_by_type.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Sales by year: line, bar, pie or area chart.
# -------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd


def sales_chart(sales_series: pd.Series, chart_type: str):
    """Receives Series (sales by year) and chart type. Returns figure."""
    fig, ax = plt.subplots(figsize=(8, 5))
    chart_type = chart_type.lower()

    if chart_type in ("lineas", "lines", "line"):
        ax.plot(sales_series.index, sales_series.values, marker="o", linewidth=2)
    elif chart_type in ("barras", "bars", "bar"):
        ax.bar(sales_series.index, sales_series.values, color="steelblue", edgecolor="black")
    elif chart_type in ("sectores", "pie", "sectors"):
        ax.pie(sales_series.values, labels=sales_series.index, autopct="%1.1f%%", startangle=90)
    elif chart_type in ("areas", "area"):
        ax.fill_between(sales_series.index, sales_series.values, alpha=0.5)
        ax.plot(sales_series.index, sales_series.values, linewidth=2)
    else:
        raise ValueError("chart_type must be: lineas, barras, sectores, areas")

    ax.set_title("Sales Evolution", fontsize=14, fontweight="bold")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sales")
    plt.tight_layout()
    return fig


if __name__ == "__main__":
    sales = pd.Series({2020: 100, 2021: 120, 2022: 115, 2023: 140})
    fig = sales_chart(sales, "lineas")
    plt.show()
