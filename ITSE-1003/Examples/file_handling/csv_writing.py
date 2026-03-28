# -------------------------------------------------
# File Name: ITSE-1003/Examples/file_handling/csv_writing.py
# Author: Florentino
# Date: 3/22/2026
# Description: Crear CSV (writer/DictWriter), añadir filas, delimitadores y TSV de prueba.
# -------------------------------------------------

import sys
from pathlib import Path

_EXAMPLES_ROOT = Path(__file__).resolve().parent.parent
if str(_EXAMPLES_ROOT) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES_ROOT))

import csv

from tabulate import tabulate

from examples_paths import GEN_DIR, PEOPLE_DICT_CSV, PEOPLE_SAMPLE_CSV


def create_sample_csv() -> None:
    """Create a sample CSV file with people data."""
    data = [
        ["Name", "Age", "Email", "City", "Phone", "Birth_Date"],
        ["Alice Johnson", 35, "alice@email.com", "New York", "555-0101", "1990-05-15"],
        ["Bob Smith", 28, "bob@email.com", "Los Angeles", "555-0202", "1985-12-25"],
        ["Charlie Brown", 42, "charlie@email.com", "Chicago", "555-0303", "2000-02-29"],
        ["Diana Prince", 31, "diana@email.com", "Houston", "555-0404", "1992-08-30"],
        ["Eve Wilson", 45, "eve@email.com", "Phoenix", "555-0505", "1975-11-12"],
    ]

    with PEOPLE_SAMPLE_CSV.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f"✅ Created {PEOPLE_SAMPLE_CSV}")


def create_dict_csv() -> None:
    """Create CSV using DictWriter."""
    fieldnames = ["name", "age", "email", "city", "registration_date"]
    people = [
        {
            "name": "Frank Miller",
            "age": 29,
            "email": "frank@email.com",
            "city": "Boston",
            "registration_date": "2026-03-20",
        },
        {
            "name": "Grace Lee",
            "age": 38,
            "email": "grace@email.com",
            "city": "Seattle",
            "registration_date": "2026-03-19",
        },
        {
            "name": "Henry Davis",
            "age": 51,
            "email": "henry@email.com",
            "city": "Miami",
            "registration_date": "2026-03-18",
        },
        {
            "name": "Iris Chen",
            "age": 26,
            "email": "iris@email.com",
            "city": "Denver",
            "registration_date": "2026-03-17",
        },
    ]

    with PEOPLE_DICT_CSV.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(people)

    print(f"✅ Created {PEOPLE_DICT_CSV}")


def append_to_csv() -> None:
    """Append new data to existing CSV."""
    print("\n➕ Appending to CSV:")
    print("=" * 50)

    new_person = [
        "Jack Wilson",
        33,
        "jack@email.com",
        "Portland",
        "555-1010",
        "1989-06-30",
    ]

    try:
        with PEOPLE_SAMPLE_CSV.open("a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(new_person)

        print(f"✅ Added {new_person[0]} to {PEOPLE_SAMPLE_CSV.name}")

        with PEOPLE_SAMPLE_CSV.open(encoding="utf-8") as file:
            reader = csv.reader(file)
            rows = list(reader)

        print(f"\n📊 Updated CSV ({len(rows) - 1} people):")
        print(tabulate(rows[1:], headers=rows[0], tablefmt="grid"))

    except Exception as e:
        print(f"❌ Error appending to file: {e}")


def demonstrate_csv_formats() -> None:
    """Demonstrate different CSV formats and options."""
    print("\n🎨 CSV Format Demonstrations:")
    print("=" * 50)

    data = [
        ["Product", "Price", "Quantity", "Category"],
        ["Laptop", 999.99, 5, "Electronics"],
        ["Mouse", 29.99, 50, "Accessories"],
        ["Keyboard", 79.99, 25, "Accessories"],
    ]

    formats = [
        ("products_default.csv", ",", '"'),
        ("products_semicolon.csv", ";", '"'),
        ("products_no_quotes.csv", ",", ""),
        ("products_tab.tsv", "\t", '"'),
    ]

    for filename, delimiter, quotechar in formats:
        out_path = GEN_DIR / filename
        with out_path.open("w", newline="", encoding="utf-8") as file:
            if quotechar:
                writer = csv.writer(file, delimiter=delimiter, quotechar=quotechar)
            else:
                writer = csv.writer(
                    file,
                    delimiter=delimiter,
                    quoting=csv.QUOTE_NONE,
                    escapechar="\\",
                )
            writer.writerows(data)

        format_type = filename.split("_")[1].split(".")[0].upper()
        print(f"✅ Created {out_path} ({format_type} format)")

        with out_path.open(encoding="utf-8") as file:
            content = file.read()
            preview = content[:200] + "..." if len(content) > 200 else content
            print(f"   {preview}")
