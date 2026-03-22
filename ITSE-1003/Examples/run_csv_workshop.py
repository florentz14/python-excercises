# -------------------------------------------------
# File Name: ITSE-1003/Examples/run_csv_workshop.py
# Author: Florentino
# Date: 3/22/2026
# Description: Ejecuta todo el taller CSV (lectura, escritura, análisis de people.csv).
# -------------------------------------------------

from examples_paths import DATA_DIR, GEN_DIR
from csv_people_analysis import analyze_csv_data, filter_csv_data
from csv_reading import read_basic_csv, read_dict_csv
from csv_writing import (
    append_to_csv,
    create_dict_csv,
    create_sample_csv,
    demonstrate_csv_formats,
)


def main() -> None:
    """Run all CSV demonstrations in order."""
    print("🗂️ CSV workshop (full run)")
    print("=" * 60)

    GEN_DIR.mkdir(parents=True, exist_ok=True)

    read_basic_csv()
    create_sample_csv()
    create_dict_csv()

    read_dict_csv()

    analyze_csv_data()
    filter_csv_data()

    append_to_csv()

    demonstrate_csv_formats()

    print("\n" + "=" * 60)
    print("✅ CSV workshop complete!")
    print(f"📁 Bundled CSVs: {DATA_DIR} (people.csv, exam_data.csv, …)")
    print(f"📁 Generated outputs: {GEN_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    main()
