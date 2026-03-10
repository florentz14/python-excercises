# -------------------------------------------------
# File Name: 99_array_delete.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Array delete operations (remove, pop, del, clear).
# -------------------------------------------------

SEPARATOR = "=" * 60
BASE_ARRAY = [15, 42, 8, 73, 31, 56, 4, 99, 27, 61]


def title(text: str) -> None:
    print(f"\n{SEPARATOR}")
    print(f"  {text}")
    print(SEPARATOR)


def subtitle(text: str) -> None:
    print(f"\n  --- {text} ---")


def delete_operation(array: list[int]) -> list[int]:
    title("7. DELETE - Remove elements from the array")
    copy_array = array.copy()
    print(f"  Initial array : {copy_array}")

    # 7a) Remove first matching value.
    subtitle("7a. Delete by value (remove)")
    copy_array.remove(31)
    print(f"  Remove value 31            : {copy_array}")

    # 7b) Remove and return by index.
    subtitle("7b. Delete by index (pop)")
    removed = copy_array.pop(2)
    print(f"  Pop index 2 (removed {removed}) : {copy_array}")

    # 7c) Delete one element using del.
    subtitle("7c. Delete with del (single index)")
    del copy_array[0]
    print(f"  del copy_array[0]          : {copy_array}")

    # 7d) Delete a full slice/range.
    subtitle("7d. Delete with del (slice)")
    del copy_array[2:5]
    print(f"  del copy_array[2:5]        : {copy_array}")

    # 7e) Delete conditionally using comprehension.
    subtitle("7e. Delete conditionally (remove even values)")
    odds_only = [x for x in copy_array if x % 2 != 0]
    print(f"  Keep odd values only       : {odds_only}")

    # 7f) Delete all elements.
    subtitle("7f. Delete all elements (clear)")
    cleared = odds_only.copy()
    cleared.clear()
    print(f"  Cleared array              : {cleared}")

    return copy_array


if __name__ == "__main__":
    result = delete_operation(BASE_ARRAY)
    print(f"\n  Final array after delete operations: {result}\n")
