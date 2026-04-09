# -------------------------------------------------
# File Name: 07_rank_interactive.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Use sample matrix or enter custom matrix from keyboard.
# -------------------------------------------------

import numpy as np

from rank_util import A, compute_matrix_rank


def interactive_rank_calculator():
    """Interactive menu: sample matrix or custom input."""
    while True:
        try:
            print("\n" + "=" * 60)
            print("MATRIX RANK CALCULATOR")
            print("=" * 60)
            print("\nOptions:")
            print("1. Use sample matrix")
            print("2. Enter custom matrix")
            print("3. Exit")

            opt = input("\nSelect option: ").strip()

            if opt == "1":
                mat = A.copy()
                print("\nSample matrix:")
                print(mat)

            elif opt == "2":
                rows = int(input("Number of rows: "))
                cols = int(input("Number of columns: "))
                print(f"\nEnter matrix elements ({rows}x{cols}):")
                print("(Space-separated per row, one row per line)")

                entries = []
                ok = True
                for i in range(rows):
                    row_str = input(f"Row {i+1}: ")
                    row = [float(x) for x in row_str.split()]
                    if len(row) != cols:
                        print(f"Error: row must have {cols} elements")
                        ok = False
                        break
                    entries.append(row)
                if not ok:
                    continue
                mat = np.array(entries)

            elif opt == "3":
                print("Goodbye.")
                break

            else:
                print("[ERROR] Invalid option")
                continue

            rank, info = compute_matrix_rank(mat, show_info=True)

            again = input("\nAnalyze another matrix? (y/n): ").lower()
            if again != "y":
                break

        except ValueError:
            print("[ERROR] Please enter valid numbers")
        except KeyboardInterrupt:
            print("\n\nCancelled")
            break
        except Exception as e:
            print(f"[ERROR] {e}")


if __name__ == "__main__":
    print("=== Version 7: Interactive ===\n")
    interactive_rank_calculator()
