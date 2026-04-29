from __future__ import annotations

from dataclasses import dataclass


@dataclass
class LoginRequest:
    username: str
    password: str
    max_attempts: int = 3
