# -------------------------------------------------
# File Name: 96_array_update.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Array update operations (modify structure/content).
# -------------------------------------------------

SEPARATOR = "=" * 60
BASE_ARRAY = [15, 42, 8, 73, 31, 56, 4, 99, 27, 61]


def title(text: str) -> None:
    print(f"\n{SEPARATOR}")
    print(f"  {text}")
    print(SEPARATOR)


def subtitle(text: str) -> None:
    print(f"\n  --- {text} ---")


def update_operation(array: list[int]) -> list[int]:
    title("4. UPDATE - Modify elements or structure")
    copy_array = array.copy()
    print(f"  Initial array : {copy_array}")

    # 4a) Update an existing element.
    subtitle("4a. Update an existing element")
    copy_array[3] = copy_array[3] + 10
    print(f"  Index 3 increased by 10 : {copy_array}")

    # 4b) Insert value at a specific position.
    subtitle("4b. Insert element at specific position")
    copy_array.insert(2, 999)
    print(f"  Insert 999 at index 2    : {copy_array}")

    # 4c-4d) Append and extend operations.
    subtitle("4c. Append element at the end")
    copy_array.append(777)
    print(f"  Append 777 at the end    : {copy_array}")

    subtitle("4d. Add multiple elements (extend)")
    copy_array.extend([11, 22, 33])
    print(f"  Extend with [11,22,33]   : {copy_array}")

    # 4e-4f) Remove by value and by index.
    subtitle("4e. Remove by value")
    copy_array.remove(999)
    print(f"  Remove value 999         : {copy_array}")

    subtitle("4f. Remove by index (pop)")
    removed = copy_array.pop(0)
    print(f"  Remove index 0 (was {removed})  : {copy_array}")

    # 4g) Update all values with a transformation.
    subtitle("4g. Update using loop logic (add 5 to all)")
    copy_array = [x + 5 for x in copy_array]
    print(f"  All elements + 5         : {copy_array}")

    return copy_array


if __name__ == "__main__":
    result = update_operation(BASE_ARRAY)
    print(f"\n  Final update result: {result}\n")
