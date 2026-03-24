# -------------------------------------------------
# File Name: ITSE-1003/Examples/hospital/models/staff.py
# Description: Base hospital staff.
# -------------------------------------------------

from datetime import date

from .enums import Department, Gender
from .person import Person


class Staff(Person):
    """Base class for hospital staff members."""

    def __init__(
        self,
        name: str,
        age: int,
        gender: Gender,
        phone: str,
        email: str,
        employee_id: str,
        department: Department,
        hire_date: date,
    ) -> None:
        super().__init__(name, age, gender, phone, email)
        self.employee_id = employee_id
        self.department = department
        self.hire_date = hire_date
        self._is_active = True

    @property
    def is_active(self) -> bool:
        return self._is_active

    def get_years_of_service(self) -> int:
        today = date.today()
        years = today.year - self.hire_date.year
        if today.month < self.hire_date.month or (
            today.month == self.hire_date.month and today.day < self.hire_date.day
        ):
            years -= 1
        return years

    def activate(self) -> None:
        self._is_active = True

    def deactivate(self) -> None:
        self._is_active = False

    def get_info(self) -> str:
        base_info = super().get_info()
        status = "Active" if self._is_active else "Inactive"
        return (
            f"{base_info} - {self.department.value} - "
            f"ID: {self.employee_id} - {status} - "
            f"Service: {self.get_years_of_service()} years"
        )
