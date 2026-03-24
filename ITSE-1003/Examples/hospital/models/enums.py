# -------------------------------------------------
# File Name: ITSE-1003/Examples/hospital/models/enums.py
# Description: Hospital domain enumerations.
# -------------------------------------------------

from enum import Enum


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
