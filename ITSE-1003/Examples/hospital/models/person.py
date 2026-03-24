# -------------------------------------------------
# File Name: ITSE-1003/Examples/hospital/models/person.py
# Description: Base person in the hospital domain.
# -------------------------------------------------

from datetime import datetime

from .enums import Gender


class Person:
    """Base class for all people in the hospital."""

    def __init__(
        self, name: str, age: int, gender: Gender, phone: str, email: str
    ) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.email = email
        self._id = self._generate_id()

    def _generate_id(self) -> str:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        name_part = self.name.replace(" ", "").lower()[:5]
        return f"{name_part}{timestamp}"

    @property
    def id(self) -> str:
        return self._id

    def get_age(self) -> int:
        return self.age

    def get_info(self) -> str:
        return f"{self.name} ({self.age}, {self.gender.value})"

    def __str__(self) -> str:
        return f"{self.name} (ID: {self._id})"
