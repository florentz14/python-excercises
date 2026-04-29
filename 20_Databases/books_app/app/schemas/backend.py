from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

BackendName = Literal["sqlite", "postgres", "sqlalchemy", "mongo"]


@dataclass
class BackendRunRequest:
    backend: BackendName
