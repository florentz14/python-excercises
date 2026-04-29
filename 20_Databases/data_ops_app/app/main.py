from __future__ import annotations

import sys

from data_ops_app.app.routers.menu import run_cli
from data_ops_app.app.schemas.script import ScriptName


def run():
    selected: ScriptName | None = None
    if len(sys.argv) > 1:
        arg = sys.argv[1].strip().lower()
        values = {
            "family_budget_loader",
            "tasks",
            "survey_load",
            "survey_filter_2002",
            "stocks",
            "customers",
        }
        if arg in values:
            selected = arg  # type: ignore[assignment]
    run_cli(selected)


if __name__ == "__main__":
    run()
