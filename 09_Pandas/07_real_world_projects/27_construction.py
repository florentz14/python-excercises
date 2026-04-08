# -------------------------------------------------
# File Name: 53_construction.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Consumption, waste, budget variance for construction materials.
# -------------------------------------------------

"""
Construction Materials Analyzer
Answers: project with most sheetrock, material with most waste, stage over budget
"""

import pandas as pd
from pathlib import Path

CSV_PATH = Path(__file__).parent.parent / "data" / "construction_materials.csv"


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
    by_project = pd.DataFrame(
        sheetrock.groupby("project", as_index=False).agg(quantity_used_sum=("quantity_used", "sum"))
    )
    by_project_rows = sorted(
        by_project.itertuples(index=False),
        key=lambda row: float(row[1]),
        reverse=True,
    )
    by_project = pd.DataFrame(by_project_rows, columns=["project", "quantity_used_sum"])
    print("\n[2] Sheetrock consumption by project:")
    print(by_project.set_index("project")["quantity_used_sum"].to_string())

    # Material with most waste (positive = overused)
    waste_by_mat = pd.DataFrame(
        df.groupby("material", as_index=False).agg(waste_sum=("waste", "sum"))
    )
    waste_by_mat = waste_by_mat[waste_by_mat["waste_sum"] > 0]
    waste_rows = sorted(
        waste_by_mat.itertuples(index=False),
        key=lambda row: float(row[1]),
        reverse=True,
    )
    most_waste = pd.DataFrame(waste_rows, columns=["material", "waste_sum"])
    print("\n[3] Materials with most waste (over planned):")
    if len(most_waste) > 0:
        print(most_waste.head(5).set_index("material")["waste_sum"].to_string())
    else:
        print("  None")

    # Stage exceeding budget most
    over_budget = df[df["budget_variance"] > 0]
    if len(over_budget) > 0:
        by_stage = pd.DataFrame(
            over_budget.groupby("stage", as_index=False).agg(
                budget_variance_sum=("budget_variance", "sum")
            )
        )
        by_stage_rows = sorted(
            by_stage.itertuples(index=False),
            key=lambda row: float(row[1]),
            reverse=True,
        )
        by_stage = pd.DataFrame(by_stage_rows, columns=["stage", "budget_variance_sum"])
        print("\n[4] Stages over budget (total variance):")
        print(by_stage.set_index("stage")["budget_variance_sum"].to_string())

    # Cost by project
    print("\n[5] Total cost by project:")
    cost = pd.DataFrame(
        df.groupby("project", as_index=False).agg(actual_cost_sum=("actual_cost", "sum"))
    )
    cost_rows = sorted(
        cost.itertuples(index=False),
        key=lambda row: float(row[1]),
        reverse=True,
    )
    cost = pd.DataFrame(cost_rows, columns=["project", "actual_cost_sum"])
    print(cost.set_index("project")["actual_cost_sum"].to_string())


if __name__ == "__main__":
    main()
