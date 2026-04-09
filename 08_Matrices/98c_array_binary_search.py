# -------------------------------------------------
# File Name: 98c_array_binary_search.py
# Author: Florentino Baez
# Date: 08_Matrices
# Description: Binary search on a sorted list.
# -------------------------------------------------

SEPARATOR = "=" * 60
BASE_ARRAY = [15, 42, 8, 73, 31, 56, 4, 99, 27, 61]


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


def subtitle(text: str) -> None:
    print(f"\n  --- {text} ---")


def binary_search(arr: list[int], value: int) -> int:
    left, right = 0, len(arr) - 1
    iterations = 0
    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        if arr[mid] == value:
            print(f"     Found in {iterations} iteration(s)")
            return mid
        if arr[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def main() -> None:
    title("6d. BINARY SEARCH - Sorted array only")
    data = BASE_ARRAY
    ordered = sorted(data)
    print(f"  Sorted array : {ordered}")
    subtitle("Lookups")
    for binary_target in [61, 100]:
        result = binary_search(ordered, binary_target)
        if result != -1:
            print(f"  Binary search for {binary_target}: index {result}")
        else:
            print(f"  Binary search for {binary_target}: not found")


if __name__ == "__main__":
    main()
