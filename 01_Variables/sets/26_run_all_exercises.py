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
    exercise_name = file_path.stem.replace('_', ' ').title()
    
    print("\n" + "=" * 70)
    print(f"RUNNING: {exercise_name}")
    print("=" * 70)
    
    try:
        # Run the exercise file
        result = subprocess.run(
            [sys.executable, str(file_path)],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        # Display output
        if result.stdout:
            print(result.stdout)
        
        # Display errors if any
        if result.stderr:
            print("ERRORS:", file=sys.stderr)
            print(result.stderr, file=sys.stderr)
        
        # Check return code
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
    script_dir = Path(__file__).parent
    
    # List of all exercise files in order
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
    
    # Run each exercise
    for exercise_file in exercise_files:
        file_path = script_dir / exercise_file
        
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
