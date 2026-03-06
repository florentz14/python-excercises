# -------------------------------------------------
# File Name: 57_tim_sort.py
# Author: Florentino Báez
# Date: Data Structures - Sorting Algorithms
# Description: Tim Sort (Tim Peters, 2002).
#              Hybrid of Merge Sort + Insertion Sort. It is the
#              algorithm behind sorted() and list.sort() in
#              Python. Divides the list into "runs" of minimum size
#              (minrun), sorts them with Insertion Sort and merges
#              them. Excellent with partially sorted data.
#              O(n) best case, O(n log n) worst case.
# -------------------------------------------------

import random
import time


# ============================================================
# 1. Compute optimal minrun
# ============================================================
MIN_MERGE = 32


def calc_min_run(n):
    """
    Computes the minimum run size.
    Returns a value between 32 and 64 such that n/minrun is close
    to a power of 2 (for efficient merges).
    """
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r


# ============================================================
# 2. Insertion Sort for small runs
# ============================================================
def insertion_sort_range(arr, left, right):
    """
    Insertion Sort in-place on range [left, right].
    Used for small runs in Tim Sort (efficient on nearly sorted segments).
    """
    for i in range(left + 1, right + 1):
        key = arr[i]  # Element to insert in sorted portion
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift larger elements right
            j -= 1
        arr[j + 1] = key  # Insert at correct position


# ============================================================
# 3. Merge of two adjacent runs
# ============================================================
def merge_runs(arr, left, mid, right):
    """
    Merges two sorted runs: arr[left..mid] and arr[mid+1..right].
    Optimized: only copies the smaller side to temporary buffer.
    """
    len_left = mid - left + 1
    len_right = right - mid

    # Copy to temporary arrays
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len_left and j < len_right:
        if left_arr[i] <= right_arr[j]:  # <= for stability
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len_left:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len_right:
        arr[k] = right_arr[j]
        j += 1
        k += 1


# ============================================================
# 4. Tim Sort - Implementation
# ============================================================
def tim_sort(lista):
    """
    Tim Sort: hybrid of Merge Sort + Insertion Sort.
    Does not modify the original list.
    """
    arr = lista.copy()
    n = len(arr)

    if n <= 1:
        return arr

    min_run = calc_min_run(n)

    # Step 1: Create runs of size min_run using Insertion Sort
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort_range(arr, start, end)

    # Step 2: Merge runs, doubling size each iteration
    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)

            if mid < right:
                merge_runs(arr, left, mid, right)

        size *= 2

    return arr


# ============================================================
# 5. Demo: Tim Sort vs partially sorted data
# ============================================================
def demonstrate_advantage():
    """Shows Tim Sort's advantage with partially sorted data."""
    n = 5000

    data_types = {
        "Random":           [random.randint(1, 10000) for _ in range(n)],
        "Almost sorted":    list(range(n)),  # Slightly shuffled below
        "Sorted blocks":    [],              # Built below
        "Few unique":       [random.choice(range(10)) for _ in range(n)],
        "Reverse":          list(range(n, 0, -1)),
    }

    # Almost sorted: swap 5% of elements
    almost = data_types["Almost sorted"]
    for _ in range(n // 20):
        i, j = random.randint(0, n-1), random.randint(0, n-1)
        almost[i], almost[j] = almost[j], almost[i]

    # Sorted blocks: 10 already sorted blocks, concatenated out of order
    blocks = []
    for _ in range(10):
        block = sorted([random.randint(1, 10000) for _ in range(n // 10)])
        blocks.extend(block)
    data_types["Sorted blocks"] = blocks

    print(f"\nTim Sort vs sorted() performance ({n} elements):")
    print("=" * 65)
    print(f"{'Data type':<22s} {'Tim Sort':>12s} {'sorted()':>12s}")
    print("-" * 65)

    for name, data in data_types.items():
        copy1 = data.copy()
        start_t = time.time()
        tim_sort(copy1)
        t_tim = time.time() - start_t

        copy2 = data.copy()
        start_t = time.time()
        sorted(copy2)
        t_python = time.time() - start_t

        print(f"  {name:<22s} {t_tim*1000:10.2f} ms {t_python*1000:10.2f} ms")


# ============================================================
# 6. Visual explanation of the process
# ============================================================
def tim_sort_visual(lista):
    """Shows the Tim Sort process step by step."""
    arr = lista.copy()
    n = len(arr)
    min_run = calc_min_run(n)

    print(f"\nTim Sort step by step")
    print(f"Original: {arr}")
    print(f"n = {n}, min_run = {min_run}")
    print("=" * 60)

    # Step 1: Create runs (min_run-sized blocks, each sorted with Insertion Sort)
    print(f"\nStep 1 - Create runs (Insertion Sort on blocks of {min_run}):")
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        before = arr[start:end + 1].copy()
        insertion_sort_range(arr, start, end)
        after = arr[start:end + 1]
        print(f"  [{start}:{end+1}] {before} -> {after}")

    # Step 2: Merge runs (size doubles each iteration until whole list merged)
    print(f"\nStep 2 - Merge runs:")
    size = min_run
    step = 0
    while size < n:
        paso += 1
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)
            if mid < right:
                print(f"  Merge [{left}:{mid+1}] + [{mid+1}:{right+1}]", end="")
                merge_runs(arr, left, mid, right)
                print(f" -> {arr[left:right+1]}")
        size *= 2

    print(f"\n{'='*60}")
    print(f"Result: {arr}")
    return arr


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    print("=== Tim Sort ===\n")

    # Visual demo
    lista_demo = [5, 21, 7, 23, 19, 10, 42, 3, 15, 8, 31, 1, 27, 12]
    tim_sort_visual(lista_demo)

    # Functionality tests
    print("\n--- Tests ---")
    cases = {
        "Random":    [random.randint(1, 50) for _ in range(15)],
        "Sorted":    list(range(1, 11)),
        "Reverse":   list(range(10, 0, -1)),
        "All same":  [5] * 8,
        "Single":    [42],
        "Empty":     [],
    }

    for name, case in cases.items():
        result = tim_sort(case)
        ok = all(result[i] <= result[i + 1] for i in range(len(result) - 1)) if len(result) > 1 else True
        print(f"  {name:15s}: {str(case[:8])}{'...' if len(case) > 8 else ''} -> {str(result[:8])}{'...' if len(result) > 8 else ''} {'OK' if ok else 'FAIL'}")

    # Advantage with partially sorted data
    demonstrate_advantage()

    print("\nNote: Python's sorted() and list.sort() use Tim Sort internally.")
    print("This implementation is educational; CPython's version is in C.")
