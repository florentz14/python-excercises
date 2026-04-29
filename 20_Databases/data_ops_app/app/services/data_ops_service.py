from __future__ import annotations

import runpy
from pathlib import Path

from data_ops_app.app.schemas.script import ScriptName

SCRIPT_MAP: dict[ScriptName, str] = {
    "family_budget_loader": "legacy/08_family_budget_loader.py",
    "tasks": "legacy/09_tasks.py",
    "survey_load": "legacy/10_survey.py",
    "survey_filter_2002": "legacy/11_survey.py",
    "stocks": "legacy/12_stocks.py",
    "customers": "legacy/13_customers.py",
}


def run_script(script: ScriptName):
    target = Path(__file__).resolve().parents[2] / SCRIPT_MAP[script]
    runpy.run_path(str(target), run_name="__main__")
