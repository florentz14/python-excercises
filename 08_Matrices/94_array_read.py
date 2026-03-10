# -------------------------------------------------
# File Name: 94_array_read.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Array read operations (indexing, slicing, stats).
# -------------------------------------------------

SEPARATOR = "=" * 60
BASE_ARRAY = [15, 42, 8, 73, 31, 56, 4, 99, 27, 61]


def title(text: str) -> None:
    print(f"\n{SEPARATOR}")
    print(f"  {text}")
    print(SEPARATOR)


def subtitle(text: str) -> None:
    print(f"\n  --- {text} ---")


def read_operation(array: list[int]) -> None:
    title("2. READ - Access array elements")

    # 2a) Access individual values by index.
    subtitle("2a. Read element by index")
    print(f"  Array             : {array}")
    print(f"  Index 0  (1st)    : {array[0]}")
    print(f"  Index 4  (5th)    : {array[4]}")
    print(f"  Index -1 (last)   : {array[-1]}")

    # 2b) Iterate through all values.
    subtitle("2b. Read all elements with a for loop")
    print("  Elements: ", end="")
    for element in array:
        print(element, end="  ")
    print()

    # 2c) Read index/value pairs with enumerate.
    subtitle("2c. Read with index and value (enumerate)")
    for idx, value in enumerate(array):
        print(f"     array[{idx}] = {value}")

    # 2d) Read subranges with slicing.
    subtitle("2d. Read a segment (slicing)")
    print(f"  array[2:6]  = {array[2:6]}")
    print(f"  array[:4]   = {array[:4]}")
    print(f"  array[7:]   = {array[7:]}")
    print(f"  array[::2]  = {array[::2]}  (every 2 positions)")

    # 2e) Basic aggregate information.
    subtitle("2e. Basic statistics")
    print(f"  Total elements : {len(array)}")
    print(f"  Minimum value  : {min(array)}")
    print(f"  Maximum value  : {max(array)}")
    print(f"  Total sum      : {sum(array)}")
    print(f"  Average        : {sum(array)/len(array):.2f}")


if __name__ == "__main__":
    read_operation(BASE_ARRAY)
