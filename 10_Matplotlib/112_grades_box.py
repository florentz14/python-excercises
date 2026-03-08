# -------------------------------------------------
# File Name: 112_grades_box.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Box plot of grade distribution.
# -------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd


def grades_box(grades_series: pd.Series):
    """Receives Pandas Series of grades. Returns box plot."""
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.boxplot(grades_series.dropna(), vert=True, patch_artist=True)
    ax.set_title("Grade Distribution", fontsize=14, fontweight="bold")
    ax.set_ylabel("Grade")
    ax.set_xticklabels(["Grades"])
    plt.tight_layout()
    return fig


if __name__ == "__main__":
    grades = pd.Series([5.5, 6.0, 7.0, 7.5, 8.0, 8.5, 9.0, 6.5, 7.2, 8.8])
    fig = grades_box(grades)
    plt.show()
