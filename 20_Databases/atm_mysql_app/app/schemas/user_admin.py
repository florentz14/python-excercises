from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal


@dataclass
class UserCreateRequest:
    username: str
    password: str
    full_name: str
    email: str | None
    phone: str | None
    initial_balance: Decimal
