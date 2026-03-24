# -------------------------------------------------
# File Name: ITSE-1003/Examples/hospital/models/doctor.py
# Description: Doctor staff role.
# -------------------------------------------------

from __future__ import annotations

from datetime import date, datetime
from typing import List

from .enums import Department, Gender
from .patient import Patient
from .staff import Staff


class Doctor(Staff):
    """Doctor class inheriting from Staff."""

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
        specialization: str,
        license_number: str,
    ) -> None:
        super().__init__(
            name, age, gender, phone, email, employee_id, department, hire_date
        )
        self.specialization = specialization
        self.license_number = license_number
        self._patients: List[Patient] = []
        self._available_times: List[datetime] = []

    def professional_name(self) -> str:
        n = self.name.strip()
        if n.lower().startswith("dr."):
            return n
        return f"Dr. {n}"

    @property
    def patients(self) -> List[Patient]:
        return self._patients.copy()

    @property
    def available_times(self) -> List[datetime]:
        return self._available_times.copy()

    def add_patient(self, patient: Patient) -> None:
        if patient not in self._patients:
            self._patients.append(patient)
            patient.add_medical_record(
                f"Assigned to {self.professional_name()} ({self.specialization})"
            )

    def remove_patient(self, patient: Patient) -> None:
        if patient in self._patients:
            self._patients.remove(patient)
            patient.add_medical_record(f"Removed from {self.professional_name()}'s care")

    def add_available_time(self, time: datetime) -> None:
        if time > datetime.now() and time not in self._available_times:
            self._available_times.append(time)
            self._available_times.sort()

    def remove_available_time(self, time: datetime) -> None:
        if time in self._available_times:
            self._available_times.remove(time)

    def prescribe_medication(self, patient: Patient, medication: str) -> None:
        if patient in self._patients:
            patient.add_medication(medication)
            patient.add_medical_record(
                f"Medication prescribed by {self.professional_name()}: {medication}"
            )
        else:
            print(
                f"Patient {patient.name} is not under {self.professional_name()}'s care."
            )

    def get_info(self) -> str:
        base_info = super().get_info()
        return (
            f"{base_info} - Dr. {self.specialization} - "
            f"License: {self.license_number} - "
            f"Patients: {len(self._patients)}"
        )
