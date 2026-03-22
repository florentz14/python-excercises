# -------------------------------------------------
# File Name: ITSE-1003/Examples/examples_paths.py
# Author: Florentino
# Date: 3/21/26
# Description: Path constants for ITSE-1003 Examples (data/, generated/).
#              Named distinctly from repo-root settings.py so type checkers resolve correctly.
# -------------------------------------------------

from pathlib import Path

# Base directories
EXAMPLES_DIR = Path(__file__).resolve().parent
DATA_DIR = EXAMPLES_DIR / "data"
GEN_DIR = DATA_DIR / "generated"

# Data file paths
PEOPLE_CSV = DATA_DIR / "people.csv"
PEOPLE_SAMPLE_CSV = GEN_DIR / "people_sample.csv"
PEOPLE_DICT_CSV = GEN_DIR / "people_dict.csv"

# Additional data files
HOSPITAL_DATA_CSV = DATA_DIR / "hospital_data.csv"
VEHICLES_CSV = DATA_DIR / "vehicles.csv"
SCHOOL_DB = DATA_DIR / "school.db"
EXAM_DATA_CSV = DATA_DIR / "exam_data.csv"

# Generated file paths
PRODUCTS_DEFAULT_CSV = GEN_DIR / "products_default.csv"
PRODUCTS_SEMICOLON_CSV = GEN_DIR / "products_semicolon.csv"
PRODUCTS_NO_QUOTES_CSV = GEN_DIR / "products_no_quotes.csv"
PRODUCTS_TAB_TSV = GEN_DIR / "products_tab.tsv"

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

# Output formatting
TABLE_FORMAT = "grid"
TABLE_HEADERS = ["Name", "Age", "Email", "City"]

# Database settings
DB_TIMEOUT = 30.0
DB_ISOLATION_LEVEL = None

# Logging configuration
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

def get_all_data_files():
    """Return a list of all data file paths."""
    return [
        PEOPLE_CSV,
        HOSPITAL_DATA_CSV,
        VEHICLES_CSV,
        SCHOOL_DB,
        EXAM_DATA_CSV
    ]

def get_all_generated_files():
    """Return a list of all generated file paths."""
    return [
        PEOPLE_SAMPLE_CSV,
        PEOPLE_DICT_CSV,
        PRODUCTS_DEFAULT_CSV,
        PRODUCTS_SEMICOLON_CSV,
        PRODUCTS_NO_QUOTES_CSV,
        PRODUCTS_TAB_TSV
    ]

def ensure_directories():
    """Ensure all required directories exist."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    GEN_DIR.mkdir(parents=True, exist_ok=True)

def print_paths():
    """Print all configured paths for debugging."""
    print("📁 Configuration Paths:")
    print("=" * 50)
    print(f"📂 EXAMPLES_DIR: {EXAMPLES_DIR}")
    print(f"📊 DATA_DIR: {DATA_DIR}")
    print(f"🗂️  GEN_DIR: {GEN_DIR}")
    print("=" * 50)
    print("📄 Data Files:")
    for file_path in get_all_data_files():
        status = "✅" if file_path.exists() else "❌"
        print(f"  {status} {file_path}")
    print("=" * 50)
    print("📄 Generated Files:")
    for file_path in get_all_generated_files():
        status = "✅" if file_path.exists() else "❌"
        print(f"  {status} {file_path}")
    print("=" * 50)

if __name__ == "__main__":
    # Test configuration
    print("🔧 Examples paths configuration test")
    print("=" * 50)

    ensure_directories()
    print_paths()

    print(f"✅ People CSV exists: {PEOPLE_CSV.exists()}")
    print(f"✅ Generated directory created: {GEN_DIR.exists()}")
    print(f"✅ All directories ready: {all([DATA_DIR.exists(), GEN_DIR.exists()])}")

    print("=" * 50)
    print("🎯 Complete!")
