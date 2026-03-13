"""
Global project settings.

Use this module as a single place for paths and shared constants.
"""

from pathlib import Path


# Base paths
PROJECT_ROOT = Path(__file__).resolve().parent
PANDAS_DIR = PROJECT_ROOT / "09_Pandas"
PANDAS_DATA_DIR = PANDAS_DIR / "data"
PANDAS_EXPORTS_DIR = PANDAS_DATA_DIR / "exports"
DATABASES_DIR = PROJECT_ROOT / "20_Databases"
DATABASES_DATA_DIR = DATABASES_DIR / "Data"
TESTS_DIR = PROJECT_ROOT / "tests"


# General behavior
DEFAULT_ENCODING = "utf-8"
RANDOM_SEED = 42


# Execution flags
DEBUG = False
