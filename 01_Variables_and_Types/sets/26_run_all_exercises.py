# -------------------------------------------------
# File Name: 26_run_all_exercises.py
# Author: Florentino Báez
# Date: Variables - Sets
# Description: Master Script — Run All Set Theory Exercises.
#              Executes all 12 set theory exercise files in
#              sequence using subprocess, displaying output
#              and tracking success/failure for each.
# -------------------------------------------------

"""
Master Script - Run All Set Theory Exercises
This script executes all 12 set theory exercises in sequence.
Each exercise demonstrates different concepts of set theory using Python.
"""

import subprocess
import sys
from pathlib import Path


def run_exercise(file_path):
    """
    Run a single exercise file and display its output.
    
    Args:
        file_path: Path to the Python exercise file
    """
    # Format exercise name for display (convert underscores to spaces, title case)
    exercise_name = file_path.stem.replace('_', ' ').title()
    
    print("\n" + "=" * 70)
    print(f"RUNNING: {exercise_name}")
    print("=" * 70)
    
    try:
        # Run the exercise file using subprocess
        # capture_output=True captures both stdout and stderr
        # text=True returns output as string instead of bytes
        # timeout=10 prevents hanging if exercise has infinite loop
        result = subprocess.run(
            [sys.executable, str(file_path)],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        # Display output from the exercise
        if result.stdout:
            print(result.stdout)
        
        # Display errors if any occurred during execution
        if result.stderr:
            print("ERRORS:", file=sys.stderr)
            print(result.stderr, file=sys.stderr)
        
        # Check return code: 0 means success, non-zero means error
        if result.returncode != 0:
            print(f"⚠ Exercise exited with code {result.returncode}")
        else:
            print("✓ Exercise completed successfully")
            
    except subprocess.TimeoutExpired:
        print("⚠ Exercise timed out after 10 seconds")
    except Exception as e:
        print(f"⚠ Error running exercise: {e}")
    
    print()


def main():
    """
    Main function to run all exercises in order.
    """
    print("=" * 70)
    print(" " * 15 + "SET THEORY EXERCISES - PYTHON 3.14")
    print(" " * 20 + "Complete Solution Set")
    print("=" * 70)
    print()
    print("This script will run all 12 set theory exercises.")
    print("Each exercise demonstrates different concepts and operations.")
    print()
    input("Press ENTER to begin...")
    
    # Get the directory containing this script
    # This ensures exercises are found regardless of where script is run from
    script_dir = Path(__file__).parent
    
    # List of all exercise files in order (must match actual filenames)
    exercise_files = [
        "exercise_01_notation_and_elements.py",
        "exercise_02_set_comprehension.py",
        "exercise_03_union.py",
        "exercise_04_intersection.py",
        "exercise_05_difference.py",
        "exercise_06_complement.py",
        "exercise_07_subsets.py",
        "exercise_08_combined_operations.py",
        "exercise_09_cardinality.py",
        "exercise_10_venn_diagram.py",
        "exercise_11_cartesian_product.py",
        "exercise_12_disjoint_sets.py",
    ]
    
    # Run each exercise in sequence
    for exercise_file in exercise_files:
        file_path = script_dir / exercise_file  # Construct full path
        
        # Check if file exists before attempting to run
        if file_path.exists():
            run_exercise(file_path)
        else:
            print(f"⚠ Warning: {exercise_file} not found!")
    
    print("=" * 70)
    print(" " * 20 + "ALL EXERCISES COMPLETED!")
    print("=" * 70)
    print()
    print("Summary:")
    print(f"  Total exercises: {len(exercise_files)}")
    print("  Topics covered:")
    print("    - Set notation and membership")
    print("    - Set comprehension")
    print("    - Union, intersection, difference")
    print("    - Complements and subsets")
    print("    - Combined operations")
    print("    - Cardinality and Venn diagrams")
    print("    - Cartesian products")
    print("    - Disjoint sets")


if __name__ == "__main__":
    main()
