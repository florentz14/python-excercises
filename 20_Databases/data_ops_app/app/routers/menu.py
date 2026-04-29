from __future__ import annotations

from data_ops_app.app.schemas.script import ScriptName
from data_ops_app.app.services.data_ops_service import run_script


def run_cli(selected: ScriptName | None = None):
    if selected:
        run_script(selected)
        return
    print("=" * 66)
    print("DATA OPS APP - SELECT SCRIPT")
    print("=" * 66)
    print("1 - Family budget loader (PostgreSQL)")
    print("2 - Tasks project DB (SQLite)")
    print("3 - Survey load")
    print("4 - Survey filter 2002")
    print("5 - Stocks loader")
    print("6 - Customers loader")
    print("7 - Exit")
    print("=" * 66)
    choice = input("Choose option (1-7): ").strip()
    mapping: dict[str, ScriptName] = {
        "1": "family_budget_loader",
        "2": "tasks",
        "3": "survey_load",
        "4": "survey_filter_2002",
        "5": "stocks",
        "6": "customers",
    }
    if choice == "7":
        print("Goodbye!")
        return
    script = mapping.get(choice)
    if not script:
        print("Invalid choice.")
        return
    run_script(script)
