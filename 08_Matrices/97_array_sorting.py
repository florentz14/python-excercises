# -------------------------------------------------
# File Name: 97_array_sorting.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Array sorting operations and manual algorithms.
# -------------------------------------------------

SEPARATOR = "=" * 60


def title(text: str) -> None:
    print(f"\n{SEPARATOR}")
    print(f"  {text}")
    print(SEPARATOR)


def subtitle(text: str) -> None:
    print(f"\n  --- {text} ---")


def sorting_operation() -> list[int]:
    title("5. SORTING - Organize array elements")
    base = [64, 34, 25, 12, 22, 11, 90, 45, 3, 78]
    print(f"  Base array : {base}")

    # 5a-5d) Built-in ordering operations.
    subtitle("5a. Sort ascending (sort - in place)")
    ascending = base.copy()
    ascending.sort()
    print(f"  Ascending  : {ascending}")

    subtitle("5b. Sort descending")
    descending = base.copy()
    descending.sort(reverse=True)
    print(f"  Descending : {descending}")

    subtitle("5c. Sort without modifying original (sorted)")
    sorted_copy = sorted(base)
    print(f"  Original   : {base}")
    print(f"  sorted()   : {sorted_copy}")

    subtitle("5d. Reverse the array (reverse)")
    reversed_array = base.copy()
    reversed_array.reverse()
    print(f"  Reversed   : {reversed_array}")

    # 5e) Custom sorting key example.
    subtitle("5e. Sort with custom key (modulo 10)")
    custom = base.copy()
    custom.sort(key=lambda x: x % 10)
    print(f"  By modulo 10: {custom}")

    # 5f) Manual Bubble Sort.
    subtitle("5f. Bubble Sort - manual implementation")
    bubble = base.copy()
    n = len(bubble)
    swaps = 0
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if bubble[j] > bubble[j + 1]:
                bubble[j], bubble[j + 1] = bubble[j + 1], bubble[j]
                swaps += 1
    print(f"  Bubble Sort: {bubble}  ({swaps} swaps)")

    # 5g) Manual Selection Sort.
    subtitle("5g. Selection Sort - manual implementation")
    selection = base.copy()
    for i in range(len(selection)):
        min_idx = i
        for j in range(i + 1, len(selection)):
            if selection[j] < selection[min_idx]:
                min_idx = j
        selection[i], selection[min_idx] = selection[min_idx], selection[i]
    print(f"  Selection Sort: {selection}")

    return ascending


if __name__ == "__main__":
    result = sorting_operation()
    print(f"\n  Final ascending result: {result}\n")
