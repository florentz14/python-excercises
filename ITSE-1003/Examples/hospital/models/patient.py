# -------------------------------------------------
# File Name: ITSE-1003/Examples/hospital/models/patient.py
# Description: Patient entity.
# -------------------------------------------------

from __future__ import annotations

from datetime import date, datetime
from typing import List, Optional

from .enums import BloodType, Gender
from .person import Person


class Patient(Person):
    """Patient class inheriting from Person."""

    def __init__(
        self,
        name: str,
        age: int,
        gender: Gender,
        phone: str,
        email: str,
        blood_type: BloodType,
        emergency_contact: str,
        emergency_phone: str,
    ) -> None:
        super().__init__(name, age, gender, phone, email)
        self.blood_type = blood_type
        self.emergency_contact = emergency_contact
        self.emergency_phone = emergency_phone
        self._medical_history: List[str] = []
        self._current_medications: List[str] = []
        self._allergies: List[str] = []
        self._admitted = False
        self._admission_date: Optional[date] = None
        self._room_number: Optional[str] = None

    @property
    def medical_history(self) -> List[str]:
        return self._medical_history.copy()

    @property
    def current_medications(self) -> List[str]:
        return self._current_medications.copy()

    @property
    def allergies(self) -> List[str]:
        return self._allergies.copy()

    @property
    def is_admitted(self) -> bool:
        return self._admitted

    @property
    def admission_date(self) -> Optional[date]:
        return self._admission_date

    @property
    def room_number(self) -> Optional[str]:
        return self._room_number

    def add_medical_record(self, record: str) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        self._medical_history.append(f"[{timestamp}] {record}")

    def add_medication(self, medication: str) -> None:
        if medication not in self._current_medications:
            self._current_medications.append(medication)

    def remove_medication(self, medication: str) -> None:
        if medication in self._current_medications:
            self._current_medications.remove(medication)

    def add_allergy(self, allergy: str) -> None:
        if allergy not in self._allergies:
            self._allergies.append(allergy)

    def admit(
        self,
        room_number: str,
        admission_date: Optional[date] = None,
    ) -> None:
        if not self._admitted:
            self._admitted = True
            self._admission_date = (
                admission_date if admission_date is not None else date.today()
            )
            self._room_number = room_number
            self.add_medical_record(f"Admitted to room {room_number}")
        else:
            print(f"Patient {self.name} is already admitted.")

    def discharge(self) -> None:
        if self._admitted:
            self._admitted = False
            room = self._room_number
            self._room_number = None
            self.add_medical_record(f"Discharged from room {room}")
        else:
            print(f"Patient {self.name} is not admitted.")

    def get_info(self) -> str:
        base_info = super().get_info()
        status = (
            f"Admitted (Room {self._room_number})" if self._admitted else "Outpatient"
        )
        return (
            f"{base_info} - {self.blood_type.value} - {status} - "
            f"Emergency: {self.emergency_contact} ({self.emergency_phone})"
        )
