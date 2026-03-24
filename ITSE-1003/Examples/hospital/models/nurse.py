# -------------------------------------------------
# File Name: ITSE-1003/Examples/hospital/models/nurse.py
# Description: Nurse staff role.
# -------------------------------------------------

from __future__ import annotations

from datetime import date
from typing import List

from .enums import Department, Gender
from .patient import Patient
from .staff import Staff


class Nurse(Staff):
    """Nurse class inheriting from Staff."""

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
        certification_level: str,
    ) -> None:
        super().__init__(
            name, age, gender, phone, email, employee_id, department, hire_date
        )
        self.certification_level = certification_level
        self._assigned_patients: List[Patient] = []
        self._shift = "Day"

    def care_name(self) -> str:
        n = self.name.strip()
        if n.lower().startswith("nurse "):
            return n
        return f"Nurse {n}"

    @property
    def assigned_patients(self) -> List[Patient]:
        return self._assigned_patients.copy()

    @property
    def shift(self) -> str:
        return self._shift

    def assign_patient(self, patient: Patient) -> None:
        if patient not in self._assigned_patients:
            self._assigned_patients.append(patient)
            patient.add_medical_record(f"Assigned to {self.care_name()}")

    def unassign_patient(self, patient: Patient) -> None:
        if patient in self._assigned_patients:
            self._assigned_patients.remove(patient)
            patient.add_medical_record(f"Unassigned from {self.care_name()}")

    def change_shift(self, new_shift: str) -> None:
        if new_shift in ["Day", "Night"]:
            self._shift = new_shift
        else:
            print("Invalid shift. Use 'Day' or 'Night'.")

    def administer_medication(self, patient: Patient, medication: str) -> None:
        if patient in self._assigned_patients:
            if medication in patient.current_medications:
                patient.add_medical_record(
                    f"Medication administered by {self.care_name()}: {medication}"
                )
            else:
                print(
                    f"Medication {medication} not prescribed for patient {patient.name}."
                )
        else:
            print(f"Patient {patient.name} is not assigned to {self.care_name()}.")

    def get_info(self) -> str:
        base_info = super().get_info()
        return (
            f"{base_info} - Nurse ({self.certification_level}) - "
            f"Shift: {self._shift} - "
            f"Assigned Patients: {len(self._assigned_patients)}"
        )
