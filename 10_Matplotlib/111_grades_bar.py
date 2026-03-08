# -------------------------------------------------
# File Name: 111_grades_bar.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Bar chart of subject grades in given color.
# -------------------------------------------------

import matplotlib.pyplot as plt


def grades_bar(grades_dict: dict, color: str):
    """Receives dict {subject: grade} and color. Returns bar chart."""
    fig, ax = plt.subplots(figsize=(8, 5))
    subjects = list(grades_dict.keys())
    grades = list(grades_dict.values())
    ax.bar(subjects, grades, color=color, edgecolor="black", linewidth=0.8)
    ax.set_title("Grades by Subject", fontsize=14, fontweight="bold")
    ax.set_xlabel("Subject")
    ax.set_ylabel("Grade")
    ax.set_ylim(0, 10)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    return fig


if __name__ == "__main__":
    grades = {"Math": 7.5, "Physics": 8.0, "Chemistry": 6.5, "English": 9.0}
    fig = grades_bar(grades, "steelblue")
    plt.show()
