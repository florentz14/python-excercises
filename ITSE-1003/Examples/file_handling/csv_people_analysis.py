# -------------------------------------------------
# File Name: ITSE-1003/Examples/file_handling/csv_people_analysis.py
# Author: Florentino
# Date: 3/22/2026
# Description: Estadísticas y filtros sobre data/people.csv con DictReader.
# -------------------------------------------------

import sys
from pathlib import Path

_EXAMPLES_ROOT = Path(__file__).resolve().parent.parent
if str(_EXAMPLES_ROOT) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES_ROOT))

import csv

from tabulate import tabulate

from examples_paths import PEOPLE_CSV


def analyze_csv_data() -> None:
    """Analyze CSV data with statistics."""
    print("\n📈 CSV Data Analysis:")
    print("=" * 50)

    try:
        with PEOPLE_CSV.open(encoding="utf-8") as file:
            reader = csv.DictReader(file)
            ages = []
            cities = set()

            for row in reader:
                age = int(row["Age"])
                ages.append(age)
                cities.add(row["City"])

            avg_age = sum(ages) / len(ages)
            min_age = min(ages)
            max_age = max(ages)

            analysis_data = [
                ["Total People", len(ages)],
                ["Average Age", f"{avg_age:.1f} years"],
                ["Youngest Age", f"{min_age} years"],
                ["Oldest Age", f"{max_age} years"],
                ["Unique Cities", len(cities)],
                ["Cities", ", ".join(sorted(cities))],
            ]

            print("📊 Analysis Results:")
            print(tabulate(analysis_data, headers=["Metric", "Value"], tablefmt="grid"))

    except FileNotFoundError:
        print(f"❌ File not found: {PEOPLE_CSV}")
    except Exception as e:
        print(f"❌ Error analyzing file: {e}")


def filter_csv_data() -> None:
    """Filter CSV data based on criteria."""
    print("\n🔍 CSV Data Filtering:")
    print("=" * 50)

    try:
        with PEOPLE_CSV.open(encoding="utf-8") as file:
            reader = csv.DictReader(file)
            older_than_30 = [row for row in reader if int(row["Age"]) > 30]

            print(f"👵 People older than 30 ({len(older_than_30)} found):")

            if older_than_30:
                display_rows = [
                    [r["Name"], r["Age"], r["City"], r["Email"]] for r in older_than_30
                ]
                headers = ["Name", "Age", "City", "Email"]
                print(tabulate(display_rows, headers=headers, tablefmt="grid"))

    except FileNotFoundError:
        print(f"❌ File not found: {PEOPLE_CSV}")
    except Exception as e:
        print(f"❌ Error filtering file: {e}")
