# -------------------------------------------------
# File Name: ITSE-1003/Examples/hospital/models/appointment.py
# Description: Scheduled patient visit.
# -------------------------------------------------

from datetime import datetime

from .doctor import Doctor
from .patient import Patient


class Appointment:
    """Appointment class for scheduling patient visits."""

    def __init__(
        self,
        patient: Patient,
        doctor: Doctor,
        appointment_time: datetime,
        reason: str = "",
    ) -> None:
        self.patient = patient
        self.doctor = doctor
        self.appointment_time = appointment_time
        self.reason = reason
        self._status = "Scheduled"
        self._notes = ""

    @property
    def status(self) -> str:
        return self._status

    @property
    def notes(self) -> str:
        return self._notes

    def confirm(self) -> None:
        if self._status == "Scheduled":
            self._status = "Confirmed"

    def cancel(self) -> None:
        if self._status in ["Scheduled", "Confirmed"]:
            self._status = "Cancelled"

    def complete(self, notes: str = "") -> None:
        if self._status in ["Scheduled", "Confirmed"]:
            self._status = "Completed"
            self._notes = notes
            self.patient.add_medical_record(
                f"Appointment with {self.doctor.professional_name()}: {notes}"
            )

    def get_info(self) -> str:
        time_str = self.appointment_time.strftime("%Y-%m-%d %H:%M")
        reason_str = f" - {self.reason}" if self.reason else ""
        return (
            f"{time_str} - {self.patient.name} with {self.doctor.professional_name()}"
            f"{reason_str} - Status: {self._status}"
        )

    def __str__(self) -> str:
        return self.get_info()
