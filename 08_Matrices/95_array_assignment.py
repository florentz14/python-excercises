# -------------------------------------------------
# File Name: 95_array_assignment.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Array assignment operations on specific positions.
# -------------------------------------------------

SEPARATOR = "=" * 60
BASE_ARRAY = [15, 42, 8, 73, 31, 56, 4, 99, 27, 61]


def title(text: str) -> None:
    print(f"\n{SEPARATOR}")
    print(f"  {text}")
    print(SEPARATOR)


def subtitle(text: str) -> None:
    print(f"\n  --- {text} ---")


def assignment_operation(array: list[int]) -> list[int]:
    title("3. ASSIGNMENT - Assign values to specific positions")
    copy_array = array.copy()
    print(f"  Original array : {copy_array}")

    # 3a) Direct assignment by index.
    subtitle("3a. Direct assignment by index")
    copy_array[0] = 100
    copy_array[9] = 200
    print(f"  After assigning 100->[0] and 200->[9] : {copy_array}")

    # 3b) Replace a slice with new values.
    subtitle("3b. Slice assignment")
    copy_array[2:5] = [300, 400, 500]
    print(f"  After assigning [300,400,500] to [2:5] : {copy_array}")

    # 3c) Assign transformed values using comprehension.
    subtitle("3c. Comprehension assignment (multiply each element by 2)")
    doubled = [x * 2 for x in array]
    print(f"  Original array x 2 : {doubled}")

    # 3d) Full array reassignment.
    subtitle("3d. Full array assignment (reassignment)")
    new_array = list(range(1, 11))
    print(f"  New assigned array: {new_array}")

    return copy_array


if __name__ == "__main__":
    result = assignment_operation(BASE_ARRAY)
    print(f"\n  Final assignment result: {result}\n")
