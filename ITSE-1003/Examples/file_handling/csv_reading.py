# -------------------------------------------------
# File Name: ITSE-1003/Examples/file_handling/csv_reading.py
# Author: Florentino
# Date: 3/22/2026
# Description: Read CSV with csv.reader (people.csv) and DictReader (generated file).
# -------------------------------------------------

import sys
from pathlib import Path

_EXAMPLES_ROOT = Path(__file__).resolve().parent.parent
if str(_EXAMPLES_ROOT) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES_ROOT))

import csv
from datetime import datetime

from tabulate import tabulate

from examples_paths import PEOPLE_CSV, PEOPLE_DICT_CSV
from utils import human_date_diff


def read_basic_csv() -> None:
    """Read and display bundled people data from data/people.csv."""
    print("\n📖 Reading Basic CSV (data folder):")
    print("=" * 50)

    try:
        with PEOPLE_CSV.open(encoding="utf-8") as file:
            reader = csv.reader(file)
            headers = next(reader)
            rows = []

            # Columns: ID, Name, Age, Email, City, Phone, Birth_Date
            for row in reader:
                rows.append(row)
                print(f"👤 [{row[0]}] {row[1]} ({row[2]} years) - {row[4]}")

            print(f"\n📊 Data Table:")
            print(tabulate(rows, headers=headers, tablefmt="grid"))

    except FileNotFoundError:
        print(f"❌ File not found: {PEOPLE_CSV}")
    except Exception as e:
        print(f"❌ Error reading file: {e}")


def read_dict_csv() -> None:
    """Read CSV using DictReader."""
    print("\n📖 Reading Dict CSV:")
    print("=" * 50)

    try:
        with PEOPLE_DICT_CSV.open(encoding="utf-8") as file:
            reader = csv.DictReader(file)
            rows = []

            for row in reader:
                row["age"] = int(row["age"])
                rows.append(row)

                reg_date = datetime.strptime(row["registration_date"], "%Y-%m-%d").date()
                time_ago = human_date_diff(datetime.combine(reg_date, datetime.min.time()))

                print(
                    f"👤 {row['name']} ({row['age']}) from {row['city']} - registered {time_ago}"
                )

            rows.sort(key=lambda x: x["age"])

            print(f"\n📊 Sorted by Age:")
            display_rows = [
                [r["name"], r["age"], r["city"], r["registration_date"]] for r in rows
            ]
            headers = ["Name", "Age", "City", "Registration Date"]
            print(tabulate(display_rows, headers=headers, tablefmt="grid"))

    except FileNotFoundError:
        print(f"❌ File not found. Run create_dict_csv() first ({PEOPLE_DICT_CSV}).")
    except Exception as e:
        print(f"❌ Error reading file: {e}")
