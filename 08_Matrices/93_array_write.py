# -------------------------------------------------
# File Name: 93_array_write.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Array write operations (create/populate).
# -------------------------------------------------

SEPARATOR = "=" * 60


def title(text: str) -> None:
    print(f"\n{SEPARATOR}")
    print(f"  {text}")
    print(SEPARATOR)


def subtitle(text: str) -> None:
    print(f"\n  --- {text} ---")


def write_operation() -> list[int]:
    title("1. WRITE - Create and populate the array")

    # 1a) Manual write with a literal list.
    subtitle("1a. Manual write (literal)")
    manual_array: list[int] = [15, 42, 8, 73, 31, 56, 4, 99, 27, 61]
    print(f"  Created array : {manual_array}")

    # 1b) Build array step-by-step with a loop.
    subtitle("1b. Loop-based write (squares from 1 to 5)")
    loop_array: list[int] = []
    for i in range(1, 6):
        loop_array.append(i ** 2)
    print(f"  Created array : {loop_array}")

    # 1c) Compact creation using list comprehension.
    subtitle("1c. List comprehension write (even numbers)")
    even_array: list[int] = [x for x in range(2, 21, 2)]
    print(f"  Created array : {even_array}")

    # 1d) Simulate user input values.
    subtitle("1d. Simulated write (as if user entered values)")
    simulated_data = [10, 25, 33, 47, 52]
    user_array: list[int] = []
    for value in simulated_data:
        user_array.append(value)
        print(f"     -> Added: {value}  | Current array: {user_array}")

    return manual_array


if __name__ == "__main__":
    base = write_operation()
    print(f"\n  Returned base array: {base}\n")
