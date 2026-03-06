# ------------------------------------------------------------
# File: 45_construction_materials.py
# Purpose: Construction materials - consumption, cost, waste, budget vs actual.
# Description: Consumption per project, cost per stage, waste, budget variance.
# ------------------------------------------------------------

"""
Construction Materials Analyzer
Answers: project with most sheetrock, material with most waste, stage over budget
"""

import pandas as pd
from pathlib import Path

CSV_PATH = Path(__file__).parent / "data" / "construction_materials.csv"


def main():
    df = pd.read_csv(CSV_PATH)
    df["date"] = pd.to_datetime(df["date"])
    df["planned_cost"] = df["quantity_planned"] * df["unit_cost"]
    df["actual_cost"] = df["quantity_used"] * df["unit_cost"]
    df["waste"] = df["quantity_used"] - df["quantity_planned"]
    df["budget_variance"] = df["actual_cost"] - df["planned_cost"]

    print("[1] Load & Explore")
    print("-" * 50)

    # Project consuming most sheetrock
    sheetrock = df[df["material"] == "sheetrock"]
    by_project = sheetrock.groupby("project")["quantity_used"].sum().sort_values(ascending=False)
    print("\n[2] Sheetrock consumption by project:")
    print(by_project.to_string())

    # Material with most waste (positive = overused)
    waste_by_mat = df.groupby("material")["waste"].sum()
    most_waste = waste_by_mat[waste_by_mat > 0].sort_values(ascending=False)
    print("\n[3] Materials with most waste (over planned):")
    if len(most_waste) > 0:
        print(most_waste.head(5).to_string())
    else:
        print("  None")

    # Stage exceeding budget most
    over_budget = df[df["budget_variance"] > 0]
    if len(over_budget) > 0:
        by_stage = over_budget.groupby("stage")["budget_variance"].sum().sort_values(ascending=False)
        print("\n[4] Stages over budget (total variance):")
        print(by_stage.to_string())

    # Cost by project
    print("\n[5] Total cost by project:")
    cost = df.groupby("project")["actual_cost"].sum().sort_values(ascending=False)
    print(cost.to_string())


if __name__ == "__main__":
    main()
