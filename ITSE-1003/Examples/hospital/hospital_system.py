# -------------------------------------------------
# File Name: ITSE-1003/Examples/hospital/hospital_system.py
# Author: Florentino
# Date: 3/20/26
# Description: Hospital management system with OOP concepts.
#              Loads patients/doctors from hospital/data/hospital_data.csv; Nurse demo in code.
#              Domain classes live in hospital/models/.
# -------------------------------------------------

import csv
import sys
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import List, Optional, Tuple

_hospital_root = Path(__file__).resolve().parent
_examples_dir = _hospital_root.parent
if str(_hospital_root) not in sys.path:
    sys.path.insert(0, str(_hospital_root))
if str(_examples_dir) not in sys.path:
    sys.path.append(str(_examples_dir))

from examples_paths import HOSPITAL_DATA_CSV

from models import (
    Appointment,
    BloodType,
    Department,
    Doctor,
    Gender,
    Nurse,
    Patient,
)

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
    Build Patient and Doctor instances from hospital/data/hospital_data.csv.
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
    print("=== Hospital System Demo (hospital/data/hospital_data.csv) ===\n")

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
