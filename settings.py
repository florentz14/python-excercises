"""
Global project settings.

Use this module as a single place for paths and shared constants.
"""

from pathlib import Path


# Base paths
PROJECT_ROOT = Path(__file__).resolve().parent

# Pandas directory
PANDAS_DIR = PROJECT_ROOT / "09_Pandas"
PANDAS_DATA_DIR = PANDAS_DIR / "data"
PANDAS_EXPORTS_DIR = PANDAS_DATA_DIR / "exports"

# Databse Directory
DATABASES_DIR = PROJECT_ROOT / "20_Databases"
DATABASES_DATA_DIR = DATABASES_DIR / "Data"

# Files Directory
FILES_DIR = PROJECT_ROOT / "16_Files"
FILES_DATA_DIR = FILES_DIR / "Data"

# Test directory
TESTS_DIR = PROJECT_ROOT / "tests"

#ITSE-1002
ITSE_1002_DIR = PROJECT_ROOT / "ITSE-1002"
ITSE_1002_DATA_DIR = ITSE_1002_DIR / "Data"

#ITSE-1003
ITSE_1003_DIR = PROJECT_ROOT / "ITSE-1003"
ITSE_1003_DATA_DIR = ITSE_1003_DIR / "Data"
GEN_DIR = ITSE_1003_DATA_DIR / "generated"

# General behavior
DEFAULT_ENCODING = "utf-8"
RANDOM_SEED = 42


# Execution flags
DEBUG = False
