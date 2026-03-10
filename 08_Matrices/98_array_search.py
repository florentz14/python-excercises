# -------------------------------------------------
# File Name: 98_array_search.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Array search operations (linear, binary, filters).
# -------------------------------------------------

SEPARATOR = "=" * 60
BASE_ARRAY = [15, 42, 8, 73, 31, 56, 4, 99, 27, 61]


def title(text: str) -> None:
    print(f"\n{SEPARATOR}")
    print(f"  {text}")
    print(SEPARATOR)


def subtitle(text: str) -> None:
    print(f"\n  --- {text} ---")


def linear_search(arr: list[int], value: int) -> int:
    # Scan one-by-one from left to right.
    for i, element in enumerate(arr):
        if element == value:
            return i
    return -1


def binary_search(arr: list[int], value: int) -> int:
    # Works only if arr is sorted.
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


def search_operation(array: list[int]) -> None:
    title("6. SEARCH - Locate elements in the array")
    data = array
    print(f"  Array : {data}")

    # 6a) Linear search.
    subtitle("6a. Linear search - find one value")
    target = 73
    idx = linear_search(data, target)
    if idx != -1:
        print(f"  Searching {target}: found at index {idx}")
    else:
        print(f"  Searching {target}: not found")

    # 6b) Membership test with 'in'.
    subtitle("6b. Search with 'in' (membership)")
    for value in [42, 100]:
        print(f"  Is {value} in the array? -> {value in data}")

    # 6c) Search helpers: index and count.
    subtitle("6c. Search with index() and count()")
    print(f"  Index of 56           : {data.index(56)}")
    duplicated = data + [42, 42]
    print(f"  Count of 42 in {duplicated}: {duplicated.count(42)}")

    # 6d) Binary search over sorted data.
    subtitle("6d. Binary search - on sorted array")
    ordered = sorted(data)
    print(f"  Sorted array : {ordered}")
    for binary_target in [61, 100]:
        result = binary_search(ordered, binary_target)
        if result != -1:
            print(f"  Binary search for {binary_target}: index {result}")
        else:
            print(f"  Binary search for {binary_target}: not found")

    # 6e) Search with filter and comprehension.
    subtitle("6e. Search with filter() and comprehension")
    greater_than_50 = list(filter(lambda x: x > 50, data))
    print(f"  Elements > 50 (filter)      : {greater_than_50}")
    even_values = [x for x in data if x % 2 == 0]
    print(f"  Even elements (comprehension): {even_values}")

    # 6f) Find min/max and their positions.
    subtitle("6f. Find minimum and maximum with index")
    print(f"  Minimum: {min(data)} at index {data.index(min(data))}")
    print(f"  Maximum: {max(data)} at index {data.index(max(data))}")


if __name__ == "__main__":
    search_operation(BASE_ARRAY)
