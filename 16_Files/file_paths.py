# -------------------------------------------------
# File Name: 16_Files/files_paths.py
# Author: Florentino
# Date: 3/21/26
# Description: Path constants for 16_Files 
# -------------------------------------------------

from pathlib import Path

#from settings import PROJECT_ROOT

# Base directory
BASE_DIR = Path(__file__).resolve().parent

# data directory
DATA_DIR = BASE_DIR / "data"

# generated directory
GEN_DIR = DATA_DIR / "generated"

# Ensure generated directory exists
GEN_DIR.mkdir(parents=True, exist_ok=True)

# File configuration constants
CSV_DELIMITER = ','
CSV_QUOTECHAR = '"'
CSV_NEWLINE = ''

# Data validation settings
MIN_AGE = 1
MAX_AGE = 120
MIN_NAME_LENGTH = 2
MAX_NAME_LENGTH = 50

# Database settings
DB_TIMEOUT = 30.0
DB_ISOLATION_LEVEL = None

# Logging configuration
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
