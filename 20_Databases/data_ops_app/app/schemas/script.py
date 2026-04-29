from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

ScriptName = Literal[
    "family_budget_loader",
    "tasks",
    "survey_load",
    "survey_filter_2002",
    "stocks",
    "customers",
]


@dataclass
class ScriptRunRequest:
    script: ScriptName
