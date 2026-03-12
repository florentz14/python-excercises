# -------------------------------------------------
# File Name: 20_main_menu.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Interactive menu to launch all student performance analyses.
# -------------------------------------------------

"""
Master Student Performance Analysis Program
Executes all available analyses with an interactive menu
"""

import subprocess
import sys
from pathlib import Path

PANDAS_FOLDER = Path(__file__).resolve().parent


def show_menu():
    """Shows the main options menu."""
    print("\n" + "=" * 80)
    print("STUDENT PERFORMANCE ANALYSIS SYSTEM")
    print("=" * 80)
    print("\nSelect the type of analysis to run:")
    print("\n1. General Analysis")
    print("   - General descriptive statistics")
    print("   - Averages by subject")
    print("   - Grade distribution")
    print("   - Subject correlations")

    print("\n2. Gender Analysis")
    print("   - Performance comparison by gender")
    print("   - Subject differences")
    print("   - High score distribution")

    print("\n3. Parental Education Analysis")
    print("   - Impact of parental education level")
    print("   - Performance trends")
    print("   - College vs non-college comparison")

    print("\n4. Test Preparation Analysis")
    print("   - Impact of preparation course")
    print("   - Subject improvements")
    print("   - Combined analysis with gender")

    print("\n5. Lunch Type Analysis (Socioeconomic)")
    print("   - Standard vs free/reduced comparison")
    print("   - Performance gaps")
    print("   - Interaction with other factors")

    print("\n6. Ethnic Group Analysis")
    print("   - Performance by group")
    print("   - Gaps between groups")
    print("   - Education and gender interactions")

    print("\n7. Run ALL analyses")
    print("\n0. Exit")
    print("\n" + "=" * 80)


def run_program(filename):
    """Executes a specific analysis program."""
    try:
        print(f"\n\nRunning {filename}...")
        print("-" * 80)
        script = PANDAS_FOLDER / filename
        result = subprocess.run(
            [sys.executable, str(script)],
            cwd=str(PANDAS_FOLDER),
            capture_output=False,
            text=True,
        )
        if result.returncode == 0:
            print("\n[OK] Analysis completed successfully")
        else:
            print("\n[ERROR] Error running analysis")
    except Exception as e:
        print(f"\n[ERROR] {e}")


def run_all():
    """Executes all available analyses."""
    programs = [
        ("03_general_analysis.py", "General Analysis"),
        ("05_gender_analysis.py", "Gender Analysis"),
        ("02_parental_education.py", "Parental Education Analysis"),
        ("06_test_preparation.py", "Test Preparation Analysis"),
        ("01_lunch_analysis.py", "Lunch Type Analysis"),
        ("04_ethnic_group.py", "Ethnic Group Analysis"),
    ]

    print("\n\n" + "=" * 80)
    print("RUNNING ALL ANALYSES")
    print("=" * 80)

    for i, (filename, name) in enumerate(programs, 1):
        print(f"\n\n[{i}/{len(programs)}] {name}")
        run_program(filename)
        if i < len(programs):
            input("\nPress ENTER to continue with next analysis...")

    print("\n\n" + "=" * 80)
    print("[OK] ALL ANALYSES COMPLETED")
    print("=" * 80)


def main():
    """Main program function."""
    options = {
        "1": ("03_general_analysis.py", "General Analysis"),
        "2": ("05_gender_analysis.py", "Gender Analysis"),
        "3": ("02_parental_education.py", "Parental Education Analysis"),
        "4": ("06_test_preparation.py", "Test Preparation Analysis"),
        "5": ("01_lunch_analysis.py", "Lunch Type Analysis"),
        "6": ("04_ethnic_group.py", "Ethnic Group Analysis"),
    }

    while True:
        show_menu()
        choice = input("\nEnter option (0-7): ").strip()

        if choice == "0":
            print("\nGoodbye!")
            break

        elif choice == "7":
            run_all()
            input("\nPress ENTER to return to main menu...")

        elif choice in options:
            filename, name = options[choice]
            print(f"\n\n{'=' * 80}")
            print(f"RUNNING: {name}")
            print("=" * 80)
            run_program(filename)
            input("\nPress ENTER to return to main menu...")

        else:
            print("\n[ERROR] Invalid option. Please select 0-7.")
            input("\nPress ENTER to continue...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user!")
        sys.exit(0)
