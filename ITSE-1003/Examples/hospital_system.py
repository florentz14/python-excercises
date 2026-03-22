# -------------------------------------------------
# File Name: hospital_system.py
# Author: Florentino
# Date: 3/20/26
# Description: Hospital management system with OOP concepts.
#              Loads patients/doctors from data/hospital_data.csv; Nurse demo in code.
# -------------------------------------------------

import csv
from datetime import datetime, date, timedelta
from enum import Enum
from pathlib import Path
from typing import List, Optional, Tuple

from examples_paths import HOSPITAL_DATA_CSV

class BloodType(Enum):
    """Blood type enumeration."""
    A_POSITIVE = "A+"
    A_NEGATIVE = "A-"
    B_POSITIVE = "B+"
    B_NEGATIVE = "B-"
    AB_POSITIVE = "AB+"
    AB_NEGATIVE = "AB-"
    O_POSITIVE = "O+"
    O_NEGATIVE = "O-"

class Gender(Enum):
    """Gender enumeration."""
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"

class Department(Enum):
    """Hospital departments enumeration."""
    EMERGENCY = "Emergency"
    CARDIOLOGY = "Cardiology"
    NEUROLOGY = "Neurology"
    PEDIATRICS = "Pediatrics"
    ORTHOPEDICS = "Orthopedics"
    GENERAL = "General Medicine"

class Person:
    """Base class for all people in the hospital."""
    
    def __init__(self, name: str, age: int, gender: Gender, phone: str, email: str) -> None:
        """
        Initialize a Person object.
        
        Args:
            name (str): Full name
            age (int): Age in years
            gender (Gender): Gender enum
            phone (str): Phone number
            email (str): Email address
        """
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.email = email
        self._id = self._generate_id()
    
    def _generate_id(self) -> str:
        """Generate a unique ID based on name and timestamp."""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        name_part = self.name.replace(" ", "").lower()[:5]
        return f"{name_part}{timestamp}"
    
    @property
    def id(self) -> str:
        """Get the person's ID."""
        return self._id
    
    def get_age(self) -> int:
        """Get the person's age."""
        return self.age
    
    def get_info(self) -> str:
        """Get basic person information."""
        return f"{self.name} ({self.age}, {self.gender.value})"
    
    def __str__(self) -> str:
        """String representation of the person."""
        return f"{self.name} (ID: {self._id})"

class Patient(Person):
    """Patient class inheriting from Person."""
    
    def __init__(self, name: str, age: int, gender: Gender, phone: str, email: str,
                 blood_type: BloodType, emergency_contact: str, 
                 emergency_phone: str) -> None:
        """
        Initialize a Patient object.
        
        Args:
            name (str): Full name
            age (int): Age in years
            gender (Gender): Gender enum
            phone (str): Phone number
            email (str): Email address
            blood_type (BloodType): Blood type enum
            emergency_contact (str): Emergency contact name
            emergency_phone (str): Emergency contact phone
        """
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
        """Get medical history (read-only)."""
        return self._medical_history.copy()
    
    @property
    def current_medications(self) -> List[str]:
        """Get current medications (read-only)."""
        return self._current_medications.copy()
    
    @property
    def allergies(self) -> List[str]:
        """Get allergies (read-only)."""
        return self._allergies.copy()
    
    @property
    def is_admitted(self) -> bool:
        """Check if patient is admitted."""
        return self._admitted
    
    @property
    def admission_date(self) -> Optional[date]:
        """Get admission date."""
        return self._admission_date
    
    @property
    def room_number(self) -> Optional[str]:
        """Get room number."""
        return self._room_number
    
    def add_medical_record(self, record: str) -> None:
        """Add a medical record."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        self._medical_history.append(f"[{timestamp}] {record}")
    
    def add_medication(self, medication: str) -> None:
        """Add a medication."""
        if medication not in self._current_medications:
            self._current_medications.append(medication)
    
    def remove_medication(self, medication: str) -> None:
        """Remove a medication."""
        if medication in self._current_medications:
            self._current_medications.remove(medication)
    
    def add_allergy(self, allergy: str) -> None:
        """Add an allergy."""
        if allergy not in self._allergies:
            self._allergies.append(allergy)
    
    def admit(
        self,
        room_number: str,
        admission_date: Optional[date] = None,
    ) -> None:
        """Admit patient to hospital."""
        if not self._admitted:
            self._admitted = True
            self._admission_date = admission_date if admission_date is not None else date.today()
            self._room_number = room_number
            self.add_medical_record(f"Admitted to room {room_number}")
        else:
            print(f"Patient {self.name} is already admitted.")
    
    def discharge(self) -> None:
        """Discharge patient from hospital."""
        if self._admitted:
            self._admitted = False
            room = self._room_number
            self._room_number = None
            self.add_medical_record(f"Discharged from room {room}")
        else:
            print(f"Patient {self.name} is not admitted.")
    
    def get_info(self) -> str:
        """Override: Add patient-specific information."""
        base_info = super().get_info()
        status = f"Admitted (Room {self._room_number})" if self._admitted else "Outpatient"
        return (f"{base_info} - {self.blood_type.value} - {status} - "
                f"Emergency: {self.emergency_contact} ({self.emergency_phone})")

class Staff(Person):
    """Base class for hospital staff members."""
    
    def __init__(self, name: str, age: int, gender: Gender, phone: str, email: str,
                 employee_id: str, department: Department, hire_date: date) -> None:
        """
        Initialize a Staff object.
        
        Args:
            name (str): Full name
            age (int): Age in years
            gender (Gender): Gender enum
            phone (str): Phone number
            email (str): Email address
            employee_id (str): Employee ID
            department (Department): Department enum
            hire_date (date): Hire date
        """
        super().__init__(name, age, gender, phone, email)
        self.employee_id = employee_id
        self.department = department
        self.hire_date = hire_date
        self._is_active = True
    
    @property
    def is_active(self) -> bool:
        """Check if staff member is active."""
        return self._is_active
    
    def get_years_of_service(self) -> int:
        """Calculate years of service."""
        today = date.today()
        years = today.year - self.hire_date.year
        if today.month < self.hire_date.month or \
           (today.month == self.hire_date.month and today.day < self.hire_date.day):
            years -= 1
        return years
    
    def activate(self) -> None:
        """Activate staff member."""
        self._is_active = True
    
    def deactivate(self) -> None:
        """Deactivate staff member."""
        self._is_active = False
    
    def get_info(self) -> str:
        """Override: Add staff-specific information."""
        base_info = super().get_info()
        status = "Active" if self._is_active else "Inactive"
        return (f"{base_info} - {self.department.value} - "
                f"ID: {self.employee_id} - {status} - "
                f"Service: {self.get_years_of_service()} years")

class Doctor(Staff):
    """Doctor class inheriting from Staff."""
    
    def __init__(self, name: str, age: int, gender: Gender, phone: str, email: str,
                 employee_id: str, department: Department, hire_date: date,
                 specialization: str, license_number: str) -> None:
        """
        Initialize a Doctor object.
        
        Args:
            name (str): Full name
            age (int): Age in years
            gender (Gender): Gender enum
            phone (str): Phone number
            email (str): Email address
            employee_id (str): Employee ID
            department (Department): Department enum
            hire_date (date): Hire date
            specialization (str): Medical specialization
            license_number (str): Medical license number
        """
        super().__init__(name, age, gender, phone, email, employee_id, department, hire_date)
        self.specialization = specialization
        self.license_number = license_number
        self._patients: List[Patient] = []
        self._available_times: List[datetime] = []

    def professional_name(self) -> str:
        """Name for display (avoid 'Dr. Dr. Smith' when CSV already includes 'Dr.')."""
        n = self.name.strip()
        if n.lower().startswith("dr."):
            return n
        return f"Dr. {n}"

    @property
    def patients(self) -> List[Patient]:
        """Get list of patients (read-only)."""
        return self._patients.copy()
    
    @property
    def available_times(self) -> List[datetime]:
        """Get available appointment times (read-only)."""
        return self._available_times.copy()
    
    def add_patient(self, patient: Patient) -> None:
        """Add a patient to the doctor's care."""
        if patient not in self._patients:
            self._patients.append(patient)
            patient.add_medical_record(
                f"Assigned to {self.professional_name()} ({self.specialization})"
            )
    
    def remove_patient(self, patient: Patient) -> None:
        """Remove a patient from the doctor's care."""
        if patient in self._patients:
            self._patients.remove(patient)
            patient.add_medical_record(f"Removed from {self.professional_name()}'s care")
    
    def add_available_time(self, time: datetime) -> None:
        """Add an available appointment time."""
        if time > datetime.now() and time not in self._available_times:
            self._available_times.append(time)
            self._available_times.sort()
    
    def remove_available_time(self, time: datetime) -> None:
        """Remove an available appointment time."""
        if time in self._available_times:
            self._available_times.remove(time)
    
    def prescribe_medication(self, patient: Patient, medication: str) -> None:
        """Prescribe medication to a patient."""
        if patient in self._patients:
            patient.add_medication(medication)
            patient.add_medical_record(
                f"Medication prescribed by {self.professional_name()}: {medication}"
            )
        else:
            print(f"Patient {patient.name} is not under {self.professional_name()}'s care.")
    
    def get_info(self) -> str:
        """Override: Add doctor-specific information."""
        base_info = super().get_info()
        return (f"{base_info} - Dr. {self.specialization} - "
                f"License: {self.license_number} - "
                f"Patients: {len(self._patients)}")

class Nurse(Staff):
    """Nurse class inheriting from Staff."""
    
    def __init__(self, name: str, age: int, gender: Gender, phone: str, email: str,
                 employee_id: str, department: Department, hire_date: date,
                 certification_level: str) -> None:
        """
        Initialize a Nurse object.
        
        Args:
            name (str): Full name
            age (int): Age in years
            gender (Gender): Gender enum
            phone (str): Phone number
            email (str): Email address
            employee_id (str): Employee ID
            department (Department): Department enum
            hire_date (date): Hire date
            certification_level (str): Nursing certification level
        """
        super().__init__(name, age, gender, phone, email, employee_id, department, hire_date)
        self.certification_level = certification_level
        self._assigned_patients: List[Patient] = []
        self._shift = "Day"  # Day or Night shift

    def care_name(self) -> str:
        """Display name without duplicating the word 'Nurse'."""
        n = self.name.strip()
        if n.lower().startswith("nurse "):
            return n
        return f"Nurse {n}"

    @property
    def assigned_patients(self) -> List[Patient]:
        """Get list of assigned patients (read-only)."""
        return self._assigned_patients.copy()
    
    @property
    def shift(self) -> str:
        """Get current shift."""
        return self._shift
    
    def assign_patient(self, patient: Patient) -> None:
        """Assign a patient to the nurse."""
        if patient not in self._assigned_patients:
            self._assigned_patients.append(patient)
            patient.add_medical_record(f"Assigned to {self.care_name()}")
    
    def unassign_patient(self, patient: Patient) -> None:
        """Unassign a patient from the nurse."""
        if patient in self._assigned_patients:
            self._assigned_patients.remove(patient)
            patient.add_medical_record(f"Unassigned from {self.care_name()}")
    
    def change_shift(self, new_shift: str) -> None:
        """Change nurse's shift."""
        if new_shift in ["Day", "Night"]:
            self._shift = new_shift
        else:
            print("Invalid shift. Use 'Day' or 'Night'.")
    
    def administer_medication(self, patient: Patient, medication: str) -> None:
        """Administer medication to a patient."""
        if patient in self._assigned_patients:
            if medication in patient.current_medications:
                patient.add_medical_record(
                    f"Medication administered by {self.care_name()}: {medication}"
                )
            else:
                print(f"Medication {medication} not prescribed for patient {patient.name}.")
        else:
            print(f"Patient {patient.name} is not assigned to {self.care_name()}.")
    
    def get_info(self) -> str:
        """Override: Add nurse-specific information."""
        base_info = super().get_info()
        return (f"{base_info} - Nurse ({self.certification_level}) - "
                f"Shift: {self._shift} - "
                f"Assigned Patients: {len(self._assigned_patients)}")

class Appointment:
    """Appointment class for scheduling patient visits."""
    
    def __init__(self, patient: Patient, doctor: Doctor, 
                 appointment_time: datetime, reason: str = "") -> None:
        """
        Initialize an Appointment object.
        
        Args:
            patient (Patient): The patient
            doctor (Doctor): The doctor
            appointment_time (datetime): Appointment date and time
            reason (str): Reason for appointment
        """
        self.patient = patient
        self.doctor = doctor
        self.appointment_time = appointment_time
        self.reason = reason
        self._status = "Scheduled"
        self._notes = ""
    
    @property
    def status(self) -> str:
        """Get appointment status."""
        return self._status
    
    @property
    def notes(self) -> str:
        """Get appointment notes."""
        return self._notes
    
    def confirm(self) -> None:
        """Confirm the appointment."""
        if self._status == "Scheduled":
            self._status = "Confirmed"
    
    def cancel(self) -> None:
        """Cancel the appointment."""
        if self._status in ["Scheduled", "Confirmed"]:
            self._status = "Cancelled"
    
    def complete(self, notes: str = "") -> None:
        """Complete the appointment."""
        if self._status in ["Scheduled", "Confirmed"]:
            self._status = "Completed"
            self._notes = notes
            self.patient.add_medical_record(
                f"Appointment with {self.doctor.professional_name()}: {notes}"
            )
    
    def get_info(self) -> str:
        """Get appointment information."""
        time_str = self.appointment_time.strftime("%Y-%m-%d %H:%M")
        reason_str = f" - {self.reason}" if self.reason else ""
        return (
            f"{time_str} - {self.patient.name} with {self.doctor.professional_name()}"
            f"{reason_str} - Status: {self._status}"
        )
    
    def __str__(self) -> str:
        """String representation of the appointment."""
        return self.get_info()


_DEPT_BY_CSV_LABEL: dict[str, Department] = {
    "Emergency": Department.EMERGENCY,
    "Cardiology": Department.CARDIOLOGY,
    "Neurology": Department.NEUROLOGY,
    "Pediatrics": Department.PEDIATRICS,
    "Orthopedics": Department.ORTHOPEDICS,
    "General": Department.GENERAL,
    "General Medicine": Department.GENERAL,
}


def _department_from_csv(label: str) -> Department:
    return _DEPT_BY_CSV_LABEL.get(label.strip(), Department.GENERAL)


def _gender_from_csv(label: str) -> Gender:
    key = label.strip().lower()
    if key == "male":
        return Gender.MALE
    if key == "female":
        return Gender.FEMALE
    return Gender.OTHER


def _blood_type_from_csv(label: str) -> BloodType:
    value = label.strip()
    for bt in BloodType:
        if bt.value == value:
            return bt
    return BloodType.O_POSITIVE


def _patient_email(name: str) -> str:
    slug = name.lower().replace(" ", ".").replace("'", "")
    return f"{slug}@patients.demo"


def load_hospital_from_csv(
    csv_path: Optional[Path] = None,
) -> Tuple[List[Patient], List[Doctor], List[Tuple[Patient, Doctor]]]:
    """
    Build Patient and Doctor instances from data/hospital_data.csv.
    Returns (patients, doctors, patient_doctor_pairs for the CSV rows in order).
    """
    path = csv_path or HOSPITAL_DATA_CSV
    if not path.is_file():
        raise FileNotFoundError(path)

    doctors_by_name: dict[str, Doctor] = {}
    patients: List[Patient] = []
    pairs: List[Tuple[Patient, Doctor]] = []

    with path.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))

    for i, row in enumerate(rows):
        doc_name = row["Doctor"].strip()
        if doc_name not in doctors_by_name:
            dept = _department_from_csv(row["Department"])
            eid = f"CSV{len(doctors_by_name) + 1:03d}"
            slug = doc_name.lower().replace(" ", ".").replace("dr.", "dr")
            doctors_by_name[doc_name] = Doctor(
                doc_name,
                40,
                Gender.FEMALE,
                f"555-8{eid[-3:]}",
                f"{slug}@hospital.demo",
                eid,
                dept,
                date(2019, 1, 1),
                "Attending Physician",
                f"LIC-{eid}",
            )

        doctor = doctors_by_name[doc_name]
        name = row["Patient_Name"].strip()
        age = int(row["Age"])
        gender = _gender_from_csv(row["Gender"])
        blood = _blood_type_from_csv(row["Blood_Type"])
        phone = f"555-2{i:03d}"
        patient = Patient(
            name,
            age,
            gender,
            phone,
            _patient_email(name),
            blood,
            "Family",
            "555-1999",
        )
        adm = date.fromisoformat(row["Admission_Date"].strip())
        patient.admit(row["Room_Number"].strip(), admission_date=adm)
        doctor.add_patient(patient)
        patients.append(patient)
        pairs.append((patient, doctor))

    return patients, list(doctors_by_name.values()), pairs


def main():
    """Main function to test the hospital system."""
    print("=== Hospital System Demo (data/hospital_data.csv) ===\n")

    patients, doctors, pairs = load_hospital_from_csv()

    patient1 = patients[0]
    patient1.add_allergy("Penicillin")
    patient1.add_medication("Lisinopril")
    patient1.add_medical_record("Initial consultation (demo after CSV load)")

    if len(patients) > 1:
        patients[1].add_allergy("Peanuts")
        patients[1].add_medication("Insulin")
    if len(patients) > 2:
        patients[2].add_medication("Metformin")

    nurse1 = Nurse(
        "Nurse Jennifer Davis",
        32,
        Gender.FEMALE,
        "555-2001",
        "davis@hospital.com",
        "NUR001",
        Department.EMERGENCY,
        date(2021, 3, 10),
        "RN Level 3",
    )
    nurse2 = Nurse(
        "Nurse Tom Anderson",
        28,
        Gender.MALE,
        "555-2002",
        "anderson@hospital.com",
        "NUR002",
        Department.PEDIATRICS,
        date(2022, 1, 20),
        "RN Level 2",
    )

    for i, p in enumerate(patients):
        (nurse1 if i % 2 == 0 else nurse2).assign_patient(p)

    tomorrow = datetime.now() + timedelta(days=1)
    appointment1 = Appointment(
        pairs[0][0],
        pairs[0][1],
        tomorrow.replace(hour=10, minute=0),
        "Cardiac checkup",
    )
    appointment2 = Appointment(
        pairs[1][0],
        pairs[1][1],
        tomorrow.replace(hour=14, minute=30),
        "Follow-up consultation",
    )
    appointment3 = Appointment(
        pairs[2][0],
        pairs[2][1],
        tomorrow.replace(hour=11, minute=15),
        "General examination",
    )

    for d in doctors[:3]:
        d.add_available_time(tomorrow.replace(hour=9, minute=0))

    print("=== Patients (loaded from CSV) ===")
    for patient in patients:
        print(patient.get_info())
    print()

    print("=== Doctors (from CSV + synthetic staff IDs) ===")
    for doctor in doctors:
        print(doctor.get_info())
    print()

    print("=== Nurses ===")
    for nurse in [nurse1, nurse2]:
        print(nurse.get_info())
    print()

    print("=== Appointments ===")
    for appointment in [appointment1, appointment2, appointment3]:
        appointment.confirm()
        print(appointment.get_info())
    print()

    appointment1.complete(
        "Patient's blood pressure is well controlled. Continue current medication."
    )
    appointment3.complete(
        "Patient is in good health. Recommended lifestyle changes."
    )

    print("=== Medical Records for first CSV patient ===")
    for record in patient1.medical_history:
        print(f"- {record}")
    print()

    print("=== Current Medications for first CSV patient ===")
    for med in patient1.current_medications:
        print(f"- {med}")
    print()

    patient1.discharge()
    print(
        f"First patient status: {'Admitted' if patient1.is_admitted else 'Discharged'}"
    )

    print("\n=== Demo Complete ===")


if __name__ == "__main__":
    main()
