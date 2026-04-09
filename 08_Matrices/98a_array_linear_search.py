# -------------------------------------------------
# File Name: 98a_array_linear_search.py
# Author: Florentino Baez
# Date: 08_Matrices
# Description: Linear scan to find a value in a list.
# -------------------------------------------------

SEPARATOR = "=" * 60
BASE_ARRAY = [15, 42, 8, 73, 31, 56, 4, 99, 27, 61]


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


def subtitle(text: str) -> None:
    print(f"\n  --- {text} ---")


def linear_search(arr: list[int], value: int) -> int:
    for i, element in enumerate(arr):
        if element == value:
            return i
    return -1


def main() -> None:
    title("6a. LINEAR SEARCH - Scan left to right")
    data = BASE_ARRAY
    print(f"  Array : {data}")
    target = 73
    idx = linear_search(data, target)
    if idx != -1:
        print(f"  Searching {target}: found at index {idx}")
    else:
        print(f"  Searching {target}: not found")


if __name__ == "__main__":
    main()
